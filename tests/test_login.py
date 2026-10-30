from config import ( BASE_URL, STANDARD_USERNAME, STANDARD_PASSWORD,LOCKED_USERNAME )
from pages.login_page import LoginPage
import pytest

pytestmark = pytest.mark.login


def test_TC01_standard_user_login(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USERNAME, STANDARD_PASSWORD)

    assert "inventory.html" in driver.current_url


def test_TC02_locked_out_user_login(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(LOCKED_USERNAME, STANDARD_PASSWORD)

    error_message = login_page.get_error_message()

    assert "locked out" in error_message.lower()


def test_TC03_invalid_login_credentials(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login("invalid_user", "wrong_password")

    error_message = login_page.get_error_message()

    assert "username and password do not match" in error_message.lower()
