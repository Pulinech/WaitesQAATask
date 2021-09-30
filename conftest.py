import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart browser chrome for test...")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart browser firefox for test...")
        browser = webdriver.Firefox()
    else:
        print(f"Browser {browser_name} still is not implemented")
    yield browser
    print("\nquit browser...")
    browser.quit()
