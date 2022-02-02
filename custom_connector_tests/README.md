# Custom Connector Tests
This module contains python programs that developers can execute to verify connector functionality. This can be used as a verification step to make sure the Lambda handlers being implemented are operating as expected and returning the correct responses (as expected by AppFlow).

## Verification Tests
The main python program class is called `run_tests.py` and can be executed using the following command:

```text
$ pip3 install -r ./requirements.txt
...
$ python3 -m custom_connector_tests.run_tests custom_connector_example.handlers.lambda_handler SalesforceLambdaHandler custom_connector_tests/configuration/TestConfig.json
```
There are 3 required arguments:
1. `Module Name` This is the name of the python module that contains the connector lambda handler class.
2. `Class Name` This is the name of the python class that defines the connector lambda handler. This class should extend **BaseLambdaConnectorHandler**.
3. `Test Configuration File` This is a JSON configuration file used by the verification tests. A sample test configuration file is provided under **custom_connector_tests/configuration/TestConfig.json**

###Results
The test results will be displayed on the console/terminal where the python program or bash script is being executed. Any errors resulting will also be output to the console.

### Test Configuration
The configuration file defines request level parameters that are used by the testing script to verify connector's validity.

As the connector developer, you should be aware of what all parameters are expected by your connector which result in successful responses. For some test cases (like DescribeConnectorConfiguration), the test will do additional verification to make sure the response contains all the valid connector configurations that is expected by AppFlow. 

As the connector developer, you should also be aware of the entities and CRUD operations structure for your SaaS application. Verification for CRUD operations can be added to these tests by adding configurations to the TestConfig file **(RetrieveRecordConfigurations, WriteRecordConfigurations and QueryRecordConfigurations)**.

**RuntimeSettings**   
Key-Value map containing the runtime settings expected by the connector. Please provide all required RuntimeSettings that elicit a successful response from your connector.

You may optionally choose to only verify for the mode your connector is built for (ConnectorProfile, Source, Destination or combination of all three). By default, ConnectorProfile runtimeSettings must be provided.

**Credentials**
Type and credentials used by the connector to authorize against the SaaS provider. Refer to `custom_connector_sdk/connector/auth.py` for the allowed auth types. Provide details for only 1 scheme that is supported by your connector.

NOTE: For OAuth2 credentials, follow the SaaS provider's directions to obtain a valid Access and Refresh token.

**TestEntityIdentifier**
The unique identifier for the entity being used to test methods such as ListEntity, DescribeEntity, etc...

As the connector developer, you should be aware of your SaaS provider's entities. For example, the Salesforce connector uses the "Account" entity to test.

**Configurations**
Configuration for record level operations such as Retrieve, Write and Query should be provided separately here. You can provide a list of as many configurations you want to test (each configuration will result in a separate request to the connector handler).

Refer to `custom_connector_sdk/lambda_handler/requests.py` to determine the parameters for each type of request (there are required and optional fields). It is up to the developer to build configs that lead to a successful response from the connector (and also SaaS provider). For example, `Account` entity with AccountNumber=12345 is a valid entity in our Salesforce account and results in a successful retrieval.

The example `TestConfig.json` file contains sample Retrieve, Write and Query configurations that result in successful response from the example custom connector (Salesforce). For example, the UPSERT write operation type:
```json
{
  "entityIdentifier": "Account",
  "operation": "UPSERT",
  "idFieldNames": ["ExternalId__c"],
  "records": [
    "{\"Name\": \"UpsertAccount\", \"ExternalId__c\": \"Identifier123\"}"
  ],
  "allOrNone": false
}
```
The `entityIdentifier` tells the connector that the write operation is for the `Account` object in our salesforce instance.

The `operation` tells the connector to make an UPSERT request (INSERT or UPDATE).

The `idFieldNames` gives the key to be used as the identifier. Salesforce only supports UPSERT for ExternalIds (custom id field). Only provide a single id field since Salesforce only supports single id field names.

The `records` gives the list of records to insert or update. These records should have the field mentioned above.

The `allOrNone` is an optional flag that determines the behavior when a record fails to write.


### Sample Execution
All the tests are passing. Using sample TestConfig.json
```text
$ python3 -m custom_connector_tests.run_tests custom_connector_example.handlers.lambda_handler SalesforceLambdaHandler custom_connector_tests/configuration/TestConfig.json

INFO:root:-----------Starting verification tests for Configuration Handler-----------
INFO:root:Testing ValidateConnectorRuntimeSettings for ConnectorProfile...
INFO:root:Handling request for requestType: ValidateConnectorRuntimeSettingsRequest
INFO:root:Testing ValidateCredentials...
INFO:root:Handling request for requestType: ValidateCredentialsRequest
INFO:root:Testing DescribeConnectorConfiguration...
INFO:root:Handling request for requestType: DescribeConnectorConfigurationRequest
INFO:root:Configuration handler was verified successfully!
INFO:root:-----------Starting verification tests for Metadata Handler-----------
INFO:root:Testing ListEntities...
INFO:root:Handling request for requestType: ListEntitiesRequest
INFO:root:Testing DescribeEntity...
INFO:root:Handling request for requestType: DescribeEntityRequest
INFO:root:Metadata handler was verified successfully!
INFO:root:-----------Starting verification tests for Record Handler-----------
INFO:root:Testing RetrieveData configuration 0...
INFO:root:Handling request for requestType: DescribeEntityRequest
INFO:root:Handling request for requestType: RetrieveDataRequest
INFO:root:Testing WriteData configuration 0...
INFO:root:Handling request for requestType: DescribeEntityRequest
INFO:root:Handling request for requestType: WriteDataRequest
INFO:root:Testing QueryData configuration 0...
INFO:root:Handling request for requestType: DescribeEntityRequest
INFO:root:Handling request for requestType: QueryDataRequest
Tests completed successfully, see above logs for results
```

Test failure during `DescribeEntity` where entity does not exist.
```text
$ python3 -m custom_connector_tests.run_tests custom_connector_example.handlers.lambda_handler SalesforceLambdaHandler custom_connector_tests/configuration/TestConfig.json

INFO:root:-----------Starting verification tests for Configuration Handler-----------
INFO:root:Testing ValidateConnectorRuntimeSettings for ConnectorProfile...
INFO:root:Handling request for requestType: ValidateConnectorRuntimeSettingsRequest
INFO:root:Testing ValidateCredentials...
INFO:root:Handling request for requestType: ValidateCredentialsRequest
INFO:root:Testing DescribeConnectorConfiguration...
INFO:root:Handling request for requestType: DescribeConnectorConfigurationRequest
INFO:root:Configuration handler was verified successfully!
INFO:root:-----------Starting verification tests for Metadata Handler-----------
INFO:root:Testing ListEntities...
INFO:root:Handling request for requestType: ListEntitiesRequest
INFO:root:Testing DescribeEntity...
INFO:root:Handling request for requestType: DescribeEntityRequest
ERROR:root:Request failed with status code 404 error reason Not Found and Salesforce response is [{"errorCode":"NOT_FOUND","message":"The requested resource does not exist"}]
--- Logging error ---
Traceback (most recent call last):
  File "/Users/aladaniy/workspace/CustomConnector/aws-appflow-custom-connector-python-sdk/custom_connector_tests/invokers/base_test_invoker.py", line 146, in invoke_metadata_handler_tests
    assert response[responses.IS_SUCCESS], f'Describe Entity response returned unsuccessful response ' \
AssertionError: Describe Entity response returned unsuccessful response for entityId: ACC

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9/logging/__init__.py", line 1083, in emit
    msg = self.format(record)
  File "/usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9/logging/__init__.py", line 927, in format
    return fmt.format(record)
  File "/usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9/logging/__init__.py", line 663, in format
    record.message = record.getMessage()
  File "/usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9/logging/__init__.py", line 367, in getMessage
    msg = msg % self.args
TypeError: not all arguments converted during string formatting
Call stack:
  File "/usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9/runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/Users/aladaniy/workspace/CustomConnector/aws-appflow-custom-connector-python-sdk/custom_connector_tests/run_tests.py", line 25, in <module>
    main()
  File "/Users/aladaniy/workspace/CustomConnector/aws-appflow-custom-connector-python-sdk/custom_connector_tests/run_tests.py", line 19, in main
    test_invoker.invoke_metadata_handler_tests()
  File "/Users/aladaniy/workspace/CustomConnector/aws-appflow-custom-connector-python-sdk/custom_connector_tests/invokers/base_test_invoker.py", line 154, in invoke_metadata_handler_tests
    logger.error("Error encountered during MetadataHandler verification!", e)
Message: 'Error encountered during MetadataHandler verification!'
Arguments: (AssertionError('Describe Entity response returned unsuccessful response for entityId: ACC'),)
ERROR:root:Verification tests failed for the given Connector Handler. See logs for details
Traceback (most recent call last):
  File "/usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9/runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/Users/aladaniy/workspace/CustomConnector/aws-appflow-custom-connector-python-sdk/custom_connector_tests/run_tests.py", line 25, in <module>
    main()
  File "/Users/aladaniy/workspace/CustomConnector/aws-appflow-custom-connector-python-sdk/custom_connector_tests/run_tests.py", line 19, in main
    test_invoker.invoke_metadata_handler_tests()
  File "/Users/aladaniy/workspace/CustomConnector/aws-appflow-custom-connector-python-sdk/custom_connector_tests/invokers/base_test_invoker.py", line 156, in invoke_metadata_handler_tests
    raise e
  File "/Users/aladaniy/workspace/CustomConnector/aws-appflow-custom-connector-python-sdk/custom_connector_tests/invokers/base_test_invoker.py", line 146, in invoke_metadata_handler_tests
    assert response[responses.IS_SUCCESS], f'Describe Entity response returned unsuccessful response ' \
AssertionError: Describe Entity response returned unsuccessful response for entityId: ACC
```
