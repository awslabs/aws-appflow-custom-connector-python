import os
import unittest
import importlib

from custom_connector_integ_test.configuration import services
from custom_connector_integ_test.configuration.test_configuration import get_configuration, TestConfiguration, \
    read_file_to_dict, read_file
from custom_connector_integ_test.utils.flow_poller import poll_for_execution_records_response
from custom_connector_integ_test.utils.request_generator import RequestGenerator
from custom_connector_integ_test.utils.resource_info_provider import ResourceInfoProvider
from custom_connector_integ_test.utils.s3_helper import S3Helper

max_poll_time = 180


class AppflowTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_config: TestConfiguration = get_configuration(os.environ['TEST_CONFIG'])

        # Allows you to see full diff for validation files
        cls.maxDiff = None
        cls.info_provider: ResourceInfoProvider = ResourceInfoProvider(cls.test_config)
        cls.request_generator = RequestGenerator(cls.info_provider, cls.test_config.test_bucket_configuration)
        cls.s3_helper = S3Helper(cls.test_config.test_bucket_configuration)

    # Test case that creates a connector, describes the connector and validates the description against a provided
    # response.
    def test_1_connector_register(self):
        for config in self.test_config.custom_connector_configurations:
            with self.subTest(p1=config.name):
                services.get_appflow().register_connector(
                    **self.request_generator.get_register_connector_request(config))
                self.info_provider.add_to_created_connectors(config.name)
                result = services.get_appflow().describe_connector(**self.request_generator
                                                                   .get_describe_connector_request(config))
                if config.validation_file_name is not None:
                    expected = read_file_to_dict(config.validation_file_name)["connectorConfiguration"]
                    expected["registeredAt"] = None
                    expected["registeredBy"] = None
                    expected["connectorLabel"] = None

                    actual = result["connectorConfiguration"]
                    actual["registeredAt"] = None
                    actual["registeredBy"] = None
                    actual["connectorLabel"] = None

                    self.assertDictEqual(expected, actual)

    # Test case that creates a connector profile.
    def test_2_profile_creation(self):
        for config in self.test_config.custom_connector_profile_configurations:
            with self.subTest(p1=config.name):
                services.get_appflow().create_connector_profile(
                    **self.request_generator.get_create_connector_profile_request(config))
                self.info_provider.add_to_created_profiles(config.name)

    # Test case that lists entities, and validates specific entities against a test file the user provides.
    def test_3_list_entities(self):
        for config in self.test_config.list_connector_entities_test_configurations:
            with self.subTest(p1=config.test_name, p2=config.entities_path):
                res = services.get_appflow().list_connector_entities(
                    **self.request_generator.get_list_connector_entities_request(config))
            if config.validation_file_name is not None:
                expected = read_file_to_dict(config.validation_file_name)
                for key, value in expected["connectorEntityMap"].items():
                    for entity in value:
                        self.assertTrue(entity in res["connectorEntityMap"][key])

    # Test case that describes an entity, and validates specific entity fields against a test file the user provides.
    def test_4_describe_entity(self):
        for config in self.test_config.describe_connector_entity_test_configurations:
            with self.subTest(p1=config.test_name, p2=config.entity_name):
                res = services.get_appflow().describe_connector_entity(
                    **self.request_generator.get_describe_connector_entity_request(config))
                if config.validation_file_name is not None:
                    expected = read_file_to_dict(config.validation_file_name)
                    for field in expected["connectorEntityFields"]:
                        self.assertTrue(field in res["connectorEntityFields"])

    # Test case that executes a flow and polls the flow until completion. The flow get data from a connector and puts
    # the data into s3.
    def test_5_source_flow_execution(self):
        for config in self.test_config.on_demand_to_s3_test_configurations:
            with self.subTest(p1=config.test_name, p2=config.flow_name):
                flow_request = self.request_generator.get_source_create_flow_request(config)
                poll_time = config.flow_timeout or max_poll_time
                services.get_appflow().create_flow(
                    **flow_request)
                res = services.get_appflow().start_flow(flowName=flow_request["flowName"])
                record = poll_for_execution_records_response(flow_request["flowName"], res["executionId"],
                                                             poll_time, int(poll_time / 5))
                self.assertIsNotNone(record)
                self.assertEqual(record["executionStatus"], "Successful")
                if config.output_size is not None:
                    self.assertEqual(config.output_size, record["executionResult"]["bytesWritten"])

    # Test case that executes a flow and polls the flow until completion. The flow gets data from s3 and puts it to
    # the connector.
    def test_6_destination_flow_execution(self):
        for config in self.test_config.on_demand_from_s3_test_configurations:
            with self.subTest(p1=config.test_name, p2=config.flow_name):
                poll_time = config.flow_timeout or max_poll_time
                file_string = None
                if config.source_data_file is not None:
                    file_string = read_file(config.source_data_file)
                elif config.data_generator_class_name is not None:
                    split = config.data_generator_class_name.rsplit(".", 1)
                    data_class = getattr(importlib.import_module(split[0]), split[1])
                    file_string = data_class().generate_data()
                else:
                    raise ValueError("Either Source data file or data generator class is needed to run test.")
                lines = file_string.split("\n")
                fields = lines[0].split(",")
                flow_request = self.request_generator.get_destination_create_flow_request(config, fields)

                self.s3_helper.upload_file(file_string, config.flow_name)
                services.get_appflow().create_flow(
                    **flow_request)
                res = services.get_appflow().start_flow(flowName=flow_request["flowName"])
                record = poll_for_execution_records_response(flow_request["flowName"], res["executionId"],
                                                             poll_time, int(poll_time / 5))
                self.assertIsNotNone(record)
                self.assertEqual(record["executionStatus"], "Successful")
                self.assertEqual(record["executionResult"]["recordsProcessed"], len(lines) - 1)

    # Tests that run after all other test cases.
    # These test cases clean up resources created in the account during the integration test run.
    @classmethod
    def tearDownClass(cls):
        profile_names = []
        request = {"maxResults": 100}
        while True:
            res = services.get_appflow().describe_connector_profiles(**request)
            for profile in res['connectorProfileDetails']:
                if profile["connectorProfileName"].startswith("Integ_Profile_" + cls.info_provider.prefix):
                    profile_names.append(profile["connectorProfileName"])
            if res.get("nextToken", None) is None:
                break
            request["nextToken"] = res.get("nextToken", None)
        for profileName in profile_names:
            services.get_appflow().delete_connector_profile(
                connectorProfileName=profileName,
                forceDelete=True)

        connector_names = []
        request = {"maxResults": 100}
        while True:
            res = services.get_appflow().list_connectors(**request)
            for connector in res['connectors']:
                if connector["connectorLabel"].startswith("Integ_Connector_" + cls.info_provider.prefix):
                    connector_names.append(connector["connectorLabel"])
            if res.get("nextToken", None) is None:
                break
            request["nextToken"] = res.get("nextToken", None)
        for name in connector_names:
            services.get_appflow().unregister_connector(
                connectorLabel=name,
                forceDelete=True)

        flow_names = []
        request = {"maxResults": 100}
        while True:

            res = services.get_appflow().list_flows(**request)
            for flow in res['flows']:
                if flow["flowName"].startswith("Integ_Flow_" + cls.info_provider.prefix):
                    flow_names.append(flow["flowName"])
            if res.get("nextToken", None) is None:
                break
            request["nextToken"] = res.get("nextToken", None)
        for name in flow_names:
            services.get_appflow().delete_flow(
                flowName=name,
                forceDelete=True)
