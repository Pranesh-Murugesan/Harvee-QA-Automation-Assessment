from config import BASE_URL, STANDARD_USERNAME, STANDARD_PASSWORD
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import pytest

pytestmark = pytest.mark.checkout


def test_TC14_full_checkout_and_verify_total(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USERNAME, STANDARD_PASSWORD)

    product_page = ProductPage(driver)
    product_page.add_products(2)
    product_page.open_cart()

    cart_page = CartPage(driver)
    assert cart_page.get_product_count() == 2

    checkout_page = CheckoutPage(driver)
    checkout_page.click_checkout()
    checkout_page.enter_customer_details("Test", "User", "12345")
    checkout_page.click_continue()

    subtotal = checkout_page.get_subtotal()
    tax = checkout_page.get_tax()
    total = checkout_page.get_total()

    assert round(subtotal + tax, 2) == round(total, 2)

    checkout_page.click_finish()
    assert checkout_page.get_completion_message() == "Thank you for your order!"

    product_page.open_cart()
    assert cart_page.is_cart_empty()


@pytest.mark.parametrize(
    "first_name, last_name, postal_code, expected_error",
    [
        ("", "User", "12345", "first name is required"),
        ("Test", "", "12345", "last name is required"),
        ("Test", "User", "", "postal code is required"),
    ],
    ids=[
        "TC15_missing_first_name",
        "TC16_missing_last_name",
        "TC17_missing_postal_code",
    ],
)
def test_checkout_required_fields(
    driver, first_name, last_name, postal_code, expected_error
):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USERNAME, STANDARD_PASSWORD)

    product_page = ProductPage(driver)
    product_page.add_products(1)
    product_page.open_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.click_checkout()
    checkout_page.enter_customer_details(
        first_name, last_name, postal_code
    )
    checkout_page.click_continue()

    error_message = checkout_page.get_error_message()

    assert expected_error in error_message.lower()


def test_TC18_subtotal_plus_tax_equals_total(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USERNAME, STANDARD_PASSWORD)

    product_page = ProductPage(driver)
    product_page.add_products(2)
    product_page.open_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.click_checkout()
    checkout_page.enter_customer_details(
        "Test", "User", "12345"
    )
    checkout_page.click_continue()

    subtotal = checkout_page.get_subtotal()
    tax = checkout_page.get_tax()
    total = checkout_page.get_total()

    assert round(subtotal + tax, 2) == round(total, 2)


def test_TC19_cart_empty_after_order(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USERNAME, STANDARD_PASSWORD)

    product_page = ProductPage(driver)
    product_page.add_products(1)
    product_page.open_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.click_checkout()
    checkout_page.enter_customer_details(
        "Test", "User", "12345"
    )
    checkout_page.click_continue()
    checkout_page.click_finish()

    product_page.open_cart()

    cart_page = CartPage(driver)
    assert cart_page.is_cart_empty()


def test_TC20_cancel_checkout(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USERNAME, STANDARD_PASSWORD)

    product_page = ProductPage(driver)
    product_page.add_products(1)
    product_page.open_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.click_checkout()

    checkout_page.click_cancel()

    assert "cart.html" in driver.current_url
