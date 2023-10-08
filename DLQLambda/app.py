import requests


def lambda_handler(event, context):
    print(event)
    print(context)

    res = requests.post(
        "SLACK_URL",
        json={"text": "DLQ Message Received" + str(context)},
        headers={"Content-Type": "application/json"},
    )
    return {"statusCode": 200, "body": res.text}
