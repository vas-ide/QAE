from locators import MainPage
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions, EdgeOptions
from selenium.webdriver.common.by import By


options = EdgeOptions()
# options.add_argument("--start-fullscreen")
# options.add_argument("--headless")
driver = webdriver.Edge(options=options)
driver.get("https://demo.opencart.com/")
element = driver.find_elements(By.CSS_SELECTOR, MainPage.nav_links)
driver.quit()


# def test_element_by_class_name_selector(parametrize_browser):
#     bro = parametrize_browser
#     bro.find_element(By.CLASS_NAME, MainPage.promoblock).click()
#     bro.find_element(By.CLASS_NAME, "breadcrumb")












