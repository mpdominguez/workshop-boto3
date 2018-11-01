#Once you have a DynamoDB.Table resource you can add new items to the table using DynamoDB.Table.put_item():
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users_workshop')

table.delete_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)
