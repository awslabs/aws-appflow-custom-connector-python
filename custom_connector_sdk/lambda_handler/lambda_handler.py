import logging
import custom_connector_sdk.lambda_handler.requests as requests
from custom_connector_sdk.lambda_handler.handlers import MetadataHandler, RecordHandler, ConfigurationHandler

VALIDATE_CONNECTOR_RUNTIME_SETTINGS = 'ValidateConnectorRuntimeSettingsRequest'
VALIDATE_CREDENTIALS = 'ValidateCredentialsRequest'
DESCRIBE_CONNECTOR_CONFIGURATION = 'DescribeConnectorConfigurationRequest'
LIST_ENTITIES = 'ListEntitiesRequest'
DESCRIBE_ENTITY = 'DescribeEntityRequest'
RETRIEVE_DATA = 'RetrieveDataRequest'
WRITE_DATA = 'WriteDataRequest'
QUERY_DATA = 'QueryDataRequest'

class BaseLambdaConnectorHandler:
    """Base class for Lambda Connector handlers. It is recommended that all connectors extend this class for Lambda
    operations, though it is possible for you to write your own from the ground up."""
    def __init__(self,
                 metadata_handler: MetadataHandler,
                 record_handler: RecordHandler,
                 configuration_handler: ConfigurationHandler):
        self.metadata_handler = metadata_handler
        self.record_handler = record_handler
        self.configuration_handler = configuration_handler

    def lambda_handler(self, event, context):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        try:
            event_type = event['type']
            logger.info('Handling request for requestType: ' + event_type)

            if event_type == VALIDATE_CONNECTOR_RUNTIME_SETTINGS:
                request = requests.ValidateConnectorRuntimeSettingsRequest.from_dict(event)
                response = self.configuration_handler.validate_connector_runtime_settings(request)
            elif event_type == VALIDATE_CREDENTIALS:
                request = requests.ValidateCredentialsRequest.from_dict(event)
                response = self.configuration_handler.validate_credentials(request)
            elif event_type == DESCRIBE_CONNECTOR_CONFIGURATION:
                request = requests.DescribeConnectorConfigurationRequest.from_dict(event)
                response = self.configuration_handler.describe_connector_configuration(request)
            elif event_type == LIST_ENTITIES:
                request = requests.ListEntitiesRequest.from_dict(event)
                response = self.metadata_handler.list_entities(request)
            elif event_type == DESCRIBE_ENTITY:
                request = requests.DescribeEntityRequest.from_dict(event)
                response = self.metadata_handler.describe_entity(request)
            elif event_type == RETRIEVE_DATA:
                request = requests.RetrieveDataRequest.from_dict(event)
                response = self.record_handler.retrieve_data(request)
            elif event_type == WRITE_DATA:
                request = requests.WriteDataRequest.from_dict(event)
                response = self.record_handler.write_data(request)
            elif event_type == QUERY_DATA:
                request = requests.QueryDataRequest.from_dict(event)
                response = self.record_handler.query_data(request)
            else:
                logger.exception(f'lambda_handler: Request type {event_type} is not supported')
                raise ValueError('No operation is defined for request type: ' + event_type)

            return response.to_dict()
        except Exception:
            logger.exception('lambda_handler: Completed with an exception')
            raise RuntimeError('Exception while processing the request')
