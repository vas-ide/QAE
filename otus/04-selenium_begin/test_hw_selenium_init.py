import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions

# @pytest.mark.parametrize("browser_name", ["chrome", "firefox"])
# def test_run(browser_name):
#     if browser_name == "chrome":
#        pass



@pytest.fixture
def chrome_browser(request):
    options = ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--start-fullscreen")
    wd = webdriver.Chrome(options=options)
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def firefox_browser(request):
    options = FirefoxOptions()
    # options.add_argument("--headless")
    options.add_argument("--start-fullscreen")
    wd = webdriver.Firefox(options=options)
    request.addfinalizer(wd.quit)
    return wd


def test_example_chrome(chrome_browser):
    chrome_browser.get("http://localhost/")
    chrome_browser.get("http://localhost/opencart/")

def test_example_firefox(firefox_browser):
    firefox_browser.get("http://localhost/")
    firefox_browser.get("http://localhost/opencart/")


