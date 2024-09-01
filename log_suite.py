import unittest
from tests.login_tests import LoginNegative, LoginPositive
from tests.forgot_password_page_tests import ForgotPasswordTests

log_suite_tests = unittest.TestSuite()

'''Positive test cases of login page'''
log_suite_tests.addTest(LoginPositive('test_correct_email_and_password_entered_by_existing_user'))
log_suite_tests.addTest(LoginPositive('test_forgot_password_link'))

'''Negative test cases of login page'''
log_suite_tests.addTest(LoginNegative('test_no_email_entered_by_existing_user'))
log_suite_tests.addTest(LoginNegative('test_invalid_email_entered_by_existing_user'))
log_suite_tests.addTest(LoginNegative('test_no_password_entered_by_existing_user'))
log_suite_tests.addTest(LoginNegative('test_invalid_password_entered_by_existing_user'))
log_suite_tests.addTest(LoginNegative('test_no_email_and_password_entered'))
log_suite_tests.addTest(LoginNegative('test_no_existing_user_log_in'))

'''Positive tests cases of forgot password page'''
log_suite_tests.addTest(ForgotPasswordTests('test_enter_email_of_existing_user'))

'''Negative test cases of forgot password page'''
log_suite_tests.addTest(ForgotPasswordTests('test_enter_email_of_no_existing_user'))
log_suite_tests.addTest(ForgotPasswordTests('test_empty_field_email'))
log_suite_tests.addTest(ForgotPasswordTests('test_incorrect_email_format'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(log_suite_tests)