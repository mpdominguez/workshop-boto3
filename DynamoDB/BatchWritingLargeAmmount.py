import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users_workshop')

# The batch writer is even able to handle a very large amount of writes to the table.

with table.batch_writer() as batch:
    for i in range(50):
        batch.put_item(
            Item={
                'account_type': 'anonymous',
                'username': 'user' + str(i),
                'first_name': 'unknown',
                'last_name': 'unknown',
                'age': str(i)
            }
        )
