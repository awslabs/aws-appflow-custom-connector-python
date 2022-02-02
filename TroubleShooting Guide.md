### TroubleShooting Guide

##### 1. OOM from the lambda: 
Since your lambda connector will perform memory/CPU bound operation you might experience OOM exception (java.lang.OutOfMemoryError). Please go to your lambda log group and check for the OutOfMemoryError exception. Below is the Sample Stack Trace: 

````
START RequestId: b86c93c6-e1d0-11e7-955b-539d8b965ff9 Version: $LATEST
REPORT RequestId: b86c93c6-e1d0-11e7-955b-539d8b965ff9 
Duration: 122204.28 ms Billed Duration: 122300 ms Memory Size: 256 MB Max Memory Used: 256 MB
RequestId: b86c93c6-e1d0-11e7-955b-539d8b965ff9 Process exited before completing request
````

To resolve this issue , Please increase the  Memory allocation of your lambda. To know more please read


- https://docs.aws.amazon.com/lambda/latest/operatorguide/configurations.html#memory-config

##### 2. Exception while processing the request due to AccessDeniedException
````
Traceback (most recent call last):
  File "/var/task/custom_connector_sdk/lambda_handler/lambda_handler.py", line 38, in lambda_handler
    response = self.configuration_handler.validate_credentials(request)
  File "/var/task/custom_connector_example/handlers/configuration.py", line 39, in validate_credentials
    list_entities_response = SalesforceMetadataHandler().list_entities(list_entities_request)
  File "/var/task/custom_connector_example/handlers/metadata.py", line 142, in list_entities
    salesforce_response = salesforce.get_salesforce_client(request.connector_context).rest_get(request_uri)
  File "/var/task/custom_connector_example/handlers/salesforce.py", line 15, in get_salesforce_client
    return HttpsClient(get_access_token_from_secret(connector_context.credentials.secret_arn))
  File "/var/task/custom_connector_example/handlers/salesforce.py", line 49, in get_access_token_from_secret
    secret = secrets_manager.get_secret_value(SecretId=secret_arn)
  File "/opt/python/botocore/client.py", line 388, in _api_call
    return self._make_api_call(operation_name, kwargs)
  File "/opt/python/botocore/client.py", line 708, in _make_api_call
    raise error_class(parsed_response, operation_name)
botocore.exceptions.ClientError: An error occurred (AccessDeniedException) when calling the GetSecretValue operation: User: arn:aws:sts::*******:assumed-role/python-memory-FunctionRole-1B6GH25FAONJ3/python-memory-Function-mQamETBP6j7L is not authorized to perform: secretsmanager:GetSecretValue on resource: arn:aws:secretsmanager:us-west-2:*********:secret:appflow!*************-python-memory-python-memory-profile-Qdj0Lu because no identity-based
 policy allows the secretsmanager:GetSecretValue action
````

Your lambda fetches the credentials from the secret created in the secret manager in your AWS account.To fetch the credentials it uses getSecrets function on the secret. This type of error indicates that 
your lambda do not have permission on getSecret on your secrets. Please add the required permissions to your lambda.

##### 3. AccessDeniedException from Secrets even after providing the correct permissions to my connector lambda.

This happens when you try to access your secret right after making the changes in the permissions. AWS Secrets Manager uses a distributed computing model called eventual consistency. Any change that you make in Secrets Manager (or other AWS services) takes time to become visible from all possible endpoints. Some of the delay results from the time it takes to send the data from server to server, from replication zone to replication zone, and from region to region around the world.

Please read  https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot_general.html#troubleshoot_general_eventual-consistency for more details.


##### 4. ResourceNotFoundException from Secret Manager.

Amazon AppFlow creates the secret in AppFlow user account and then pass the secret arn to the connector. AWS Secrets Manager uses a distributed computing model called eventual consistency. Any change that you make in Secrets Manager (or other AWS services) takes time to become visible from all possible endpoints. Some of the delay results from the time it takes to send the data from server to server, from replication zone to replication zone, and from region to region around the world.

Please read  https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot_general.html#troubleshoot_general_eventual-consistency for more details.

#### 5. How do I put logs or find logs
AppFlow provides `flowName/connectorProfileLabel/executionId` to the `ConnectorContext`. Please use these string to query the log group for your lambda in the cloudwatch. Please Read more here : https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html for more advanced cloudwatch queries.

#### 6. Resolving issues becuase of connector lambda cold start.
This can happen when connector lambda is being invoked after a long period of inactivity. This cold start can result in timeout issues. Please follow the below links to know more on how to avoid such issues: 
https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-1/
https://aws.amazon.com/blogs/compute/new-for-aws-lambda-predictable-start-up-times-with-provisioned-concurrency/



