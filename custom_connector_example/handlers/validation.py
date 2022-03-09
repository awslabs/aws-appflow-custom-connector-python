from typing import List, Optional

from custom_connector_sdk.lambda_handler.responses import ErrorDetails, ErrorCode
from custom_connector_sdk.connector.context import ConnectorContext, Credentials
import custom_connector_sdk.lambda_handler.requests as requests
import custom_connector_example.constants as constants

def validate_write_data_request(request: requests.WriteDataRequest) -> Optional[ErrorDetails]:
    errors = []
    if request.operation not in constants.SUPPORTED_WRITE_OPERATIONS:
        errors.append(f'Operation {request.operation.name} not supported by Salesforce')
    errors += check_connector_context_errors(request.connector_context)
    if not errors:
        return None
    return ErrorDetails(error_code=ErrorCode.InvalidArgument, error_message=','.join(errors))

def validate_credentials(request: requests.ValidateCredentialsRequest) -> Optional[ErrorDetails]:
    errors = check_credentials_input_errors(request.credentials)
    if not errors:
        return None
    return ErrorDetails(error_code=ErrorCode.InvalidArgument, error_message=','.join(errors))

def validate_connector_runtime_settings(request: requests.ValidateConnectorRuntimeSettingsRequest) -> \
        Optional[ErrorDetails]:
    errors = check_connector_runtime_settings_errors(request.connector_runtime_settings)
    if not errors:
        return None
    return ErrorDetails(error_code=ErrorCode.InvalidArgument, error_message=','.join(errors))

def validate_request_connector_context(request) -> Optional[ErrorDetails]:
    errors = check_connector_context_errors(request.connector_context)
    if not errors:
        return None
    return ErrorDetails(error_code=ErrorCode.InvalidArgument, error_message=','.join(errors))

def check_connector_context_errors(connector_context: ConnectorContext) -> List[str]:
    errors = check_credentials_input_errors(connector_context.credentials)
    errors += check_connector_runtime_settings_errors(connector_context.connector_runtime_settings)
    return errors

def check_credentials_input_errors(credentials: Credentials) -> List[str]:
    errors = []
    if not credentials.secret_arn:
        errors.append('OAuth2 credentials should be provided using SecretsManager ARN')
    return errors

def check_connector_runtime_settings_errors(connector_runtime_settings: dict) -> List[str]:
    errors = []
    if not connector_runtime_settings or constants.INSTANCE_URL_KEY not in connector_runtime_settings:
        errors.append(f'{constants.INSTANCE_URL_KEY} should be provided as runtime setting for Salesforce connector')
    return errors
