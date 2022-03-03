FROM public.ecr.aws/lambda/python:3.8

# Copy function code
COPY custom_connector_example ${LAMBDA_TASK_ROOT}
COPY custom_connector_sdk ${LAMBDA_TASK_ROOT}
COPY custom_connector_queryfilter ${LAMBDA_TASK_ROOT}

# Install the function's dependencies using file requirements.txt
# from your project folder.
COPY requirements.txt  .
RUN  pip3 install -r ./requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "custom_connector_example.handlers.lambda_handler.salesforce_lambda_handler" ]