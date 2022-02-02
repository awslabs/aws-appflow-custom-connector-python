import re
import custom_connector_sdk.lambda_handler.responses as responses
import custom_connector_sdk.connector.auth as auth
from custom_connector_tests.exceptions.ValidationException import ValidationException
from urllib.parse import urlparse

pattern = re.compile("([Aa][Ww][Ss]|[Aa][Mm][Aa][Zz][Oo][Nn]|[Aa][Pp][Pp][Ff][Ll][Oo][Ww]).*")
reserved_keywords = ["aws", "amazon", "appflow"]

def validate_connector_configuration_response(response):
    validation_errors = []

    if check_for_reserved_keywords(response[responses.CONNECTOR_NAME]):
        validation_errors.append(f'ConnectorName should not contain these reserved keywords {reserved_keywords}')
    if check_for_reserved_keywords(response[responses.CONNECTOR_OWNER]):
        validation_errors.append(f'ConnectorOwner should not contain these reserved keywords {reserved_keywords}')

    if not response[responses.CONNECTOR_MODES]:
        validation_errors.append(f'ConnectorModes cannot be null for Connector')

    validation_errors += validate_authentication_config(response[responses.AUTHENTICATION_CONFIG])

    if validation_errors:
        error_message = f'ConnectorConfiguration from the connector failed with following validation validationErrors. {validation_errors}'
        raise ValidationException(error_message)

def check_for_reserved_keywords(input_string):
    return pattern.match(input_string)

def validate_authentication_config(auth_config):
    validation_errors = []

    if auth_config[auth.IS_CUSTOM_AUTH_SUPPORTED] and not auth_config[auth.CUSTOM_AUTH_CONFIG]:
        validation_errors.append("For custom Authentication, CustomAuthConfig is required.")
    if not auth_config[auth.IS_CUSTOM_AUTH_SUPPORTED] and auth_config[auth.CUSTOM_AUTH_CONFIG]:
        validation_errors.append("CustomAuthConfig can only be provided for CustomAuthentication.")
    if auth_config[auth.IS_O_AUTH_2_SUPPORTED] and not auth_config[auth.O_AUTH_2_DEFAULTS]:
        validation_errors.append("For OAuth2 Authentication, OAuth2Defaults cannot be null.")
    if not auth_config[auth.IS_O_AUTH_2_SUPPORTED] and auth_config[auth.O_AUTH_2_DEFAULTS]:
        validation_errors.append("OAuth2Defaults can only be provided for OAuth2 Authentication.")

    if auth_config[auth.IS_O_AUTH_2_SUPPORTED] and auth_config[auth.O_AUTH_2_DEFAULTS]:
        o_auth_defaults = auth_config[auth.O_AUTH_2_DEFAULTS]
        validation_errors.extend(validate_urls(o_auth_defaults[auth.LOGIN_URL]) +
                                 validate_urls(o_auth_defaults[auth.AUTH_URL]) +
                                 validate_urls(o_auth_defaults[auth.REFRESH_URL]))
        if o_auth_defaults[auth.REDIRECT_URL]:
            validation_errors += validate_urls(o_auth_defaults[auth.REDIRECT_URL])

    return validation_errors

def validate_urls(urls):
    validation_errors = []

    for url in urls:
        try:
            validate(url)
        except ValidationException as e:
            validation_errors.append(f'Validation failed for url {url} with error {e}')

    return validation_errors

def validate(url):
    if not url:
        return

    try:
        url_parsed = urlparse(url)
        if not "https".__eq__(url_parsed.scheme):
            error_message = f'Invalid protocol in url {url}. Only https format is supported'
            raise ValidationException(error_message)
    except ValueError:
        error_message = f'Invalid format for url {url}. Please check if the url syntax is correct and resolves to a known host'
        raise ValidationException(error_message)
