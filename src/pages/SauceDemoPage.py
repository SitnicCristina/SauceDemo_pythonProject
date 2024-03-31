from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import json


class SauceDemoPage(BasePage):
    """This class represents the login page of the SauceDemo application."""

    # Locators for elements on the login page
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    # Locators for elements on the checkout page
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")

    def login(self, username, password):
        """Method to perform login with provided username and password."""
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_user_redirect_home_screen(self):
        try:
            # Check for the presence of an element that indicates the redirect to right page
            home_page_element = self.driver.find_element(By.CLASS_NAME, "app_logo")
            return "Swag Labs" in home_page_element.text
        except:
            # If the element is not found or an exception occurs, return False
            return False

    def is_user_redirect_login_screen(self):
        try:
            # Check for the presence of an element that indicates the redirect to right page
            home_page_element = self.driver.find_element(By.CLASS_NAME, "login_logo")
            return "Swag Labs" in home_page_element.text
        except:
            # If the element is not found or an exception occurs, return False
            return False

    def get_error_message(self):
        """Method to get the error message displayed on the login page."""
        return self.wait_for_element_visibility(self.ERROR_MESSAGE).text

    def add_items_to_cart(self, items):
        for item in items:
            item_id = f'add-to-cart-{item.lower().replace(" ", "-")}'
            self.driver.find_element(By.ID, item_id).click()

    def simple_remove_items(self, items):
        for item in items:
            item_id = f'remove-{item.lower().replace(" ", "-")}'
            self.driver.find_element(By.ID, item_id).click()

    def clickById(self, element_id):
        self.driver.find_element(By.ID, element_id).click()

    def item_is_in_cart(self, item_names):
        try:
            # Wait for cart items to be visible
            self.wait_for_element_visibility(self.CART_ITEMS)

            # Get text of all cart items
            cart_item_elements = self.driver.find_elements(*self.CART_ITEMS)
            cart_item_names = [item.find_element(By.CLASS_NAME, "inventory_item_name").text for item in
                               cart_item_elements]

            # Check if all specified item names are present in the cart
            return all(cart_item_names)
        except:
            return False

    def enter_personal_data(self):
        # Load personal data from json file
        data = open('testData/personalData.json', 'r')
        persData = json.load(data)
        # Enter data on the fields
        self.driver.find_element(*self.FIRST_NAME).send_keys(persData.get("firstName"))
        self.driver.find_element(*self.LAST_NAME).send_keys(persData.get("lastName"))
        self.driver.find_element(*self.POSTAL_CODE).send_keys(persData.get("zipPostalCode"))
