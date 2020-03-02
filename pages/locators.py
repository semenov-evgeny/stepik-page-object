from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_LINK_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_LINK_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_LINK_LOG_IN = (By.CSS_SELECTOR, "login_submit")
    REG_LINK_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_LINK_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_LINK_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_LINK_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_LINK_EMAIL = (By.CSS_SELECTOR, "registration_submit")
