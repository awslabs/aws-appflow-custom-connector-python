from enum import Enum, auto
from typing import List

from custom_connector_sdk.connector.context import Entity, EntityDefinition
from custom_connector_sdk.connector.settings import CacheControl, ConnectorRuntimeSetting
from custom_connector_sdk.connector.configuration import ConnectorOperator, ConnectorModes, TriggerFrequency, TriggerType
from custom_connector_sdk.connector.auth import AuthenticationConfig
from custom_connector_sdk.connector.fields import WriteOperationType

LIST_ENTITIES_RESPONSE = 'ListEntitiesResponse'
DESCRIBE_ENTITY_RESPONSE = 'DescribeEntityResponse'
VALIDATE_CONNECTOR_RUNTIME_SETTINGS_RESPONSE = 'ValidateConnectorRuntimeSettingsResponse'
VALIDATE_CREDENTIALS_RESPONSE = 'ValidateCredentialsResponse'
DESCRIBE_CONNECTOR_CONFIGURATION_RESPONSE = 'DescribeConnectorConfigurationResponse'
RETRIEVE_DATA_RESPONSE = 'RetrieveDataResponse'
WRITE_DATA_RESPONSE = 'WriteDataResponse'
QUERY_DATA_RESPONSE = 'QueryDataResponse'
TYPE = 'type'
ERROR_CODE = 'errorCode'
ERROR_MESSAGE = 'errorMessage'
RETRY_AFTER_SECONDS = 'retryAfterSeconds'
IS_SUCCESS = 'isSuccess'
RECORD_ID = 'recordId'
ERROR_DETAILS = 'errorDetails'
ENTITIES = 'entities'
NEXT_TOKEN = 'nextToken'
CACHE_CONTROL = 'cacheControl'
ENTITY_DEFINITION = 'entityDefinition'
IS_VALID = 'isValid'
CONNECTOR_OWNER = 'connectorOwner'
CONNECTOR_NAME = 'connectorName'
CONNECTOR_VERSION = 'connectorVersion'
CONNECTOR_MODES = 'connectorModes'
AUTHENTICATION_CONFIG = 'authenticationConfig'
SUPPORTED_API_VERSIONS = 'supportedApiVersions'
CONNECTOR_RUNTIME_SETTING = 'connectorRuntimeSetting'
LOGO_URL = 'logoURL'
OPERATORS_SUPPORTED = 'operatorsSupported'
TRIGGER_FREQUENCIES_SUPPORTED = 'triggerFrequenciesSupported'
SUPPORTED_TRIGGER_TYPES = 'supportedTriggerTypes'
SUPPORTED_WRITE_OPERATIONS = 'supportedWriteOperations'
WRITE_RECORD_RESULTS = 'writeRecordResults'
ERRORS_BY_INPUT_FIELD = 'errorsByInputField'
RECORDS = 'records'

ALL_OPERATORS = [op for op in ConnectorOperator]
ALL_TRIGGER_FREQUENCIES = [freq for freq in TriggerFrequency]
ALL_WRITE_OPERATION_TYPES = [op for op in WriteOperationType]
ALL_TRIGGER_TYPES = [op for op in TriggerType]

class ErrorCode(Enum):
    """Collection of all normalized error codes for returning errors back to AppFlow."""
    # Invalid arguments provided as input/HttpStatus 400/413 from application/Bad Request exception from Application.
    # For example QueryURI too large, write request payload too large etc.
    InvalidArgument = auto()

    # Credentials were rejected by the underlying application/HttpStatus 401 from Application.
    InvalidCredentials = auto()

    # Resource access denied by the underlying application/HttpStatus 403 from Application.
    AccessDenied = auto()

    # The request to the underlying application timed out/HttpStatus 408 from Application/
    # HttpClient timeout while sending request.
    RequestTimeout = auto()

    # Request got rejected by the underlying application due to rate limit violation/HttpStatus 429 from Application.
    RateLimitExceeded = auto()

    # Application is not available to serve the requests at the moment/HttpStatus 503 from Application.
    ServiceUnavailable = auto()

    # Specifies error is due to client or HttpStatus 4XX from Application.
    # Use specific error codes if present.
    ClientError = auto()

    # Specifies error is due to Application or HttpStatus 5XX from Application.
    # Use specific error codes if present.
    ServerError = auto()

    # Unknown Error from the Application. Use this ErrorCode only when you are not able to use the
    # other specific error codes.
    UnknownError = auto()

    # Specifies that the connector encountered failure, for some records, while writing to the application.
    PartialWriteFailure = auto()

    # Specifies that the connector is unable to find resource like AWS SecretManagerARN etc.
    ResourceNotFoundError = auto()

class ErrorDetails:
    """Represents the error details."""
    def __init__(self, error_code: ErrorCode, error_message: str, retry_after_seconds: int = None):
        # Error code.
        self.error_code = error_code

        # Detailed error message corresponding to the error code.
        self.error_message = error_message

        # Specifies the time delay in seconds after which operation can be retried.
        self.retry_after_seconds = retry_after_seconds

    def __repr__(self):
        return f'{self.error_code}: {self.error_message}'

    def to_dict(self):
        return {ERROR_CODE: self.error_code.name,
                ERROR_MESSAGE: self.error_message,
                RETRY_AFTER_SECONDS: self.retry_after_seconds}

class WriteRecordResult:
    """Specifies if the record is written successfully or not."""
    def __init__(self, is_success: bool, record_id: str, error_message: str = None):
        # Specifies if the record is written successfully or not.
        self.is_success = is_success

        # Unique identifier for the record.
        self.record_id = record_id

        # Error message if the record is not written to the destination successfully.
        self.error_message = error_message

    def to_dict(self):
        return {IS_SUCCESS: self.is_success,
                RECORD_ID: self.record_id,
                ERROR_MESSAGE: self.error_message}

class ListEntitiesResponse:
    """Represents the output of a RetrieveData operation."""
    def __init__(self,
                 is_success: bool,
                 error_details: ErrorDetails = None,
                 entities: List[Entity] = None,
                 next_token: str = None,
                 cache_control: CacheControl = None):
        # Specifies if the operation is successful or not.
        self.is_success = is_success

        # Error details if the Operation is unsuccessful.
        self.error_details = error_details

        # List of entities.
        self.entities = entities

        # The pagination token for the next page of data.
        self.next_token = next_token

        # Caching policy for the list of entities.
        self.cache_control = cache_control

    def to_dict(self):
        return {IS_SUCCESS: self.is_success,
                ERROR_DETAILS: self.error_details and self.error_details.to_dict(),
                ENTITIES: self.entities and [entity.to_dict() for entity in self.entities],
                NEXT_TOKEN: self.next_token,
                CACHE_CONTROL: self.cache_control and self.cache_control.to_dict()}

class DescribeEntityResponse:
    """Represents the output of a DescribeEntity operation."""
    def __init__(self, is_success: bool,
                 error_details: ErrorDetails = None,
                 entity_definition: EntityDefinition = None,
                 cache_control: CacheControl = None):
        # Specifies if the operation is successful or not.
        self.is_success = is_success

        # Error details if the Operation is unsuccessful.
        self.error_details = error_details

        # Data model of the entity.
        self.entity_definition = entity_definition

        # Caching policy
        self.cache_control = cache_control

    def to_dict(self):
        return {IS_SUCCESS: self.is_success,
                ERROR_DETAILS: self.error_details and self.error_details.to_dict(),
                ENTITY_DEFINITION: self.entity_definition and self.entity_definition.to_dict(),
                CACHE_CONTROL: self.cache_control and self.cache_control.to_dict()}

class ValidateCredentialsResponse:
    """Represents the output of a ValidateCredentialsResponse operation."""
    def __init__(self, is_success: bool, error_details: ErrorDetails = None):
        # Specifies if the operation is successful or not.
        self.is_success = is_success

        # Error details contains ErrorCode and ErrorMessage if the Operation is unsuccessful.
        self.error_details = error_details

    def to_dict(self):
        return {IS_SUCCESS: self.is_success,
                ERROR_DETAILS: self.error_details and self.error_details.to_dict()}

class DescribeConnectorConfigurationResponse:
    """Represents the output of a DescribeConnectorConfiguration operation."""
    def __init__(self,
                 connector_owner: str,
                 connector_name: str,
                 connector_version: str,
                 connector_modes: List[ConnectorModes],
                 supported_api_versions: List[str],
                 is_success: bool,
                 operators_supported: List[ConnectorOperator] = ALL_OPERATORS,
                 trigger_frequencies_supported: List[TriggerFrequency] = ALL_TRIGGER_FREQUENCIES,
                 supported_write_operations: List[WriteOperationType] = ALL_WRITE_OPERATION_TYPES,
                 supported_trigger_types: List[TriggerType] = ALL_TRIGGER_TYPES,
                 authentication_config: AuthenticationConfig = None,
                 connector_runtime_setting: List[ConnectorRuntimeSetting] = None,
                 logo_url: str = None,
                 error_details: ErrorDetails = None):
        # Name of the connector owner.
        self.connector_owner = connector_owner

        # Name of the connector.
        self.connector_name = connector_name

        # Version of the connector.
        self.connector_version = connector_version

        # List of ConnectorModes supported by the connector.
        self.connector_modes = connector_modes

        # AuthenticationConfig supported by teh connector.
        self.authentication_config = authentication_config

        # List of API versions supported by connector for the underlying application. For example, if the underlying
        # application is Salesforce, then example could be list of {v46.0, v47.0, v48.9}.
        self.supported_api_versions = supported_api_versions

        # Specifies if the operation is successful or not.
        self.is_success = is_success

        # Custom connector runtime settings for which connector requires input from the end user.
        self.connector_runtime_setting = connector_runtime_setting

        # Logo URL for display purposes for connector icon.
        self.logo_url = logo_url

        # Error details if the Operation is unsuccessful.
        self.error_details = error_details

        # Operators supported by the connector. Default: all the operators
        self.operators_supported = operators_supported

        # Trigger frequencies supported by the connector. Default: all trigger frequencies
        self.trigger_frequencies_supported = trigger_frequencies_supported

        # Write Operations supported by Connector. Only applicable if the connector supports DESTINATION mode. Default
        # is all the Write Operation types supported.
        self.supported_write_operations = supported_write_operations

        self.supported_trigger_types = supported_trigger_types

    def to_dict(self):
        return {CONNECTOR_OWNER: self.connector_owner,
                CONNECTOR_NAME: self.connector_name,
                CONNECTOR_VERSION: self.connector_version,
                CONNECTOR_MODES: [mode.name for mode in self.connector_modes],
                AUTHENTICATION_CONFIG: self.authentication_config.to_dict(),
                SUPPORTED_API_VERSIONS: self.supported_api_versions,
                IS_SUCCESS: self.is_success,
                CONNECTOR_RUNTIME_SETTING: self.connector_runtime_setting and
                [setting.to_dict() for setting in self.connector_runtime_setting],
                LOGO_URL: self.logo_url,
                ERROR_DETAILS: self.error_details and self.error_details.to_dict(),
                OPERATORS_SUPPORTED: [op.name for op in self.operators_supported],
                TRIGGER_FREQUENCIES_SUPPORTED: [freq.name for freq in self.trigger_frequencies_supported],
                SUPPORTED_WRITE_OPERATIONS: [op.name for op in self.supported_write_operations],
                SUPPORTED_TRIGGER_TYPES: [op.name for op in self.supported_trigger_types]}

class ValidateConnectorRuntimeSettingsResponse:
    """Represents the output of a ValidateConnectorRuntimeSettings operation."""

    def __init__(self, is_success: bool, errors_by_input_field: dict = None, error_details: ErrorDetails = None):
        # Specifies if the operation is successful or not.
        self.is_success = is_success

        # Error message for the invalid connector settings keys. Key will be ConnectorRuntimeSetting (string) provided
        # as input and value will be the error message (string).
        self.errors_by_input_field = errors_by_input_field

        # Error details contains ErrorCode and ErrorMessage if the Operation is unsuccessful.
        self.error_details = error_details

    def to_dict(self):
        return {IS_SUCCESS: self.is_success,
                ERRORS_BY_INPUT_FIELD: self.errors_by_input_field,
                ERROR_DETAILS: self.error_details and self.error_details.to_dict()}

class RetrieveDataResponse:
    """Represents the output of a RetrieveData operation."""
    def __init__(self, is_success: bool, error_details: ErrorDetails = None, records: List[str] = None):
        # Specifies if the operation is successful or not.
        self.is_success = is_success

        # Error details if the Operation is unsuccessful.
        self.error_details = error_details

        # List of JSON serialized string of the entity record as per the entity metadata.
        self.records = records

    def to_dict(self):
        return {IS_SUCCESS: self.is_success,
                ERROR_DETAILS: self.error_details and self.error_details.to_dict(),
                RECORDS: self.records}

class WriteDataResponse:
    """Represents the output of a WriteData operation."""
    def __init__(self, is_success: bool,
                 error_details: ErrorDetails = None,
                 write_record_results: List[WriteRecordResult] = None):
        # Specifies if the operation is successful or not. In case of partial failure,
        # this flag should be set to false and the error code should be set to PartialWriteFailure.
        self.is_success = is_success

        # Error details if the Operation is unsuccessful.
        self.error_details = error_details

        # List of input records write call response with success and failure details.
        self.write_record_results = write_record_results

    def to_dict(self):
        return {IS_SUCCESS: self.is_success,
                ERROR_DETAILS: self.error_details and self.error_details.to_dict(),
                WRITE_RECORD_RESULTS: self.write_record_results and [result.to_dict() for result in
                                                                     self.write_record_results]}

class QueryDataResponse:
    """Represents the output of a QueryData operation."""
    def __init__(self,
                 is_success: bool,
                 error_details: ErrorDetails = None,
                 next_token: str = None,
                 records: List[str] = None):
        # Specifies if the operation is successful or not.
        self.is_success = is_success

        # Error details if the Operation is unsuccessful.
        self.error_details = error_details

        # The pagination token for the next page of data.
        self.next_token = next_token

        # List of json serialized string of the entity record as per the entity metadata.
        self.records = records


    def to_dict(self):
        return {IS_SUCCESS: self.is_success,
                ERROR_DETAILS: self.error_details and self.error_details.to_dict(),
                NEXT_TOKEN: self.next_token,
                RECORDS: self.records}
