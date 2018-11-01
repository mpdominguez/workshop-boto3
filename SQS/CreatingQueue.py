import boto3
#Queues are created with a name. You may also optionally set queue attributes, such as the number of seconds
#to wait before an item may be processed. The examples below will use the queue name test.
#Before creating a queue, you must first get the SQS service resource:

# Get the service resource
sqs = boto3.resource('sqs')

# Create the queue. This returns an SQS.Queue instance
queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})

# You can now access identifiers and attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))
