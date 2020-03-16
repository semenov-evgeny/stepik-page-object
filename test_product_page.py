from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import time, pytest, faker


@pytest.mark.login_guest
class TestGuestAddToBasketFromProductPage():

    @pytest.mark.need_review
    # реализован метод добавления товара в корзину с параметрами
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"])
    def test_guest_can_add_product_to_basket(self, browser, link):
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.add_to_basket_from_product_card()
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_be_add_to_basket()

    # реализован метод наличия сообщения об успешном добавлении товара в корзину
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.add_to_basket_from_product_card()
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_be_add_to_basket()
        product_page.should_not_be_success_message()

    # реализован метод отсутствия сообщения об успешном добавлении товара в корзину
    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        main_page = MainPage(browser, link)
        main_page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_not_be_success_message()

    # реализован метод проверки отсутствия исчезнования сообщения после добавления товара в корзину
    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.add_to_basket_from_product_card()
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_be_add_to_basket()
        product_page.should_not_be_success_message()

    # реализован метод наличия линка на логин со страницы продукта
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_login_link()

    @pytest.mark.need_review
    # реализован метод перехода на логин со страницы продукта
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_login_page()

    @pytest.mark.need_review
    # реализован метод переходав в корзину со со страницы продукта и отсутствия в нем успешного сообщения о добавленном продукте
    def test_guest_cant_see_product_in_basket_opened_from_product_pag(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_basket_page()
        basket_page = BasketPage(browser, link)
        basket_page.should_be_empty_basket()

@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage():

    # реализована фикстура регистрации клиента
    @pytest.fixture(scope="function")
    def setup_method(self, browser):
        f = faker.Faker()
        email_user = f.email()
        password_user = f.password()
        link = "http://selenium1py.pythonanywhere.com/"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email_user, password_user)
        main_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, setup_method):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        main_page = MainPage(browser, link)
        main_page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, setup_method):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.add_to_basket_from_product_card()
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_be_add_to_basket()
