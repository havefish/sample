import a


def lambda_handler(event, context):
    params = event["pathParameters"]
    return a.f(**params)
