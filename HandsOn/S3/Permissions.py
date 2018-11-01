# The Scenario
# In this example, a Python code is used to display the bucket access control list (ACL) for a selected bucket. The code uses the AWS SDK for Python to manage Amazon S3 bucket access permissions using this method of the Amazon S3 client class:
# get_bucket_acl.
# For more information about access control lists for Amazon S3 buckets, see Managing Access with ACLs in the Amazon Simple Storage Service Developer Guide.

# Get a Specified Bucket Access Control (ACL) List
# Access control lists (ACLs) are one of the resource-based access policy option you can use to manage access to your buckets and objects. You can use ACLs to grant basic read/write permissions to other AWS accounts.


# Get the bucket ACL for a specified bucket using get_bucket_acl.
import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Call to S3 to retrieve the policy for the given bucket
result = s3.get_bucket_acl(Bucket='my-bucket-mrtdom')
print(result)
