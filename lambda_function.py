import a


def lambda_handler(event, context):
    params = event["pathParameters"]
    return {"data": a.f(**params)}
