import json
import unittest
from unittest.mock import patch
import custom_connector_example.handlers.lambda_handler as lambda_handler
from custom_connector_example.handlers.salesforce import SalesforceResponse

class SalesforceConfigurationHandlerTests(unittest.TestCase):
    """Test class to validate handling of Configuration requests by Salesforce connector."""
    def test_validate_connector_runtime_settings_request_valid(self):
        with open('custom_connector_example/test/resources/validate_connector_runtime_settings_request_valid.json',
                  'r') as json_file:
            data = json.load(json_file)
        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), True)

    def test_validate_connector_runtime_settings_request_invalid(self):
        with open('custom_connector_example/test/resources/validate_connector_runtime_settings_request_invalid.json',
                  'r') as json_file:
            data = json.load(json_file)
        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), False)

    @patch('custom_connector_example.handlers.client.HttpsClient.rest_get')
    def test_validate_credentials_request_success(self, mock):
        mock.return_value = SalesforceResponse(200, '{}', '')

        with open('custom_connector_example/test/resources/validate_credentials_request_valid.json',
                  'r') as json_file:
            data = json.load(json_file)
        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), True)

    @patch('custom_connector_example.handlers.client.HttpsClient.rest_get')
    def test_validate_credentials_request_failure(self, mock):
        mock.return_value = SalesforceResponse(401, '{}', 'Invalid Credentials')

        with open('custom_connector_example/test/resources/validate_credentials_request_valid.json',
                  'r') as json_file:
            data = json.load(json_file)
        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), False)

    def test_validate_credentials_request_invalid(self):
        with open('custom_connector_example/test/resources/validate_credentials_request_invalid.json',
                  'r') as json_file:
            data = json.load(json_file)
        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), False)

    def test_describe_connector_configuration_request(self):
        with open('custom_connector_example/test/resources/describe_connector_configuration_request_valid.json',
                  'r') as json_file:
            data = json.load(json_file)
        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), True)
