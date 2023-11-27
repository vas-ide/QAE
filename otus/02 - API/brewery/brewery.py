import pytest


@pytest.mark.parametrize("input_brebary_city, output_brebary_city",
                         [("Norman", "Norman"), ("Mount Pleasant", "Mount Pleasant"), ('South Bend', 'South Bend'),
                          ("San Diego", "San Diego")])
def test_city(api_client, input_brebary_city, output_brebary_city):
    response = api_client.get(path="/",
                              params={
                                  "by_city": input_brebary_city
                              }).json()
    print(f"In {output_brebary_city} - {len(response)} brebary's")
    for i in response:
        assert i["city"] == output_brebary_city


@pytest.mark.parametrize("input_brebary_state, output_brebary_state",
                         [("New York", "New York"), ("California", "California"), ("Oregon", "Oregon")])
def test_state(api_client, input_brebary_state, output_brebary_state):
    response = api_client.get(path="/",
                              params={
                                  "by_state": input_brebary_state
                              }).json()
    print(f"In {output_brebary_state} - {len(response)} brebary's")
    for i in response:
        assert i["state"] == output_brebary_state
