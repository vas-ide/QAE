import requests

from locators import MainLogo
from selenium.webdriver.common.by import By
import pytest


# def test_open_opencart_deffault(browser):
#     print(browser)
#
# def test_open_opencart_deffault_url(browser, api_client):
#     print(api_client.base_address)

def test_open_opencart_edge_url(browser, api_client):
    browser.get(requests.get(url=f"http://localhost/en-gb/product/iphone"))
    # print(api_client.base_address)

# def test_seartch_id_opencart(browser):
#     elem = browser.find_element(By.ID, MainLogo.logo_id)
#     print(elem)
# browser.find_element(By.ID, MainLogo.logo_id)

# print(browser)


# def test_open_opencart_edge(browser):
#     print(browser)


# def test_open_opencart_all(parametrize_browser):
#     print(parametrize_browser)
