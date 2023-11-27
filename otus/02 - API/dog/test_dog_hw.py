from pprint import pprint
import pytest
import requests


@pytest.mark.parametrize("input_dog, output_dog",
                         [("mudhol", "indian"), ("hound", "afghan"), ("hound", "basset"), ("hound", "blood"),
                          ("hound", "english"),
                          ("hound", "ibizan"), ("hound", "plott"), ("hound", "walker")])
def test_hound(api_client, input_dog, output_dog):
    response = api_client.get(path="/").json()
    dog = response.get("message").get(input_dog)
    print(input_dog, output_dog)
    print(dog, output_dog)
    assert f"{output_dog}" in dog


def test_pointer():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    search_dog = response.json()['message']['pointer']
    assert search_dog == ['german', 'germanlonghair']


def test_tervuren():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    search_dog = response.json()['message']['tervuren']
    assert search_dog == []


class TestTerrier:
    def test_terrier(self):
        response = requests.get("https://dog.ceo/api/breeds/list/all")
        search_dog = response.json()['message']['terrier']
        answer = ['american', 'australian', 'bedlington', 'border', 'cairn', 'dandie', 'fox', 'irish', 'kerryblue',
                  'lakeland', 'norfolk', 'norwich', 'patterdale', 'russell', 'scottish', 'sealyham', 'silky', 'tibetan',
                  'toy', 'welsh', 'westhighland', 'wheaten', 'yorkshire']
        assert search_dog == answer
