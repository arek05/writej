from .base_page import BasePage
from utils.locators import ForgotPasswordPageLocators

class ForgotPasswordPage(BasePage):
    def enter_email(self, email):
        self.sh.wait_and_input_text(self.driver, ForgotPasswordPageLocators.EMAIL_FIELD, email)

    def click_send_instructions_button(self):
        self.sh.wait_and_click_button(self.driver, ForgotPasswordPageLocators.SEND_INSTRUCTION_BTN)

    def get_toast_message(self):
        toast_message = self.driver.find_element(*ForgotPasswordPageLocators.TOAST_MESSAGE_FORGOT_PAGE)
        return toast_message.text