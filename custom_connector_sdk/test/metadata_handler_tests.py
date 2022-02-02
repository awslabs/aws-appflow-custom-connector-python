import json
import unittest
from custom_connector_sdk.connector.auth import AuthenticationType
import custom_connector_sdk.lambda_handler.requests as requests
import custom_connector_sdk.lambda_handler.responses as responses
import custom_connector_sdk.connector.settings as settings

class MetadataHandlerTests(unittest.TestCase):
    """Unit tests for MetadataHandler requests and responses."""
    def test_create_describe_entity_request_with_required_parameters(self):
        """Tests that a DescribeEntityRequest can be created with only the required parameters."""
        with open('custom_connector_sdk/test/resources/describe_entity_request_required.json', 'r') as json_file:
            data = json.load(json_file)

        request = requests.DescribeEntityRequest.from_dict(data)
        self.assertIsInstance(request, requests.DescribeEntityRequest)
        self.assertEqual(request.connector_context.api_version, 'v47.0')
        self.assertIsNotNone(request.connector_context.credentials.secret_arn)
        self.assertEqual(request.connector_context.credentials.authentication_type, AuthenticationType.BasicAuth)

    def test_create_describe_entity_request_with_optional_parameters(self):
        """Tests that a DescribeEntityRequest can be created with optional parameters."""
        with open('custom_connector_sdk/test/resources/describe_entity_request_optional.json', 'r') as json_file:
            data = json.load(json_file)

        request = requests.DescribeEntityRequest.from_dict(data)
        self.assertIsInstance(request, requests.DescribeEntityRequest)
        self.assertEqual(request.connector_context.entity_definition.fields[0].field_name, 'testField')
        self.assertIsNotNone(request.connector_context.credentials.secret_arn)
        self.assertEqual(request.connector_context.credentials.authentication_type, AuthenticationType.OAuth2)
        self.assertEqual(request.connector_context.entity_definition.custom_properties['customProperty'],
                         'customPropertyValue')

    def test_create_describe_entity_request_without_required_parameters(self):
        """Tests that a DescribeEntityRequest CANNOT be created without required parameters."""
        with open('custom_connector_sdk/test/resources/describe_entity_request_invalid.json', 'r') as json_file:
            data = json.load(json_file)

        self.assertRaises(AssertionError, requests.DescribeEntityRequest.from_dict, data)

    def test_create_list_entities_request_with_required_parameters(self):
        """Tests that a ListEntitiesRequest can be created with only required parameters."""
        with open('custom_connector_sdk/test/resources/list_entities_request_required.json', 'r') as json_file:
            data = json.load(json_file)

        request = requests.ListEntitiesRequest.from_dict(data)
        self.assertIsInstance(request, requests.ListEntitiesRequest)
        self.assertEqual(request.connector_context.api_version, 'v47.0')
        self.assertEqual(request.max_result, None)
        self.assertIsNotNone(request.connector_context.credentials.secret_arn)
        self.assertEqual(request.connector_context.credentials.authentication_type, AuthenticationType.BasicAuth)

    def test_create_list_entities_request_with_optional_parameters(self):
        """Tests that a ListEntitiesRequest can be created with optional parameters."""
        with open('custom_connector_sdk/test/resources/list_entities_request_optional.json', 'r') as json_file:
            data = json.load(json_file)

        request = requests.ListEntitiesRequest.from_dict(data)
        self.assertIsInstance(request, requests.ListEntitiesRequest)
        self.assertEqual(request.max_result, 500)
        self.assertIsNotNone(request.connector_context.credentials.secret_arn)
        self.assertEqual(request.connector_context.credentials.authentication_type, AuthenticationType.OAuth2)
        self.assertEqual(request.connector_context.entity_definition.fields[0].sub_fields[0].field_name, 'subFieldName')
        self.assertEqual(request.connector_context.entity_definition.fields[0].filter_operators, [])

    def test_create_list_entities_request_without_required_parameters(self):
        """Tests that a ListEntitiesRequest CANNOT be created without required parameters."""
        with open('custom_connector_sdk/test/resources/list_entities_request_invalid.json', 'r') as json_file:
            data = json.load(json_file)

        self.assertRaises(AssertionError, requests.ListEntitiesRequest.from_dict, data)

    def test_create_describe_entity_response_with_required_parameters(self):
        """Tests that a DescribeEntityResponse can be created with only required parameters."""
        response = responses.DescribeEntityResponse(is_success=True)
        encoded_response = response.to_json()

        with open('custom_connector_sdk/test/resources/describe_entity_response_required.json', 'r') as json_file:
            expected = json.dumps(json.load(json_file))

        self.assertEqual(encoded_response, expected)

    def test_create_describe_entity_response_with_optional_parameters(self):
        """Tests that a DescribeEntityResponse can be created with optional parameters."""
        error_details = responses.ErrorDetails(responses.ErrorCode.ServerError, 'this is an error', 20)
        cache_control = settings.CacheControl(60, settings.TimeUnit.SECONDS)

        response = responses.DescribeEntityResponse(is_success=True,
                                                    error_details=error_details,
                                                    cache_control=cache_control)
        encoded_response = response.to_json()

        with open('custom_connector_sdk/test/resources/describe_entity_response_optional.json', 'r') as json_file:
            expected = json.dumps(json.load(json_file))

        self.assertEqual(encoded_response, expected)

    def test_create_describe_entity_response_without_required_parameters(self):
        """Tests that a DescribeEntityResponse CANNOT be created without required parameters."""
        error_details = responses.ErrorDetails(responses.ErrorCode.ServerError, 'this is an error', 20)
        cache_control = (60, settings.TimeUnit.SECONDS)

        self.assertRaises(TypeError,
                          responses.DescribeEntityResponse,
                          error_details=error_details,
                          cache_control=cache_control)

    def test_create_list_entities_response_with_required_parameters(self):
        """Tests that a ListEntitiesResponse can be created with only required parameters."""
        response = responses.ListEntitiesResponse(is_success=True)
        encoded_response = response.to_json()

        with open('custom_connector_sdk/test/resources/list_entities_response_required.json', 'r') as json_file:
            expected = json.dumps(json.load(json_file))

        self.assertEqual(encoded_response, expected)

    def test_create_list_entities_response_with_optional_parameters(self):
        """Tests that a ListEntitiesResponse can be created with optional parameters."""
        error_details = responses.ErrorDetails(responses.ErrorCode.ServerError, 'this is an error', 20)
        cache_control = settings.CacheControl(60, settings.TimeUnit.SECONDS)

        response = responses.ListEntitiesResponse(is_success=True,
                                                  error_details=error_details,
                                                  next_token='2',
                                                  cache_control=cache_control)
        encoded_response = response.to_json()

        with open('custom_connector_sdk/test/resources/list_entities_response_optional.json', 'r') as json_file:
            expected = json.dumps(json.load(json_file))

        self.assertEqual(encoded_response, expected)

    def test_create_list_entities_response_without_required_parameters(self):
        """Tests that a ListEntitiesResponse CANNOT be created without required parameters."""
        error_details = responses.ErrorDetails(responses.ErrorCode.ServerError, 'this is an error', 20)
        cache_control = (60, settings.TimeUnit.SECONDS)

        self.assertRaises(TypeError,
                          responses.ListEntitiesResponse,
                          error_details=error_details,
                          cache_control=cache_control)
