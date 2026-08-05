import json
import boto3
import re

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TweetHashtags')

def lambda_handler(event, context):

    for record in event['Records']:

        body = json.loads(record['body'])

        tweet_id = body['tweet_id']
        text = body['text']

        hashtags = re.findall(r"#(\w+)", text)

        table.put_item(
            Item={
                "tweet_id": tweet_id,
                "hashtags": hashtags
            }
        )

    return {
        'statusCode': 200
    }
