import json
    
def lambda_handler(event, context):
    body = {
        "message": "Test",
        "input": event
    }

    print("log test")

    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }
