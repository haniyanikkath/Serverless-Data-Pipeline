import boto3
import json

sqs = boto3.client("sqs")

QUEUE_URL = "https://sqs.ap-southeast-2.amazonaws.com/361738333309/TweetQueue"

tweet = {
    "username": "testuser",
    "text": "Hello from producer.py!"
}

response = sqs.send_message(
    QueueUrl=QUEUE_URL,
    MessageBody=json.dumps(tweet)
)

print("Message sent!")
