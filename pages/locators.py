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

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BUTTON_WRITE_A_REVIEW = (By.CSS_SELECTOR, "#write_review")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_PRICE_AT_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    #PRODUCT_TITLE_TEXT = browser.find_element_by_css_selector('.product_main h1').text
    PRODUCT_TITLE_AT_BASKET = (By.CSS_SELECTOR, "#messages .alertinner strong")
    #PRODUCT_TITLE_AT_BASKET_TEXT = PRODUCT_TITLE_AT_BASKET.text
    PRODUCT_AT_BASKET = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(2) .alertinner")
