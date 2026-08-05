import json
import boto3
import uuid

s3 = boto3.client('s3')

BUCKET = "tweet-archive-haniya"

def lambda_handler(event, context):

    for record in event['Records']:

        filename = str(uuid.uuid4()) + ".json"

        s3.put_object(
            Bucket=BUCKET,
            Key=filename,
            Body=record['body'],
            ContentType='application/json'
        )

    return {
        "statusCode": 200,
        "body": json.dumps("Tweets stored successfully in S3")
    }
