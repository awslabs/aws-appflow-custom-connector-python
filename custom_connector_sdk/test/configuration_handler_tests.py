import json
import unittest
import custom_connector_sdk.lambda_handler.requests as requests
import custom_connector_sdk.lambda_handler.responses as responses
import custom_connector_sdk.connector.settings as settings
from custom_connector_sdk.connector.auth import AuthenticationConfig, AuthParameter, CustomAuthConfig, OAuth2Defaults, OAuth2GrantType, AuthenticationType
from custom_connector_sdk.connector.configuration import ConnectorOperator, TriggerFrequency
from custom_connector_sdk.connector.fields import WriteOperationType

class ConfigurationHandlerTests(unittest.TestCase):
    """Unit tests for ConfigurationHandler requests and responses."""
    def test_create_validate_credentials_request_with_required_parameters(self):
        """Tests that a ValidateCredentialsRequest can be created with only required parameters."""
        with open('custom_connector_sdk/test/resources/validate_credentials_request_required.json', 'r') as json_file:
            data = json.load(json_file)

        request = requests.ValidateCredentialsRequest.from_dict(data)
        self.assertIsInstance(request, requests.ValidateCredentialsRequest)
        self.assertIsNotNone(request.credentials.secret_arn)
        self.assertEqual(request.credentials.authentication_type, AuthenticationType.ApiKey)

    def test_create_validate_credentials_request_with_optional_parameters(self):
        """Tests that a ValidateCredentialsRequest can be created with optional parameters."""
        with open('custom_connector_sdk/test/resources/validate_credentials_request_optional.json', 'r') as json_file:
            data = json.load(json_file)

        request = requests.ValidateCredentialsRequest.from_dict(data)
        self.assertIsInstance(request, requests.ValidateCredentialsRequest)
        self.assertIsNotNone(request.credentials.secret_arn)
        self.assertEqual(request.credentials.authentication_type, AuthenticationType.CustomAuth)
        self.assertEqual(request.connector_runtime_settings['testSettingKey2'], 'testSettingValue2')

    def test_create_validate_credentials_request_without_required_parameters(self):
        """Tests that a ValidateCredentialsRequest CANNOT be created without required parameters."""
        with open('custom_connector_sdk/test/resources/validate_credentials_request_invalid.json', 'r') as json_file:
            data = json.load(json_file)

        self.assertRaises(AssertionError, requests.ValidateCredentialsRequest.from_dict, data)

    def test_create_describe_connector_configuration_request(self):
        """Tests that a DescribeConnectorConfigurationRequest can be created."""
        with open('custom_connector_sdk/test/resources/describe_connector_configuration_request_required.json',
                  'r') as json_file:
            data = json.load(json_file)

        request = requests.DescribeConnectorConfigurationRequest.from_dict(data)
        self.assertIsInstance(request, requests.DescribeConnectorConfigurationRequest)

    def test_create_describe_connector_configuration_request_with_optional_parameters(self):
        """Tests that a DescribeConnectorConfigurationRequest can be created with optional parameters."""
        with open('custom_connector_sdk/test/resources/describe_connector_configuration_request_optional.json',
                  'r') as json_file:
            data = json.load(json_file)

        request = requests.DescribeConnectorConfigurationRequest.from_dict(data)
        self.assertIsInstance(request, requests.DescribeConnectorConfigurationRequest)
        self.assertEqual(request.locale, 'en-US')

    def test_create_validate_connector_runtime_settings_request_with_required_parameters(self):
        """Tests that a ValidateConnectorRuntimeSettingsRequest can be created with required parameters."""
        with open('custom_connector_sdk/test/resources/validate_connector_runtime_settings_request_required.json',
                  'r') as json_file:
            data = json.load(json_file)

        request = requests.ValidateConnectorRuntimeSettingsRequest.from_dict(data)
        self.assertIsInstance(request, requests.ValidateConnectorRuntimeSettingsRequest)
        self.assertEqual(request.scope.name, 'DESTINATION')
        self.assertEqual(request.connector_runtime_settings['testSettingKey'], 'testSettingValue')
        self.assertEqual(request.connector_runtime_settings['testSettingKey2'], 'testSettingValue2')

    def test_create_validate_connector_runtime_settings_request_without_required_parameters(self):
        """Tests that a ValidateConnectorRuntimeSettingsRequest CANNOT be created without required parameters."""
        with open('custom_connector_sdk/test/resources/validate_connector_runtime_settings_request_invalid.json',
                  'r') as json_file:
            data = json.load(json_file)

        self.assertRaises(AssertionError, requests.ValidateConnectorRuntimeSettingsRequest.from_dict, data)

    def test_create_validate_credentials_response_with_required_parameters(self):
        """Tests that a ValidateCredentialsResponse can be created with only required parameters."""
        response = responses.ValidateCredentialsResponse(is_success=False)
        encoded_response = response.to_json()

        with open('custom_connector_sdk/test/resources/validate_credentials_response_required.json', 'r') as json_file:
            expected = json.dumps(json.load(json_file))

        self.assertEqual(encoded_response, expected)

    def test_create_validate_credentials_response_with_optional_parameters(self):
        """Tests that a ValidateCredentialsResponse can be created with optional parameters."""
        error_details = responses.ErrorDetails(responses.ErrorCode.ServerError, 'this is an error', 20)

        response = responses.ValidateCredentialsResponse(is_success=True, error_details=error_details)
        encoded_response = response.to_json()

        with open('custom_connector_sdk/test/resources/validate_credentials_response_optional.json', 'r') as json_file:
            expected = json.dumps(json.load(json_file))

        self.assertEqual(encoded_response, expected)

    def test_create_validate_credentials_response_without_required_parameters(self):
        """Tests that a ValidateCredentialsResponse CANNOT be created without required parameters."""
        error_details = responses.ErrorDetails(responses.ErrorCode.ServerError, 'this is an error', 20)

        self.assertRaises(TypeError,
                          responses.ValidateCredentialsResponse,
                          is_valid=True,
                          error_details=error_details)

    def test_create_describe_connector_configuration_response_with_required_parameters(self):
        """Tests that a DescribeConnectorConfigurationResponse can be created with only required parameters."""
        authentication_config = AuthenticationConfig(is_basic_auth_supported=True)

        response = responses.DescribeConnectorConfigurationResponse(connector_owner='owner',
                                                                    connector_name='name',
                                                                    connector_version='v1.0',
                                                                    connector_modes=[responses.ConnectorModes.SOURCE],
                                                                    authentication_config=authentication_config,
                                                                    supported_api_versions=['v1.0', 'v1.1'],
                                                                    is_success=True)
        encoded_response = response.to_json()

        with open('custom_connector_sdk/test/resources/describe_connector_configuration_response_required.json',
                  'r') as json_file:
            expected = json.dumps(json.load(json_file))

        self.assertEqual(encoded_response, expected)

    def test_create_describe_connector_configuration_response_with_optional_parameters(self):
        data_type = settings.ConnectorRuntimeSettingDataType.String
        connector_runtime_setting = settings.ConnectorRuntimeSetting(key='key',
                                                                     data_type=data_type,
                                                                     required=True,
                                                                     label='label',
                                                                     description='description',
                                                                     scope=settings.ConnectorRuntimeSettingScope.SOURCE)
        o_auth_2_defaults = OAuth2Defaults(['a'], ['b'], ['c'], [OAuth2GrantType.CLIENT_CREDENTIALS], ['e'], ['f'])
        auth_param = AuthParameter(key='testKey',
                                   required=True,
                                   label='testLabel',
                                   description='testDescription',
                                   sensitive_field=True,
                                   connector_supplied_values=['testValue'])
        custom_auth_config = CustomAuthConfig(authentication_type='testType', auth_parameters=[auth_param])
        authentication_config = AuthenticationConfig(is_basic_auth_supported=True,
                                                     is_api_key_auth_supported=True,
                                                     is_oauth_2_supported=False,
                                                     is_custom_auth_supported=False,
                                                     o_auth_2_defaults=o_auth_2_defaults,
                                                     custom_auth_config=[custom_auth_config])

        operators = [ConnectorOperator.ADDITION, ConnectorOperator.CONTAINS]
        trigger_frequencies = [TriggerFrequency.Once, TriggerFrequency.Daily]
        write_operations = [WriteOperationType.DELETE, WriteOperationType.INSERT]

        response = responses.DescribeConnectorConfigurationResponse(connector_owner='owner',
                                                                    connector_name='name',
                                                                    connector_version='v1.0',
                                                                    connector_modes=[responses.ConnectorModes.SOURCE],
                                                                    authentication_config=authentication_config,
                                                                    supported_api_versions=['v1.0', 'v1.1'],
                                                                    is_success=True,
                                                                    connector_runtime_setting=[connector_runtime_setting],
                                                                    logo_url='test.amazon.com',
                                                                    operators_supported=operators,
                                                                    trigger_frequencies_supported=trigger_frequencies,
                                                                    supported_write_operations=write_operations)
        encoded_response = response.to_json()

        with open('custom_connector_sdk/test/resources/describe_connector_configuration_response_optional.json',
                  'r') as json_file:
            expected = json.dumps(json.load(json_file))

        self.assertEqual(encoded_response, expected)

    def test_create_describe_connector_configuration_response_without_required_parameters(self):
        """Tests that a DescribeConnectorConfigurationResponse CANNOT be created without required parameters."""
        self.assertRaises(TypeError,
                          responses.DescribeConnectorConfigurationResponse,
                          connector_owner='owner',
                          connector_name='name',
                          connector_version='v1.0',
                          connector_modes=[responses.ConnectorModes.SOURCE],
                          supported_api_versions=['v1.0', 'v1.1'],
                          is_success=True)

    def test_create_validate_connector_runtime_settings_response_with_required_parameters(self):
        """Tests that a ValidateConnectorRuntimeSettingsResponse can be created with only required parameters."""
        response = responses.ValidateConnectorRuntimeSettingsResponse(is_success=False)
        encoded_response = response.to_json()

        with open('custom_connector_sdk/test/resources/validate_connector_runtime_settings_response_required.json',
                  'r') as json_file:
            expected = json.dumps(json.load(json_file))

        self.assertEqual(encoded_response, expected)

    def test_create_validate_connector_runtime_settings_response_with_optional_parameters(self):
        """Tests that a ValidateConnectorRuntimeSettingsResponse can be created with optional parameters."""
        error_details = responses.ErrorDetails(responses.ErrorCode.ServerError, 'this is an error', 20)

        response = responses.ValidateConnectorRuntimeSettingsResponse(is_success=True,
                                                                      errors_by_input_field={'field': 'error'},
                                                                      error_details=error_details)
        encoded_response = response.to_json()

        with open('custom_connector_sdk/test/resources/validate_connector_runtime_settings_response_optional.json',
                  'r') as json_file:
            expected = json.dumps(json.load(json_file))

        self.assertEqual(encoded_response, expected)

    def test_create_validate_connector_runtime_settings_response_without_required_parameters(self):
        """Tests that a ValidateConnectorRuntimeSettingsResponse CANNOT be created without required parameters."""
        error_details = responses.ErrorDetails(responses.ErrorCode.ServerError, 'this is an error', 20)

        self.assertRaises(TypeError,
                          responses.ValidateConnectorRuntimeSettingsResponse,
                          errors_by_input_field={'field': 'error'},
                          error_details=error_details)
