from .base_page import BasePage
from .forgot_password_page import ForgotPasswordPage
from utils.locators import LogInPageLocators

class LogInPage(BasePage):
    def enter_email(self, email_address):
        self.sh.wait_and_input_text(self.driver, LogInPageLocators.EMAIL_FIELD, email_address)

    def enter_password(self, password):
        self.sh.wait_and_input_text(self.driver, LogInPageLocators.PASSWORD_FIELD, password)

    def get_toast_message(self):
        error_message = self.driver.find_element(*LogInPageLocators.TOAST_MESSAGE)
        return error_message.text

    def click_forgot_password_link(self):
        self.sh.wait_and_click_button(self.driver, LogInPageLocators.FORGOT_PASSWORD_LINK)
        return ForgotPasswordPage(self.driver)


    def click_sign_in_btn(self):
        self.sh.wait_and_click_button(self.driver, LogInPageLocators.SIGN_IN_BUTTON)





