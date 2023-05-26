from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger import Logger


class BasePage:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.timeout = 10
        self.poll = 1
        self.logger = Logger(__name__)

    def go_to_url(self, url):
        self.driver.get(url)
        self.logger.info(f"Opened url: {url}")

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        self.logger.info(f"Got title: {self.driver.title}")

    def wait(self, timeout=10):
        self.driver.implicitly_wait(timeout)

    def find_element(self, *locator):
        try:
            element = WebDriverWait(self.driver, self.timeout, self.poll).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except TimeoutException:
            self.logger.info("Element not found: {}".format(locator))
            return None

    def click_element(self, locator):
        element = self.find_element(*locator)
        if element is not None and element.is_displayed():
            element.click()
        self.logger.info(f"Clicked element: {locator}")

    def send_keys_to_element(self, keys, locator):
        element = self.find_element(*locator)
        if element is not None:
            element.send_keys(keys)
        self.logger.info(f"Sent keys: {keys} to element: {locator}")

    def get_element_text(self, locator):
        element = self.find_element(*locator)
        if element is not None:
            return element.text
        self.logger.info(f"Got text from element: {locator}")

    def is_element_displayed(self, locator):
        element = self.find_element(*locator)
        if element is not None:
            return element.is_displayed()
        else:
            return False

    def wait_for_element(self, locator, timeout=10):
        self.logger.info(f"Waiting for element: {locator}")
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(*locator)
        )

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        self.logger.info(f"Waiting for element to be clickable: {locator}")
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(*locator)
        )

    def find_elements(self, locator):
        self.logger.info(f"Finding elements: {locator}")
        return self.driver.find_elements(*locator)

    def get_element_attribute(self, locator, attribute):
        element = self.find_element(*locator)
        if element is not None:
            return element.get_attribute(attribute)
        self.logger.info(f"Got attribute: {attribute} from element: {locator}")

    def send_keys(self, keys, locator):
        element = self.find_element(*locator)
        if element is not None:
            element.send_keys(keys)
        self.logger.info(f"Sent keys: {keys} to element: {locator}")
