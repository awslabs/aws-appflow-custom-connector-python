from enum import Enum, auto

class ConnectorModes(Enum):
    """Enumerates the supported connector Modes. Used by Connectors to declare the modes of operation a custom
    connector supports.

    """
    SOURCE = auto()
    DESTINATION = auto()

class ConnectorOperator(Enum):
    """Enumerates the set of operations that are allowed for constructing filter criteria against specific entity
    fields.

    """
    # TODO: Need to add description for each of the following

    # Column Filter Operator
    PROJECTION = auto()

    # Row Filter Operators
    LESS_THAN = auto()
    GREATER_THAN = auto()
    BETWEEN = auto()
    LESS_THAN_OR_EQUAL_TO = auto()
    GREATER_THAN_OR_EQUAL_TO = auto()
    EQUAL_TO = auto()
    CONTAINS = auto()
    NOT_EQUAL_TO = auto()

    # Operators with a Destination Field
    ADDITION = auto()
    SUBTRACTION = auto()
    MULTIPLICATION = auto()
    DIVISION = auto()

    # Masking related operators
    MASK_ALL = auto()
    MASK_FIRST_N = auto()
    MASK_LAST_N = auto()

    # Validation specific operators
    VALIDATE_NON_NULL = auto()
    VALIDATE_NON_ZERO = auto()
    VALIDATE_NON_NEGATIVE = auto()
    VALIDATE_NUMERIC = auto()

    NO_OP = auto()

class TriggerFrequency(Enum):
    """Enum for flow trigger frequency."""
    BYMINUTE = auto()
    HOURLY = auto()
    DAILY = auto()
    WEEKLY = auto()
    MONTHLY = auto()
    ONCE = auto()

class TriggerType(Enum):
    """Enum for flow trigger type."""
    SCHEDULED = auto()
    ONDEMAND = auto()
