import unittest
from tests.registration_tests import RegistrationPositiveTest, RegistrationNegativeTest

register_suite_tests = unittest.TestSuite()

'''Positive test cases of registration new user page'''
register_suite_tests.addTest(RegistrationPositiveTest('test_register_new_user_succes'))

'''Positive test cases of registration new user page'''
register_suite_tests.addTest(RegistrationNegativeTest('test_register_new_user_with_empty_all_fields'))
register_suite_tests.addTest(RegistrationNegativeTest('test_register_new_user_with_empty_field_name'))
register_suite_tests.addTest((RegistrationNegativeTest('test_register_new_user_with_empty_field_surname')))
register_suite_tests.addTest(RegistrationNegativeTest('test_register_new_user_with_empty_field_email'))
register_suite_tests.addTest(RegistrationNegativeTest('test_register_new_user_with_empty_field_password'))
register_suite_tests.addTest(RegistrationNegativeTest('test_register_new_user_with_empty_field_confirm_password'))
register_suite_tests.addTest(RegistrationNegativeTest('test_register_new_user_with_too_short_password'))
register_suite_tests.addTest(RegistrationNegativeTest('test_register_new_user_with_incorrect_password_confirmation'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(register_suite_tests)