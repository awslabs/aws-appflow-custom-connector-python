from enum import Enum, auto
from decimal import Decimal
from typing import List

from custom_connector_sdk.connector.configuration import ConnectorOperator

MIN_RANGE = 'minRange'
MAX_RANGE = 'maxRange'
ALLOWED_LENGTH_RANGE = 'allowedLengthRange'
ALLOWED_VALUE_RANGE = 'allowedValueRange'
ALLOWED_VALUES = 'allowedValues'
ALLOWED_VALUES_REGEX_PATTERN = 'allowedValuesRegexPattern'
ALLOWED_DATE_FORMAT = 'allowedDateFormat'
IS_RETRIEVABLE = 'isRetrievable'
IS_NULLABLE = 'isNullable'
IS_QUERYABLE = 'isQueryable'
IS_TIMESTAMP_FIELD_FOR_INCREMENTAL_QUERIES = 'isTimestampFieldForIncrementalQueries'
IS_CREATABLE = 'isCreatable'
IS_UPDATABLE = 'isUpdatable'
IS_UPSERTABLE = 'isUpsertable'
IS_DEFAULTED_ON_CREATE = 'isDefaultedOnCreate'
SUPPORTED_WRITE_OPERATIONS = 'supportedWriteOperations'
FIELD_NAME = 'fieldName'
DATA_TYPE = 'dataType'
DATA_TYPE_LABEL = 'dataTypeLabel'
LABEL = 'label'
DESCRIPTION = 'description'
IS_PRIMARY_KEY = 'isPrimaryKey'
DEFAULT_VALUE = 'defaultValue'
IS_DEPRECATED = 'isDeprecated'
CONSTRAINTS = 'constraints'
READ_PROPERTIES = 'readProperties'
WRITE_PROPERTIES = 'writeProperties'
FILTER_OPERATORS = 'filterOperators'
CUSTOM_PROPERTIES = 'customProperties'

class FieldDataType(Enum):
    """Data type of a field."""
    String = auto()
    Integer = auto()
    Float = auto()
    Double = auto()
    Long = auto()
    Short = auto()
    BigInteger = auto()
    BigDecimal = auto()
    ByteArray = auto()
    Boolean = auto()
    Date = auto()
    DateTime = auto()
    Struct = auto()
    Map = auto()
    List = auto()

class RangeConstraint:
    """Represents the range for a field."""
    def __init__(self, min_range: Decimal, max_range: Decimal):
        # Minimum value of the range.
        self.min_range = min_range

        # Maximum value of the range.
        self.max_range = max_range

    @classmethod
    def from_dict(cls, constraint: dict):
        if constraint is None:
            return None

        required_keys = {MIN_RANGE, MAX_RANGE}
        assert constraint.keys() >= required_keys, f'{cls.__name__} is missing required parameters {required_keys}'

        min_range = Decimal(constraint.get(MIN_RANGE))
        max_range = Decimal(constraint.get(MAX_RANGE))

        return cls(min_range, max_range)

    def to_dict(self):
        return {MIN_RANGE: self.min_range,
                MAX_RANGE: self.max_range}

class FieldConstraints:
    """Constraints that are applicable to the Field."""
    def __init__(self,
                 allowed_length_range: RangeConstraint = None,
                 allowed_value_range: RangeConstraint = None,
                 allowed_values: List[str] = None,
                 allowed_values_regex_pattern: str = None,
                 allowed_date_format: str = None):
        # Min and Max range of the length of the value.
        self.allowed_length_range = allowed_length_range

        # Min and Max range of value of this field.
        self.allowed_value_range = allowed_value_range

        # List of allowed values for this field.
        self.allowed_values = allowed_values

        # Value of the field should match with this regex pattern.
        self.allowed_values_regex_pattern = allowed_values_regex_pattern

        # Allowed date format for the field.
        self.allowed_date_format = allowed_date_format

    @classmethod
    def from_dict(cls, constraints: dict):
        if constraints is None:
            return None

        allowed_length_range = RangeConstraint.from_dict(constraints.get(ALLOWED_LENGTH_RANGE))
        allowed_value_range = RangeConstraint.from_dict(constraints.get(ALLOWED_VALUE_RANGE))
        allowed_values = constraints.get(ALLOWED_VALUES)
        allowed_values_regex_pattern = constraints.get(ALLOWED_VALUES_REGEX_PATTERN)
        allowed_date_format = constraints.get(ALLOWED_DATE_FORMAT)

        return cls(allowed_length_range,
                   allowed_value_range,
                   allowed_values,
                   allowed_values_regex_pattern,
                   allowed_date_format)

    def to_dict(self):
        return {ALLOWED_LENGTH_RANGE: self.allowed_length_range and self.allowed_length_range.to_dict(),
                ALLOWED_VALUE_RANGE: self.allowed_value_range and self.allowed_value_range.to_dict(),
                ALLOWED_VALUES: self.allowed_values,
                ALLOWED_VALUES_REGEX_PATTERN: self.allowed_values_regex_pattern,
                ALLOWED_DATE_FORMAT: self.allowed_date_format}

class ReadOperationProperty:
    """The properties that can be applied to a field when the connector is being used as a source."""
    def __init__(self,
                 is_retrievable: bool = None,
                 is_nullable: bool = None,
                 is_queryable: bool = None,
                 is_timestamp_field_for_incremental_queries: bool = None):
        # Specifies if the source field can be returned in a search result.
        self.is_retrievable = is_retrievable

        # Specifies if the source field can have a null value.
        self.is_nullable = is_nullable

        # Specifies if the source field can be queried.
        self.is_queryable = is_queryable

        # Specifies if the source field can be used for incremental queries.
        self.is_timestamp_field_for_incremental_queries = is_timestamp_field_for_incremental_queries

    @classmethod
    def from_dict(cls, properties: dict):
        if properties is None:
            return None

        is_retrievable = properties.get(IS_RETRIEVABLE)
        is_nullable = properties.get(IS_NULLABLE)
        is_queryable = properties.get(IS_QUERYABLE)
        is_timestamp_field_for_incremental_queries = properties.get(IS_TIMESTAMP_FIELD_FOR_INCREMENTAL_QUERIES)

        return cls(is_retrievable, is_nullable, is_queryable, is_timestamp_field_for_incremental_queries)

    def to_dict(self):
        return {IS_RETRIEVABLE: self.is_retrievable,
                IS_NULLABLE: self.is_nullable,
                IS_QUERYABLE: self.is_queryable,
                IS_TIMESTAMP_FIELD_FOR_INCREMENTAL_QUERIES: self.is_timestamp_field_for_incremental_queries}

class WriteOperationType(Enum):
    """Enum for Write operation type."""
    INSERT = auto()
    UPDATE = auto()
    UPSERT = auto()
    DELETE = auto()

class WriteOperationProperty:
    """The properties that can be applied to a field when connector is being used as a destination."""
    def __init__(self,
                 is_creatable: bool = None,
                 is_updatable: bool = None,
                 is_nullable: bool = None,
                 is_upsertable: bool = None,
                 is_defaulted_on_create: bool = None,
                 supported_write_operations: List[WriteOperationType] = None):
        # Specifies if the destination field can be created by the current user.
        self.is_creatable = is_creatable

        # Specifies whether the field can be updated during an UPDATE or UPSERT write operation.
        self.is_updatable = is_updatable

        # Specifies if the destination field can have a null value.
        self.is_nullable = is_nullable

        # Specifies if the flow run can either insert new rows in the destination field if they do not already exist,
        # or update them if they do.
        self.is_upsertable = is_upsertable

        # Specifies if the default value will be used by application while creating records if not provided.
        self.is_defaulted_on_create = is_defaulted_on_create

        # A list of supported write operations. For each write operation listed, this field can be used in idFieldNames
        # when that write operation is present as a destination option.
        self.supported_write_operations = supported_write_operations

    @classmethod
    def from_dict(cls, properties: dict):
        if properties is None:
            return None

        is_creatable = properties.get(IS_CREATABLE)
        is_updatable = properties.get(IS_UPDATABLE)
        is_nullable = properties.get(IS_NULLABLE)
        is_upsertable = properties.get(IS_UPSERTABLE)
        is_defaulted_on_create = properties.get(IS_DEFAULTED_ON_CREATE)

        if SUPPORTED_WRITE_OPERATIONS in properties and properties.get(SUPPORTED_WRITE_OPERATIONS) is not None:
            supported_write_operations = list(map(lambda op: WriteOperationType[op],
                                                  properties.get(SUPPORTED_WRITE_OPERATIONS)))
        else:
            supported_write_operations = None

        return cls(is_creatable,
                   is_updatable,
                   is_nullable,
                   is_upsertable,
                   is_defaulted_on_create,
                   supported_write_operations)

    def to_dict(self):
        return {IS_CREATABLE: self.is_creatable,
                IS_UPDATABLE: self.is_updatable,
                IS_NULLABLE: self.is_nullable,
                IS_UPSERTABLE: self.is_upsertable,
                IS_DEFAULTED_ON_CREATE: self.is_defaulted_on_create,
                SUPPORTED_WRITE_OPERATIONS: self.supported_write_operations and
                [op_type.name for op_type in self.supported_write_operations]}

class FieldDefinition:
    """Describes the data model of a field. For example, for an account entity, the fields would be account name,
    account ID, and so on.

    """
    def __init__(self,
                 field_name: str,
                 data_type: FieldDataType,
                 data_type_label: str = None,
                 label: str = None,
                 description: str = None,
                 is_primary_key: bool = None,
                 default_value: str = None,
                 is_deprecated: bool = None,
                 constraints: FieldConstraints = None,
                 read_properties: ReadOperationProperty = None,
                 write_properties: WriteOperationProperty = None,
                 filter_operators: List[ConnectorOperator] = None,
                 custom_properties: dict = None):
        # The unique identifier of the connector field.
        self.field_name = field_name

        # DataType of this field.
        self.data_type = data_type

        # Application specific description of the data type, so that AppFlow user can be presented with the same
        # information in the public API for exposing connector specific metadata.
        if data_type_label is None:
            self.data_type_label = data_type.name
        else:
            self.data_type_label = data_type_label

        # Label for this field.
        self.label = label

        # Description of this field.
        self.description = description

        # Specifies if it can be used as a primary key.
        self.is_primary_key = is_primary_key

        # Default value of the field.
        self.default_value = default_value

        # Specifies if this field is deprecated.
        self.is_deprecated = is_deprecated

        # Constraints applicable to this field like length, value, etc.
        self.constraints = constraints

        # The properties that can be applied to a field when the connector is being used as a source.
        self.read_properties = read_properties

        # The properties that can be applied to a field when the connector is being used as a destination.
        self.write_properties = write_properties

        # Filter Operators applicable for this field. This value be overridden by the connector developers for specific
        # use cases. For example, if they wish to disallow certain operators for specific data types, that can be
        # modified by overriding this method.
        if filter_operators is not None:
            self.filter_operators = filter_operators
        elif self.data_type in (FieldDataType.Integer, FieldDataType.Float, FieldDataType.Double, FieldDataType.Long,
                                FieldDataType.Short, FieldDataType.BigInteger, FieldDataType.BigDecimal):
            self.filter_operators = [ConnectorOperator.NOT_EQUAL_TO,
                                     ConnectorOperator.EQUAL_TO,
                                     ConnectorOperator.LESS_THAN,
                                     ConnectorOperator.LESS_THAN_OR_EQUAL_TO,
                                     ConnectorOperator.GREATER_THAN,
                                     ConnectorOperator.GREATER_THAN_OR_EQUAL_TO]
        elif self.data_type in (FieldDataType.Date, FieldDataType.DateTime):
            self.filter_operators = [ConnectorOperator.EQUAL_TO,
                                     ConnectorOperator.LESS_THAN,
                                     ConnectorOperator.LESS_THAN_OR_EQUAL_TO,
                                     ConnectorOperator.GREATER_THAN,
                                     ConnectorOperator.GREATER_THAN_OR_EQUAL_TO,
                                     ConnectorOperator.BETWEEN]
        elif self.data_type == FieldDataType.String:
            self.filter_operators = [ConnectorOperator.CONTAINS,
                                     ConnectorOperator.EQUAL_TO,
                                     ConnectorOperator.NOT_EQUAL_TO]
        elif self.data_type == FieldDataType.Boolean:
            self.filter_operators = [ConnectorOperator.EQUAL_TO,
                                     ConnectorOperator.NOT_EQUAL_TO]
        elif self.data_type in (FieldDataType.Map, FieldDataType.List):
            self.filter_operators = [ConnectorOperator.CONTAINS]
        elif self.data_type in (FieldDataType.Struct, FieldDataType.ByteArray):
            self.filter_operators = []
        else:
            raise ValueError

        # Custom properties defined for this field.
        self.custom_properties = custom_properties

    @classmethod
    def from_dict(cls, definition: dict):
        if definition is None:
            return None

        required_keys = {FIELD_NAME, DATA_TYPE}
        assert definition.keys() >= required_keys, f'{cls.__name__} is missing required parameters {required_keys}'

        field_name = definition.get(FIELD_NAME)
        data_type = FieldDataType[definition.get(DATA_TYPE)]
        label = definition.get(LABEL)
        description = definition.get(DESCRIPTION)
        is_primary_key = definition.get(IS_PRIMARY_KEY)
        default_value = definition.get(DEFAULT_VALUE)
        is_deprecated = definition.get(IS_DEPRECATED)
        constraints = FieldConstraints.from_dict(definition.get(CONSTRAINTS))
        read_properties = ReadOperationProperty.from_dict(definition.get(READ_PROPERTIES))
        write_properties = WriteOperationProperty.from_dict(definition.get(WRITE_PROPERTIES))
        custom_properties = definition.get(CUSTOM_PROPERTIES)

        if definition.get(FILTER_OPERATORS) is not None:
            filter_operators = [ConnectorOperator[op] for op in definition.get(FILTER_OPERATORS)]
        else:
            filter_operators = None

        if DATA_TYPE_LABEL in definition:
            data_type_label = definition.get(DATA_TYPE_LABEL)
        else:
            data_type_label = data_type.name

        return cls(field_name,
                   data_type,
                   data_type_label,
                   label,
                   description,
                   is_primary_key,
                   default_value,
                   is_deprecated,
                   constraints,
                   read_properties,
                   write_properties,
                   filter_operators,
                   custom_properties)

    def to_dict(self):
        return {FIELD_NAME: self.field_name,
                DATA_TYPE: self.data_type.name,
                DATA_TYPE_LABEL: self.data_type_label,
                LABEL: self.label,
                DESCRIPTION: self.description,
                IS_PRIMARY_KEY: self.is_primary_key,
                DEFAULT_VALUE: self.default_value,
                IS_DEPRECATED: self.is_deprecated,
                CONSTRAINTS: self.constraints and self.constraints.to_dict(),
                READ_PROPERTIES: self.read_properties and self.read_properties.to_dict(),
                WRITE_PROPERTIES: self.write_properties and self.write_properties.to_dict(),
                FILTER_OPERATORS: self.filter_operators and [op.name for op in self.filter_operators],
                CUSTOM_PROPERTIES: self.custom_properties}
