import a


def lambda_handler(event, context):
    params = event["pathParameters"]
    return {"result": a.f(**params)}
