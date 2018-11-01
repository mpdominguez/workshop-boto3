import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users_workshop')

# Current Value of the item
response = table.get_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)
item = response['Item']
print("Current Value: ")
print(item)


#You can then update attributes of the item in the table:

update_value=26

table.update_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    },
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={
        ':val1': update_value
    }
)
#Then if you retrieve the item again, it will be updated appropriately:

response = table.get_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)
item = response['Item']
print("Updated Value: ")
print(item)
