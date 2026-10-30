from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BUTTONS = (By.CLASS_NAME, "cart_button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_product_names(self):
        self.wait.until(EC.presence_of_all_elements_located(self.CART_ITEMS))
        return [
            item.find_element(*self.PRODUCT_NAMES).text
            for item in self.driver.find_elements(*self.CART_ITEMS)
        ]

    def remove_first_product(self):
        buttons = self.wait.until(EC.presence_of_all_elements_located(self.REMOVE_BUTTONS))
        buttons[0].click()

    
    def get_product_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def is_cart_empty(self):
        return len(self.driver.find_elements(*self.CART_ITEMS)) == 0