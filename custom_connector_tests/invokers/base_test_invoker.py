import logging
import sys

import custom_connector_sdk.lambda_handler.requests as requests
import custom_connector_sdk.lambda_handler.responses as responses
import custom_connector_sdk.lambda_handler.lambda_handler as handler
import custom_connector_sdk.connector.context as context
from custom_connector_tests.invokers.test_invoker import ConnectorTestInvoker
from custom_connector_sdk.lambda_handler.lambda_handler import BaseLambdaConnectorHandler
from custom_connector_sdk.connector.settings import ConnectorRuntimeSettingScope
from custom_connector_tests.validation.connector_configuration_validator \
    import validate_connector_configuration_response

EVENT_TYPE = "type"
RUNTIME_SETTINGS = "runtimeSettings"
CONNECTOR_PROFILE = "connectorProfile"
SOURCE = "source"
DESTINATION = "destination"
CREDENTIALS = "credentials"
TEST_ENTITY_IDENTIFIER = "testEntityIdentifier"
ENTITY_IDENTIFIER = "entityIdentifier"
SELECTED_FIELD_NAMES = "selectedFieldNames"
ID_FIELD_NAME = "idFieldName"
IDS = "ids"
OPERATION = "operation"
RECORDS = "records"
ID_FIELD_NAMES = "idFieldNames"
ALL_OR_NONE = "allOrNone"
FILTER_EXPRESSION = "filterExpression"
API_VERSION = "apiVersion"
RETRIEVE_RECORD_CONFIGURATIONS = "retrieveRecordConfigurations"
WRITE_RECORD_CONFIGURATIONS = "writeRecordConfigurations"
QUERY_RECORD_CONFIGURATIONS = "queryRecordConfigurations"

class BaseConnectorTestInvoker(ConnectorTestInvoker):
    def __init__(self, connector_handler: BaseLambdaConnectorHandler, test_config):
        self.connector_handler = connector_handler
        self.test_config = test_config
        logging.basicConfig()
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        self.logger = logger

    def invoke_configuration_handler_tests(self):
        test_config = self.test_config
        logger = self.logger
        logger.info("-----------Starting verification tests for Configuration Handler-----------")

        try:
            if CONNECTOR_PROFILE in test_config[RUNTIME_SETTINGS]:
                logger.info("Testing ValidateConnectorRuntimeSettings for ConnectorProfile...")
                event = {
                    EVENT_TYPE: handler.VALIDATE_CONNECTOR_RUNTIME_SETTINGS,
                    requests.SCOPE: ConnectorRuntimeSettingScope.CONNECTOR_PROFILE.name,
                    requests.CONNECTOR_RUNTIME_SETTINGS: test_config[RUNTIME_SETTINGS][CONNECTOR_PROFILE]
                }

                response = self.connector_handler.lambda_handler(event, None)
                assert response
                assert response[responses.IS_SUCCESS], "Validate Connector Runtime response was unsuccessful for the provided TestConfiguration"

            if SOURCE in test_config[RUNTIME_SETTINGS]:
                logger.info("Testing ValidateConnectorRuntimeSettings for Source...")
                event = {
                    EVENT_TYPE: handler.VALIDATE_CONNECTOR_RUNTIME_SETTINGS,
                    requests.SCOPE: ConnectorRuntimeSettingScope.SOURCE.name,
                    requests.CONNECTOR_RUNTIME_SETTINGS: test_config[RUNTIME_SETTINGS][SOURCE]
                }

                response = self.connector_handler.lambda_handler(event, None)
                assert response
                assert response[responses.IS_SUCCESS], "Validate Connector Runtime response was unsuccessful for the provided TestConfiguration"

            if DESTINATION in test_config[RUNTIME_SETTINGS]:
                logger.info("Testing ValidateConnectorRuntimeSettings for Destination...")
                event = {
                    EVENT_TYPE: handler.VALIDATE_CONNECTOR_RUNTIME_SETTINGS,
                    requests.SCOPE: ConnectorRuntimeSettingScope.DESTINATION.name,
                    requests.CONNECTOR_RUNTIME_SETTINGS: test_config[RUNTIME_SETTINGS][DESTINATION]
                }

                response = self.connector_handler.lambda_handler(event, None)
                assert response
                assert response[responses.IS_SUCCESS], "Validate Connector Runtime response was unsuccessful for the provided TestConfiguration"

            logger.info("Testing ValidateCredentials...")
            event = {
                EVENT_TYPE: handler.VALIDATE_CREDENTIALS,
                requests.CREDENTIALS: test_config[CREDENTIALS],
                requests.CONNECTOR_RUNTIME_SETTINGS: self.__build_connector_runtime_settings_map()
            }

            response = self.connector_handler.lambda_handler(event, None)
            assert response
            assert response[responses.IS_SUCCESS], "Validate Credentials response was unsuccessful for the provided TestConfiguration"

            logger.info("Testing DescribeConnectorConfiguration...")
            event = {
                EVENT_TYPE: handler.DESCRIBE_CONNECTOR_CONFIGURATION
            }

            response = self.connector_handler.lambda_handler(event, None)
            assert response
            assert response[responses.IS_SUCCESS], "Describe Connector Configuration response was unsuccessful for the provided TestConfiguration"
            assert response[responses.CONNECTOR_NAME], "Connector Name is required in Describe Connector Configuration"
            assert response[responses.CONNECTOR_OWNER], "Connector Owner is required in Describe Connector Configuration"
            assert response[responses.CONNECTOR_VERSION], "Connector Version is required in Describe Connector Configuration"
            validate_connector_configuration_response(response)

            logger.info("Configuration handler was verified successfully!")
        except Exception as e:
            logger.error("Error encountered during ConfigurationHandler verification!")
            logger.error("Verification tests failed for the given Connector Handler. See logs for details")
            print(e)
            sys.exit(1)

    def invoke_metadata_handler_tests(self):
        test_config = self.test_config
        logger = self.logger
        logger.info("-----------Starting verification tests for Metadata Handler-----------")

        try:
            test_entity_identifier = test_config[TEST_ENTITY_IDENTIFIER]
            logger.info("Testing ListEntities...");
            event = {
                EVENT_TYPE: handler.LIST_ENTITIES,
                requests.CONNECTOR_CONTEXT: self.__build_connector_context(),
                requests.ENTITIES_PATH: test_entity_identifier
            }

            response = self.connector_handler.lambda_handler(event, None)
            assert response
            assert response[responses.IS_SUCCESS], f'List Entities response returned unsuccessful response for entityId: {test_entity_identifier}'
            assert response[responses.ENTITIES], f'No Entities were returned for entityId: {test_entity_identifier}. Please use a valid entity with existing records'

            logger.info("Testing DescribeEntity...")
            event = {
                EVENT_TYPE: handler.DESCRIBE_ENTITY,
                requests.CONNECTOR_CONTEXT: self.__build_connector_context(),
                requests.ENTITY_IDENTIFIER: test_entity_identifier
            }

            response = self.connector_handler.lambda_handler(event, None)
            assert response
            assert response[responses.IS_SUCCESS], f'Describe Entity response returned unsuccessful response for entityId: {test_entity_identifier}'
            assert response[responses.ENTITY_DEFINITION], f'EntityDefinition was null for entityId: {test_entity_identifier}. Describe Entity response should contain definition'

            logger.info("Metadata handler was verified successfully!")
        except Exception as e:
            logger.error("Error encountered during MetadataHandler verification!")
            logger.error("Verification tests failed for the given Connector Handler. See logs for details")
            print(e)
            sys.exit(1)

    def invoke_record_handler_tests(self):
        test_config = self.test_config
        logger = self.logger
        logger.info("-----------Starting verification tests for Record Handler-----------")

        try:
            if RETRIEVE_RECORD_CONFIGURATIONS in test_config:
                for index, configuration in enumerate(test_config[RETRIEVE_RECORD_CONFIGURATIONS]):
                    logger.info(f'Testing RetrieveData configuration {index}...')
                    entity_identifier = configuration[ENTITY_IDENTIFIER]

                    event = {
                        EVENT_TYPE: handler.RETRIEVE_DATA,
                        requests.CONNECTOR_CONTEXT: self.__build_test_config_connector_context(entity_identifier),
                        requests.ENTITY_IDENTIFIER: entity_identifier,
                        requests.SELECTED_FIELD_NAMES: configuration[SELECTED_FIELD_NAMES]
                    }

                    # Optional arguments
                    if ID_FIELD_NAME in configuration:
                        event[requests.ID_FIELD_NAME] = configuration[ID_FIELD_NAME]
                    if IDS in configuration:
                        event[requests.IDS] = configuration[IDS]

                    response = self.connector_handler.lambda_handler(event, None)
                    assert response
                    assert response[responses.IS_SUCCESS], "Retrieve Data response returned unsuccessful response for the provided TestConfiguration"
                    assert response[responses.RECORDS], f'Retrieve Data response does not have any records for entityId: {entity_identifier}. Please use an EntityId that contains records'

            if WRITE_RECORD_CONFIGURATIONS in test_config:
                for index, configuration in enumerate(test_config[WRITE_RECORD_CONFIGURATIONS]):
                    logger.info(f'Testing WriteData configuration {index}...')
                    entity_identifier = configuration[ENTITY_IDENTIFIER]

                    event = {
                        EVENT_TYPE: handler.WRITE_DATA,
                        requests.CONNECTOR_CONTEXT: self.__build_test_config_connector_context(entity_identifier),
                        requests.ENTITY_IDENTIFIER: entity_identifier,
                    }

                    # Optional arguments
                    if OPERATION in configuration:
                        event[requests.OPERATION] = configuration[OPERATION]
                    if RECORDS in configuration:
                        event[requests.RECORDS] = configuration[RECORDS]
                    if ID_FIELD_NAMES in configuration:
                        event[requests.ID_FIELD_NAMES] = configuration[ID_FIELD_NAMES]
                    if ALL_OR_NONE in configuration:
                        event[requests.ALL_OR_NONE] = configuration[ALL_OR_NONE]

                    response = self.connector_handler.lambda_handler(event, None)
                    assert response
                    assert response[responses.IS_SUCCESS], f'Write Data response returned unsuccessful response for entityId: {entity_identifier} and operation: {configuration[OPERATION]}'

            if QUERY_RECORD_CONFIGURATIONS in test_config:
                for index, configuration in enumerate(test_config[QUERY_RECORD_CONFIGURATIONS]):
                    logger.info(f'Testing QueryData configuration {index}...')
                    entity_identifier = configuration[ENTITY_IDENTIFIER]

                    event = {
                        EVENT_TYPE: handler.QUERY_DATA,
                        requests.CONNECTOR_CONTEXT: self.__build_test_config_connector_context(entity_identifier),
                        requests.ENTITY_IDENTIFIER: entity_identifier,
                        requests.SELECTED_FIELD_NAMES: configuration[SELECTED_FIELD_NAMES],
                    }

                    # Optional arguments
                    if FILTER_EXPRESSION in configuration:
                        event[requests.FILTER_EXPRESSION] = configuration[FILTER_EXPRESSION]

                    response = self.connector_handler.lambda_handler(event, None)
                    assert response
                    assert response[responses.IS_SUCCESS], f'Query Data response returned unsuccessful response for entityId: {entity_identifier} and filter: {configuration[FILTER_EXPRESSION]}'
                    assert response[responses.RECORDS], f'Query Data response returned no records for entityId: {entity_identifier} and filter: {configuration[FILTER_EXPRESSION]}. Please use a valid expression that returns some records'

        except Exception as e:
            logger.error("Error encountered during RecordHandler verification!")
            logger.error("Verification tests failed for the given Connector Handler. See logs for details")
            print(e)
            sys.exit(1)

    def __build_connector_runtime_settings_map(self) -> dict:
        test_config = self.test_config
        runtime_settings = {}
        for scope in [CONNECTOR_PROFILE, SOURCE, DESTINATION]:
            if scope in test_config[RUNTIME_SETTINGS]:
                runtime_settings.update(test_config[RUNTIME_SETTINGS][scope])

        return runtime_settings

    def __build_connector_context(self) -> dict:
        test_config = self.test_config
        return {
            requests.CONNECTOR_RUNTIME_SETTINGS: self.__build_connector_runtime_settings_map(),
            requests.CREDENTIALS: test_config[CREDENTIALS],
            context.API_VERSION: test_config[RUNTIME_SETTINGS][CONNECTOR_PROFILE][API_VERSION]
        }

    def __build_test_config_connector_context(self, entity_identifier) -> dict:
        test_config = self.test_config
        event = {
            EVENT_TYPE: handler.DESCRIBE_ENTITY,
            requests.CONNECTOR_CONTEXT: self.__build_connector_context(),
            requests.ENTITY_IDENTIFIER: entity_identifier
        }
        describe_entity_response = self.connector_handler.lambda_handler(event, None)

        return {
            requests.CONNECTOR_RUNTIME_SETTINGS: self.__build_connector_runtime_settings_map(),
            requests.CREDENTIALS: test_config[CREDENTIALS],
            context.API_VERSION: test_config[RUNTIME_SETTINGS][CONNECTOR_PROFILE][API_VERSION],
            context.ENTITY_DEFINITION: describe_entity_response[responses.ENTITY_DEFINITION]
        }
