import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://todomvc.com/examples/vanillajs/")
    yield driver
    driver.quit()