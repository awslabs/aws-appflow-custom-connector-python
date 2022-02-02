import json
import logging
import boto3
from typing import Optional
import custom_connector_example.constants as constants
from custom_connector_sdk.connector.context import ConnectorContext
from custom_connector_sdk.lambda_handler.responses import ErrorDetails, ErrorCode
from custom_connector_sdk.connector.auth import ACCESS_TOKEN
from custom_connector_example.handlers.client import HttpsClient, SalesforceResponse

HTTP_STATUS_CODE_RANGE = range(200, 300)
LOGGER = logging.getLogger()

def get_salesforce_client(connector_context: ConnectorContext):
    return HttpsClient(get_access_token_from_secret(connector_context.credentials.secret_arn))

def check_for_errors_in_salesforce_response(response: SalesforceResponse) -> Optional[ErrorDetails]:
    """Parse Salesforce response for errors and convert them to an ErrorDetails object."""
    status_code = response.status_code

    if status_code in HTTP_STATUS_CODE_RANGE:
        return None

    if status_code == 401:
        error_code = ErrorCode.InvalidCredentials
    elif status_code == 400:
        error_code = ErrorCode.InvalidArgument
    else:
        error_code = ErrorCode.ServerError

    error_message = f'Request failed with status code {status_code} error reason {response.error_reason} and ' + \
                    f'Salesforce response is {response.response}'
    LOGGER.error(error_message)

    return ErrorDetails(error_code=error_code, error_message=error_message)

def build_salesforce_request_uri(connector_context: ConnectorContext, url_format: str, request_path: str) -> str:
    connector_runtime_settings = connector_context.connector_runtime_settings
    instance_url = connector_runtime_settings.get(constants.INSTANCE_URL_KEY)
    instance_url = add_path(instance_url)
    api_version = connector_context.api_version

    request_uri = url_format.format(instance_url, api_version, request_path)

    return request_uri

def get_access_token_from_secret(secret_arn: str) -> str:
    secrets_manager = boto3.client('secretsmanager')
    secret = secrets_manager.get_secret_value(SecretId=secret_arn)

    return json.loads(secret["SecretString"])[ACCESS_TOKEN]

def get_string_value(response: dict, field_name: str) -> Optional[str]:
    if field_name is None or response.get(field_name) is None:
        return None
    elif isinstance(response.get(field_name), bool):
        return str(response.get(field_name)).lower()
    else:
        return str(response.get(field_name))

def get_boolean_value(response: dict, field_name: str) -> bool:
    if field_name is None:
        return False
    elif field_name == 'true':
        return True
    elif response.get(field_name) is None:
        return False
    else:
        return bool(response.get(field_name))


def add_path(url: str) -> str:
    if url.endswith('/'):
        return url
    return url + '/'
