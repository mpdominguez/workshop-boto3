#The Scenario
#A dead letter queue is one that other (source) queues can target for messages that can't be processed successfully. You can set aside and isolate these messages in the dead letter queue to determine why their processing did not succeed. You must individually configure each source queue that sends messages to a dead letter queue. Multiple queues can target a single dead letter queue.

#In this example, Python code is used to route messages to a dead letter queue. The code uses the SDK for Python to use dead letter queues using this method of the AWS.SQS client class:

#set_queue_attributes.
#Configure a source queue using set_queue_attributes.
import json

import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'SOURCE_QUEUE_URL'
dead_letter_queue_arn = 'DEAD_LETTER_QUEUE_ARN'

redrive_policy = {
    'deadLetterTargetArn': dead_letter_queue_arn,
    'maxReceiveCount': '10'
}


# Configure queue to send messages to dead letter queue
sqs.set_queue_attributes(
    QueueUrl=queue_url,
    Attributes={
        'RedrivePolicy': json.dumps(redrive_policy)
    }
)
