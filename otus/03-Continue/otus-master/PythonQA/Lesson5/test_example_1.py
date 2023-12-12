import pytest
from selenium import webdriver

from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def chrome_browser(request):
    options = Options()
    options.add_argument("--headless")
     # options.add_argument("--start-fullscreen")

    # options.add_argument("-headless")
    # options.add_argument('--disable-gpu')
    wd = webdriver.Chrome(options=options)
    request.addfinalizer(wd.quit)
    return wd


def test_example(chrome_browser):
    """
    First test
    """
    chrome_browser.get("https://otus.ru/")
    # assert chrome_browser.find_element_by_class_name('header2-menu__phone').text == '+7 499 959-43-99'
    # assert chrome_browser.find_element_by_class_name('sc-myimc2-0 iUcqLR').text == '+7 499 938-92-02'

