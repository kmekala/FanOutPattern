import json
import boto3

client = boto3.client('lambda')
BATCH_SIZE = 100

def lambda_handler(event, context):
    urls = []
    for i in range(0, 10000):
        urls.append('url_{}'.format(i))

    chunks = [urls[i:i + BATCH_SIZE] for i in range(0, len(urls), BATCH_SIZE)]
    for chunk in chunks:
        response = client.invoke(
            FunctionName='triggerer',
            InvocationType='Event',
            Payload=json.dumps({'urls': chunk})
        )

    return