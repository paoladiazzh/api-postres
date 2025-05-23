import boto3
import json
from postres.views import postres  # lista en memoria

def receive_messages():
    sqs = boto3.client(
        'sqs',
        region_name='us-east-1',
        aws_access_key_id='ASIARDSSQLQUQNBX4IWX',
        aws_secret_access_key='7da/AeNtTIJJbj6meT+81XxzCHPvbbc+3QgqWHJ+',
        aws_session_token='IQoJb3JpZ2luX2VjEC0aCXVzLXdlc3QtMiJHMEUCIQDqq1Mf9hXF+Cf1pqeUkOAyyAkOWDQgmabViqowxnUNhgIgdc6km+U2ZFIYEYxGvj8fhQbucoVo8pBQd476Bcu9uUYqrQII5f//////////ARABGgwwNzY0MDg3MDgxMzciDGT25fzxtep1ge46niqBAmGdKHTU/i4lYj2V2SdYG46VVnYxPjipk+yaOAFNrAi6N8m3BemZc5MO4gqmwBe7pWV1yimgl48R57rnjv+pZa76r6lxj3fo2c45dra9EMelRTivqLreavGDSoplklriPXo516DbfRuFLRoh5WUa7ZQAaFlYN+N4mKbDuxGF6ADTJwbsXF7A6lx1DkVLIOUWplQa1owkDK9AKSJOuhms1aqNPbfUOED4HZQmF/R891eU8X33oWwhofe6tKkaPbPgDL/ewq3hDMmezd2uD8Cdqd8hL+zhe+TOwJAPEyHcvbds4SdkuZj5t0mAOCtFMOpEy8ryK1lK7xRNA4aLTEaz7371MNzvv8EGOp0B3IkPnY/HlEiEzJMbHloT3MxoW5f7mo7F/1bpwXHH6V29D9qm+eMz/aXb2rXFqUQonVz+SVN+DslUENgyVFW1kiIiwZ9J61xw7f2SvEoWOHPJsJ0gyEdkp5X6kkI9aNGHirSsxcNnLw/m/Yn41PvtFFzuiiAhTg+4KDNKXgVyZriJ70HsxfZRo42HoXY9CeaveOHysFM5IjEI6FoTAQ=='
    )
    queue_url = 'https://sqs.us-east-1.amazonaws.com/076408708137/postres-queue'
    
    response = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1)
    for msg in response.get('Messages', []):
        body = json.loads(msg['Body'])
        postres.append(body)
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=msg['ReceiptHandle'])