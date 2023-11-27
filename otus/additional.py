from pprint import pprint

import requests

# url = "https://dog.ceo/dog-api/"
url = "https://dog.ceo/api/breeds/list/all"
# url = "https://dog.ceo/api/breed/hound/list"
# url = "https://dog.ceo/api/breeds/image/random"
response = requests.get(url)

# pprint(response.json())
# pprint(pprint(response.json()))
# print(response.headers['Date'])
# pprint(response.json())
# pprint(response.json()['status'])
pprint(response.json()['message'])
pprint(response.json()['message']['pointer'])

