#To upload a readable file-like object, use one of the upload_fileobj methods. Note that this file-like object must produce binary when read from, not text:

import boto3
s3_bucket = "test-uala"
s3_file="tmp.txt"
# Get the service client
s3 = boto3.client('s3')

# Upload a file-like object to s3_bucket at key-name
with open("tmp.txt", "rb") as f:
    s3.upload_fileobj(f, s3_bucket, s3_file)

#When uploading, ExtraArgs can be used to specify a variety of additional parameters. For example, to supply user metadata:

s3.upload_file(
    "tmp.txt", s3_bucket, s3_file,
    ExtraArgs={"Metadata": {"mykey": "myvalue"}}
)
#To set a canned ACL:

s3.upload_file(
    'tmp.txt', s3_bucket, s3_file,
    ExtraArgs={'ACL': 'public-read'}
)
#To set custom or multiple ACLs:

s3.upload_file(
    'tmp.txt', s3_bucket, s3_file,
    ExtraArgs={
        'GrantRead': 'uri="http://acs.amazonaws.com/groups/global/AllUsers"',
        'GrantFullControl': 'id="79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be"',
    }
)
#All valid ExtraArgs are listed at boto3.s3.transfer.S3Transfer.ALLOWED_UPLOAD_ARGS
