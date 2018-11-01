# Sometimes depending on your connection speed, it is desired to limit or increase potential bandwidth usage.
# Setting the max_concurrency can help tune the potential bandwidth usage by decreasing or increasing the maximum amount
# of concurrent S3 transfer-related API requests:

import boto3
from boto3.s3.transfer import TransferConfig
s3_bucket = "test-uala"
s3_file="tmp.txt.large"

# Get the service client
s3 = boto3.client('s3')

# Decrease the max concurrency from 10 to 5 to potentially consume
# less downstream bandwidth.
config = TransferConfig(max_concurrency=5)

# Download object at s3_bucket with key-name to tmp.txt with the
# set configuration
s3.download_file(s3_bucket, s3_file, s3_file, Config=config)

# Increase the max concurrency to 20 to potentially consume more
# downstream bandwidth.
config = TransferConfig(max_concurrency=20)

# Download object at s3_bucket with key-name to tmp.txt with the
# set configuration
s3.download_file(s3_bucket, s3_file, s3_file, Config=config)
