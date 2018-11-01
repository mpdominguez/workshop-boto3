# With the table full of items, you can then query or scan the items in the table using the DynamoDB.Table.query()
# or DynamoDB.Table.scan() methods respectively. To add conditions to scanning and querying the table, you will need
# to import the boto3.dynamodb.conditions.Key and boto3.dynamodb.conditions.Attr classes. The boto3.dynamodb.conditions.Key
# should be used when the condition is related to the key of the item. The boto3.dynamodb.conditions.Attr should be used when
# the condition is related to an attribute of the item:
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users_workshop')

from boto3.dynamodb.conditions import Key, Attr
# This queries for all of the users_workshop whose username key equals johndoe:

response = table.query(
    KeyConditionExpression=Key('username').eq('johndoe')
)
items = response['Items']
print("This queries for all of the users_workshop whose username key equals johndoe:")
print(items)
print("---------------------------------------------------------------")
print("")

# Similarly you can scan the table based on attributes of the items. For example, this scans for all the users_workshop whose age is less than 27:

response = table.scan(
    FilterExpression=Attr('age').lt(27)
)
items = response['Items']
print("This scans for all the users_workshop whose age is less than 27:")
print(items)
print("---------------------------------------------------------------")
print("")

# You are also able to chain conditions together using the logical operators: & (and), | (or), and ~ (not).
# For example, this scans for all users_workshop whose first_name starts with J and whose account_type is super_user:

response = table.scan(
    FilterExpression=Attr('first_name').begins_with('J') & Attr('account_type').eq('super_user')
)
items = response['Items']
print("This scans for all users_workshop whose first_name starts with J and whose account_type is super_user:")
print(items)
print("---------------------------------------------------------------")
print("")

# You can even scan based on conditions of a nested attribute. For example this scans for all users_workshop whose state in their address is CA:

response = table.scan(
    FilterExpression=Attr('address.state').eq('CA')
)
items = response['Items']
print("This scans for all users_workshop whose state in their address is CA:")
print(items)
print("---------------------------------------------------------------")
print("")
