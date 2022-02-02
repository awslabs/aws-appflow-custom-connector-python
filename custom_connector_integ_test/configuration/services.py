import boto3

# File with amazon service singletons

SECRETS_MANAGER = None

APP_FLOW = None

S3 = None


def get_appflow():
    global APP_FLOW
    if APP_FLOW is None:
        APP_FLOW = boto3.client('appflow')
    return APP_FLOW


def get_s3():
    global S3
    if S3 is None:
        S3 = boto3.client('s3')
    return S3


def get_secrets_manager():
    global SECRETS_MANAGER
    if SECRETS_MANAGER is None:
        SECRETS_MANAGER = boto3.client('secretsmanager')
    return SECRETS_MANAGER
