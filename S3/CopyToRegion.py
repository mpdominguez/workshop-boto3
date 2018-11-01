# To do a managed copy where the region of the source bucket is different than the region of the final
# bucket, provide a SourceClient that shares the same region as the source bucket:

import boto3
s3_bucket = "test-uala"
s3_file="tmp.txt"

# Get a service client for us-west-2 region
s3 = boto3.client('s3', 'us-west-2')
# Get a service client for the eu-central-1 region
source_client = boto3.client('s3', 'eu-central-1')

# Copies object located in mybucket at mykey in eu-central-1 region
# to the location otherbucket at otherkey in the us-west-2 region
copy_source = {
    'Bucket': s3_bucket,
    'Key': s3_file
}
s3.copy(copy_source, 'test-uala2', s3_file, SourceClient=source_client)
