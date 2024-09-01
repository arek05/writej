
__copyright__ = "Copyright (C) 2024 Arkadiusz Jezierski"
print(__copyright__)

from utils.selenium_helper import SeleniumHelper
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.sh = SeleniumHelper(self.driver)


