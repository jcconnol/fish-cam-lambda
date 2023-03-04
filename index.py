import json
import datetime
from responses import response
import boto3

client = boto3.client('iot-data', region_name='us-east-2')
BUCKET_NAME = "fish_cam"
FISH_DATA_JSON_FILE_NAME = "fish_data.json"
FISH_DATA_JPG_IMAGE_NAME = "fish_pic.jpg"


def endpoint(event, context):
    
    try:
        response = client.publish(
            topic='fish_data',
            qos=0,
            payload=b"{\"message\": \"invoke fish cam!\"}"
        )
        print(response)
        print("got here")
        
        bucket = "fish-cam"
        filename = "fish_data.json"
        
        unsigned_url = boto3.client('s3').generate_presigned_url(
        ClientMethod='get_object', 
        Params={'Bucket': BUCKET_NAME, 'Key': FISH_DATA_JPG_IMAGE_NAME}, ExpiresIn=3600)
            
        s3 = boto3.resource('s3')
        fish_cam_content = s3.Object(bucket, filename)
        fish_cam_json = fish_cam_content.get()['Body'].read().decode('utf-8') 
        
        fish_cam_json["s3_url"] = unsigned_url

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": 'application/json',
            },
            "body": json.dumps(fish_cam_json),
            "isBase64Encoded": False
        }
    except Exception as e:
        print(e)
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": 'application/json',
            },
            "body": json.dumps(e),
            "isBase64Encoded": False
        }
