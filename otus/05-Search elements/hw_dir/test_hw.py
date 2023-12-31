import time
import os

import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as Service_edge
from selenium.webdriver.chrome.service import Service as Service_chrome
from selenium.webdriver.firefox.service import Service as Service_firefox
from selenium.webdriver import ChromeOptions, FirefoxOptions, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators import MainLogo, CartIPhone, CartMacBook


# ser_edge = Service_edge(executable_path="/home/vas/Documents/Python/QAE/otus/driver/edgedriver_linux64/msedgedriver")
# options_edge = EdgeOptions()
# options_edge.add_argument("--headless")
# options_edge.add_argument("--start-fullscreen")
# driver = webdriver.Edge(service=ser_edge)
# driver = webdriver.Edge()
# ser_chrome = Service_chrome(executable_path="//home/vas/Documents/Python/QAE/otus/driver/chromedriver_linux64/chromedriver")
# options_chrome = ChromeOptions()
# options_chrome.add_argument("--start-fullscreen")
# driver = webdriver.Chrome(service=ser_chrome)
# driver = webdriver.Chrome(options=options_chrome)
# ser_firefox = Service_firefox(executable_path="/home/vas/Documents/Python/QAE/otus/driver/geckodriver-v0.33.0-linux64/geckodriver")
# driver = webdriver.Firefox(service=ser_firefox)
# driver = webdriver.Firefox()
# #
# try:
#     # driver.maximize_window()
#     driver.get("http://localhost/opencart")
#     main_macbook = driver.find_element(By.PARTIAL_LINK_TEXT, CartMacBook.cart_partial_link_text).click()
#     time.sleep(1)
#     logo = driver.find_element(By.XPATH, MainLogo.logo_xpath).click()
#     time.sleep(1)
#     main_iphone = driver.find_element(By.PARTIAL_LINK_TEXT, CartIPhone.cart_partial_link_text).click()
#     time.sleep(1)
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()


class TestOpenCart():
    base_url = "http://localhost/opencart"

    #
    # @pytest.fixture(params=["chrome", "edge", "firefox"])
    # def parametrize_browser(request):
    #     browser_param = request.param
    #     if browser_param == "chrome":
    # @pytest.mark.browser_param("edge")
    # @pytest.param(browser_param = "edge")

    def test_simple_browser(self, browser):
        browser_param = "edge"
        # browser_param = "edge"
        driver = browser
        try:
            driver.get(self.base_url)
            main_macbook = driver.find_element(By.PARTIAL_LINK_TEXT, CartMacBook.cart_partial_link_text).click()
            time.sleep(1)
            logo = driver.find_element(By.XPATH, MainLogo.logo_xpath).click()
            time.sleep(1)
            main_iphone = driver.find_element(By.PARTIAL_LINK_TEXT, CartIPhone.cart_partial_link_text).click()
            time.sleep(1)
        except Exception as ex:
            print(ex)

    # def test_simple_browser(self, browser):
    #     # driver = browser(browser_param="edge")
    #     driver = browser
    #     try:
    #         driver.get(self.base_url)
    #         main_macbook = driver.find_element(By.PARTIAL_LINK_TEXT, CartMacBook.cart_partial_link_text).click()
    #         time.sleep(1)
    #         logo = driver.find_element(By.XPATH, MainLogo.logo_xpath).click()
    #         time.sleep(1)
    #         main_iphone = driver.find_element(By.PARTIAL_LINK_TEXT, CartIPhone.cart_partial_link_text).click()
    #         time.sleep(1)
    #     except Exception as ex:
    #         print(ex)

    # def test_all_browsers(self, parametrize_browser):
    #     driver = parametrize_browser
    #     try:
    #         driver.get(self.base_url)
    #         main_macbook = driver.find_element(By.PARTIAL_LINK_TEXT, CartMacBook.cart_partial_link_text).click()
    #         time.sleep(1)
    #         logo = driver.find_element(By.XPATH, MainLogo.logo_xpath).click()
    #         time.sleep(1)
    #         main_iphone = driver.find_element(By.PARTIAL_LINK_TEXT, CartIPhone.cart_partial_link_text).click()
    #         time.sleep(1)
    #     except Exception as ex:
    #         print(ex)
