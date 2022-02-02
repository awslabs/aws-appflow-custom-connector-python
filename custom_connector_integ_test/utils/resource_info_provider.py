import time
from unittest import SkipTest

from custom_connector_integ_test.configuration.test_configuration import TestConfiguration


# This class also helps in defaulting resource names if they are not explicitly provided in the configuration.

class ResourceInfoProvider:
    versions = {}
    names = {}

    created_profiles = set()
    created_connectors = set()

    integ_connector = "Integ_Connector_"

    integ_profile = "Integ_Profile_"

    integ_flow = "Integ_Flow_"

    def __init__(self,
                 config: TestConfiguration):
        self.config = config
        self.prefix = config.resource_prefix or ""
        self.default_connector_name = config.custom_connector_configurations[0].name
        self.default_profile_name = config.custom_connector_profile_configurations[0].name
        for profileConfig in config.custom_connector_profile_configurations:
            self.versions[profileConfig.name] = profileConfig.default_api_version or 1
        for profileConfig in config.custom_connector_profile_configurations:
            self.names[profileConfig.name] = profileConfig.connector_name or self.default_connector_name
        self.test_start_time = str(int(time.time()))

    def get_api_for_profile_name(self, profile_name, api_version):
        return api_version or self.versions[profile_name or self.default_profile_name]

    def get_version_for_profile(self, profile_name):
        return self.versions[profile_name]

    def get_connector_for_profile(self, profile_name):
        return self.names[profile_name]

    def generate_resource_name(self, name, resource_type):
        return resource_type + self.prefix + name + self.test_start_time

    def generate_profile_name(self, name):
        return self.generate_resource_name(name, self.integ_profile)

    def generate_flow_name(self, name):
        return self.generate_resource_name(name, self.integ_flow)

    def generate_connector_name(self, name):
        return self.generate_resource_name(name, self.integ_connector)

    def get_connector_for_profile_name(self, profile_name):
        return self.get_connector_name(self.names[profile_name or self.default_profile_name])

    def get_connector_name(self, connector_name):
        return self.get_connector_name_if_created(connector_name or self.default_connector_name)

    def get_profile_name(self, profile_name):
        return self.get_profile_name_if_created(profile_name or self.default_profile_name)

    def get_connector_name_if_created(self, name):
        if not self.created_connectors.__contains__(name):
            raise SkipTest(f'Connector {name} failed to Create')
        return self.generate_connector_name(name)

    def get_profile_name_if_created(self, name):
        if not self.created_profiles.__contains__(name):
            raise SkipTest(f'Profile {name} failed to Create')
        return self.generate_profile_name(name)

    def add_to_created_profiles(self, name):
        self.created_profiles.add(name)

    def add_to_created_connectors(self, name):
        self.created_connectors.add(name)
