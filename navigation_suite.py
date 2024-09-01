
import unittest
from tests.home_page_tests import HomePageTest


navigation_test_suite = unittest.TestSuite()

navigation_test_suite.addTest(HomePageTest('test_home_page_loaded_correctly'))
navigation_test_suite.addTest(HomePageTest('test_open_login_page'))
navigation_test_suite.addTest(HomePageTest('test_open_register_page'))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(navigation_test_suite)