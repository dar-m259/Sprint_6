import pytest

from url import MAIN_URL, ORDER_URL
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    
    yield driver
    driver.quit()

@pytest.fixture
def main_page_driver(driver):
    driver.get(MAIN_URL)
    return driver

@pytest.fixture
def order_page_driver(driver):
    driver.get(ORDER_URL)
    return driver