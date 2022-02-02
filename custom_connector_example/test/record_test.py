import json
import unittest
from unittest.mock import patch
import custom_connector_example.handlers.lambda_handler as lambda_handler
from custom_connector_example.handlers.salesforce import SalesforceResponse

class SalesforceRecordHandlerTests(unittest.TestCase):
    """Test class to validate handling of Record requests by Salesforce connector."""
    @patch('custom_connector_example.handlers.client.HttpsClient.rest_get')
    def test_retrieve_data_request_success(self, mock):
        with open('custom_connector_example/test/resources/describe_sobject_server_response.json',
                  'r') as json_response:
            server_response = json_response.read()
        mock.return_value = SalesforceResponse(200, server_response, '')

        with open('custom_connector_example/test/resources/retrieve_data_request_valid.json', 'r') as json_file:
            data = json.load(json_file)

        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), True)

    @patch('custom_connector_example.handlers.client.HttpsClient.rest_get')
    def test_retrieve_data_request_no_matches(self, mock):
        mock.return_value = SalesforceResponse(200, '{}', '')

        with open('custom_connector_example/test/resources/retrieve_data_request_valid.json', 'r') as json_file:
            data = json.load(json_file)

        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), True)

    @patch('custom_connector_example.handlers.client.HttpsClient.rest_get')
    def test_retrieve_data_request_server_error(self, mock):
        mock.return_value = SalesforceResponse(400, '{}', 'Invalid argument')

        with open('custom_connector_example/test/resources/retrieve_data_request_valid.json', 'r') as json_file:
            data = json.load(json_file)

        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), False)

    @patch('custom_connector_example.handlers.client.HttpsClient.rest_get')
    def test_retrieve_data_request_invalid_context(self, mock):
        with open('custom_connector_example/test/resources/describe_sobject_server_response.json',
                  'r') as json_response:
            server_response = json_response.read()
        mock.return_value = SalesforceResponse(200, server_response, '')

        with open('custom_connector_example/test/resources/retrieve_data_request_invalid.json', 'r') as json_file:
            data = json.load(json_file)

        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), False)

    @patch('custom_connector_example.handlers.client.HttpsClient.rest_post')
    def test_write_data_request_success(self, mock):
        mock.return_value = SalesforceResponse(200, '{}', '')

        with open('custom_connector_example/test/resources/write_data_request_valid.json', 'r') as json_file:
            data = json.load(json_file)

        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), True)

    @patch('custom_connector_example.handlers.client.HttpsClient.rest_post')
    def test_write_data_request_server_error(self, mock):
        mock.return_value = SalesforceResponse(401, '{}', 'Invalid credentials')

        with open('custom_connector_example/test/resources/write_data_request_valid.json', 'r') as json_file:
            data = json.load(json_file)

        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), False)

    @patch('custom_connector_example.handlers.client.HttpsClient.rest_post')
    def test_write_data_request_invalid_context(self, mock):
        mock.return_value = SalesforceResponse(200, '{}', '')

        with open('custom_connector_example/test/resources/write_data_request_invalid.json', 'r') as json_file:
            data = json.load(json_file)

        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), False)

    @patch('custom_connector_example.handlers.client.HttpsClient.rest_get')
    def test_query_data_request_filter_expression(self, mock):
        mock.return_value = SalesforceResponse(200, '{}', '')

        with open('custom_connector_example/test/resources/query_data_request_filter_expression.json',
                  'r') as json_file:
            data = json.load(json_file)

        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), True)

    @patch('custom_connector_example.handlers.client.HttpsClient.rest_get')
    def test_query_data_request_no_filter_expression(self, mock):
        mock.return_value = SalesforceResponse(200, '{}', '')

        with open('custom_connector_example/test/resources/query_data_request_no_filter_expression.json',
                  'r') as json_file:
            data = json.load(json_file)

        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), True)

    @patch('custom_connector_example.handlers.client.HttpsClient.rest_get')
    def test_query_data_request_no_selected_fields(self, mock):
        mock.return_value = SalesforceResponse(200, '{}', '')

        with open('custom_connector_example/test/resources/query_data_request_no_selected_fields.json',
                  'r') as json_file:
            data = json.load(json_file)

        self.assertRaises(RuntimeError, lambda_handler.salesforce_lambda_handler, data, None)

    @patch('custom_connector_example.handlers.client.HttpsClient.rest_get')
    def test_query_data_request_server_error(self, mock):
        mock.return_value = SalesforceResponse(400, '{}', 'Argument is invalid')

        with open('custom_connector_example/test/resources/query_data_request_filter_expression.json',
                  'r') as json_file:
            data = json.load(json_file)

        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), False)

    @patch('custom_connector_example.handlers.client.HttpsClient.rest_get')
    def test_query_data_request_invalid_context(self, mock):
        mock.return_value = SalesforceResponse(200, '{}', '')

        with open('custom_connector_example/test/resources/query_data_request_invalid.json', 'r') as json_file:
            data = json.load(json_file)

        response = lambda_handler.salesforce_lambda_handler(data, None)
        self.assertEqual(response.get('isSuccess'), False)
