#To download to a file by name, use one of the download_file methods:
import boto3
s3_bucket = "test-uala"
s3_file="tmp.txt"

# Get the service client
s3 = boto3.client('s3')

# Download object at s3_bucket with key-name to tmp.txt
s3.download_file(s3_bucket, s3_file, s3_file)
