import json

from typing import List

from custom_connector_integ_test.configuration import services
from custom_connector_integ_test.configuration.test_configuration import AuthenticationType, CustomConnectorConfiguration, TestBucketConfiguration, \
    CustomConnectorProfileConfiguration, DescribeConnectorEntityTestConfiguration, \
    ListConnectorEntitiesTestConfiguration, OnDemandFromS3TestConfiguration, OnDemandToS3TestConfiguration
from custom_connector_integ_test.utils.resource_info_provider import ResourceInfoProvider

# Utility class used to Generate Requests for the testcases.
def get_tasks(fields: List[str], operator):
    tasks = []
    for field in fields:
        tasks.append({
            "taskType": "Map",
            "connectorOperator": {
                "S3": "NO_OP"
            },
            "taskProperties": {},
            "sourceFields": [field],
            "destinationField": field
        })
    tasks.append(
        {
            "taskType": "Filter",
            "taskProperties": {},
            "sourceFields": fields,
            "connectorOperator": operator
        }
    )
    return tasks


class RequestGenerator:

    def __init__(self, resource_info_provider: ResourceInfoProvider, bucket_config: TestBucketConfiguration):

        self.resource_info_provider = resource_info_provider
        self.bucket_config = bucket_config

    def get_register_connector_request(self, config: CustomConnectorConfiguration):
        request = {}
        request["connectorLabel"] = self.resource_info_provider.generate_connector_name(config.name)
        request["description"] = "Integration test connector"
        request["connectorProvisioningType"] = "LAMBDA"
        request["connectorProvisioningConfig"] = {"lambda": {"lambdaArn": f"{config.lambda_arn}"}}
        return request

    def get_describe_connector_request(self, config: CustomConnectorConfiguration):
        request = {}
        request["connectorLabel"] = self.resource_info_provider.generate_connector_name(config.name)
        request["connectorType"] = "CustomConnector"
        return request

    def get_create_connector_profile_request(self, config: CustomConnectorProfileConfiguration):
        creds = {}

        if not config.authentication_type == AuthenticationType.NO_AUTH:

            result = services.get_secrets_manager().get_secret_value(
                SecretId=config.secrets_manager_arn)
            secrets = json.loads(result["SecretString"])

            authType = AuthenticationType[config.authentication_type]

            if authType is AuthenticationType.OAUTH2:
                creds["authenticationType"] = "OAUTH2"
                creds["oauth2"] = secrets

            if authType is AuthenticationType.BASIC:
                creds["authenticationType"] = AuthenticationType.BASIC
                creds["basic"] = secrets

            if authType is AuthenticationType.CUSTOM:
                creds["authenticationType"] = AuthenticationType.CUSTOM
                creds["custom"] = secrets

        request = {}
        request["connectorProfileName"] = self.resource_info_provider.generate_profile_name(config.name)
        request["connectorType"] = "CustomConnector"
        request["connectorLabel"] = self.resource_info_provider.get_connector_name(config.connector_name)
        request["connectionMode"] = "Public"

        request["connectorProfileConfig"] = {
            "connectorProfileProperties": {
                "CustomConnector": {
                    "profileProperties": config.profile_properties,
                    "oAuth2Properties": config.o_auth2_properties
                }
            },
            "connectorProfileCredentials": {
                "CustomConnector": creds
            }
        }
        return request

    def get_describe_connector_entity_request(self, config: DescribeConnectorEntityTestConfiguration):
        request = {}
        request["connectorProfileName"] = self.resource_info_provider.get_profile_name(
            config.profile_name)
        request["connectorType"] = "CustomConnector"
        request["apiVersion"] = self.resource_info_provider.get_api_for_profile_name(config.profile_name,
                                                                                     config.api_version)
        request["connectorEntityName"] = config.entity_name
        return request

    def get_list_connector_entities_request(self, config: ListConnectorEntitiesTestConfiguration):
        request = {}
        request["connectorProfileName"] = self.resource_info_provider.get_profile_name(
            config.profile_name)
        request["connectorType"] = "CustomConnector"
        request["apiVersion"] = self.resource_info_provider.get_api_for_profile_name(config.profile_name,
                                                                                     config.api_version)
        if config.entities_path is not None:
            request["entitiesPath"] = config.entities_path
        return request

    def get_destination_create_flow_request(self, config: OnDemandFromS3TestConfiguration, fields: List[str]):

        custom_connector_props = {
            "entityName": config.entity_name,
            "writeOperationType": config.write_operation_type,
            "errorHandlingConfig": {
                "failOnFirstDestinationError": False,
                "bucketName": self.bucket_config.bucket_name,
                "bucketPrefix": self.bucket_config.bucket_prefix + "integ-test-errors/"
            },
            "customProperties": config.destination_runtime_properties
        }

        if config.id_field_names is not None:
            custom_connector_props["idFieldNames"] = config.id_field_names

        request = {
            "description": "Flow Created by IntegrationTestFramework.",
            "flowName": self.resource_info_provider.generate_flow_name(config.flow_name),
            "sourceFlowConfig": {
                "connectorType": "S3",
                "sourceConnectorProperties": {
                    "S3": {
                        "bucketName": self.bucket_config.bucket_name,
                        "bucketPrefix": self.bucket_config.bucket_prefix + config.flow_name
                    }
                }
            },
            "triggerConfig": {
                "triggerType": "OnDemand"
            },
            "destinationFlowConfigList": [{
                "connectorType": "CustomConnector",
                "connectorProfileName": self.resource_info_provider.get_profile_name(config.profile_name),
                "apiVersion": self.resource_info_provider.get_api_for_profile_name(config.profile_name,
                                                                                   config.api_version),
                "destinationConnectorProperties": {
                    "CustomConnector": custom_connector_props
                }
            }],
            "tasks": get_tasks(fields, {
                "S3": "PROJECTION"
            })
        }
        return request

    def get_source_create_flow_request(self, config: OnDemandToS3TestConfiguration):
        request = {
            "description": "Flow Created by IntegrationTestFramework.",
            "flowName": self.resource_info_provider.generate_flow_name(config.flow_name),
            "sourceFlowConfig": {
                "connectorType": "CustomConnector",
                "connectorProfileName": self.resource_info_provider.get_profile_name(config.profile_name),
                "apiVersion": self.resource_info_provider.get_api_for_profile_name(config.profile_name,
                                                                                   config.api_version),
                "sourceConnectorProperties": {
                    "CustomConnector": {
                        "entityName": config.entity_name,
                        "customProperties": config.source_runtime_properties
                    }
                }
            },
            "triggerConfig": {
                "triggerType": "OnDemand"
            },
            "destinationFlowConfigList": [{
                "connectorType": "S3",
                "connectorProfileName": self.resource_info_provider.get_profile_name(config.profile_name),
                "apiVersion": self.resource_info_provider.get_api_for_profile_name(config.profile_name,
                                                                                   config.api_version),
                "destinationConnectorProperties": {
                    "S3": {
                        "bucketName": self.bucket_config.bucket_name,
                        "bucketPrefix": self.bucket_config.bucket_prefix + "integ-test-errors/",
                        "s3OutputFormatConfig": {
                            "fileType": "CSV"
                        }
                    }
                }
            }],
            "tasks": get_tasks(config.entity_fields, {
                "CustomConnector": "PROJECTION"
            })
        }
        return request
