from config import BASE_URL, STANDARD_USERNAME, STANDARD_PASSWORD
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
import pytest

pytestmark = pytest.mark.cart

def test_TC10_add_two_products_and_verify_cart(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USERNAME, STANDARD_PASSWORD)

    product_page = ProductPage(driver)
    product_page.add_products(2)

    assert product_page.get_cart_badge_count() == 2

    product_page.open_cart()

    cart_page = CartPage(driver)
    cart_names = cart_page.get_product_names()

    assert len(cart_names) == 2



def test_TC11_remove_one_product_from_cart(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USERNAME, STANDARD_PASSWORD)

    product_page = ProductPage(driver)
    product_page.add_products(2)

    assert product_page.get_cart_badge_count() == 2

    product_page.open_cart()

    cart_page = CartPage(driver)
    original_names = cart_page.get_product_names()

    assert len(original_names) == 2

    cart_page.remove_first_product()

    remaining_names = cart_page.get_product_names()

    assert len(remaining_names) == 1
    assert remaining_names[0] in original_names
    assert remaining_names[0] != original_names[0]


def test_TC13_empty_cart(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USERNAME, STANDARD_PASSWORD)

    product_page = ProductPage(driver)
    product_page.open_cart()

    cart_page = CartPage(driver)

    assert cart_page.is_cart_empty()
