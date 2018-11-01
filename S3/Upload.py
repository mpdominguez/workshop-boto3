#To upload a file by name, use one of the upload_file methods:
import boto3

s3_file="tmp.txt"
s3_bucket="test-uala"

# Get the service client
s3 = boto3.client('s3')

# Upload tmp.txt to bucket-name at key-name
s3.upload_file(s3_file, s3_bucket, s3_file)
