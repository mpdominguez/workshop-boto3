# Threads are used by default in the managed transfer methods. To ensure no threads are used in the transfer process,
# set use_threads to False. Note that in setting use_threads to False, the value for max_concurrency is ignored as the
# main thread will only ever be used:

import boto3
from boto3.s3.transfer import TransferConfig
s3_bucket = "test-uala"
s3_file="tmp.txt.large"

# Get the service client
s3 = boto3.client('s3')

# Ensure that no threads are used.
config = TransferConfig(use_threads=False)

# Download object at s3_bucket with key-name to tmp.txt with the
# set configuration
s3.download_file(s3_bucket, s3_file, s3_file, Config=config)
