from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket(self):
        self.should_be_button_add_to_basket()
        self.should_be_cost()
        self.should_be_equal_cost()
        self.should_be_equal_product_name()
        self.should_be_massege_add_to_basket()


    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), \
        "Button 'Add to basket' is not presented"
        # реализована проверка наличия кнопки Добавить в корзину
        assert True

    def should_be_button_write_a_review(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_WRITE_A_REVIEW), \
        "Button 'Write a review' is not presented"
        # реализована проверка наличия кнопки оставить отзыв
        assert True

    def should_be_cost(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), \
        "Product price not specified"
        # реализована проверка наличия цены у товара
        assert True

    def should_be_equal_cost(self):
        price_on_card = self.browser.find_element_by_css_selector('.product_main .price_color').text
        # переделать для подтягивания данных из файла с локаторами
        #print(f' цена в заголовке - {price_on_card}')
        price_on_basket = self.browser.find_element_by_css_selector('.alert-info .alertinner strong').text
        # переделать для подтягивания данных из файла с локаторами
        #print(f' цена в корзине - {price_on_basket}')
        assert price_on_card == price_on_basket, \
        "The price of the item in the basket and the price of the item in the display"
        # реализована проверка соответствия цен
        assert True

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE), \
        "Product without title"
        # реализована проверка наличия названия у товара
        assert True

    def should_be_equal_product_name(self):
        product_title = self.browser.find_element_by_css_selector('.product_main h1').text
        # переделать для подтягивания данных из файла с локаторами
        #print(f' титул в заголовке - {product_title}')
        product_title_at_basket = self.browser.find_element_by_css_selector('.alertinner strong').text
        # переделать для подтягивания данных из файла с локаторами
        #print(f' титул в корзине - {product_title_at_basket}')
        assert product_title == product_title_at_basket, \
        "Product title is error"
        # реализована проверка соответствия имен товара и товара в корзине
        assert True

    def should_be_massege_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_AT_BASKET), \
        "Product not add to basket"
        # реализована проверка добавления товара в корзину с учетом акции
        assert True
