#To do a managed copy, use one of the copy methods:

import boto3
s3_bucket = "test-uala"
s3_file="tmp.txt"

# Get the service client
s3 = boto3.client('s3')

# Copies object located in mybucket at mykey
# to the location otherbucket at otherkey
copy_source = {
    'Bucket': s3_bucket,
    'Key': s3_file
}
s3.copy(copy_source, 'test-uala2', s3_file)
