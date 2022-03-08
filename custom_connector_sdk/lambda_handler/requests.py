from typing import List

from custom_connector_sdk.connector.context import ConnectorContext
from custom_connector_sdk.connector.settings import ConnectorRuntimeSettingScope
from custom_connector_sdk.connector.fields import WriteOperationType
from custom_connector_sdk.connector.auth import Credentials

ENTITY_IDENTIFIER = 'entityIdentifier'
CONNECTOR_CONTEXT = 'connectorContext'
ENTITIES_PATH = 'entitiesPath'
NEXT_TOKEN = 'nextToken'
MAX_RESULT = 'maxResult'
CREDENTIALS = 'credentials'
CONNECTOR_RUNTIME_SETTINGS = 'connectorRuntimeSettings'
LOCALE = 'locale'
SCOPE = 'scope'
SELECTED_FIELD_NAMES = 'selectedFieldNames'
ID_FIELD_NAME = 'idFieldName'
IDS = 'ids'
OPERATION = 'operation'
ID_FIELD_NAMES = 'idFieldNames'
RECORDS = 'records'
ALL_OR_NONE = 'allOrNone'
MAX_RESULTS = 'maxResults'
FILTER_EXPRESSION = 'filterExpression'

DEFAULT_MAX_RESULT = 1000
DEFAULT_LOCALE = 'en-US'

class DescribeEntityRequest:
    """Represents the input of a DescribeEntity operation."""
    def __init__(self, entity_identifier: str, connector_context: ConnectorContext):
        # Unique identifier for the entity. Can be entityId, entityName, entityPath+name, entityUrl, etc.
        self.entity_identifier = entity_identifier

        # Context contains the connector settings, credentials, API version, etc.
        self.connector_context = connector_context

    @classmethod
    def from_dict(cls, request: dict):
        if request is None:
            return None

        required_keys = {ENTITY_IDENTIFIER, CONNECTOR_CONTEXT}
        assert request.keys() >= required_keys, f'{cls.__name__} is missing required parameters {required_keys}'

        entity_identifier = request.get(ENTITY_IDENTIFIER)
        connector_context = ConnectorContext.from_dict(request.get(CONNECTOR_CONTEXT))

        return cls(entity_identifier, connector_context)

class ListEntitiesRequest:
    """Represents the input of a ListEntities operation."""
    def __init__(self,
                 connector_context: ConnectorContext,
                 entities_path: str = None,
                 next_token: str = None,
                 max_result: int = DEFAULT_MAX_RESULT):
        # Context contains the connector settings, credentials, API version, etc.
        self.connector_context = connector_context

        # Path/URI of entities
        self.entities_path = entities_path

        # The pagination token - next page should start from this token value
        self.next_token = next_token

        # Maximum number of records needs to be returned as part of single call. Default value is DEFAULT_MAX_RESULT.
        self.max_result = max_result

    @classmethod
    def from_dict(cls, request: dict):
        if request is None:
            return None

        required_keys = {CONNECTOR_CONTEXT}
        assert request.keys() >= required_keys, f'{cls.__name__} is missing required parameters {required_keys}'

        connector_context = ConnectorContext.from_dict(request.get(CONNECTOR_CONTEXT))
        entities_path = request.get(ENTITIES_PATH)
        next_token = request.get(NEXT_TOKEN)
        max_result = request.get(MAX_RESULT, DEFAULT_MAX_RESULT)

        return cls(connector_context, entities_path, next_token, max_result)

class ValidateCredentialsRequest:
    """Represents the input of a ValidateCredentials operation."""
    def __init__(self, credentials: Credentials, connector_runtime_settings: dict = None):
        # Credentials to validate.
        self.credentials = credentials

        # Connector Settings provided for validating the connector credentials. All the Connector Settings for
        # CONNECTOR_PROFILE scope will be provided as input (str -> object).
        self.connector_runtime_settings = connector_runtime_settings

    @classmethod
    def from_dict(cls, request: dict):
        if request is None:
            return None

        required_keys = {CREDENTIALS}
        assert request.keys() >= required_keys, f'{cls.__name__} is missing required parameters {required_keys}'

        credentials = Credentials.from_dict(request.get(CREDENTIALS))
        connector_runtime_settings = request.get(CONNECTOR_RUNTIME_SETTINGS)

        return cls(credentials, connector_runtime_settings)

class DescribeConnectorConfigurationRequest:
    """Represents the input of a DescribeConnectorConfiguration operation."""
    def __init__(self, locale: str = DEFAULT_LOCALE):
        # Locale value to get the localized string values for labels and descriptions for connector settings. Default
        # is en-US.
        self.locale = locale

    @classmethod
    def from_dict(cls, request: dict):
        if request is None:
            return None

        locale = request.get(LOCALE, DEFAULT_LOCALE)

        return cls(locale)

class ValidateConnectorRuntimeSettingsRequest:
    """Represents the input of a ValidateConnectorRuntimeSettings operation."""
    def __init__(self, scope: ConnectorRuntimeSettingScope, connector_runtime_settings: dict):
        # Scope of the connector runtime settings to be validated.
        self.scope = scope

        # Connector settings input. Key will be ConnectorSetting (string) and value will be input provided by user.
        self.connector_runtime_settings = connector_runtime_settings

    @classmethod
    def from_dict(cls, request: dict):
        if request is None:
            return None

        required_keys = {SCOPE, CONNECTOR_RUNTIME_SETTINGS}
        assert request.keys() >= required_keys, f'{cls.__name__} is missing required parameters {required_keys}'

        scope = ConnectorRuntimeSettingScope[request.get(SCOPE)]
        connector_runtime_settings = request.get(CONNECTOR_RUNTIME_SETTINGS)

        return cls(scope, connector_runtime_settings)

class RetrieveDataRequest:
    """Represents the input of a RetrieveData operation."""
    def __init__(self,
                 entity_identifier: str,
                 connector_context: ConnectorContext,
                 selected_field_names: List[str] = None,
                 id_field_name: str = None,
                 ids: List[str] = None):
        # Unique identifier for the entity. Can be entity_id, entity_name, entity_path+name, entity_url, etc.
        self.entity_identifier = entity_identifier

        # Context contains the connector settings, credentials, API version, etc.
        self.connector_context = connector_context

        # Field values to retrieve. If null, it will provide all the fields for the entity.
        self.selected_field_names = selected_field_names

        # Field name which will be used as part of where statement to retrieve the data. Can be primary or any other
        # column name.
        self.id_field_name = id_field_name

        # List of values for id_field_name.
        self.ids = ids

    @classmethod
    def from_dict(cls, request: dict):
        if request is None:
            return None

        required_keys = {ENTITY_IDENTIFIER, CONNECTOR_CONTEXT}
        assert request.keys() >= required_keys, f'{cls.__name__} is missing required parameters {required_keys}'

        entity_identifier = request.get(ENTITY_IDENTIFIER)
        connector_context = ConnectorContext.from_dict(request.get(CONNECTOR_CONTEXT))
        selected_field_names = request.get(SELECTED_FIELD_NAMES)
        id_field_name = request.get(ID_FIELD_NAME)
        ids = request.get(IDS)

        return cls(entity_identifier, connector_context, selected_field_names, id_field_name, ids)

class WriteDataRequest:
    """Represents the input of a WriteData operation."""
    def __init__(self,
                 entity_identifier: str,
                 connector_context: ConnectorContext,
                 operation: WriteOperationType = None,
                 id_field_names: List[str] = None,
                 records: List[str] = None,
                 all_or_none: bool = None):
        # Unique identifier for the entity. Can be entity_id, entity_name, entity_path+name, entity_url, etc.
        self.entity_identifier = entity_identifier

        # Context contains the connector settings, credentials, API version, etc.
        self.connector_context = connector_context

        # Write operation type needs to be called.
        self.operation = operation

        # Primary keys of the entity. Used for DELETE/UPDATE/UPSERT operations.
        self.id_field_names = id_field_names

        # List of JSON serialized string of the entity record as per the entity metadata.
        self.records = records

        # Specifies that the WRITE operation must fail immediately after encountering the first instance of failure
        # when writing a batch of records to the Application. Alternatively, if the application supports the all_or_none
        # behavior the connector can pass on the flag to the application.
        self.all_or_none = all_or_none

    @classmethod
    def from_dict(cls, request: dict):
        if request is None:
            return None

        required_keys = {ENTITY_IDENTIFIER, CONNECTOR_CONTEXT}
        assert request.keys() >= required_keys, f'{cls.__name__} is missing required parameters {required_keys}'

        entity_identifier = request.get(ENTITY_IDENTIFIER)
        connector_context = ConnectorContext.from_dict(request.get(CONNECTOR_CONTEXT))
        id_field_names = request.get(ID_FIELD_NAMES)
        records = [] if request.get(RECORDS) is None else request.get(RECORDS)
        all_or_none = request.get(ALL_OR_NONE)

        if OPERATION in request:
            operation = WriteOperationType[request.get(OPERATION)]
        else:
            operation = None

        return cls(entity_identifier, connector_context, operation, id_field_names, records, all_or_none)

class QueryDataRequest:
    """Represents the input of a QueryData operation."""
    def __init__(self,
                 entity_identifier: str,
                 connector_context: ConnectorContext,
                 selected_field_names: List[str] = None,
                 filter_expression: str = None,
                 next_token: str = None,
                 max_results: int = DEFAULT_MAX_RESULT):
        # Unique identifier for the entity. Can be entity_id, entity_name, entity_path+name, entity_url, etc.
        self.entity_identifier = entity_identifier

        # Context contains the connector settings, credentials, API version, etc.
        self.connector_context = connector_context

        # Field values to retrieve. If null, it will provide all the fields for the entity.
        self.selected_field_names = selected_field_names

        # Filter expression string similar to the WHERE clause in SQL.
        self.filter_expression = filter_expression

        # The pagination token - next page should start from this token value.
        self.next_token = next_token

        # Maximum number of records to be returned as part of a single call. Default value is 1000.
        self.max_results = max_results

    @classmethod
    def from_dict(cls, request):
        if request is None:
            return None

        required_keys = {ENTITY_IDENTIFIER, CONNECTOR_CONTEXT}
        assert request.keys() >= required_keys, f'{cls.__name__} is missing required parameters {required_keys}'

        entity_identifier = request.get(ENTITY_IDENTIFIER)
        connector_context = ConnectorContext.from_dict(request.get(CONNECTOR_CONTEXT))
        selected_field_names = request.get(SELECTED_FIELD_NAMES)
        filter_expression = request.get(FILTER_EXPRESSION)
        next_token = request.get(NEXT_TOKEN)
        max_results = request.get(MAX_RESULTS, DEFAULT_MAX_RESULT)

        return cls(entity_identifier,
                   connector_context,
                   selected_field_names,
                   filter_expression,
                   next_token,
                   max_results)
