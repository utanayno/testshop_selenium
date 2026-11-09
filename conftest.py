from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from pages.cart_page import CartPage
from pages.catalog_category_page import CatalogCatPage
from pages.item_page import ItemPage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    return chrome_driver

@pytest.fixture
def cart_page(driver):
    return CartPage(driver)

@pytest.fixture
def catalog_category_page(driver):
    return CatalogCatPage(driver)

@pytest.fixture
def item_page(driver):
    return ItemPage(driver)

