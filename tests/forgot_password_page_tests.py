from .base_test import BaseTest
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LogInPage


class ForgotPasswordTests(BaseTest):

    def setUp(self):
        super().setUp()
        self.forgot_password = ForgotPasswordPage(self.driver)
        self.login_page = LogInPage(self.driver)
        self.home_page.click_signin_button()
        self.login_page.click_forgot_password_link()



    def test_enter_email_of_existing_user(self):
        self.forgot_password.enter_email(self.email_of_existing_user)
        self.forgot_password.click_send_instructions_button()
        self.assertEqual('Password reset link sent succesfully. Please also check your spam folder.', self.forgot_password.get_toast_message())


    def test_enter_email_of_no_existing_user(self):
        self.forgot_password.enter_email(self.email_of_no_existing_user)
        self.forgot_password.click_send_instructions_button()
        self.assertEqual('These credentials do not match our records.', self.forgot_password.get_toast_message())


    def test_empty_field_email(self):
        self.forgot_password.click_send_instructions_button()
        self.assertEqual('Please enter your email address.', self.forgot_password.get_toast_message())

    def test_incorrect_email_format(self):
        self.forgot_password.enter_email('incorrectemailadrress.com')
        self.forgot_password.click_send_instructions_button()
        self.assertEqual('The email field must be a valid email address.', self.forgot_password.get_toast_message())

