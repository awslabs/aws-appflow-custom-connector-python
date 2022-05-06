import json
import logging
from typing import List

import custom_connector_sdk.lambda_handler.requests as requests
import custom_connector_sdk.lambda_handler.responses as responses
import custom_connector_sdk.connector.context as context
import custom_connector_sdk.connector.fields as fields
import custom_connector_example.handlers.validation as validation
import custom_connector_example.handlers.salesforce as salesforce
from custom_connector_sdk.lambda_handler.handlers import MetadataHandler

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

SALESFORCE_SOBJECTS_URL_FORMAT = '{}services/data/{}/sobjects'
SALESFORCE_SOBJECT_DESCRIBE_URL_FORMAT = '{}services/data/{}/sobjects/{}/describe'

# Salesforce response keys
SOBJECTS_KEY = 'sobjects'
OBJECT_DESCRIBE_KEY = 'objectDescribe'
CHILD_RELATIONSHIPS_KEY = 'childRelationships'
HAS_SUBTYPES_KEY = 'hasSubtypes'
NAME_KEY = 'name'
FIELDS_KEY = 'fields'
TYPE_KEY = 'type'
LABEL_KEY = 'label'
FILTERABLE_KEY = 'filterable'
EXTERNAL_ID_KEY = 'externalId'
ID_LOOKUP_KEY = 'idLookup'
CREATEABLE_KEY = 'createable'
UPDATEABLE_KEY = 'updateable'
NILLABLE_KEY = 'nillable'
DEFAULTED_ON_CREATE_KEY = 'defaultedOnCreate'
DEFAULT_VALUE_KEY = 'defaultValue'
UNIQUE_KEY = 'unique'

def parse_entities(json_string: str) -> List[context.Entity]:
    """Parse JSON response from Salesforce query into a list of Entities."""
    parent_object = json.loads(json_string)
    entity_list = []

    if parent_object.get(SOBJECTS_KEY):
        sobjects = parent_object.get(SOBJECTS_KEY)
        for sobject in sobjects:
            entity_list.append(build_entity(sobject))
    elif parent_object.get(OBJECT_DESCRIBE_KEY):
        entity_list.append(build_entity(parent_object.get(OBJECT_DESCRIBE_KEY)))

    return entity_list

def build_entity(field: dict) -> context.Entity:
    """Build Entity from Salesforce field."""
    description = field.get(LABEL_KEY)
    has_child_relationships = CHILD_RELATIONSHIPS_KEY in field and len(field.get(CHILD_RELATIONSHIPS_KEY)) != 0
    has_nested_entities = salesforce.get_boolean_value(field, HAS_SUBTYPES_KEY) or has_child_relationships
    return context.Entity(entity_identifier=salesforce.get_string_value(field, NAME_KEY),
                          label=description,
                          has_nested_entities=has_nested_entities,
                          description=description,
                          is_writable=field.get(CREATEABLE_KEY))

def parse_entity_definition(json_string: str) -> context.EntityDefinition:
    """Parse JSON response from Salesforce query into an entity definition."""
    parent_object = json.loads(json_string)
    field_definitions = []
    entity = build_entity(parent_object)

    if FIELDS_KEY in parent_object:
        field_list = parent_object.get(FIELDS_KEY)
        for field in field_list:
            field_definitions.append(build_field_definition(field))
    return context.EntityDefinition(entity=entity, fields=field_definitions)

def build_field_definition(field: dict) -> context.FieldDefinition:
    """Build FieldDefinition from Salesforce field.`"""
    data_type_label = salesforce.get_string_value(field, TYPE_KEY)
    data_type = convert_data_type(data_type_label)
    display_name = salesforce.get_string_value(field, LABEL_KEY)
    read_operation_property = fields.ReadOperationProperty(is_queryable=salesforce
                                                           .get_boolean_value(field, FILTERABLE_KEY),
                                                           is_retrievable=True)

    write_operation_types = set()
    if salesforce.get_boolean_value(field, EXTERNAL_ID_KEY):
        write_operation_types.add(responses.WriteOperationType.UPSERT)
    elif salesforce.get_boolean_value(field, ID_LOOKUP_KEY):
        write_operation_types.add(responses.WriteOperationType.UPDATE)
        write_operation_types.add(responses.WriteOperationType.UPSERT)
    write_operation_property = fields.WriteOperationProperty(is_creatable=salesforce
                                                             .get_boolean_value(field, CREATEABLE_KEY),
                                                             is_updatable=salesforce
                                                             .get_boolean_value(field, UPDATEABLE_KEY),
                                                             is_nullable=salesforce
                                                             .get_boolean_value(field, NILLABLE_KEY),
                                                             is_defaulted_on_create=salesforce
                                                             .get_boolean_value(field, DEFAULTED_ON_CREATE_KEY),
                                                             supported_write_operations=list(write_operation_types))

    return context.FieldDefinition(field_name=salesforce.get_string_value(field, NAME_KEY),
                                   data_type=data_type,
                                   data_type_label=data_type_label,
                                   label=display_name,
                                   description=display_name,
                                   default_value=salesforce.get_string_value(field, DEFAULT_VALUE_KEY),
                                   is_primary_key=salesforce.get_boolean_value(field, UNIQUE_KEY),
                                   read_properties=read_operation_property,
                                   write_properties=write_operation_property)

def convert_data_type(data_type_name: str):
    data_type_map = {
        'int': fields.FieldDataType.Integer,
        'double': fields.FieldDataType.Double,
        'long': fields.FieldDataType.Long,
        'id': fields.FieldDataType.String,
        'string': fields.FieldDataType.String,
        'textarea': fields.FieldDataType.String,
        'date': fields.FieldDataType.Date,
        'datetime': fields.FieldDataType.DateTime,
        'time': fields.FieldDataType.DateTime,
        'boolean': fields.FieldDataType.Boolean
    }
    try:
        return data_type_map[data_type_name]
    except KeyError:
        return fields.FieldDataType.Struct

class SalesforceMetadataHandler(MetadataHandler):
    """Salesforce Metadata handler."""
    def list_entities(self, request: requests.ListEntitiesRequest) -> responses.ListEntitiesResponse:
        error_details = validation.validate_request_connector_context(request)
        if error_details:
            LOGGER.error('ListEntities request failed with ' + str(error_details))
            return responses.ListEntitiesResponse(is_success=False, error_details=error_details)

        if request.entities_path:
            request_uri = salesforce.build_salesforce_request_uri(connector_context=request.connector_context,
                                                                  url_format=SALESFORCE_SOBJECTS_URL_FORMAT,
                                                                  request_path=request.entities_path)
        else:
            request_uri = salesforce.build_salesforce_request_uri(connector_context=request.connector_context,
                                                                  url_format=SALESFORCE_SOBJECTS_URL_FORMAT,
                                                                  request_path='')

        salesforce_response = salesforce.get_salesforce_client(request.connector_context).rest_get(request_uri)
        error_details = salesforce.check_for_errors_in_salesforce_response(salesforce_response)

        if error_details:
            return responses.ListEntitiesResponse(is_success=False, error_details=error_details)
        return responses.ListEntitiesResponse(is_success=True, entities=parse_entities(salesforce_response.response))

    def describe_entity(self, request: requests.DescribeEntityRequest) -> responses.DescribeEntityResponse:
        error_details = validation.validate_request_connector_context(request)
        if error_details:
            LOGGER.error('DescribeEntity request failed with ' + str(error_details))
            return responses.DescribeEntityResponse(is_success=False, error_details=error_details)

        request_uri = salesforce.build_salesforce_request_uri(connector_context=request.connector_context,
                                                              url_format=SALESFORCE_SOBJECT_DESCRIBE_URL_FORMAT,
                                                              request_path=request.entity_identifier)

        salesforce_response = salesforce.get_salesforce_client(request.connector_context).rest_get(request_uri)
        error_details = salesforce.check_for_errors_in_salesforce_response(salesforce_response)

        if error_details:
            return responses.DescribeEntityResponse(is_success=False, error_details=error_details)
        return responses.DescribeEntityResponse(is_success=True,
                                                entity_definition=parse_entity_definition(salesforce_response.response))
