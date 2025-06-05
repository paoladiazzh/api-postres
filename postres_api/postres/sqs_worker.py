import boto3
import json
from django.conf import settings
from postres.views import postres  # lista en memoria

def receive_messages():
    try:
        sqs = boto3.client(
            'sqs',
            region_name=settings.AWS_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            aws_session_token=settings.AWS_SESSION_TOKEN
        )
        queue_url = 'https://sqs.us-east-1.amazonaws.com/076408708137/postres-queue'
        
        response = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1)
        for msg in response.get('Messages', []):
            body = json.loads(msg['Body'])
            postres.append(body)
            sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=msg['ReceiptHandle'])
    
    except Exception as e:
        print(f"Error al recibir mensajes de SQS: {e}")