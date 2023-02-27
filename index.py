import json
import datetime
from responses import response
import boto3

# send message to home/fish-cam iot core topic
# then retrieve data from s3 bucket: fish-cam
client = boto3.client('iot-data', region_name='us-east-2')

def endpoint(event, context):
    
    print(event)
    print(event["bucket_path"])
    
    if event["bucket_path"] != "fish-cam":
        return response(400, "please provide required parameter")
    
    try:
        rpi_response = client.publish(
            topic='fish-cam',
            qos=0,
            payload=json.dumps({"foo":"bar"})
        )
        
        print(response)
        
        bucketname = "fish-cam"
        filename = "fish_data.json"
        
        s3 = boto3.client('s3')
        s3_response = s3.get_object(bucketname, filename)
        fish_cam_content = s3_response['Body'].read().decode('utf-8')

        return response(200, fish_cam_content)
    except Exception as e:
        print(e)
        return response(500, e)
