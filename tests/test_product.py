from config import BASE_URL, STANDARD_USERNAME, STANDARD_PASSWORD
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest

pytestmark = pytest.mark.product


def test_TC06_sort_products_name_az(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USERNAME, STANDARD_PASSWORD)

    product_page = ProductPage(driver)
    product_page.sort_by_name_az()

    actual_names = product_page.get_product_names()
    expected_names = sorted(actual_names, key=str.lower)

    assert actual_names == expected_names


def test_TC08_sort_products_price_low_to_high(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USERNAME, STANDARD_PASSWORD)

    product_page = ProductPage(driver)
    product_page.sort_by_price_low_to_high()

    actual_prices = product_page.get_product_prices()

    assert actual_prices == sorted(actual_prices)


def test_TC09_sort_products_price_high_to_low(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USERNAME, STANDARD_PASSWORD)

    product_page = ProductPage(driver)
    product_page.sort_by_price_high_to_low()

    actual_prices = product_page.get_product_prices()

    assert actual_prices == sorted(actual_prices, reverse=True)
