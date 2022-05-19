from typing import List

from custom_connector_sdk.connector.fields import FieldDefinition
from custom_connector_sdk.connector.auth import Credentials

ENTITY_IDENTIFIER = 'entityIdentifier'
HAS_NESTED_ENTITIES = 'hasNestedEntities'
IS_WRITABLE = 'isWritable'
LABEL = 'label'
DESCRIPTION = 'description'
ENTITY = 'entity'
FIELDS = 'fields'
CUSTOM_PROPERTIES = 'customProperties'
CREDENTIALS = 'credentials'
API_VERSION = 'apiVersion'
CONNECTOR_RUNTIME_SETTINGS = 'connectorRuntimeSettings'
ENTITY_DEFINITION = 'entityDefinition'

class Entity:
    """Represents the entity structure."""
    def __init__(self,
                 entity_identifier: str,
                 has_nested_entities: bool,
                 is_writable: bool,
                 label: str = None,
                 description: str = None):
        # Unique identifier for the entity. Can be entityId, entityName, entityPath+name, entityUrl, etc.
        self.entity_identifier = entity_identifier

        # Specifies whether the connector entity is a parent or a category and has more entities nested underneath it.
        self.has_nested_entities = has_nested_entities
        
        # Specifies if entity is writable
        self.is_writable = is_writable

        # Label of the entity.
        self.label = label

        # Description of the entity.
        self.description = description

    def to_dict(self):
        return {ENTITY_IDENTIFIER: self.entity_identifier,
                HAS_NESTED_ENTITIES: self.has_nested_entities,
                IS_WRITABLE: self.is_writable,
                LABEL: self.label,
                DESCRIPTION: self.description}

    @classmethod
    def from_dict(cls, entity: dict):
        if entity is None:
            return None

        required_keys = {ENTITY_IDENTIFIER, HAS_NESTED_ENTITIES}
        assert entity.keys() >= required_keys, f'{cls.__name__} is missing required parameters {required_keys}'

        entity_identifier = entity.get(ENTITY_IDENTIFIER)
        has_nested_entities = entity.get(HAS_NESTED_ENTITIES)
        is_writable = entity.get(IS_WRITABLE)
        label = entity.get(LABEL)
        description = entity.get(DESCRIPTION)

        return cls(entity_identifier, has_nested_entities, is_writable, label, description)

class EntityDefinition:
    """Data model of the Entity."""
    def __init__(self, entity: Entity, fields: List[FieldDefinition], custom_properties: dict = None):
        # Contains its name, description, label or if it has child properties or not.
        self.entity = entity

        # List of data models of the fields an Entity has.
        self.fields = fields

        # Custom properties defined for an Entity (str -> object)
        self.custom_properties = custom_properties

    @classmethod
    def from_dict(cls, definition: dict):
        if definition is None:
            return None

        required_keys = {ENTITY, FIELDS}
        assert definition.keys() >= required_keys, f'{cls.__name__} is missing required parameters {required_keys}'

        entity = Entity.from_dict(definition.get(ENTITY))
        fields = [FieldDefinition.from_dict(field) for field in definition.get(FIELDS)]
        custom_properties = definition.get(CUSTOM_PROPERTIES)

        return cls(entity, fields, custom_properties)

    def to_dict(self):
        return {ENTITY: self.entity.to_dict(),
                FIELDS: [field.to_dict() for field in self.fields],
                CUSTOM_PROPERTIES: self.custom_properties}

class ConnectorContext:
    """Represents the Connector Context which contains the connector runtime settings, credentials, api version, and
    entity metadata.

    """
    def __init__(self,
                 api_version: str,
                 connector_runtime_settings: dict = None,
                 entity_definition: EntityDefinition = None,
                 credentials: Credentials = None):
        # Credentials which will be used to make API call
        self.credentials = credentials

        # API version to use. Value will be the API Version supported by Connector as part of Connector Configuration.
        self.api_version = api_version

        # Connector settings required for API call. For example, for the Read API it will contain all the
        # ConnectorSettingScope.SOURCE settings. Key will be Connector Setting (str) and value will be the input
        # provided by the user (object).
        self.connector_runtime_settings = connector_runtime_settings

        # Entity definition in compressed form, as it will be required by calling application as well as connector
        # metadata to serialize/deserialize request/response payload.
        self.entity_definition = entity_definition

    @classmethod
    def from_dict(cls, context: dict):
        if context is None:
            return None

        required_keys = {API_VERSION}
        assert context.keys() >= required_keys, f'{cls.__name__} is missing required parameters {required_keys}'

        credentials = Credentials.from_dict(context.get(CREDENTIALS))
        api_version = context.get(API_VERSION)
        connector_runtime_settings = context.get(CONNECTOR_RUNTIME_SETTINGS)
        entity_definition = EntityDefinition.from_dict(context.get(ENTITY_DEFINITION))

        return cls(
            credentials=credentials,
            api_version=api_version,
            connector_runtime_settings=connector_runtime_settings,
            entity_definition=entity_definition)
