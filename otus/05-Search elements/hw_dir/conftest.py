
import requests
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions, EdgeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="base browser")
    # parser.addoption("--url", "-U", action="store", default="https://google.com", help="base url")
    # parser.addoption("--url", "-U", action="store", default="https://localhost/", help="base url")
    parser.addoption("--url", "-U", action="store", default="https://localhost/opencart", help="base url")
    # parser.addoption("--url", "-U", action="store", default="https://localhost/en-gb/product/macbook", help="base url")


@pytest.fixture
def browser(request, browser_param=None):
    if browser_param is None:
        browser_param = request.config.getoption("--browser")

    if browser_param == "chrome":
        options = ChromeOptions()
        # options.add_argument("--headless")
        options.add_argument("--start-fullscreen")
        driver = webdriver.Chrome(options=options)
    elif browser_param == "firefox":
        options = FirefoxOptions()

        # options.add_argument("--headless")
        options.add_argument("--start-fullscreen")
        driver = webdriver.Firefox(options=options)
    elif browser_param == "edge":
        options = EdgeOptions()
        # options.add_argument("--headless")
        options.add_argument("--start-fullscreen")
        driver = webdriver.Edge(options=options)
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(2)
    request.addfinalizer(driver.close)
    driver.get(request.config.getoption("--url"))

    return driver


@pytest.fixture(params=["chrome", "edge", "firefox"])
def parametrize_browser(request):
    browser_param = request.param
    if browser_param == "chrome":
        options = ChromeOptions()
        # options.add_argument("--headless")
        options.add_argument("--start-fullscreen")
        driver = webdriver.Chrome(options=options)
    elif browser_param == "firefox":
        options = FirefoxOptions()
        # options.add_argument("--headless")
        options.add_argument("--start-fullscreen")
        driver = webdriver.Firefox(options=options)
    elif browser_param == "edge":
        options = EdgeOptions()
        # options.add_argument("--headless")
        options.add_argument("--start-fullscreen")
        driver = webdriver.Edge(options=options)
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(2)
    request.addfinalizer(driver.quit)
    driver.get(request.config.getoption("--url"))

    return driver


class APIClient:
    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        return requests.post(url=self.base_address + path, params=params, data=data, headers=headers)

    def get(self, path="/", params=None):
        return requests.get(url=self.base_address + path, params=params)


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    return APIClient(base_address=base_url)
