import json
import unittest
from unittest.mock import patch
import custom_connector_example.handlers.lambda_handler as lambda_handler
from custom_connector_example.handlers.salesforce import SalesforceResponse

class SalesforceMetadataHandlerTests(unittest.TestCase):
    """Test class to validate handling of Metadata requests by Salesforce connector."""
    @patch('custom_connector_example.handlers.client.HttpsClient.rest_get')
    def test_list_entities_request_success(self, mock):
        with open('custom_connector_example/test/resources/get_sobjects_server_response.json', 'r') as json_response:
            server_response = json_response.read()
        mock.return_value = SalesforceResponse(200, server_response, '')

        with open('custom_connector_example/test/resources/list_entities_request_valid.json', 'r') as json_file:
            data = json.load(json_file)

        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), True)

    @patch('custom_connector_example.handlers.client.HttpsClient.rest_get')
    def test_list_entities_request_no_path(self, mock):
        with open('custom_connector_example/test/resources/get_sobjects_server_response.json', 'r') as json_response:
            server_response = json_response.read()
        mock.return_value = SalesforceResponse(200, server_response, '')

        with open('custom_connector_example/test/resources/list_entities_request_no_path.json', 'r') as json_file:
            data = json.load(json_file)

        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), True)

    @patch('custom_connector_example.handlers.client.HttpsClient.rest_get')
    def test_list_entities_request_no_sobjects(self, mock):
        with open('custom_connector_example/test/resources/null_sobjects_server_response.json', 'r') as json_response:
            server_response = json_response.read()
        mock.return_value = SalesforceResponse(200, server_response, '')

        with open('custom_connector_example/test/resources/list_entities_request_no_path.json', 'r') as json_file:
            data = json.load(json_file)

        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), True)

    @patch('custom_connector_example.handlers.client.HttpsClient.rest_get')
    def test_list_entities_request_server_error(self, mock):
        mock.return_value = SalesforceResponse(500, '', 'Internal server error')

        with open('custom_connector_example/test/resources/list_entities_request_valid.json', 'r') as json_file:
            data = json.load(json_file)

        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), False)

    @patch('custom_connector_example.handlers.client.HttpsClient.rest_get')
    def test_list_entities_request_invalid_context(self, mock):
        with open('custom_connector_example/test/resources/get_sobjects_server_response.json', 'r') as json_response:
            server_response = json_response.read()
        mock.return_value = SalesforceResponse(200, server_response, '')

        with open('custom_connector_example/test/resources/list_entities_request_invalid.json', 'r') as json_file:
            data = json.load(json_file)

        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), False)

    @patch('custom_connector_example.handlers.client.HttpsClient.rest_get')
    def test_describe_entity_request_success(self, mock):
        with open('custom_connector_example/test/resources/describe_sobject_server_response.json',
                  'r') as json_response:
            server_response = json_response.read()
        mock.return_value = SalesforceResponse(200, server_response, '')

        with open('custom_connector_example/test/resources/describe_entity_request_valid.json', 'r') as json_file:
            data = json.load(json_file)

        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), True)

    @patch('custom_connector_example.handlers.client.HttpsClient.rest_get')
    def test_describe_entity_request_server_error(self, mock):
        mock.return_value = SalesforceResponse(500, '{}', 'Internal server error')

        with open('custom_connector_example/test/resources/describe_entity_request_valid.json', 'r') as json_file:
            data = json.load(json_file)

        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), False)

    @patch('custom_connector_example.handlers.client.HttpsClient.rest_get')
    def test_describe_entity_request_invalid_context(self, mock):
        with open('custom_connector_example/test/resources/describe_sobject_server_response.json',
                  'r') as json_response:
            server_response = json_response.read()
        mock.return_value = SalesforceResponse(200, server_response, '')

        with open('custom_connector_example/test/resources/describe_entity_request_invalid.json', 'r') as json_file:
            data = json.load(json_file)

        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), False)
