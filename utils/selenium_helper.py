from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

import time

class SeleniumHelper:
    def __init__(self, driver):
        self.driver = driver

    def wait_and_click_button(self, driver, locator):
        time.sleep(3)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((locator))
            ).click()
        except StaleElementReferenceException:
            #time.sleep(5)
            WebDriverWait(self.driver).until(
                EC.visibility_of_element_located(locator)
            ).click()

    def wait_and_input_text(self, driver, locator, text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

