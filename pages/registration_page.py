from .base_page import BasePage
from utils.locators import RegisterPageLocators


class RegistrationPage(BasePage):

    def enter_name(self, first_name):
       self.sh.wait_and_input_text(self.driver, RegisterPageLocators.NAME_FIELD, first_name)

    def enter_surname(self, last_name):
        self.sh.wait_and_input_text(self.driver, RegisterPageLocators.LAST_NAME_FIELD, last_name)

    def enter_email(self, email):
       self.sh.wait_and_input_text(self.driver, RegisterPageLocators.REGISTER_EMAIL_FIELD, email)

    def enter_password(self, user_password):
       self.sh.wait_and_input_text(self.driver, RegisterPageLocators.REGISTER_PASSWORD_FIELD, user_password)

    def repeat_password(self, user_password):
       self.sh.wait_and_input_text(self.driver, RegisterPageLocators.CONFIRM_PASSWORD_FIELD, user_password)

    def click_signup_button(self):
        self.sh.wait_and_click_button(self.driver, RegisterPageLocators.SIGN_UP_BUTTON)

    def get_toast_error_message(self):
        error_message = self.driver.find_element(*RegisterPageLocators.TOAST_MESSAGE_NAME_FIELD_REQUIRED)
        return error_message




