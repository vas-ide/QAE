import time
import os
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
# driver = webdriver.Chrome()
# ser_firefox = Service_firefox(executable_path="/home/vas/Documents/Python/QAE/otus/driver/geckodriver-v0.33.0-linux64/geckodriver")
# driver = webdriver.Firefox(service=ser_firefox)
driver = webdriver.Firefox()

try:
    driver.maximize_window()
    driver.get("http://localhost/opencart")
    main_macbook = driver.find_element(By.PARTIAL_LINK_TEXT, CartMacBook.cart_partial_link_text).click()
    time.sleep(1)
    logo = driver.find_element(By.XPATH, MainLogo.logo_xpath).click()
    time.sleep(1)
    main_iphone = driver.find_element(By.PARTIAL_LINK_TEXT, CartIPhone.cart_partial_link_text).click()
    time.sleep(1)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

