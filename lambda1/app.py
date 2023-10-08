import boto3
import json
import redis

lambda_client = boto3.client("lambda")


def lambda_handler(event, context):
    # 호출할 Lambda 함수의 이름과 입력 데이터 지정
    input_data = {"key1": "value1", "key2": "hihi"}
    print("phase 1")

    # Redis 클라이언트 생성 및 연결
    try:
        elasticache_client = redis.Redis(
            host="please-ro.7dylcs.ng.0001.apn2.cache.amazonaws.com",
            port=6379,
            socket_timeout=5,
        )
        print("phase 2")
    except Exception as e:
        print(f"Failed to connect to Elasticache: {str(e)}")
        return {"statusCode": 500, "body": "Failed to connect to Elasticache"}

    try:
        print("phase 3")
        elasticache_client.set("a", "b")
        elasticache_client.set("a", "b")
        print(elasticache_client.get("a"))
        print("Data written successfully")
    except Exception as e:
        print(f"Failed to write data to Elasticache: {str(e)}")
        return {"statusCode": 500, "body": "Failed to write data to Elasticache"}
    print("phase 4")
    # Lambda 함수를 비동기적으로 호출
    response = lambda_client.invoke(
        FunctionName="sam-app-MyLambdaFunction2-1DkntZbUYTSg",
        InvocationType="Event",  # 비동기 호출을 위해 'Event' 사용
        Payload=json.dumps(input_data),
    )
    print("phase 5")

    # Lambda 함수 호출 결과 확인
    if response["StatusCode"] == 202:
        print(f"Lambda 함수 2을 비동기적으로 호출했습니다.")
    else:
        print(f"Lambda 함수 호출에 실패했습니다. 응답 코드: {response['StatusCode']}")
