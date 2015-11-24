from model.application import Application
from selenium import webdriver
import pytest

@pytest.fixture
def app(request):
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    request.addfinalizer(driver.quit)
    return Application(driver)
