#Once you have a DynamoDB.Table resource you can add new items to the table using DynamoDB.Table.put_item():
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users_workshop')

table.put_item(
   Item={
        'username': 'janedoe',
        'first_name': 'Jane',
        'last_name': 'Doe',
        'age': 25,
        'account_type': 'standard_user',
    }
)
