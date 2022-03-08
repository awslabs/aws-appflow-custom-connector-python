from enum import Enum, auto
from typing import List

TIME_TO_LIVE = 'timeToLive'
TIME_TO_LIVE_UNIT = 'timeToLiveUnit'
KEY = 'key'
DATA_TYPE = 'dataType'
REQUIRED = 'required'
LABEL = 'label'
DESCRIPTION = 'description'
SCOPE = 'scope'
CONNECTOR_SUPPLIED_VALUE_OPTIONS = 'connectorSuppliedValueOptions'

class ConnectorRuntimeSettingDataType(Enum):
    """Enum for connector runtime setting data type."""
    String = auto()
    Date = auto()
    DateTime = auto()
    Long = auto()
    Integer = auto()
    Boolean = auto()

class ConnectorRuntimeSettingScope(Enum):
    """Defines the scope for a given connector runtime setting. All connector runtime settings will be aggregated
    and will be sent along with every function invocation on the connector.

    """
    # Settings to be populated during connector profile creation.
    CONNECTOR_PROFILE = auto()

    # Setting to be populated during a flow creation if the connector is chosen as a source connector.
    SOURCE = auto()

    # Setting to be populated during a flow creation if the connector is chosen as a destination connector.
    DESTINATION = auto()

    # Setting to be populated during a flow creation if the connector is chosen either as a source or a destination
    # connector.
    SOURCE_AND_DESTINATION = auto()

class TimeUnit(Enum):
    """Enum of time units."""
    NANOSECONDS = auto()
    MICROSECONDS = auto()
    MILLISECONDS = auto()
    SECONDS = auto()
    MINUTES = auto()
    HOURS = auto()
    DAYS = auto()

class CacheControl:
    """Represents the caching policy for metadata for the supported entities."""
    def __init__(self, time_to_live: int = None, time_to_live_unit: TimeUnit = None):
        # Time to keep the metadata in cache.
        # Return a large number when entity metadata is not dynamic and can
        # be cached for long time. The minimum allowed value is 600 seconds.
        self.time_to_live = time_to_live

        # TimeUnit for the time_to_live
        self.time_to_live_unit = time_to_live_unit

    def to_dict(self):
        return {TIME_TO_LIVE: self.time_to_live,
                TIME_TO_LIVE_UNIT: self.time_to_live_unit and self.time_to_live_unit.name}

class ConnectorRuntimeSetting:
    """Represents the setting that the connector needs at runtime and the input will be provided by the AppFlow user.
    For eg. instanceUrl, maxParallelism, etc.

    """
    def __init__(self,
                 key: str,
                 data_type: ConnectorRuntimeSettingDataType,
                 required: bool,
                 label: str,
                 description: str,
                 scope: ConnectorRuntimeSettingScope,
                 connector_supplied_value_options: List[str] = None):
        # Unique identifier for the connector runtime setting
        self.key = key

        # Data type for the connector runtime setting.
        self.data_type = data_type

        # Specifies if this setting is required or not.
        self.required = required

        # Label for the connector runtime setting.
        self.label = label

        # Description of the connector runtime setting.
        self.description = description

        # Scope of the runtime setting needed for CONNECTOR_PROFILE, SOURCE, DESTINATION, etc.
        self.scope = scope

        # Optional connector supplied value options (with matching data type) that the user can pick from as a value
        # for this runtime setting.
        self.connector_supplied_value_options = connector_supplied_value_options

    def to_dict(self):
        return {KEY: self.key,
                DATA_TYPE: self.data_type.name,
                REQUIRED: self.required,
                LABEL: self.label,
                DESCRIPTION: self.description,
                SCOPE: self.scope.name,
                CONNECTOR_SUPPLIED_VALUE_OPTIONS: self.connector_supplied_value_options}
