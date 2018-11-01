# The Scenario
# In this example, Python code is used to obtain a list of existing Amazon S3 buckets, create a bucket, and upload a file to a specified bucket. The code uses the AWS SDK for Python to get information from and upload files to an Amazon S3 bucket using these methods of the Amazon S3 client class:
# list_buckets
# create_bucket
# upload_file


#List buckets using list_buckets.
import boto3
# Create an S3 client
s3 = boto3.client('s3')
# Call S3 to list current buckets
response = s3.list_buckets()
# Get a list of all bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]
# Print out the bucket list
print("Bucket List: %s" % buckets)

##############################################################################
# Create an Amazon S3 Bucket
# The example below shows how to:
# Create a new bucket using create_bucket.
import boto3
s3.create_bucket(Bucket='my-bucket-mrtdom')

##############################################################################
# Upload a File to an Amazon S3 Bucket
# Upload a file to a bucket using upload_file.
import boto3
# Create an S3 client
s3 = boto3.client('s3')
filename = 'file.txt'
bucket_name = 'my-bucket-mrtdom'

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
s3.upload_file(filename, bucket_name, filename)
##############################################################################
s3.delete_bucket(Bucket='my-bucket-mrtdom')
