import json

def handler(event, context):
    return {
        'statusCode': 420,
        'body': json.dumps('Snoopdog approves this lambda message')
    }
