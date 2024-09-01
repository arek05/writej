from .base_page import BasePage
from utils.locators import HomePageLocators
from .login_page import LogInPage
from .registration_page import RegistrationPage

class HomePage(BasePage):
    def click_signin_button(self):
        self.sh.wait_and_click_button(self.driver, HomePageLocators.SIGN_IN_BTN)
        return LogInPage(self.driver)

    def click_join_hub_button(self):
        self.sh.wait_and_click_button(self.driver, HomePageLocators.JOIN_HUB_BTN)
        return RegistrationPage(self.driver)



