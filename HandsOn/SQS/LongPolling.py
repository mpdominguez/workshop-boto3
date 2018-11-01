#The Scenario
#Long polling reduces the number of empty responses by allowing Amazon SQS to wait a specified time for a message to become available in the queue before sending a response. Also, long polling eliminates false empty responses by querying all of the servers instead of a sampling of servers. To enable long polling, you must specify a non-zero wait time for received messages. You can do this by setting the ReceiveMessageWaitTimeSeconds parameter of a queue or by setting the WaitTimeSeconds parameter on a message when it is received.

#In this example, Python code is used to enable long polling. The code uses the AWS SDK for Python to enable long polling using these methods of the AWS.SQS client class:

#create_queue
#set_queue_attributes.
#receive_message.

#Create a queue and enable long polling using create_queue.
import boto3

# Create SQS client
sqs = boto3.client('sqs')

# Create a SQS queue with long polling enabled
response = sqs.create_queue(
    QueueName='SQS_QUEUE_NAME',
    Attributes={'ReceiveMessageWaitTimeSeconds': '20'}
)

print(response['QueueUrl'])
#Enable Long Polling on an Existing Queue
#Enable long polling on an existing queue using set_queue_attributes.
import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'SQS_QUEUE_URL'

# Enable long polling on an existing SQS queue
sqs.set_queue_attributes(
    QueueUrl=queue_url,
    Attributes={'ReceiveMessageWaitTimeSeconds': '20'}
)
#Enable Long Polling on Message Receipt
#Get one or more messages (up to 10), from the specified queue. Using the WaitTimeSeconds parameter enables long-poll support. For more information, see Amazon SQS Long Polling in the Amazon SQS Developer Guide.

#Enable a long poll for message on provided SQS queue using receive_message.
import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'SQS_QUEUE_URL'

# Long poll for message on provided SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    WaitTimeSeconds=20
)

print(response)

