import boto3
#Sending a message adds it to the end of the queue:
# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='test')

#Messages can also be sent in batches. For example, sending the two messages described above in a single request would look like the following:

response = queue.send_messages(Entries=[
    {
        'Id': '1',
        'MessageBody': 'world'
    },
    {
        'Id': '2',
        'MessageBody': 'boto3',
        'MessageAttributes': {
            'Author': {
                'StringValue': 'Daniel',
                'DataType': 'String'
            }
        }
    }
])

# Print out any failures
print(response.get('Failed'))
#In this case, the response contains lists of Successful and Failed messages, so you can retry failures if needed.
