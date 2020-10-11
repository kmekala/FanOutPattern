import json
import boto3

client = boto3.client('lambda')

def lambda_handler(event, context):
    for url in event.get('urls', []):
        response = client.invoke(
            FunctionName='testLambdaWorker',
            InvocationType='Event',
            Payload=json.dumps({'url': url})
        )

    return