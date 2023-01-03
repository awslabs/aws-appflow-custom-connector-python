# Deploy a connector
This document explains how you can deploy a lambda connector into your AWS account. This script uses the AWS CloudFormation template to deploy the custom connector lambda into the given AWS account.

## Prerequisites:

- pip3
- aws cli

## Command:

Run this command from the connector module which you want to deploy. Make sure that cloudformation template exists for the connector inside the connector module.

#### Command : ../custom-connector-tools/deploy.sh AWS_REGION BUCKET_NAME STACK_NAME

- AWS_REGION : AWS region where you want to deploy your custom connector. By default it will use the us-east-1 region, if the value that is provided is an empty string ("").

- BUCKET_NAME : S3 bucket where you want to upload artifacts to deploy the connector. By default it will create the S3 bucket, if the value that is provided is an empty string ("").

- STACK_NAME : Name of the stack to be displayed in AWS CloudFormation.

- PACKAGE_NAME : Name of the folder which will be created in the same directory as SDK and it will delete the existing folder if already exists.

Sample command : `../custom_connector_tools/deploy.sh us-west-2 agrshubh-awsappflow-us-west-2-test custom-connector package`
Sample command with region and S3 bucket as empty strings: `../custom_connector_tools/deploy.sh "" "" custom-connector package`

### Creating a template.yml for cloudformation.
Define the AWS CloudFormation template by cloning the template named template.yaml for Lambda connector deployment. Alternatively, you can copy the AWS CloudFormation template from the example connector module and change the handler parameter appropriately. Please make sure to verify the policies. This template.yml will put a policy as below on the execution role of lambda

if you want to restrict lambda access to the secrets. You can update the policy as below. 
##### Please fill your accountId and connectorLabel in the policy before deploying.

````
{
    "Version": "2012-10-17",
    "Statement": {
        "Action": "secretsmanager:GetSecretValue",
        "Resource": "arn:aws:secretsmanager:us-west-2:<your-aws-account>:secret:appflow!<your-aws-account>-<you-connector-label>-*”,
        "Effect": "Allow"
    }

}
````
This will allow lambda to access the secrets only for the connector profiles that were created using this lambda connector.

2. This script also attaches below policy
##### Please fill your accountId in the policy before deploying.
   ````
   {
   "Version": "2012-10-17",
   "Id": "default",
   "Statement": [
   {
   "Sid": "PolicyPermission-1CM96J5MWQY04",
   "Effect": "Allow",
   "Principal": {
   "Service": "appflow.amazonaws.com"
   },
   "Action": "lambda:InvokeFunction",
   "Resource": "arn:aws:lambda:us-west-2:<your-aws-account>:function:custom-connector-lN7JnmKTetlM",
   "Condition": {
   "StringEquals": {
   "AWS:SourceAccount": "<your-aws-account>"
   },
   "ArnLike": {
   "AWS:SourceArn": "arn:aws:appflow:us-west-2:<your-aws-account>:*"
          }
        }
      }
     ]
   }
   ````

## Deploying the example connector:

- Step 1 : Set your AWS account credentials to use aws cli using ‘aws configure’ command. Follow this link to get the creds: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-creds

- Step 2: Run the script from custom-connector-example module and it will deploy the connector the given AWS account.

## Deploying the new connector:

- Step 1: Define the AWS CloudFormation template by cloning the template named template.yaml for Lambda connector deployment. Alternatively, you can copy the AWS CloudFormation template from the example connector module and change the handler parameter appropriately.

- Step 2 : Set your AWS account credentials to use aws cli using ‘aws configure’ command. Follow this link to get the creds: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-creds

- Step 3: Run the script from newly built connector module and it will deploy the connector in the corresponding AWS account.

# Sharing the logs with the connector developer
There can be situation when as a AppFlow user you want to share the logs of the custom connector with the custom connector developer. Since lambda will be deployed in you account , AppFlow and Connector developer will be dependent on you to share the logs. We understand that you might not feel comfortable in providing the access to your log groups to either Connector Developer or AppFlow. Hence we have provided a script to fetch the selected logs.

To use the script , please run the below command 
````
./logfetcher.sh
````

Sample Inputs to the command
````
Provide Region:us-east-1
--------------
Provide Loggroup (Should be in the format of /aws/lambda/custom-connector-logging-Aaw0rrvylsya):/aws/lambda/custom-connector-logging-poc-function-Aaw0rrvylsya
------------------------------------------------------------------------------------------------
Provide name for log file that will be generated:debug-logs
-------------------------------------------------
Provide start time (in epoc seconds) for log query:1635383800
--------------------------------------------------
Provide End Time (in epoc seconds) for log query:1635384000
-------------------------------------------------
Provide Query String:filter @message like /appflow/ | fields @timestamp,@message | sort @timestamp desc
--------------------
Provide Bucket for log file:logbucket
---------------------------
Provide number of seconds until the pre-signed URL expires. 2000
-----------------------------------------------------------
Cloudwatch query takes time to execute. The time depends on the interval for which logs are being fetched.Provide wait time (seconds) before query finished.300
Are above details correct, Please select y/n:y
````

Read more here : https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html for more advanced cloudwatch queries.
