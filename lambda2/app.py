import json


def lambda_handler(event, context):
    print("Lambda Function 2 invoked with event:", json.dumps(event))
    raise Exception("Something went wrong in Lambda Function 2")
    return {"statusCode": 200, "body": json.dumps("Hello from Lambda Function 2!")}
