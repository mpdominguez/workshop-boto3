# Downloading a File
# The example below tries to download an S3 object to a file. If the service returns a 404 error, it prints an error message indicating that the object doesn't exist.

import boto3
import botocore

BUCKET_NAME = 'my-bucket-mrtdom' # replace with your bucket name
KEY = 'file.txt' # replace with your object key

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'file2.txt')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
