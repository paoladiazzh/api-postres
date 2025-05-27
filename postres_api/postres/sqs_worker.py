import boto3
import json
from postres.views import postres  # lista en memoria

def receive_messages():
    sqs = boto3.client(
        'sqs',
        region_name='us-east-1',
        aws_access_key_id='ASIARDSSQLQU7QAVYKR2',
        aws_secret_access_key='HYg9DG+anAMYGypUhQc610MQefKXoiTq3qCsaVNm',
        aws_session_token='IQoJb3JpZ2luX2VjEIj//////////wEaCXVzLXdlc3QtMiJIMEYCIQDskuC91imJ/xhzAljHRU0JR6It52554vA7wNoFKevEVwIhAPcYU9Dk/2NAI9iwkxvYJ6oHFOcCweXvXbqBMNU628/mKqQCCFEQARoMMDc2NDA4NzA4MTM3IgxiksvphppGORcK0QIqgQKeG3EbN1CsWg3uGUA5uI3IQjgpK8qXzYxc8U7Q8K201f7pTeavDH6N/8dxCk5CVJrpyNJAuaEBX7Nh5feqN99nKXMtWHWQ56n8Yh+7o9WHxpzrN1UBSUgbWnV4DfvOuFEK9DWOk0D8UWKbDIvvgHOAtG2hx8LX8OrmJOPYVikoHy+7/qeRkDDT7Hvj5gQik1c6qDPMIFzS5U/QWiw8HwE/JAaP61Y2UpZYBuNx5qPy1YY8V5eVruRvPEFvjwQZbEqifKosiJyIdnPnXOHIxc9OontGhCfGyyOc/gaP6c+2WomkAhLlJmW3XA/WeRV1sjnPMfvrto8tyylHfB+MKNaW9zDbh9TBBjqcAZz85Cv5uvzk/VnP5TGZNVeMlf2WQTq2qBUkr1n5g3tNmNniPq7wsXu4AK1LWlynmac7F7Mb39US1hoMEJyAwTYmLqREorBl6KlRmUlHo7R6IJM1Y3l7qTDydZiKvl7jgxy8H5s/52ANh1Rr3CFpW7sIf1FXQjmxWZ8CGIzEH7CAUX8mnu6phhqS7xJgd5aJd/LYgGUsuLRFrmd7Tw=='
    )
    queue_url = 'https://sqs.us-east-1.amazonaws.com/076408708137/postres-queue'
    
    response = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1)
    for msg in response.get('Messages', []):
        body = json.loads(msg['Body'])
        postres.append(body)
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=msg['ReceiptHandle'])