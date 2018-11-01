# Generating Presigned URLs
# Pre-signed URLs allow you to give your users access to a specific object in your bucket without requiring them to have AWS security
# credentials or permissions. To generate a pre-signed URL, use the S3.Client.generate_presigned_url() method:

import boto3
import requests
s3_bucket = "test-uala"
s3_file="tmp.txt"

# Get the service client.
s3 = boto3.client('s3')

# Generate the URL to get 'key-name' from s3_bucket
url = s3.generate_presigned_url(
    ClientMethod='get_object',
    Params={
        'Bucket': s3_bucket,
        'Key': s3_file
    },
    ExpiresIn=30
)

print(url)
