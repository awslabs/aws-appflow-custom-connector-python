# Integration Test FrameWork
This document explains how to run the integration tests provided by AppFlow for a custom connector.

## Prerequisites:

- python

## Test Case Overview:

The framework provides the following test cases.

1. Register and Describing the connector.
2. Calling the metadata apis.
3. Running a flow from s3 -> connector
4. Running a flow from the connector -> s3

Additionally, we provide a test class that cleans up all AppFlow resources created by the integration tests.
This test case cleans up resources based on the prefix "Integ_{ResourceType}" e.g. Integ_Profile. 
You can also provide a prefix in the test configuration which will be appended to all resources.
If you are running multiple test cases in the same aws account, be sure to use this prefix. Otherwise,
one test run might delete resources deployed by another test run.

All tests are written using unittest.

## Configuration File Overview

The test cases are driven by a set of configuration files. The main configuration file location is set
as an env variable.

The test configuration allows you to specifiy any number of custom connectors and connector profiles.
These resources are given a name. This name will be used as part of a randomly
generated name. All tests cases take as input either a connector name or a connector profile name
as an optinal parameter. If this name is not provided, then the first profile in the configuration
list will be used. To make the configuration simple, it may be worth specifying one profile and
connector per test file. Instead, you can use multiple configuration files.

You are also free to include as many connectors as you want in one configuration file. In general, anything that
can be done in multiple test configuration files, can be done in a single file.

The configuration file is in json. It includes a json list for each test case. Each json object in the list
is a test case.
e.g.

```
"listConnectorEntitiesTestConfigurations": [ // Test for the list connector
    {
      // Optional: This file is identical to the response provided by list connector entities api.
      // However, not all entities need to be provided. The test case will only evaluate equality between entities in validation file.
      "validationFileName": "string",
      "profileName":"string", // Optional: Profile used to run the test. Uses first profile otherwise.
      "apiVersion": "string", // Optional: Api version used in request input. Uses default api version from profile otherwise.
      "testName": "string", // Optional: Test name used to associate the test report with this test case.
      "entitiesPath": "string" // Optional: Paramater used in list entities request.
    }
  ],
```

There is a test case called listConnectorEntitiesTest. 
This test takes in the following parameters shown in the sample-test-config.json
You can specify multiple test cases per test by adding another json payload to the list. 
Alternatively, an empty list won't run any test cases for that test.

An example set of configuration files can be found in the salesforce custom connector example.

A base configuration file can be found in the current directory. 


## Running the tests
###Resources 
The configuration file requires several aws resources to already exist in your account. The purpose of these
resources is described in the sample-test-config.json file.
1. A S3 bucket with AppFlow bucket policy.
2. A Secrets Manager secret for each set of credentials.
3. A Lambda custom connector.

Note: The integration tests will not delete files that are created during the test run. 
The test bucket you're using, should have an object expiration for the specific prefix used by the test cases.

###Environment Configuration
The integration tests rely on both the AWS_DEFAULT_REGION environment variable, a TEST_CONFIG env variable 
and aws credentials environment variables.

```
TEST_CONFIG=custom_connector_example/salesforce-example-test-files/test-file.json;
AWS_DEFAULT_REGION=us-west-2;
AWS_ACCESS_KEY_ID=keyId;
AWS_SECRET_ACCESS_KEY=key;
```

###Running the test
The test class can be run directly or subclassed.
For example, in the salesforce example connector we sub-class the test class. 
```
class SalesTest(AppflowTestCase):
    pass
```
The tests can then be run with the following command.
```
python -m unittest -v custom_connector_example.integ_test.sales_test_case.SalesTest
```


##Writing your own test cases
You can extend the class AppflowTestCase if you want to write your test cases using the utility 
classes used by the integration tests.

For example, you can use the ResourceInfoProvider to get the name for a connector or profile generated during the test run.
If the resource failed to create then this method will raise a skip exception.

You can also use ServiceProvider class to get the amazon sdk clients used by the integration tests as well as a FlowPoller
class which you can use to poll flow executions. 

Tests in unittest run in alphabetical order. Be sure to name your test so that it happens after the connector is 
registered and before the profile is created.


This ensures that the AppFlow test cases always run, run after the connectors and connector profiles are created, 
and run before all resources are deleted.