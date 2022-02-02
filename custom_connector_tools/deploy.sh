#!/bin/bash
set -o pipefail

cat << EOF
# Run this script from the custom_connector_tools directory.
# This script performs the following actions:
# 1. Creates the bucket if you have provided empty string.
# 2. Removes the package name directory from the directory where python sdk exists.
# 3. Install the requirements in the  package name directory.
# 3. Uploads the packaged connector code to the S3 bucket you specified/or created if not specified.
# 5. Deploys the connector.
# 6. Describe the connector stack resources created.
# 7. Please verify the policies in custom-connector-example/template.yml.
EOF

while true; do
    read -p "Do you wish to proceed? (yes or no) " yn
    case $yn in
        [Yy]* ) echo "Proceeding..."; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

if [ "$#" -lt 4 ]; then
    echo "\n\nERROR: Script requires 4 arguments \n"
    echo "\n1. The AWS_REGION to target (e.g. us-east-1 or us-east-2) \n"
    echo "\n2. S3_BUCKET used for publishing artifacts.\n"
    echo "\n3. The STACK_NAME to create in cloudformation \n"
    echo "\n4. The PACKAGE_NAME to install the dependency libraries. \n"
    exit;
fi

AWS_REGION=$1
if [ -z "$AWS_REGION" ]
then
      AWS_REGION="us-east-1"
fi
echo "Using AWS Region $AWS_REGION"

BUCKET_NAME=$2
if [ -z "$BUCKET_NAME" ]
then
  BUCKET_ID=$(dd if=/dev/random bs=8 count=1 2>/dev/null | od -An -tx1 | tr -d ' \t\n')
  BUCKET_NAME=customconnector-artifacts-$BUCKET_ID
  aws --region $AWS_REGION s3 mb s3://$BUCKET_NAME
fi
echo "Using Bucket Name $BUCKET_NAME"

STACK_NAME=$3
echo "Using Stack Name $STACK_NAME"

PACKAGE_NAME=$4
echo "Using Package Name $PACKAGE_NAME"

rm -rf ../../"$PACKAGE_NAME"
pip install --target ../../"$PACKAGE_NAME"/python -r ../requirements.txt

aws --region $AWS_REGION cloudformation package --template-file template.yml --s3-bucket "$BUCKET_NAME" --output-template-file out.yml
aws --region $AWS_REGION cloudformation deploy --template-file out.yml --stack-name "$STACK_NAME" --capabilities CAPABILITY_NAMED_IAM
aws --region $AWS_REGION cloudformation describe-stack-resources --stack-name "$STACK_NAME"
