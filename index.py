import json
import datetime
from responses import response

# send message to home/fish-cam iot core topic
# then retrieve data from s3 bucket: fish-cam

def endpoint(event, context):
    current_time = datetime.datetime.now().time()
    body = {
        "message": "Hello, the current time is " + str(current_time)
    }

    return response(200, body)
