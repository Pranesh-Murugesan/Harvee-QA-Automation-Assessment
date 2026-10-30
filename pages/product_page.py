from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ADD_BUTTONS = (By.CLASS_NAME, "btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")



    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def sort_by_name_az(self):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN))
        Select(dropdown).select_by_value("az")

    
    def sort_by_price_low_to_high(self):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN))
        Select(dropdown).select_by_value("lohi")

    
    def sort_by_price_high_to_low(self):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN))
        Select(dropdown).select_by_value("hilo")

    def get_product_names(self):
        self.wait.until(
            EC.visibility_of_all_elements_located(self.PRODUCT_NAMES))
        return [
            element.text
            for element in self.driver.find_elements(*self.PRODUCT_NAMES)
        ]

    
    def add_products(self, count):
        buttons = self.wait.until(EC.presence_of_all_elements_located(self.ADD_BUTTONS))
        for button in buttons[:count]:
            button.click()

    def get_cart_badge_count(self):
        badge = self.wait.until(EC.visibility_of_element_located(self.CART_BADGE))
        return int(badge.text)

    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_LINK)).click()

    
    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.MENU_BUTTON)).click()

        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()

    def get_product_prices(self):
        self.wait.until(EC.visibility_of_all_elements_located(self.PRODUCT_PRICES) )
        return [
        float(price.text.replace("$", ""))
        for price in self.driver.find_elements(*self.PRODUCT_PRICES) ]
