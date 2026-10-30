from config import BASE_URL, STANDARD_USERNAME, STANDARD_PASSWORD
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest

pytestmark = pytest.mark.access

def test_TC21_open_products_url_after_logout(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USERNAME, STANDARD_PASSWORD)

    product_page = ProductPage(driver)
    product_page.logout()

    driver.get(BASE_URL + "inventory.html")

    assert "inventory.html" not in driver.current_url
    assert "saucedemo.com" in driver.current_url
