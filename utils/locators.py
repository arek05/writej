from selenium.webdriver.common.by import By

class HomePageLocators:
    SIGN_IN_BTN = (By.XPATH, '/html/body/header/nav/div[2]/a[1]')
    JOIN_HUB_BTN = (By.XPATH, '/html/body/header/nav/div[2]/a[2]')

class LogInPageLocators:
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'password')
    SIGN_IN_BUTTON = (By.ID, 'LoginFormButton')
    TOAST_MESSAGE = (By.XPATH, '// *[ @ id = "toast-container"]')
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, 'Forgot Password?')

class RegisterPageLocators:
    NAME_FIELD = (By.ID, 'name_register')
    LAST_NAME_FIELD = (By.ID, 'surname_register')
    REGISTER_EMAIL_FIELD = (By.ID, 'email_register')
    REGISTER_PASSWORD_FIELD = (By.ID, 'password_register')
    CONFIRM_PASSWORD_FIELD = (By.ID, 'password_confirmation_register')
    SIGN_UP_BUTTON = (By.ID, 'RegisterFormButton')
    SIGN_IN_LINK = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a')
    TERMS_AND_CONDITION_LINK = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div[1]/form/div[6]/a[1]')
    PRIVACY_POLICY_LINK = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div[1]/form/div[6]/a[2]')
    BACK_TO_HOME_LINK = (By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div[2]/a')
    LOGO = (By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div[1]/a/img[1]')
    PASSWORD_VISIBLE_BUTTON = (By.CSS_SELECTOR, "div.lqd-input-container:nth-child(6) > div:nth-child(2) > button:nth-child(2)")
    REPEAT_PASSWORD_VISIBLE_BUTTON = (By.XPATH, '/ html / body / div[2] / div / div / div / div[2] / div[1] / div / div[1] / form / div[5] / div / button / svg[1] / \
      path[1]')
    TOAST_MESSAGE_NAME_FIELD_REQUIRED = (By.XPATH, '/html/body/div[3]/div/div')

class ForgotPasswordPageLocators:
    EMAIL_FIELD = (By.ID, 'password_reset_email')
    SEND_INSTRUCTION_BTN = (By.ID, 'PasswordResetFormButton')
    TOAST_MESSAGE_FORGOT_PAGE = (By.XPATH, '//*[@id="toast-container"]/div/div')

