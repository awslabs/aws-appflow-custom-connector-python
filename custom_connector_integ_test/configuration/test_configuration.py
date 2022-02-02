import json
import re
from enum import Enum, auto

from typing import List

# Refer to sample-test-config.json for an explanation of the configuration file setup

pattern = re.compile(r'(?<!^)(?=[A-Z])')


class AuthenticationType(Enum):
    OAUTH2 = auto()
    BASIC = auto()
    API_KEY = auto()
    CUSTOM = auto()
    NO_AUTH = auto()


class CustomConnectorConfiguration:
    def __init__(self,
                 name: str,
                 lambda_arn: str,
                 validation_file_name: str = None):
        self.lambda_arn: str = lambda_arn
        self.name: str = name
        self.validation_file_name: str = validation_file_name


class CustomConnectorProfileConfiguration:
    def __init__(self,
                 authentication_type: str,
                 name: str,
                 connector_name: str = None,
                 profile_properties: dict = None,
                 default_api_version: str = None,
                 o_auth2_properties: dict = None,
                 secrets_manager_arn: str = None,
                 ):
        self.secrets_manager_arn: str = secrets_manager_arn
        self.o_auth2_properties: dict = o_auth2_properties
        self.authentication_type = authentication_type
        self.default_api_version: str = default_api_version
        self.profile_properties: dict = profile_properties
        self.name: str = name
        self.connector_name: str = connector_name


class TestBucketConfiguration:
    def __init__(self,
                 bucket_name: str,
                 bucket_prefix: str):
        self.bucket_prefix: str = bucket_prefix
        self.bucket_name: str = bucket_name


class ListConnectorEntitiesTestConfiguration:
    def __init__(self,
                 validation_file_name: str = None,
                 profile_name: str = None,
                 api_version: str = None,
                 test_name: str = None,
                 entities_path: str = None):
        self.entities_path: str = entities_path
        self.test_name: str = test_name
        self.api_version: str = api_version
        self.profile_name: str = profile_name
        self.validation_file_name: str = validation_file_name


class DescribeConnectorEntityTestConfiguration:
    def __init__(self,
                 api_version: str = None,
                 profile_name: str = None,
                 test_name: str = None,
                 validation_file_name: str = None,
                 entity_name: str = None):
        self.entity_name: str = entity_name
        self.validation_file_name: str = validation_file_name
        self.test_name: str = test_name
        self.profile_name: str = profile_name
        self.api_version: str = api_version


class OnDemandFromS3TestConfiguration:
    def __init__(self,
                 flow_name: str,
                 entity_name: str,
                 write_operation_type: str,
                 test_name: str = None,
                 api_version: str = None,
                 profile_name: str = None,
                 id_field_names: List[str] = None,
                 source_data_file: str = None,
                 data_generator_class_name: str = None,
                 destination_runtime_properties: dict = None,
                 flow_timeout: int = None):
        self.write_operation_type: str = write_operation_type
        self.api_version: str = api_version
        self.id_field_names: List[str] = id_field_names
        self.destination_runtime_properties: dict = destination_runtime_properties
        self.data_generator_class_name: str = data_generator_class_name
        self.source_data_file: str = source_data_file
        self.entity_name: str = entity_name
        self.flow_name: str = flow_name
        self.profile_name: str = profile_name
        self.flow_timeout: int = flow_timeout
        self.test_name: str = test_name


class OnDemandToS3TestConfiguration:
    def __init__(self,
                 flow_name: str,
                 entity_fields: List[str],
                 entity_name: str,
                 api_version: str = None,
                 test_name: str = None,
                 profile_name: str = None,
                 query: str = None,
                 source_runtime_properties: dict = None,
                 output_size: int = None,
                 flow_timeout: int = None):
        self.api_version: str = api_version
        self.entity_fields: List[str] = entity_fields
        self.query: str = query
        self.entity_name: str = entity_name
        self.source_runtime_properties: dict = source_runtime_properties
        self.output_size: int = output_size
        self.entity_name: str = entity_name
        self.flow_name: str = flow_name
        self.profile_name: str = profile_name
        self.flow_timeout: int = flow_timeout
        self.test_name: str = test_name


class TestConfiguration:
    def __init__(self,
                 custom_connector_configurations: List[CustomConnectorConfiguration],
                 custom_connector_profile_configurations: List[CustomConnectorProfileConfiguration],
                 test_bucket_configuration: TestBucketConfiguration,
                 list_connector_entities_test_configurations: List[ListConnectorEntitiesTestConfiguration],
                 describe_connector_entity_test_configurations: List[DescribeConnectorEntityTestConfiguration],
                 on_demand_from_s3_test_configurations: List[OnDemandFromS3TestConfiguration],
                 on_demand_to_s3_test_configurations: List[OnDemandToS3TestConfiguration],
                 resource_prefix: str = None):
        self.resource_prefix = resource_prefix
        self.on_demand_to_s3_test_configurations: List[
            OnDemandToS3TestConfiguration] = on_demand_to_s3_test_configurations
        self.on_demand_from_s3_test_configurations: List[
            OnDemandFromS3TestConfiguration] = on_demand_from_s3_test_configurations
        self.describe_connector_entity_test_configurations: List[
            DescribeConnectorEntityTestConfiguration] = describe_connector_entity_test_configurations
        self.list_connector_entities_test_configurations: List[
            ListConnectorEntitiesTestConfiguration] = list_connector_entities_test_configurations
        self.test_bucket_configuration: TestBucketConfiguration = test_bucket_configuration
        self.custom_connector_profile_configurations: List[
            CustomConnectorProfileConfiguration] = custom_connector_profile_configurations
        self.custom_connector_configurations: List[CustomConnectorConfiguration] = custom_connector_configurations


def check_configuration_list(param, name: str, func):
    configs = []
    if param is None or not isinstance(param, List):
        raise ValueError(name + "must be a list")
    for item in param:
        x2 = convert_keys(item)
        configs.append(func(x2))
    return configs


def convert_keys(param: dict):
    converted_dict = {}
    for key in param.keys():
        converted_dict[pattern.sub('_', key).lower()] = param[key]
    return converted_dict


def read_file_to_dict(file_path: str):
    return json.loads(read_file(file_path))


def read_file(file_path: str):
    file = open(file_path)
    string = file.read()
    file.close()
    return string


def get_configuration(config):
    json_config = read_file_to_dict(config)

    test = TestConfiguration(
        check_configuration_list(json_config.get("customConnectorConfigurations", None),
                                 "customConnectorConfigurations",
                                 lambda params: CustomConnectorConfiguration(**params)),
        check_configuration_list(json_config.get("customConnectorProfileConfigurations", None),
                                 "customConnectorProfileConfigurations",
                                 lambda params: CustomConnectorProfileConfiguration(**params)),
        TestBucketConfiguration(json_config["testBucketConfiguration"]["bucketName"],
                                json_config["testBucketConfiguration"]["bucketPrefix"]),
        check_configuration_list(json_config.get("listConnectorEntitiesTestConfigurations", None),
                                 "listConnectorEntitiesTestConfigurations",
                                 lambda params: ListConnectorEntitiesTestConfiguration(**params)),
        check_configuration_list(json_config.get("describeConnectorEntityTestConfigurations", None),
                                 "describeConnectorEntityTestConfigurations",
                                 lambda params: DescribeConnectorEntityTestConfiguration(**params)),
        check_configuration_list(json_config.get("onDemandFromS3TestConfigurations", None),
                                 "onDemandFromS3TestConfigurations",
                                 lambda params: OnDemandFromS3TestConfiguration(**params)),
        check_configuration_list(json_config.get("onDemandToS3TestConfigurations", None),
                                 "onDemandToS3TestConfigurations",
                                 lambda params: OnDemandToS3TestConfiguration(**params)),
        json_config.get("resourcePrefix", None))
    return test
