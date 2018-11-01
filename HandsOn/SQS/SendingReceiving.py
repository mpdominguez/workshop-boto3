#In this example, Python code is used to send and receive messages. The code uses the AWS SDK for Python to send and receive messages by using these methods of the AWS.SQS client class:

#send_message.
#receive_message.
#delete_message.
#Send a message to a queue using send_message.
import boto3

# Create SQS client
sqs = boto3.client('sqs')

# Create a SQS queue
response = sqs.create_queue(
    QueueName='test-uala',
    Attributes={
        'DelaySeconds': '1',
        'MessageRetentionPeriod': '86400'
    }
)

print(response['QueueUrl'])

queue_url = response['QueueUrl']

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=1,
    MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'The Whistler'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'John Grisham'
        },
        'WeeksOn': {
            'DataType': 'Number',
            'StringValue': '6'
        }
    },
    MessageBody=(
        'Information about current NY Times fiction bestseller for '
        'week of 12/11/2016.'
    )
)

print(response['MessageId'])
#Receive and Delete Messages from a Queue

#Receive a message from a queue using receive_message.
#Delete a message from a queue using delete_message.
import boto3

# Create SQS client
sqs = boto3.client('sqs')


# Receive message from SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

message = response['Messages'][0]
receipt_handle = message['ReceiptHandle']

# Delete received message from queue
sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle
)
print('Received and deleted message: %s' % message)
