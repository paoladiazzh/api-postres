import boto3
import json
from postres.views import postres  # lista en memoria

def receive_messages():
    sqs = boto3.client('sqs', region_name='us-east-1')
    queue_url = 'https://sqs.us-east-1.amazonaws.com/076408708137/postres-queue'
    
    response = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1)
    for msg in response.get('Messages', []):
        body = json.loads(msg['Body'])
        postres.append(body)
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=msg['ReceiptHandle'])