#The Scenario
#In this example, Python code is used to work with queues. The code uses the AWS SDK for Python to use queues using these methods of the AWS.SQS client class:

#list_queues.
#create_queue.
#get_queue_url.
#delete_queue.
SQS_QUEUE_NAME="test-uala"

#List queues using list_queues.
import boto3

# Create SQS client
sqs = boto3.client('sqs')

# List SQS queues
response = sqs.list_queues()

print(response['QueueUrls'])
###########################################################
#Create a Queue
#Create a queue using create_queue.
import boto3

# Create SQS client
sqs = boto3.client('sqs')

# Create a SQS queue
response = sqs.create_queue(
    QueueName='SQS_QUEUE_NAME',
    Attributes={
        'DelaySeconds': '60',
        'MessageRetentionPeriod': '86400'
    }
)

print(response['QueueUrl'])
###########################################################
# Get the URL for a queue using get_queue_url.
import boto3

# Create SQS client
sqs = boto3.client('sqs')

# Get URL for SQS queue
response = sqs.get_queue_url(QueueName='SQS_QUEUE_NAME')

print(response['QueueUrl'])
###########################################################
#Delete a queue using delete_queue.
import boto3

# Create SQS client
sqs = boto3.client('sqs')

# Delete SQS queue
sqs.delete_queue(QueueUrl=response['QueueUrl'])
