import lambda_function


def test_lambda_function():
    event = {"pathParameters": {"a": "hello", "b": "world"}}
    assert lambda_function.lambda_handler(event, {}) == {"data": "helloworld"}
