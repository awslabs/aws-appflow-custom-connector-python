from enum import Enum, auto
from typing import List

KEY = 'key'
TYPE = 'type'
REQUIRED = 'required'
LABEL = 'label'
DESCRIPTION = 'description'
SENSITIVE_FIELD = 'sensitiveField'
CONNECTOR_SUPPLIED_VALUES = 'connectorSuppliedValues'
USERNAME = 'userName'
PASSWORD = 'password'
API_KEY = 'apiKey'
SECRET_KEY = 'secretKey'
SECRET_ARN = 'secretArn'
ACCESS_TOKEN = 'accessToken'
REFRESH_TOKEN = 'refreshToken'
O_AUTH_SCOPES = 'oAuthScopes'
TOKEN_URL = 'tokenURL'
AUTH_URL = 'authURL'
REFRESH_URL = 'refreshURL'
REDIRECT_URL = 'redirectURL'
O_AUTH_2_GRANT_TYPES_SUPPORTED = 'oAuth2GrantTypesSupported'
DEFAULT_VALUES = 'defaultValues'
AUTHENTICATION_TYPE = 'authenticationType'
CUSTOM_CREDENTIALS = 'customCredentials'
AUTH_PARAMETERS = 'authParameters'
O_AUTH_2_CUSTOM_PROPERTIES = 'oAuth2CustomProperties'
ADD_BASIC_AUTH_HEADER = 'addBasicAuthHeader'
BASIC_AUTH_CREDENTIALS = 'basicAuthCredentials'
API_KEY_CREDENTIALS = 'apiKeyCredentials'
O_AUTH_2_CREDENTIALS = 'oAuth2Credentials'
CUSTOM_AUTH_CREDENTIALS = 'customAuthCredentials'
IS_BASIC_AUTH_SUPPORTED = 'isBasicAuthSupported'
IS_API_KEY_AUTH_SUPPORTED = 'isApiKeyAuthSupported'
IS_O_AUTH_2_SUPPORTED = 'isOAuth2Supported'
IS_CUSTOM_AUTH_SUPPORTED = 'isCustomAuthSupported'
O_AUTH_2_DEFAULTS = 'oAuth2Defaults'
CUSTOM_AUTH_CONFIG = 'customAuthConfig'
O_AUTH_2_CONTENT_TYPE = 'oAuth2ContentType'
O_AUTH_2_METHOD_TYPE = 'oAuth2MethodType'

class OAuth2CustomPropType(Enum):
    TOKEN_URL = auto()
    AUTH_URL = auto()

class AuthParameter:
    """Represents the authentication parameter."""
    def __init__(self,
                 key: str,
                 required: bool,
                 label: str,
                 description: str,
                 sensitive_field: bool = None,
                 connector_supplied_values: List[str] = None):
        # Unique identifier for AuthParameter.
        self.key = key

        # Specifies if this AuthParameter is required or not.
        self.required = required

        # Label of the Auth Parameter.
        self.label = label

        # Description of the Auth Parameter.
        self.description = description

        # Specifies if this field data is sensitive/critical that shouldn't be stored as plain text.
        self.sensitive_field = sensitive_field

        # Values provided by connector which can be used as input for this AuthParameter.
        self.connector_supplied_values = connector_supplied_values

    def to_dict(self):
        return {KEY: self.key,
                REQUIRED: self.required,
                LABEL: self.label,
                DESCRIPTION: self.description,
                SENSITIVE_FIELD: self.sensitive_field,
                CONNECTOR_SUPPLIED_VALUES: self.connector_supplied_values}

class Oauth2CustomParameter:
    """Represents the custom parameter required for oauth2 authentication."""
    def __init__(self,
                 key: str,
                 required: bool,
                 label: str,
                 description: str,
                 type: OAuth2CustomPropType,
                 sensitive_field: bool = None,
                 connector_supplied_values: List[str] = None):
        # Unique identifier for custom Oauth2 parameter..
        self.key = key

        # Specifies if this Oauth2 parameter is related to Token Url or Auth Url
        self.type = type

        # Specifies if this Oauth2 parameter is required or not.
        self.required = required

        # Label of the custom Oauth2 parameter.
        self.label = label

        # Description of the custom Oauth2 parameter.
        self.description = description

        # Specifies if this field data is sensitive/Critical that shouldn't be stored as plain text.
        self.sensitive_field = sensitive_field

        # Values provided by connector which can be used as input for this Parameter.
        self.connector_supplied_values = connector_supplied_values

    def to_dict(self):
        return {KEY: self.key,
                REQUIRED: self.required,
                LABEL: self.label,
                DESCRIPTION: self.description,
                SENSITIVE_FIELD: self.sensitive_field,
                TYPE: self.type,
                CONNECTOR_SUPPLIED_VALUES: self.connector_supplied_values}

class BasicAuthCredentials:
    """Credentials for Basic Authentication."""
    def __init__(self, username: str, password: str):
        # Username
        self.username = username

        # Password
        self.password = password

    @classmethod
    def from_dict(cls, credentials: dict):
        if credentials is None:
            return None

        required_keys = {USERNAME, PASSWORD}
        assert credentials.keys() >= required_keys, f'{cls.__name__} is missing required parameters {required_keys}'

        username = credentials.get(USERNAME)
        password = credentials.get(PASSWORD)

        return cls(username, password)

class ApiKeyCredentials:
    """Credentials for ApiKey authentication."""
    def __init__(self, api_key: str, secret_key: str = None):
        # API key.
        self.api_key = api_key

        # Secret key.
        self.secret_key = secret_key

    @classmethod
    def from_dict(cls, credentials: dict):
        if credentials is None:
            return None

        required_keys = {API_KEY}
        assert credentials.keys() >= required_keys, f'{cls.__name__} is missing required parameters {required_keys}'

        api_key = credentials.get(API_KEY)
        secret_key = credentials.get(SECRET_KEY)

        return cls(api_key, secret_key)

class OAuth2Credentials:
    """Credentials for OAuth2 authentication."""
    def __init__(self, access_token: str, refresh_token: str = None):
        # Access Token.
        self.access_token = access_token

        # Refresh Token.
        self.refresh_token = refresh_token

    @classmethod
    def from_dict(cls, credentials: dict):
        if credentials is None:
            return None

        required_keys = {ACCESS_TOKEN}
        assert credentials.keys() >= required_keys, f'{cls.__name__} is missing required parameters {required_keys}'

        access_token = credentials.get(ACCESS_TOKEN)
        refresh_token = credentials.get(REFRESH_TOKEN)

        return cls(access_token, refresh_token)

class OAuth2GrantType(Enum):
    CLIENT_CREDENTIALS = auto()
    AUTHORIZATION_CODE = auto()

class OAuth2ContentType(Enum):
    URL_ENCODED = auto()
    APPLICATION_JSON = auto()

class OAuth2MethodType(Enum):
    HTTP_POST = auto()
    HTTP_GET = auto()

class OAuth2Defaults:
    """Default OAuth2 Params values defined by connector."""
    def __init__(self,
                 token_url: List[str],
                 auth_url: List[str],
                 o_auth_2_grant_types_supported: List[OAuth2GrantType],
                 o_auth_scopes: List[str] = None,
                 o_auth_2_custom_parameters: List[Oauth2CustomParameter] = None,
                 add_basic_auth_header: bool = False,
                 o_auth_2_content_type: OAuth2ContentType = OAuth2ContentType.URL_ENCODED,
                 o_auth_2_method_type: OAuth2MethodType = OAuth2MethodType.HTTP_POST):
        # OAuth Scopes.
        self.o_auth_scopes = o_auth_scopes

        # This URL can be in two format - Static and Template based where we need the input from the Customer to build the complete URL.
        # For Static URLs you can add the URL directly to this list like
        # - https://login.salesforce.com/services/oauth2/token
        # And for template based URLs, you can use this format
        # - https://{{SALESFORCE_SUBDOMAIN}}.auth.marketingcloudapis.com/v2/token where the SALESFORCE_SUBDOMAIN
        # will be the user input and AppFlow will ask the customers to provide its value while
        # configuring the connector profile.
        self.token_url = token_url

        # This URL can be in two format - Static and Template based where we need the input from the Customer to build the complete URL.
        # For Static URLs you can add the URL directly to this list like
        #  - https://login.salesforce.com/services/oauth2/token.
        # And for template based URLs, you can use this format
        # - https://{{SALESFORCE_SUBDOMAIN}}.auth.marketingcloudapis.com/v2/token where the SALESFORCE_SUBDOMAIN
        # will be the user input and AppFlow will ask the customers to provide its value while
        # configuring the connector profile.
        self.auth_url = auth_url

        # OAuth2 Grant types supported by connector.
        self.o_auth_2_grant_types_supported = o_auth_2_grant_types_supported

        # OAuth2 custom parameters needed by the connector. In case of 3 legged OAuth2 AppFlow have clientId and
        # scope defined as the default parameter for AUTH_URL to generate the Authorization code.
        # Connector developer doesn't have to define clientId and scope as OAuth2Custom Parameter for AUTH_URL.
        self.o_auth_2_custom_parameters = o_auth_2_custom_parameters
		
        # Specifies if clientId and clientSecret should be added to basic auth header
        self.add_basic_auth_header = add_basic_auth_header

        # OAuth2 content type used for login requests. URL_ENCODED or APPLICATION_JSON.
        # Default: URL_ENCODED
        self.o_auth_2_content_type = o_auth_2_content_type

        # Rest method type used for OAuth2 login requests. GET or POST.
        # Default: POST
        self.o_auth_2_method_type = o_auth_2_method_type

    def to_dict(self):
        return {
                TOKEN_URL: self.token_url,
                AUTH_URL: self.auth_url,
                O_AUTH_2_GRANT_TYPES_SUPPORTED: [grant_type.name for grant_type in self.o_auth_2_grant_types_supported],
                O_AUTH_SCOPES: self.o_auth_scopes,
                O_AUTH_2_CUSTOM_PROPERTIES: self.o_auth_2_custom_parameters and [param.to_dict() for param in self.o_auth_2_custom_parameters],
                ADD_BASIC_AUTH_HEADER: self.add_basic_auth_header and [param.to_dict() for param in self.add_basic_auth_header],
                O_AUTH_2_CONTENT_TYPE: self.o_auth_2_content_type.name,
                O_AUTH_2_METHOD_TYPE: self.o_auth_2_method_type.name}

class CustomAuthCredentials:
    """Credentials for Custom Authentication supported by connector. This structure is embedded in the Credentials
    structure withing the ConnectorConnect that is sent with every API call.

    """
    def __init__(self, authentication_type: str, custom_credentials: dict):
        # Authentication Type defined by Connector.
        self.authentication_type = authentication_type

        # Custom Credentials provided by connector user. Key will be Auth Parameter (str) and value will be the input
        # provided by user (str).
        self.custom_credentials = custom_credentials

    @classmethod
    def from_dict(cls, credentials: dict):
        if credentials is None:
            return None

        required_keys = {AUTHENTICATION_TYPE, CUSTOM_CREDENTIALS}
        assert credentials.keys() >= required_keys, f'{cls.__name__} is missing required parameters {required_keys}'

        authentication_type = credentials.get(AUTHENTICATION_TYPE)
        custom_credentials = credentials.get(CUSTOM_CREDENTIALS)

        return cls(authentication_type, custom_credentials)

class CustomAuthConfig:
    """Represents the Custom Authentication configuration."""
    def __init__(self, authentication_type: str, auth_parameters: List[AuthParameter]):
        # AuthenticationType string value defined by connector.
        self.authentication_type = authentication_type

        # List of Auth Parameters.
        self.auth_parameters = auth_parameters

    def to_dict(self):
        return {AUTHENTICATION_TYPE: self.authentication_type,
                AUTH_PARAMETERS: [param.to_dict() for param in self.auth_parameters]}

class AuthenticationType(Enum):
    """Enum of Authentication Types"""

    # Basic Authentication credentials.
    BasicAuth = auto
    # Custom Authentication credentials.
    CustomAuth = auto()
    # OAuth2 Authentication credentials.
    OAuth2 = auto()
    # ApiKey Authentication credentials.
    ApiKey = auto()

class Credentials:
    """ This class represents the Credentials structure. These credentials will be passed along with every connector
    invocation within the ConnectorContext.

    The AuthenticationType will denote the type of credentials that is being used. The credentials details should be
    obtained by fetching from SecretsManager using the SecretArn.
    """
    def __init__(self,
                 secret_arn: str,
                 authentication_type: AuthenticationType = None):
        self.secret_arn = secret_arn
        self.authentication_type = authentication_type

    @classmethod
    def from_dict(cls, credentials: dict):
        if credentials is None:
            return None

        secret_arn = credentials.get(SECRET_ARN)
        authentication_type = AuthenticationType[credentials.get(AUTHENTICATION_TYPE)]

        return cls(secret_arn, authentication_type)

class AuthenticationConfig:
    """Represents Authentication types supported by the connector."""
    def __init__(self,
                 is_basic_auth_supported: bool = None,
                 is_api_key_auth_supported: bool = None,
                 is_oauth_2_supported: bool = None,
                 is_custom_auth_supported: bool = None,
                 o_auth_2_defaults: OAuth2Defaults = None,
                 custom_auth_config: List[CustomAuthConfig] = None):
        # Specifies if Basic Auth is supported by connector.
        self.is_basic_auth_supported = is_basic_auth_supported

        # Specifies if ApiKey Auth is supported by connector.
        self.is_api_key_auth_supported = is_api_key_auth_supported

        # Specifies if OAuth2 is supported by connector.
        self.is_oauth_2_supported = is_oauth_2_supported

        # Specifies if Custom Authentication is supported by connector.
        self.is_custom_auth_supported = is_custom_auth_supported

        # OAuth2 default values provided by connector.
        self.o_auth_2_defaults = o_auth_2_defaults

        # Configuration for custom Authentication defined by connector.
        self.custom_auth_config = custom_auth_config

    def to_dict(self):
        return {IS_BASIC_AUTH_SUPPORTED: self.is_basic_auth_supported,
                IS_API_KEY_AUTH_SUPPORTED: self.is_api_key_auth_supported,
                IS_O_AUTH_2_SUPPORTED: self.is_oauth_2_supported,
                IS_CUSTOM_AUTH_SUPPORTED: self.is_custom_auth_supported,
                O_AUTH_2_DEFAULTS: self.o_auth_2_defaults and self.o_auth_2_defaults.to_dict(),
                CUSTOM_AUTH_CONFIG: self.custom_auth_config and
                [config.to_dict() for config in self.custom_auth_config]}
