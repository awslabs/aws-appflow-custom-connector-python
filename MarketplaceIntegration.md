# Sharing AppFlow connectors via AWS Marketplace

Amazon AppFlow allows 3rd party developers and partners to author connectors and share them with other AppFlow users using AWS Marketplace. As a developer you can upload the Lambda as a “Container” product on AWS Marketplace to sell it to Amazon AppFlow customers or to share it for free. This guide provides the details on the development and publishing process. 

# Overview of creating connectors for AWS Marketplace

Amazon AppFlow customers discover and subscribe to connectors of interest on AWS Marketplace. 
This section helps the connector developers to build and test custom connectors, and deploy them for integration testing with Amazon AppFlow. Summary of steps:

1. Develop a custom connector.
2. Create a new product in AWS Marketplace.
3. Create Repository for your container.
4. Test/Validate your connector.
5. After you've completed the above steps, post your product onto AWS Marketplace.

## Step 1:  Developing Marketplace connectors

Amazon AppFlow provides support for developing the connector for various SaaS applications in Java and Python.

## Step 2:  Create your Connector product in AWS Marketplace

Amazon AppFlow only supports the “Container” product type for publishing custom connectors on Marketplace. Creating a product in AWS Marketplace involves the following steps: 

1. Create the product ID. https://docs.aws.amazon.com/marketplace/latest/userguide/container-product-getting-started.html#create-initial-container-product
2. Create the pricing details. https://docs.aws.amazon.com/marketplace/latest/userguide/container-product-getting-started.html#container-product-load-form
    Note : Amazon AppFlow only supports Free and Monthly subscription based model for pricing. It does not provide support for Custom/Hourly metering.
3. For paid products, integrate metering into your product. 
    1. To validate if the customer is entitled to use the paid product, you can add a validation in lambda to call the EntitlementUtil helper class provided with the SDK.
    2. To call the Entitlement checker you need to provide the ProductId as input.
    3. Instead of calling this entitlement check for every Lambda invocation, you are recommended to call it at a specific frequency of your choice from the Lambda code. e.g. once per hour or once per day

Once your request is approved from the AWS Marketplace for Limited use, proceed to the next step.

## Step 3: Create Repository for your container.

1. Select your product: Choose `Server` from the `Products` drop down tab of your AWS Marketplace Management Portal (https://4hs3rzdz.r.us-east-1.awstrack.me/L0/https:%2F%2Faws.amazon.com%2Fmarketplace%2Fmanagement%2Fhomepage/1/0100017c18e8d88e-e5c55f5d-9c02-4aea-aaf8-313d15621a11-000000/a08CntXX0hvPwR0OBuFAHEtxlLM=237) to go to the Server Products (https://4hs3rzdz.r.us-east-1.awstrack.me/L0/https:%2F%2Faws.amazon.com%2Fmarketplace%2Fmanagement%2Fproducts%2Fserver/1/0100017c18e8d88e-e5c55f5d-9c02-4aea-aaf8-313d15621a11-000000/dHlwBH29mAefqfiNc4YhN0Os4vo=237) page. Select your product using the corresponding radio button or by clicking its Title. 

2. Add repositories: From the `Request changes` drop down, choose `Add repositories` to create repositories that you can then push your product’s resources into. 

3. Push images to your repository: On the `Add repositories` page, click on `View existing repositories` to see all available repositories that were successfully added. Select the repository name, and choose `View push commands` to view instructions to push your container images and resources to the selected repository. Follow the steps provided below in *Packaging and uploading Marketplace connectors section below. 

4. Create a new version: On the `Products` page, select your product, and choose `Add new version` to create a version of your product using the container images and resources that you added to the repository. 

5. Update product details: Select `Update product information` to edit the data that buyers will see when they select your product. 

Note: Currently, AWS marketplace does not support the Lambda product types. So, it is your responsibility to provide the usage instructions to the users.

## Step 4: Test/Validate your connector. 

Please Follow the steps provided in Unit testing and Integration testing guidelines.

## Step 5: Publish the product to the public* 

After completing all the previous steps, you can publish your product to make it visible to all AWS AppFlow customers. Follow the instructions in Publishing container products (https://docs.aws.amazon.com/marketplace/latest/userguide/container-product-getting-started.html#container-product-publishing) in the AWS Marketplace Seller Guide. 

# Packaging and uploading Marketplace connectors* 

This section describes how to create and publish a container product with the required connector JAR files to AWS Marketplace. 

Prerequisites:

1.  Setup AWS Command Line Interface (AWSCLI). 
2.  Install Docker Engine.

Steps:

1. Create a DockerFile in your connector directory. You can use the DockerFile provided in the example.

        FROM public.ecr.aws/lambda/python:3.8

        #Copy function code
        COPY custom_connector_example ${LAMBDA_TASK_ROOT}
        COPY custom_connector_sdk ${LAMBDA_TASK_ROOT}
        COPY custom_connector_queryfilter ${LAMBDA_TASK_ROOT}

        #Install the function's dependencies using file requirements.txt from your project folder.
        COPY requirements.txt  .
        RUN  pip3 install -r ../requirements.txt --target "${LAMBDA_TASK_ROOT}"

        #Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
        CMD [ "custom_connector_example.handlers.lambda_handler.salesforce_lambda_handler" ]

2. Build your docker image by using the following command.

        docker build -t salesforcepaid .
      
3. Authenticate to the registry created from step 2.4a.

        aws ecr get-login-password --region region | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com (http://aws_account_id.dkr.ecr.region.amazonaws.com/)

4. Tag the image to push to repository.

        docker tag hello-world:1.0 aws_account_id.dkr.ecr.us-east-1.amazonaws.com/hello-world:1.0

5. Push the image

        docker push aws_account_id.dkr.ecr.us-east-1.amazonaws.com/hello-world:1.0

6. Validate the image is created in ECR or not.

        aws ecr describe-images --registry-id 709825985650 --repository-name test-product/salesforcepaid —region us-east-1

# Usage Instruction for Connector Users:

Ensure you have installed the latest version of the AWS CLI and Docker. For more information, see ECR documentation

For macOS or Linux systems, use the AWS CLI:

## Step 1: Retrieve the login command to authenticate your Docker client to your registry.

        aws ecr get-login-password --region us-east-1 | docker login --username AWS —password-stdin 709825985650.dkr.ecr.us-east-1.amazonaws.com

For Windows systems, use AWS Tools for PowerShell:

        Invoke-Expression -Command (Get-ECRLoginCommand -Region us-east-1 -RegistryId "709825985650").Command

Note: If you receive an 'Unknown options: -no-include-email' error when using the AWS CLI, ensure that you have the latest version installed.

## Step 2: Pull the docker images listed below.

        docker pull 709825985650.dkr.ecr.us-east-1.amazonaws.com/test-product/salesforcejava:1.0 (http://709825985650.dkr.ecr.us-east-1.amazonaws.com/test-product/salesforcejava:1.0)

## Step 3: Create an ECR repository in your account. Follow this to create repository https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html

## Step 4: Tag a new image based on the original source image.

        docker tag $SOURCE_IMAGE:$VERSION $TARGET_IMAGE:$VERSION

## Step 5: Run this for your AWS account where you want to deploy this.

        aws ecr get-login-password --region AWS_REGION | docker login --username AWS --password-stdin AWS_ACCOUNT.dkr.ecr.AWS_REGION.amazonaws.com (http://aws_account.dkr.ecr.us-east-1.amazonaws.com/)

## Step 6: Push the image into the repository you created.

        docker push docker push $TARGET_IMAGE:$VERSION

## Step 7: Create a lambda function in your account by using the container image.

You are all set to use this Lambda Connector.
