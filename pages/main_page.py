from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators, ProductPageLocators
from .login_page import LoginPage
from .product_page import ProductPage

class MainPage(BasePage):

    # заглушка
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
    #Конструктор выше с ключевым словом super на самом деле только вызывает конструктор класса предка и передает ему все те аргументы, которые мы передали в конструктор MainPage

    # метод добавления товара в корзину
    def add_to_basket_from_product_card(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_basket.click()
        self.solve_quiz_and_get_code()
        #self.should_be_add_to_basket()
