# Configuration Settings
# To configure the various managed transfer methods, a boto3.s3.transfer.TransferConfig object can be provided
# to the Config parameter. Please note that the default configuration should be well-suited for most scenarios and
# a Config should only be provided for specific use cases. Here are some common use cases for configuring the managed s3 transfer methods:
# To ensure that multipart uploads only happen when absolutely necessary, you can use the multipart_threshold configuration parameter:

import boto3
from boto3.s3.transfer import TransferConfig
s3_bucket = "test-uala"
s3_file="tmp.txt.large"

# Get the service client
s3 = boto3.client('s3')

GB = 1024 ** 3
# Ensure that multipart uploads only happen if the size of a transfer
# is larger than S3's size limit for nonmultipart uploads, which is 5 GB.
config = TransferConfig(multipart_threshold=5 * GB)

# Upload tmp.txt to s3_bucket at key-name
s3.upload_file(s3_file, s3_bucket, s3_file, Config=config)
