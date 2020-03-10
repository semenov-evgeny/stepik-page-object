from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    # проверка пустой корзины
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT_FORM), \
        "Basket without empty message"

    # реализована проверка отсутствия элемента успешного добавления товара в корзину
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    # реализована проверка исчезновения элемента успешного добавления товара в корзину
    def should_be_success_message(self):
        assert self.is_disappeared(*BasketPageLocators.SUCCESS_MESSAGE), \
       "Success message is not presented, but should be it"
