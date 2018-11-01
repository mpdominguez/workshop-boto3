import boto3
#It is possible to look up a queue by its name. If the queue does not exist, then an exception will be thrown:

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue. This returns an SQS.Queue instance
queue = sqs.get_queue_by_name(QueueName='test')

# You can now access identifiers and attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))
# It is also possible to list all of your existing queues:

# Print out each queue name, which is part of its ARN
for queue in sqs.queues.all():
        print(queue.url)
