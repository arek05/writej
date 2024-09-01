from .base_test import BaseTest
from pages.login_page import LogInPage

class LoginPositive(BaseTest):

    def setUp(self):
        super().setUp()
        self.login_page = LogInPage(self.driver)
        self.home_page.click_signin_button()

    def test_correct_email_and_password_entered_by_existing_user(self):
        self.login_page.enter_email(self.email_of_existing_user)
        self.login_page.enter_password(self.password_of_existing_user)
        self.login_page.click_sign_in_btn()
        self.assertEqual('Login Successful, Redirecting...', self.login_page.get_toast_message())

    def test_forgot_password_link(self):
        self.login_page.click_forgot_password_link()
        self.assertIn('Smart Content Creator | Reset Password', self.driver.title)




class LoginNegative(BaseTest):

    def setUp(self):
        super().setUp()
        self.login_page = LogInPage(self.driver)
        self.home_page.click_signin_button()

    def test_no_email_entered_by_existing_user(self):
        self.login_page.enter_password(self.password_of_existing_user)
        self.login_page.click_sign_in_btn()
        self.assertEqual('Please enter your email address.', self.login_page.get_toast_message())


    def test_invalid_email_entered_by_existing_user(self):
        self.login_page.enter_email(self.email_of_no_existing_user)
        self.login_page.enter_password(self.password_of_existing_user)
        self.login_page.click_sign_in_btn()
        self.assertEqual('These credentials do not match our records.', self.login_page.get_toast_message())

    def test_no_password_entered_by_existing_user(self):
        self.login_page.enter_email(self.email_of_existing_user)
        self.login_page.click_sign_in_btn()
        self.assertEqual('Please enter your password.', self.login_page.get_toast_message())


    def test_invalid_password_entered_by_existing_user(self):
        self.login_page.enter_email(self.email_of_existing_user)
        self.login_page.enter_password(self.password_of_no_existing_user)
        self.login_page.click_sign_in_btn()
        self.assertEqual('These credentials do not match our records.', self.login_page.get_toast_message())

    def test_no_email_and_password_entered(self):
        self.login_page.click_sign_in_btn()
        self.assertEqual('Please enter your email address.', self.login_page.get_toast_message())

    def test_no_existing_user_log_in(self):
        self.login_page.enter_email(self.email_of_no_existing_user)
        self.login_page.enter_password(self.password_of_no_existing_user)
        self.login_page.click_sign_in_btn()
        self.assertEqual('These credentials do not match our records.', self.login_page.get_toast_message())

