from custom_connector_example.handlers.record import SalesforceRecordHandler
from custom_connector_example.handlers.metadata import SalesforceMetadataHandler
from custom_connector_example.handlers.configuration import SalesforceConfigurationHandler
from custom_connector_sdk.lambda_handler.lambda_handler import BaseLambdaConnectorHandler

class SalesforceLambdaHandler(BaseLambdaConnectorHandler):
    def __init__(self):
        super().__init__(SalesforceMetadataHandler(), SalesforceRecordHandler(), SalesforceConfigurationHandler())

def salesforce_lambda_handler(event, context):
    """Lambda entry point."""
    return SalesforceLambdaHandler().lambda_handler(event, context)
