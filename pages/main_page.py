from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators, ProductPageLocators
from .login_page import LoginPage
from .product_page import ProductPage

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def add_to_basket_from_product_card(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_basket.click()
        self.solve_quiz_and_get_code()
        
        #self.should_be_add_to_basket()
