import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture
def firefox_browser(request):

    # desired_capabilities = {'browserName': 'htmlunit',
    #                         'version': '2',
    #                         'javascriptEnabled': True}
    # wd = webdriver.Chrome(desired_capabilities=desired_capabilities)
    wd = webdriver.Firefox()

    print(wd.capabilities)

    request.addfinalizer(wd.quit)
    return wd


def test_example(firefox_browser):
    """
    Example with cookie and run with capabilities
    """
    firefox_browser.get("https://otus.ru/")
    firefox_browser.add_cookie({'name': 'test', 'value': 'bar'})  # Добавить Cookie
    firefox_browser.get_cookie('test')  # Считать информацию о cookie
    firefox_browser.delete_cookie('test')  # Удалить Cookie
    firefox_browser.delete_all_cookies()  # Удалить все cookies
