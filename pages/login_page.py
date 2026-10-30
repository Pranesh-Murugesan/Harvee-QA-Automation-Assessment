from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD)).send_keys(username)

    def enter_password(self, password):self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD)).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text


    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
