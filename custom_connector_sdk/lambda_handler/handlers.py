import abc
import custom_connector_sdk.lambda_handler.requests as requests
import custom_connector_sdk.lambda_handler.responses as responses

class MetadataHandler(metaclass=abc.ABCMeta):
    """This abstract base class defines the functionality to be implemented by custom connectors for metadata
    operations.

    """
    @abc.abstractmethod
    def list_entities(self, request: requests.ListEntitiesRequest) -> responses.ListEntitiesResponse:
        """Lists all the entities available in a paginated fashion. This API is recursive in nature
        and provides a heretical entity listing based on entityPath. If the ListEntitiesResponse
        returns has_children=true, that indicates that there are more entities in the next level.

        Parameters:
        request (ListEntitiesRequest)

        Return:
        ListEntitiesResponse

        """
        pass

    @abc.abstractmethod
    def describe_entity(self, request: requests.DescribeEntityRequest) -> responses.DescribeEntityResponse:
        """Describes the entity definition with its field level metadata.
        
        Parameters:
        request (DescribeEntityRequest)

        Return:
        DescribeEntityResponse
        
        """
        pass

class ConfigurationHandler(metaclass=abc.ABCMeta):
    """This abstract base class defines the functionality to be implemented by custom connectors for configurations,
    credentials related operations.

    """
    @abc.abstractmethod
    def validate_connector_runtime_settings(self, request: requests.ValidateConnectorRuntimeSettingsRequest) -> \
            responses.ValidateConnectorRuntimeSettingsResponse:
        """Validates the user inputs corresponding to the connector settings for a given ConnectorRuntimeSettingScope

        Parameters:
        request (ValidateConnectorRuntimeSettingsRequest)

        Return:
        ValidateConnectorRuntimeSettingsResponse

        """
        pass

    @abc.abstractmethod
    def validate_credentials(self, request: requests.ValidateCredentialsRequest) -> \
            responses.ValidateCredentialsResponse:
        """Validates the user provided credentials.

        Parameters:
        request (ValidateCredentialsRequest)

        Return:
        ValidateCredentialsResponse

        """
        pass

    @abc.abstractmethod
    def describe_connector_configuration(self, request: requests.DescribeConnectorConfigurationRequest) -> \
            responses.DescribeConnectorConfigurationResponse:
        """Describes the Connector Configuration supported by the connector.

        Parameters:
        request (DescribeConnectorConfigurationRequest)

        Return:
        DescribeConnectorConfigurationResponse

        """
        pass

class RecordHandler(metaclass=abc.ABCMeta):
    """This abstract base class defines the functionality to be implemented by custom connectors for record related
    operations.

    """
    @abc.abstractmethod
    def retrieve_data(self, request: requests.RetrieveDataRequest) -> responses.RetrieveDataResponse:
        """Retrieves the batch of records against a set of identifiers from the source application.

        Parameters:
        request (RetrieveDataRequest)

        Return:
        RetrieveDataResponse
        """
        pass

    @abc.abstractmethod
    def write_data(self, request: requests.WriteDataRequest) -> responses.WriteDataResponse:
        """Writes batch of records to the destination application.

        Parameters:
        request (WriteDataRequest)

        Return:
        WriteDataResponse
        """
        pass

    @abc.abstractmethod
    def query_data(self, request: requests.QueryDataRequest) -> responses.QueryDataResponse:
        """Queries the data from the source application against the supplied filter conditions.

        Parameters:
        request (QueryDataRequest)

        Return:
        QueryDataResponse
        """
        pass
