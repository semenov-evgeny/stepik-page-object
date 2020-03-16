from .base_page import BasePage
from .locators import ProductPageLocators, BasketPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket(self):
        self.should_be_button_add_to_basket()
        self.should_be_cost()
        self.should_be_equal_cost()
        self.should_be_equal_product_name()
        self.should_be_massege_add_to_basket()

    # реализована проверка наличия кнопки Добавить в корзину
    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), \
        "Button 'Add to basket' is not presented"
        assert True

    # реализована проверка наличия кнопки оставить отзыв
    def should_be_button_write_a_review(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_WRITE_A_REVIEW), \
        "Button 'Write a review' is not presented"
        assert True

    # реализована проверка наличия цены у товара
    def should_be_cost(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), \
        "Product price not specified"
        assert True

    # реализована проверка соответствия цен
    def should_be_equal_cost(self):
        price_on_card = self.browser.find_element(*ProductPageLocators.PRICE_ON_CARD).text
        price_on_basket = self.browser.find_element(*ProductPageLocators.PRICE_ON_BASKET).text
        assert price_on_card == price_on_basket, \
        "The price of the item in the basket and the price of the item in the display"
        assert True

    # реализована проверка наличия названия у товара
    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE), \
        "Product without title"
        assert True

    # реализована проверка соответствия имен товара и товара в корзине
    def should_be_equal_product_name(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        product_title_at_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE_AT_BASKET).text
        assert product_title == product_title_at_basket, \
        "Product title is error"
        assert True

    # реализована проверка добавления товара в корзину с учетом акции
    def should_be_massege_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Product not add to basket"
        assert True

    # реализована проверка отсутствия элемента успешного добавления товара в корзину
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    # реализована проверка исчезновения элемента успешного добавления товара в корзину
    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is not presented, but should be it"
