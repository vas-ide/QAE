


def test_api(api_client):
    response = api_client.get(path="/")
    print(response)
    print(response.status_code)
