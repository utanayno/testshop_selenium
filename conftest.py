from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pytest

from pages.cart_page import CartPage
from pages.catalog_category_page import CatalogCatPage
from pages.item_page import ItemPage
import allure
from allure_commons.types import AttachmentType


@pytest.fixture
def driver():
    options = Options()
    # режим, чтобы тесты запускались фоново (браузер не моргал)
    #options.add_argument('--headless')
    #отключаем sandbox браузера
    #options.add_argument('--no-sandbox')
    #options.add_argument('--disable-dev-shm-usage')
    #options.add_argument('window-size=1920x1080')
    #указываем путь к браузеру Chromium
    #options.binary_location = '/usr/bin/chromium'

    #service = Service('/usr/bin/chromedriver')

    chrome_driver = webdriver.Chrome(
        options=options
    )
    chrome_driver.maximize_window()
    yield chrome_driver
    #allure.attach(chrome_driver.get_screenshot_as_png(),name='Screenshot', attachment_type=AttachmentType.PNG)
    chrome_driver.quit()

@pytest.fixture
def cart_page(driver):
    return CartPage(driver)

@pytest.fixture
def catalog_category_page(driver):
    return CatalogCatPage(driver)

@pytest.fixture
def item_page(driver):
    return ItemPage(driver)

