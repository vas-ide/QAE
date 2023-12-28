import time
import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service as Service_edge
from selenium.webdriver.chrome.service import Service as Service_chrome
from selenium.webdriver.firefox.service import Service as Service_firefox
from selenium.webdriver import ChromeOptions, FirefoxOptions, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators import MainLogo


ser_edge = Service_edge(executable_path="/home/vas/Documents/Python/QAE/otus/05-Search elements/driver/edgedriver_linux64/msedgedriver")
# options_edge = EdgeOptions()
# options_edge.add_argument("--headless")
# options_edge.add_argument("--start-fullscreen")
driver = webdriver.Edge(service=ser_edge)

try:
    driver.maximize_window()
    driver.get("http://localhost/opencart")
    main_macbook = driver.find_element(By.PARTIAL_LINK_TEXT, "MacBook").click()
    time.sleep(1)
    logo = driver.find_element(By.XPATH, MainLogo.logo_xpath).click()
    time.sleep(1)
    main_iphone = driver.find_element(By.PARTIAL_LINK_TEXT, "iPhone").click()
    time.sleep(1)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

