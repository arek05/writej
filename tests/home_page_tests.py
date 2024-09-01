from tests.base_test import BaseTest

class HomePageTest(BaseTest):

    def test_home_page_loaded_correctly(self):
        assert 'Smart Content Creator | Home' in self.driver.title

    def test_open_login_page(self):
        self.home_page.click_signin_button()
        assert 'Smart Content Creator | Sign in' in self.driver.title

    def test_open_register_page(self):
        self.home_page.click_join_hub_button()
        assert 'Smart Content Creator | Register' in self.driver.title



