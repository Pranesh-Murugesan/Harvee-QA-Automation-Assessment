from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUBTOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")
    CANCEL_BUTTON = (By.ID, "cancel")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    
    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()

    def enter_customer_details(self, first_name, last_name, postal_code):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()

    def click_finish(self):
        self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)).click()

    def get_price(self, locator):
        price_text = self.wait.until(EC.visibility_of_element_located(locator)).text
        return float(price_text.split("$")[-1])

    def get_subtotal(self):
        return self.get_price(self.SUBTOTAL)

    def get_tax(self):
        return self.get_price(self.TAX)

    def get_total(self):
        return self.get_price(self.TOTAL)

    def get_completion_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER)).text

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text

    
    def click_cancel(self):
        self.wait.until(EC.element_to_be_clickable(self.CANCEL_BUTTON)).click()
