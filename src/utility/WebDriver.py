from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class WebDriver:
    """Class to manage WebDriver instances."""

    @staticmethod
    def get_driver():
        # Method to initialize and return a Chrome WebDriver instance.
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")

        caps = DesiredCapabilities.CHROME.copy()
        caps['goog:loggingPrefs'] = {'browser': 'ALL'}

        driver = webdriver.Chrome(options=chrome_options)
        return driver

    @staticmethod
    def quit_driver(driver):
        # Method to quit the WebDriver instance."""
        if driver:
            driver.quit()

