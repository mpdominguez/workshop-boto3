#To download to a writeable file-like object, use one of the download_fileobj methods. Note that this file-like object must allow binary to be written to it, not just text:
import boto3
s3_bucket = "test-uala"
s3_file="tmp.txt"

# Get the service client
s3 = boto3.client('s3')

# Download object at s3_bucket with key-name to file-like object
with open(s3_file, "wb") as f:
    s3.download_fileobj(s3_bucket, s3_file, f)

#To download using any extra parameters such as version ids, use the ExtraArgs parameter:

# Get the service client
s3 = boto3.client('s3')

# Download object at s3_bucket with key-name to tmp.txt
s3.download_file(
    s3_bucket, s3_file, s3_file,
    ExtraArgs={"VersionId": "my-version-id"}
)
#All valid ExtraArgs are listed at boto3.s3.transfer.S3Transfer.ALLOWED_DOWNLOAD_ARGS
