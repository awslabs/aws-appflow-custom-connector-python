from custom_connector_integ_test.configuration import services
from custom_connector_integ_test.configuration.test_configuration import TestBucketConfiguration


class S3Helper:
    def __init__(self,
                 bucket_config: TestBucketConfiguration):
        self.bucket_config = bucket_config

    def upload_file(self, file: str, file_name: str):
        services.get_s3().put_object(Bucket=self.bucket_config.bucket_name,
                                     Key=self.bucket_config.bucket_prefix + file_name,
                                     Body=str.encode(file))
