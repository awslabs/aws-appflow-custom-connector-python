import abc


class ConnectorTestInvoker(metaclass=abc.ABCMeta):
    """
        This interface defines the functionality that is required for testing custom connector implementation.
        The tests must verify behavior of all three handlers along with some implementation specific validations.
    """

    def invoke_configuration_handler_tests(self):
        """
            Tests for the ConfigurationHandler. This includes verifying behaviour of validate_credentials,
            validate_connector_runtime_settings and describe_connector_configuration.
        """
        pass

    def invoke_metadata_handler_tests(self):
        """
            Tests for the MetadataHandler. This includes verifying behaviour of list_entities and describe_entity.
        """
        pass

    def invoke_record_handler_tests(self):
        """
            Tests for the RecordHandler. This includes verifying behaviour of retrieve_data, write_data and query_data.
        """
        pass
