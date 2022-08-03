import custom_connector_sdk.lambda_handler.requests as requests
import custom_connector_sdk.lambda_handler.responses as responses
import custom_connector_sdk.connector.settings as settings
import custom_connector_sdk.connector.configuration as config
import custom_connector_sdk.connector.context as context
import custom_connector_sdk.connector.auth as auth
import custom_connector_example.constants as constants
import custom_connector_example.handlers.validation as validation
import custom_connector_example.handlers.salesforce as salesforce
from custom_connector_sdk.lambda_handler.handlers import ConfigurationHandler
from custom_connector_example.handlers.client import HttpsClient, SalesforceResponse

CONNECTOR_OWNER = 'SampleConnector'
CONNECTOR_NAME = 'SamplePythonSalesforceConnector'
CONNECTOR_VERSION = '1.0'

API_VERSION = 'v51.0'
API_VERSION_KEY = 'api_version'
IS_SANDBOX_ACCOUNT = "is_sandbox_account"

AUTH_URL = 'https://login.salesforce.com/services/oauth2/authorize'
TOKEN_URL = 'https://login.salesforce.com/services/oauth2/token'
SANDBOX_AUTH_URL = 'https://test.salesforce.com/services/oauth2/authorize'
SANDBOX_TOKEN_URL = 'https://test.salesforce.com/services/oauth2/token'
REFRESH_URL = 'https://login.salesforce.com/services/oauth2/token'
REDIRECT_URL = 'https://login.salesforce.com'
SALESFORCE_USERINFO_URL_FORMAT = 'https://login.salesforce.com/services/oauth2/userinfo'
SALESFORCE_USERINFO_SANDBOX_URL_FORMAT = 'https://test.salesforce.com/services/oauth2/userinfo'
TRUE = 'true'

def buildSalesforceUserInfoRequest(connector_runtime_settings: dict) -> str:
        is_sandbox = connector_runtime_settings.get(IS_SANDBOX_ACCOUNT)
        if is_sandbox and is_sandbox.lower() == TRUE:
            return SALESFORCE_USERINFO_SANDBOX_URL_FORMAT
        return SALESFORCE_USERINFO_URL_FORMAT

def get_salesforce_client(secret_arn: str):
        return HttpsClient(salesforce.get_access_token_from_secret(secret_arn))

class SalesforceConfigurationHandler(ConfigurationHandler):
    """Salesforce Configuration Handler."""
    def validate_connector_runtime_settings(self, request: requests.ValidateConnectorRuntimeSettingsRequest) -> \
            responses.ValidateConnectorRuntimeSettingsResponse:
        errors = validation.validate_connector_runtime_settings(request)
        if errors:
            return responses.ValidateConnectorRuntimeSettingsResponse(is_success=False, error_details=errors)
        return responses.ValidateConnectorRuntimeSettingsResponse(is_success=True)

    def validate_credentials(self, request: requests.ValidateCredentialsRequest) -> \
            responses.ValidateCredentialsResponse:
        connector_context = context.ConnectorContext(credentials=request.credentials,
                                                     api_version=API_VERSION,
                                                     connector_runtime_settings=request.connector_runtime_settings)
        request_uri = buildSalesforceUserInfoRequest(request.connector_runtime_settings)
        salesforce_response = get_salesforce_client(request.credentials.secret_arn).rest_get(request_uri)
        error_details = salesforce.check_for_errors_in_salesforce_response(salesforce_response)
        if error_details:
            return responses.ValidateCredentialsResponse(is_success=False,
                                                         error_details=error_details)
        return responses.ValidateCredentialsResponse(is_success=True)

    def describe_connector_configuration(self, request: requests.DescribeConnectorConfigurationRequest) -> \
            responses.DescribeConnectorConfigurationResponse:
        connector_modes = [config.ConnectorModes.SOURCE, config.ConnectorModes.DESTINATION]

        instance_url_setting = settings.ConnectorRuntimeSetting(key=constants.INSTANCE_URL_KEY,
                                                                data_type=settings.ConnectorRuntimeSettingDataType
                                                                .String,
                                                                required=True,
                                                                label='Salesforce Instance URL',
                                                                description='URL of the instance where user wants to ' +
                                                                            'run the operations',
                                                                scope=settings.ConnectorRuntimeSettingScope
                                                                .CONNECTOR_PROFILE)
        is_sandbox_account_setting = settings.ConnectorRuntimeSetting(key=IS_SANDBOX_ACCOUNT,
                                                               data_type=settings.ConnectorRuntimeSettingDataType
                                                               .Boolean,
                                                               required=True,
                                                               label='Type of salesforce account',
                                                               description='Is Salesforce account a sandbox account',
                                                               scope=settings.ConnectorRuntimeSettingScope
                                                               .CONNECTOR_PROFILE)
        connector_runtime_settings = [instance_url_setting, is_sandbox_account_setting]

        o_auth_2_defaults = auth.OAuth2Defaults(auth_url=[AUTH_URL, SANDBOX_AUTH_URL],
                                                token_url=[TOKEN_URL, SANDBOX_TOKEN_URL],
                                                o_auth_scopes=['api', 'refresh_token'],
                                                o_auth_2_grant_types_supported=[auth.OAuth2GrantType.AUTHORIZATION_CODE])
        authentication_config = auth.AuthenticationConfig(is_oauth_2_supported=True,
                                                          o_auth_2_defaults=o_auth_2_defaults)

        return responses.DescribeConnectorConfigurationResponse(is_success=True,
                                                                connector_owner=CONNECTOR_OWNER,
                                                                connector_name=CONNECTOR_NAME,
                                                                connector_version=CONNECTOR_VERSION,
                                                                connector_modes=connector_modes,
                                                                connector_runtime_setting=connector_runtime_settings,
                                                                authentication_config=authentication_config,
                                                                supported_api_versions=[API_VERSION],
                                                                supported_write_operations=constants
                                                                .SUPPORTED_WRITE_OPERATIONS)
