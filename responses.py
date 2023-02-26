import json

def response(code, message):
    if(code == 400):
        return {
            "statusCode": 400,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": 'application/json',
            },
            "body": json.dumps(message),
            "isBase64Encoded": False
        }
    
    elif(code == 200):
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": 'application/json',
            },
            "body": json.dumps(message),
            "isBase64Encoded": False
        }
    
    else:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": 'application/json',
            },
            "body": "something went wrong",
            "isBase64Encoded": False
        }
    