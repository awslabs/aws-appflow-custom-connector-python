# Example AppFlow custom connector

This module is meant to serve as a guided example for writing and deploying a connector to enable Amazon AppFlow to use custom connectors as source or destination. The goal is to help you understand the development process and point out capabilities.

This tutorial also includes an example of Salesforce connector that you can use immediately in AppFlow and test custom connector functionalities. This tutorial includes details about Salesforce connector built using aws-appflow-custom-connector-python-sdk module.

## SalesforceExampleConnector:

A sample connector built using aws-appflow-custom-connector-python-sdk module to interact with Salesforce APIs using Http REST APIs in Amazon AppFlow with following capabilities,

* Accessing Salesforce:
    * Use OAuth2 credentials
* Connector as Source:
    * Fetch given data set of record IDs or apply query filtering to fetch data from Salesforce.
    * Fetch all possible records using pagination token
    * Incrementally pull delta from Salesforce
* Connector as destination:
    * Write a batch of records to Salesforce from Amazon AppFlow

This sample connector can be used as with any other compatible connector in AppFlow to transfer data from any other connector to Salesforce and Salesforce to any other connector. Additionally, this same connection can be used as both source and destination to transfer within Salesforce. A connector should have ConfigurationHandler, MetadataHandler and RecordHandler to make it use within Amazon AppFlow.

In the next sections we take a closer look at the methods we must implement on the ConfigurationHandler, MetadataHandler and RecordHandler to make this work end to end with Amazon AppFlow.

### LambdaHandler

The connector built using Lambda function should have an entry point that deals with various capabilities of the connector such as Metadata, Configuration and RecordHandler. The abstract class BaseLambdaConnectorHandler we are extending takes care of all the Lambda interface bits and delegates on the discrete operations that are relevant to the task at hand. A connector should have these three handlers at minimum, otherwise a connector cannot be used in AppFlow to execute a flow end to end. While deploying this connector code as Lambda function, the fully qualified name of  com.amazonaws.appflow.custom.connector.example.handler::SalesforceLambdaHandler should be used as handler function in Lambda.

```python
def salesforce_lambda_handler(event, context):
    """Lambda entry point."""
    return SalesforceLambdaHandler().lambda_handler(event, context)
  ```

### ConfigurationHandler

Let’s take a closer look at ConfigurationHandler requirements. In the following example, we have the basic functions that you need to implement when using the Amazon AppFlow ConfigurationHandler to satisfy the boiler plate work of serialization and initialization. The abstract class we are extending takes care of all the Lambda interface bits and delegates on the discrete operations that are relevant to the task at hand.

The describeConnectorConfiguration defines the capability of the connector such as supported modes, supported Auth types, scheduling frequencies, runtime settings of different scopes(source mode, destination mode, both and connector profile) etc., This information is fetched during connector registration process and stored in AppFlow connector registry. Using this information Amazon AppFlow UI renders the connector and navigate the user accordingly.

The capabilities of this sample connector defined as part of connector configuration:

* Connector modes: Source and Destination
* Authentication config: OAuth2 and its defaults
    * Additionally, this has other inputs user has to provide such as loginUrl, authCodeUrl.
    * Connector defaults the OAuth parameters so that user doesn’t have to provide explicitly.

```python
AUTH_URL = 'https://login.salesforce.com/services/oauth2/authorize'
LOGIN_URL = 'https://login.salesforce.com/services/oauth2/token'
REFRESH_URL = 'https://login.salesforce.com/services/oauth2/token'
REDIRECT_URL = 'https://login.salesforce.com'
    
o_auth_2_defaults = auth.OAuth2Defaults(auth_url=[AUTH_URL],
                        login_url=[LOGIN_URL],
                        refresh_url=[REFRESH_URL],
                        redirect_url=[REDIRECT_URL],
                        o_auth_scopes=['api', 'refresh_token', 'id'],
                        o_auth_2_grant_types_supported=[auth.OAuth2GrantType.AUTHORIZATION_CODE])
```
* Supported API versions: v51.0
    * Today this sample connector uses Salesforce v51.0 version of the APIs. In future we may add more supported API versions. When there are more API versions, AppFlow users can choose a particular version and execute their flows.
* Supported trigger types: Defaults OnDemand and Scheduled
    * Amazon AppFlow allows users to run their flows to execute once or in incremental scheduled data pull using this connector.
* Supported write operation: Insert
    * When this connector used as destination in AppFlow, only operation allowed is Insert.

A successful registration of a connector enables user to create connector profile according to the supported Auth types and flows according to supported modes. A successful connector profile includes validating the user credentials and connector profile runtime settings. During this process Amazon AppFlow invokes validateCredentials  to validate the user credentials and validateRuntimeSettings with connector_profile scope to validate the runtime settings.

A successful connector profile creation enables user to create the flow using the connector as per the mode(source or destination). During the flow creation, Amazon AppFlow invokes the validateRuntimeSettings with respective scope(SOURCE, DESTINATION or SOURCE_AND_DESTINATION).

```python
class SalesforceConfigurationHandler(ConfigurationHandler):
    """Salesforce Configuration Handler."""
    def validate_connector_runtime_settings(self, request: requests.ValidateConnectorRuntimeSettingsRequest) -> \
            responses.ValidateConnectorRuntimeSettingsResponse:
            switcher = {
                SOURCE_AND_DESTINATION: """Validate the fields common to source and destination"""
                SOURCE:"""Validate the fields specific to source"""
                DESTINATION:"""Validate the fields specific to destination"""
                CONNECTOR_PROFILE:"""Validate the fields specific to connector profile"""                   
            }
        return responses.ValidateConnectorRuntimeSettingsResponse(is_success=True)

    def validate_credentials(self, request: requests.ValidateCredentialsRequest) -> \
            responses.ValidateCredentialsResponse:
        """Validate the given credentails and permissions either by making metadata call or method preferred by SaaS provider."""
        return responses.ValidateCredentialsResponse(is_success=True)

    def describe_connector_configuration(self, request: requests.DescribeConnectorConfigurationRequest) -> \
            responses.DescribeConnectorConfigurationResponse:
        connector_modes = [config.ConnectorModes.SOURCE, config.ConnectorModes.DESTINATION]

        instance_url_setting = settings.ConnectorRuntimeSetting(key=constants.INSTANCE_URL_KEY,
                                                                data_type=settings.ConnectorRuntimeSettingDataType
                                                                .String,
                                                                required=True,
                                                                label='Salesforce Instance URL',
                                                                description='URL of the instance where user wants to ' +
                                                                            'run the operations',
                                                                scope=settings.ConnectorRuntimeSettingScope
                                                                .CONNECTOR_PROFILE)
        api_version_setting = settings.ConnectorRuntimeSetting(key=API_VERSION_KEY,
                                                               data_type=settings.ConnectorRuntimeSettingDataType
                                                               .String,
                                                               required=True,
                                                               label='Salesforce API version',
                                                               description='Salesforce API version to use.',
                                                               scope=settings.ConnectorRuntimeSettingScope
                                                               .CONNECTOR_PROFILE)
        connector_runtime_settings = [instance_url_setting, api_version_setting]

        o_auth_2_defaults = auth.OAuth2Defaults(auth_url=[AUTH_URL],
                                                login_url=[LOGIN_URL],
                                                refresh_url=[REFRESH_URL],
                                                redirect_url=[REDIRECT_URL],
                                                o_auth_scopes=['api', 'refresh_token', 'id'],
                                                o_auth_2_grant_types_supported=[auth.OAuth2GrantType.AUTHORIZATION_CODE])
        authentication_config = auth.AuthenticationConfig(is_oauth_2_supported=True,
                                                          o_auth_2_defaults=o_auth_2_defaults)

        return responses.DescribeConnectorConfigurationResponse(is_success=True,
                                                                connector_owner=CONNECTOR_OWNER,
                                                                connector_name=CONNECTOR_NAME,
                                                                connector_version=CONNECTOR_VERSION,
                                                                connector_modes=connector_modes,
                                                                connector_runtime_setting=connector_runtime_settings,
                                                                authentication_config=authentication_config,
                                                                supported_api_versions=[API_VERSION],
                                                                supported_write_operations=constants
                                                                .SUPPORTED_WRITE_OPERATIONS)

```

### MetadataHandler

Amazon AppFlow deals with metadata of the object to create proper query for fetching the data from source and apply the transformations given in the flow tasks. AppFlow restricts users to use only the entities defined the listEntities for both source and destination modes in the flows. Also restricts users to use only the fields and its properties defined in the describeEntity in tasks in order to apply the transformations such as mapping, masking, filtering etc., during data processing step of the flow execution. The properties of the entity such as datatype, queryable, updatable etc., helps customers to define the filter condition, mapping tasks and flow triggers correctly. For example, date fields can be used for incremental pull by adjusting the time window.

```python
class SalesforceMetadataHandler(MetadataHandler):
    """Salesforce Metadata handler."""
    def list_entities(self, request: requests.ListEntitiesRequest) -> responses.ListEntitiesResponse:
        """Using the credentials provided in the request, invoke metadata API calls"""
        """to Salesforce and convert the response to the Entity format."""

    def describe_entity(self, request: requests.DescribeEntityRequest) -> responses.DescribeEntityResponse:
        """Using the credentials provided in the request, invoke metadata API calls"""
        """to Salesforce and convert the response to the EntityDefinition format."""
```

### RecordHandler

AppFlow’s Flow execution for a custom connector mostly depends on the implementation of of this RecordHandler interface. This is where we expect customers to implement the core functionality of making requests source/destination application in order to get/post data. In the Salesforce example we have implemented three methods of RecordHandler. RetrieveData is used to lookup records against a batch of id’s from the source connector. Input request object for this method contains fieldname along with batch of id’s corresponding to that filed .  QueryData method is used when users is interested in querying the under laying application by using a filter query.  The filter query given by the user should follow specific AppFlow DSL and AppFlow SDK will help in parsing this filter expression. WriteData method is used to write a batch of records to destination connector. Request object which is passed as a parameter this method will have a list objects which have to be written to destination application. In the given Salesforce example we process each record present in the list and write it to Saleforce by building an appropriate write query.
```python
class SalesforceRecordHandler(RecordHandler):
    """Salesforce Record handler."""
    def retrieve_data(self, request: requests.RetrieveDataRequest) -> responses.RetrieveDataResponse:
        """Retrieves the batch of records against a set of identifiers from Salesforce"""
        """Build a salesforce request URI with the list of identifiers and make request"""
        """using credentials provided in the request."""
    def write_data(self, request: requests.WriteDataRequest) -> responses.WriteDataResponse:
        """Writes batch of records to the Salesforce"""
        """Request object contains batch of records to be written to salesforce."""
        """build a request object to write records to salesforce using the customer"""
        """credentials provided in the request."""
    def query_data(self, request: requests.QueryDataRequest) -> responses.QueryDataResponse:
        """Queries the data from Salesforce  against the supplied filter conditions."""
        """Request object contains a filter expression which is used the saleforce request URI."""
```

### Connected App configuration in Salesforce for Private Beta:

Follow these instructions to create a connected app in Salesforce if you haven't done so already.
*To create a global connected app in Salesforce*

1. Log in to Salesforce with an account that has administrator rights, and go to *Setup*.
2. In the navigation pane under *Platform Tools*, expand *Apps* and choose *App Manager*.
3. Choose *New Connected App* in the upper-right corner, and enter the following information for your connected app:

    1. The name of your connected app, such as "Amazon AppFlow Embedded Login App".
    2. The API name for your connected app. This is auto-generated and can be edited, if needed.
    3. The contact email address for Salesforce to use if they need to contact you about your connected app.
    4. The logo image URL and icon, if you have one. This is optional.
    5. A brief description to specify what the connected app is for, such as "Application which handles interaction between Salesforce and Amazon AppFlow console".
4. Select the *Enable OAuth Settings* check box.
5. In the *Callback URL* text field, enter the URLs for the console for the stages and Regions in which you will use the connected app. Enter these URLs on separate lines.
   
- https://us-west-2.console.aws.amazon.com/appflow/oauth
- https://us-east-2.console.aws.amazon.com/appflow/oauth
- https://us-west-1.console.aws.amazon.com/appflow/oauth
- https://ap-south-1.console.aws.amazon.com/appflow/oauth
- https://ap-southeast-1.console.aws.amazon.com/appflow/oauth
- https://ap-southeast-2.console.aws.amazon.com/appflow/oauth
- https://ap-northeast-1.console.aws.amazon.com/appflow/oauth
- https://ap-northeast-2.console.aws.amazon.com/appflow/oauth
- https://ca-central-1.console.aws.amazon.com/appflow/oauth
- https://eu-central-1.console.aws.amazon.com/appflow/oauth
- https://eu.west-1.console.aws.amazon.com/appflow/oauth
- https://eu-west-2.console.aws.amazon.com/appflow/oauth
- https://eu-west-3.console.aws.amazon.com/appflow/oauth
- https://sa-east-1.console.aws.amazon.com/appflow/oauth
- https://af-south-1.console.aws.amazon.com/appflow/oauth

6. Select the *Require Secret for Web Server Flow* check box.
7. In the *Available OAuth Scopes* list, select the following items and then choose *add* to move them to the *Selected OAuth Scopes* list. You can customize this list as needed.
    1. Access and manage your data (api)
    2. Access custom permissions (custom_permissions)
    3. Access your basic information (id, profile, email, address, phone)
    4. Allow access to your unique identifier (openid)
    5. Perform requests on your behalf at any time (refresh_token, offline_access)
8. Choose *Save*.

To retrieve the client ID and client secret for use in your OAuth flow, you can view your connected app in Salesforce by choosing *Apps* and then *App Manager*, and then selecting the connected app that you created.
For more information on connected apps in Salesforce, see Connected Apps (https://help.salesforce.com/articleView?id=connected_app_overview.html)
in the Salesforce documentation.

### How to use this Sample Connector in Amazon AppFlow?

Follow below steps in order to use the sample connector with Amazon AppFlow.

1. Go to the Connector Registry page of AppFlow and register the lambda as a new connector.
2. After registering the connector, Go to Connections tab and choose the custom connector you have registered and click on Create Connection. Please fill all the required details for authenticating to the connector and click on continue. A new connector profile is created for the custom connector
3. Based on the connector configuration you can use this custom connector as a source or destination or both and create a flow.

For more information on using the connector, please refer to the Amazon AppFlow user guide.
