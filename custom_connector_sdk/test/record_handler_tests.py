import json
import unittest
from custom_connector_sdk.connector.auth import AuthenticationType
import custom_connector_sdk.lambda_handler.requests as requests
import custom_connector_sdk.lambda_handler.responses as responses

class RecordHandlerTests(unittest.TestCase):
    """Unit tests for RecordHandler requests and responses."""
    def test_create_retrieve_data_request_with_required_parameters(self):
        """Tests that a RetrieveDataRequest can be created with only required parameters."""
        with open('custom_connector_sdk/test/resources/retrieve_data_request_required.json', 'r') as json_file:
            data = json.load(json_file)

        request = requests.RetrieveDataRequest.from_dict(data)
        self.assertIsInstance(request, requests.RetrieveDataRequest)
        self.assertEqual(request.entity_identifier, 'identifier')
        self.assertEqual(request.connector_context.api_version, 'v47.0')
        self.assertIsNotNone(request.connector_context.credentials.secret_arn)
        self.assertEqual(request.connector_context.credentials.authentication_type, AuthenticationType.OAuth2)

    def test_create_retrieve_data_request_with_optional_parameters(self):
        """Tests that a RetrieveDataRequest can be created with optional parameters."""
        with open('custom_connector_sdk/test/resources/retrieve_data_request_optional.json', 'r') as json_file:
            data = json.load(json_file)

        request = requests.RetrieveDataRequest.from_dict(data)
        self.assertIsInstance(request, requests.RetrieveDataRequest)
        self.assertEqual(request.connector_context.entity_definition.fields[0].description, 'testFieldDescription')
        self.assertEqual(request.connector_context.connector_runtime_settings['instanceUrl'], 'test.amazon.com')
        self.assertEqual(request.selected_field_names, ['fieldA', 'fieldB'])
        self.assertEqual(request.id_field_name, 'idField')
        self.assertEqual(request.ids, ['idA', 'idB'])

    def test_create_retrieve_data_request_without_required_parameters(self):
        """Tests that a RetrieveDataRequest CANNOT be created without required parameters."""
        with open('custom_connector_sdk/test/resources/retrieve_data_request_invalid.json', 'r') as json_file:
            data = json.load(json_file)

        self.assertRaises(AssertionError, requests.RetrieveDataRequest.from_dict, data)

    def test_create_write_data_request_with_required_parameters(self):
        """Tests that a WriteDataRequest can be created with only required parameters."""
        with open('custom_connector_sdk/test/resources/write_data_request_required.json', 'r') as json_file:
            data = json.load(json_file)

        request = requests.WriteDataRequest.from_dict(data)
        self.assertIsInstance(request, requests.WriteDataRequest)
        self.assertEqual(request.entity_identifier, 'identifier')
        self.assertEqual(request.connector_context.api_version, 'v47.0')
        self.assertIsNotNone(request.connector_context.credentials.secret_arn)
        self.assertEqual(request.connector_context.credentials.authentication_type, AuthenticationType.OAuth2)

    def test_create_write_data_request_with_optional_parameters(self):
        """Tests that a WriteDataRequest can be created with optional parameters."""
        with open('custom_connector_sdk/test/resources/write_data_request_optional.json', 'r') as json_file:
            data = json.load(json_file)

        request = requests.WriteDataRequest.from_dict(data)
        self.assertIsInstance(request, requests.WriteDataRequest)
        self.assertEqual(request.operation.name, 'UPDATE')
        self.assertEqual(request.connector_context.entity_definition.entity.has_nested_entities, True)
        self.assertEqual(request.id_field_names, ['idFieldA', 'idFieldB'])
        self.assertEqual(request.records, ['recordA', 'recordB'])
        self.assertEqual(request.all_or_none, False)

    def test_create_write_data_request_without_required_parameters(self):
        """Tests that a WriteDataRequest CANNOT be created without required parameters."""
        with open('custom_connector_sdk/test/resources/write_data_request_invalid.json', 'r') as json_file:
            data = json.load(json_file)

        self.assertRaises(AssertionError, requests.WriteDataRequest.from_dict, data)

    def test_create_query_data_request_with_required_parameters(self):
        """Tests that a QueryDataRequest can be created with only required parameters."""
        with open('custom_connector_sdk/test/resources/query_data_request_required.json', 'r') as json_file:
            data = json.load(json_file)

        request = requests.QueryDataRequest.from_dict(data)
        self.assertIsInstance(request, requests.QueryDataRequest)
        self.assertEqual(request.entity_identifier, 'identifier')
        self.assertIsNotNone(request.connector_context.credentials.secret_arn)
        self.assertEqual(request.connector_context.credentials.authentication_type, AuthenticationType.BasicAuth)
        self.assertEqual(request.max_results, requests.DEFAULT_MAX_RESULT)

    def test_create_query_data_request_with_optional_parameters(self):
        """Tests that a QueryDataRequest can be created with optional parameters."""
        with open('custom_connector_sdk/test/resources/query_data_request_optional.json', 'r') as json_file:
            data = json.load(json_file)

        request = requests.QueryDataRequest.from_dict(data)
        self.assertIsInstance(request, requests.QueryDataRequest)
        self.assertEqual(request.connector_context.entity_definition.fields[0].constraints.allowed_length_range
                         .max_range, 30)
        self.assertEqual(request.selected_field_names, ['fieldA', 'fieldB'])
        self.assertEqual(request.next_token, 'testToken')
        self.assertEqual(request.max_results, 50)

    def test_create_query_data_request_without_required_parameters(self):
        """Tests that a QueryDataRequest CANNOT be created without required parameters."""
        with open('custom_connector_sdk/test/resources/query_data_request_invalid.json', 'r') as json_file:
            data = json.load(json_file)

        self.assertRaises(AssertionError, requests.QueryDataRequest.from_dict, data)

    def test_create_retrieve_data_response_with_required_parameters(self):
        """Tests that a RetrieveDataResponse can be created with only required parameters."""
        response = responses.RetrieveDataResponse(is_success=False)
        encoded_response = response.to_json()

        with open('custom_connector_sdk/test/resources/retrieve_data_response_required.json', 'r') as json_file:
            expected = json.dumps(json.load(json_file))

        self.assertEqual(encoded_response, expected)

    def test_create_retrieve_data_response_with_optional_parameters(self):
        """Tests that a RetrieveDataResponse can be created with optional parameters."""
        error_details = responses.ErrorDetails(responses.ErrorCode.ClientError, 'test error', 120)
        records = ['recordA', 'recordB']

        response = responses.RetrieveDataResponse(is_success=False, error_details=error_details, records=records)
        encoded_response = response.to_json()

        with open('custom_connector_sdk/test/resources/retrieve_data_response_optional.json', 'r') as json_file:
            expected = json.dumps(json.load(json_file))

        self.assertEqual(encoded_response, expected)

    def test_create_retrieve_data_response_without_required_parameters(self):
        """Tests that a RetrieveDataResponse CANNOT be created without required parameters."""
        error_details = responses.ErrorDetails(responses.ErrorCode.ClientError, 'test error', 120)
        records = ['recordA', 'recordB', 'recordC']

        self.assertRaises(TypeError, responses.RetrieveDataResponse, error_details=error_details, records=records)

    def test_create_write_data_response_with_required_parameters(self):
        """Tests that a WriteDataResponse can be created with only required parameters."""
        response = responses.WriteDataResponse(is_success=False)
        encoded_response = response.to_json()

        with open('custom_connector_sdk/test/resources/write_data_response_required.json', 'r') as json_file:
            expected = json.dumps(json.load(json_file))

        self.assertEqual(encoded_response, expected)

    def test_create_write_data_response_with_optional_parameters(self):
        """Tests that a WriteDataResponse can be created with optional parameters."""
        error_details = responses.ErrorDetails(responses.ErrorCode.ClientError, 'test error', 120)
        result = responses.WriteRecordResult(is_success=False, record_id='testId', error_message='write error')

        response = responses.WriteDataResponse(is_success=False,
                                               error_details=error_details,
                                               write_record_results=result)
        encoded_response = response.to_json()

        with open('custom_connector_sdk/test/resources/write_data_response_optional.json', 'r') as json_file:
            expected = json.dumps(json.load(json_file))

        self.assertEqual(encoded_response, expected)

    def test_create_write_data_response_without_required_parameters(self):
        """Tests that a WriteDataResponse CANNOT be created without required parameters"""
        result = responses.WriteRecordResult(is_success=False, record_id='testId', error_message='write error')

        self.assertRaises(TypeError, responses.WriteDataResponse, write_record_results=result)

    def test_create_query_data_response_with_required_parameters(self):
        """Tests that a QueryDataResponse can be created with only required parameters."""
        response = responses.QueryDataResponse(is_success=True)
        encoded_response = response.to_json()

        with open('custom_connector_sdk/test/resources/query_data_response_required.json', 'r') as json_file:
            expected = json.dumps(json.load(json_file))

        self.assertEqual(encoded_response, expected)

    def test_create_query_data_response_with_optional_parameters(self):
        """Tests that a QueryDataResponse can be created with optional parameters."""
        error_details = responses.ErrorDetails(responses.ErrorCode.ClientError, 'test error', 120)
        records = ['recordA', 'recordB']

        response = responses.QueryDataResponse(is_success=False,
                                               error_details=error_details,
                                               next_token='testToken',
                                               records=records)
        encoded_response = response.to_json()

        with open('custom_connector_sdk/test/resources/query_data_response_optional.json', 'r') as json_file:
            expected = json.dumps(json.load(json_file))

        self.assertEqual(encoded_response, expected)

    def test_create_query_data_response_without_required_parameters(self):
        """Tests that a QueryDataResponse CANNOT be created without required parameters"""
        self.assertRaises(TypeError, responses.QueryDataResponse)
