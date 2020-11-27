import pytest
import sys
import logging
from selenium import webdriver
sys.path.append('../app')
from app import app as flask_app

driver = None

@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def browser(request):
    global driver
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        if sys.platform == 'win32':
            driver = webdriver.Chrome(executable_path="selenium_drivers/chromedriver.exe")
        elif sys.platform == 'linux':
            driver = webdriver.Chrome(executable_path="selenium_drivers/chromedriver")
        else:
            logging.info("chrome driver not found for this platform")
    elif browser_name == "firefox":
        if sys.platform == 'win32':
            driver = webdriver.Firefox(executable_path="selenium_drivers/geckodriver.exe")
        elif sys.platform == 'linux':
            driver = webdriver.Firefox(executable_path="selenium_drivers/geckodriver")
        else:
            logging.info("firefox driver not found for this platform")
    elif browser_name == "IE":
        logging.info("ie driver not found for this platform")
    driver.get("http://localhost")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.logging = logging
    yield
    driver.close()