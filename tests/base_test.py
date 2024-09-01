import unittest
from selenium import webdriver
from pages.home_page import HomePage
from utils.csv_tool import SaveDataToFile
from utils.data_generator import TestDataGenerator

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://writej.com/')
        self.driver.implicitly_wait(10)
        self.home_page = HomePage(self.driver)
        self.email_of_existing_user = SaveDataToFile().read_user_data()[0]
        self.password_of_existing_user = SaveDataToFile().read_user_data()[1]
        self.email_of_no_existing_user = TestDataGenerator().generate_email_with_name_and_surname()
        self.password_of_no_existing_user = TestDataGenerator().password

    def tearDown(self):
        self.driver.quit()