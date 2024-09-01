from .base_test import BaseTest
from pages.registration_page import RegistrationPage
from utils.csv_tool import SaveDataToFile
from utils.data_generator import TestDataGenerator
import time

class RegistrationPositiveTest(BaseTest):

    user_name = TestDataGenerator().name
    user_surname = TestDataGenerator().surname

    def setUp(self):
        super().setUp()
        self.registration_page = RegistrationPage(self.driver)
        self.save_data = SaveDataToFile()
        self.home_page.click_join_hub_button()

    def test_register_new_user_succes(self):
        self.registration_page.enter_name(self.user_name)
        self.registration_page.enter_surname(self.user_surname)
        self.registration_page.enter_email(self.email_of_no_existing_user)
        self.registration_page.enter_password(self.password_of_no_existing_user)
        self.save_data.save_user_data_to_file(self.user_name, self.user_surname, self.email_of_no_existing_user, self.password_of_no_existing_user)
        self.registration_page.repeat_password(self.password_of_no_existing_user)
        self.registration_page.click_signup_button()
        time.sleep(5)
        self.assertIn('writej.com/dashboard/user', self.driver.current_url)


class RegistrationNegativeTest(BaseTest):

    user_name = TestDataGenerator().name
    user_surname = TestDataGenerator().surname
    short_password = TestDataGenerator().short_password

    def setUp(self):
        super().setUp()
        self.registration_page = RegistrationPage(self.driver)
        self.driver.implicitly_wait(10)
        self.home_page.click_join_hub_button()


    def test_register_new_user_with_empty_all_fields(self):
        self.registration_page.click_signup_button()
        self.assertNotIn('writej.com/dashboard/user', self.driver.current_url)

    def test_register_new_user_with_empty_field_name(self):
        self.registration_page.enter_surname(self.user_surname)
        self.registration_page.enter_email(self.email_of_no_existing_user)
        self.registration_page.enter_password(self.password_of_no_existing_user)
        self.registration_page.repeat_password(self.password_of_no_existing_user)
        self.registration_page.click_signup_button()
        self.assertIn('The name field is required.', self.registration_page.get_toast_error_message().text)

    def test_register_new_user_with_empty_field_surname(self):
        self.registration_page.enter_name(self.user_name)
        self.registration_page.enter_email(self.email_of_no_existing_user)
        self.registration_page.enter_password(self.password_of_no_existing_user)
        self.registration_page.repeat_password(self.password_of_no_existing_user)
        self.registration_page.click_signup_button()
        self.assertIn('The surname field is required.', self.registration_page.get_toast_error_message().text)


    def test_register_new_user_with_empty_field_email(self):
        self.registration_page.enter_name(self.user_name)
        self.registration_page.enter_surname(self.user_surname)
        self.registration_page.enter_password(self.password_of_no_existing_user)
        self.registration_page.repeat_password(self.password_of_no_existing_user)
        self.registration_page.click_signup_button()
        self.assertIn('The email field is required.', self.registration_page.get_toast_error_message().text)

    def test_register_new_user_with_empty_field_password(self):
        self.registration_page.enter_name(self.user_name)
        self.registration_page.enter_surname(self.user_surname)
        self.registration_page.enter_email(self.email_of_no_existing_user)
        self.registration_page.click_signup_button()
        self.assertIn('The password field is required.',
                      self.registration_page.get_toast_error_message().text)


    def test_register_new_user_with_empty_field_confirm_password(self):
        self.registration_page.enter_name(self.user_name)
        self.registration_page.enter_surname(self.user_surname)
        self.registration_page.enter_email(self.email_of_no_existing_user)
        self.registration_page.enter_password(self.password_of_no_existing_user)
        self.registration_page.click_signup_button()
        self.assertIn('The password field confirmation does not match.',
                      self.registration_page.get_toast_error_message().text)




    def test_register_new_user_with_too_short_password(self):
        self.registration_page.enter_name(self.user_name)
        self.registration_page.enter_surname(self.user_surname)
        self.registration_page.enter_email(self.email_of_no_existing_user)
        self.registration_page.enter_password(self.short_password)
        self.registration_page.repeat_password(self.short_password)
        self.registration_page.click_signup_button()
        self.assertIn('The password field must be at least 8 characters.',
                      self.registration_page.get_toast_error_message().text)


    def test_register_new_user_with_incorrect_password_confirmation(self):
        self.registration_page.enter_name(self.user_name)
        self.registration_page.enter_surname(self.user_surname)
        self.registration_page.enter_email(self.email_of_no_existing_user)
        self.registration_page.enter_password(self.password_of_no_existing_user)
        self.registration_page.repeat_password(self.password_of_existing_user)
        self.registration_page.click_signup_button()
        self.assertIn('The password field confirmation does not match.',
                      self.registration_page.get_toast_error_message().text)
