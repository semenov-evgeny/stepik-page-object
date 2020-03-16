from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):
    # тест кейс проверок
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # реализована проверка на корректный url адрес
    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, \
        "Word login is not presented in url"
        assert True

    # реализована проверка, что есть форма логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK_FORM), \
        "Login form is not presented"
        assert True

    # реализована проверка, что есть форма регистрации на странице
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_LINK_FORM), \
        "Reg form is not presented"
        assert True

    # реализован метод регистрации пользователя
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REG_LINK_EMAIL)
        email_input.send_keys(email)
        pass_input = self.browser.find_element(*LoginPageLocators.REG_LINK_PASSWORD)
        pass_input.send_keys(password)
        pass_conf_input = self.browser.find_element(*LoginPageLocators.REG_LINK_CONFIRM_PASSWORD)
        pass_conf_input.send_keys(password)
        press_button_registration = self.browser.find_element(*LoginPageLocators.REG_LINK_REGISTRATION).click()
