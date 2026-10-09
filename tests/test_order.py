import allure
import pytest

from helpers import data
from helpers.urls import MAIN_PAGE_URL, DZEN_URL
from pages.page_main import PageMain
from pages.page_order import PageOrder


class TestOrder:

    @allure.title("Кнопка «Заказать» в шапке отображается")
    def test_is_order_button_displayed(self, driver):
        main_page = PageMain(driver)
        assert main_page.is_order_button_top_displayed()

    @allure.title("Заказ самоката через кнопку «Заказать» ({order_button})")
    @pytest.mark.parametrize(
        "order_button, name, surname, address, phone, color, comment",
        [
            ("top", data.ORDER_NAME_1, data.ORDER_SURNAME_1, data.ORDER_ADDRESS_1,
             data.ORDER_PHONE_1, data.COLOR_BLACK, data.ORDER_COMMENT_1),
            ("bottom", data.ORDER_NAME_2, data.ORDER_SURNAME_2, data.ORDER_ADDRESS_2,
             data.ORDER_PHONE_2, data.COLOR_GREY, data.ORDER_COMMENT_2),
        ],
        ids=["top_button", "bottom_button"]
    )
    def test_create_order(self, driver, order_button, name, surname, address, phone, color, comment):
        main_page = PageMain(driver)
        main_page.click_order_button(order_button)

        order_page = PageOrder(driver)
        order_page.fill_customer_form(name, surname, address, phone)
        order_page.fill_rent_form(data.DELIVERY_DATE, color, comment)
        order_page.confirm_order()

        assert order_page.is_order_placed_modal_displayed()

    @allure.title("Логотип «Самоката» ведёт на главную страницу")
    def test_click_scooter_logo_opens_main_page(self, driver):
        main_page = PageMain(driver)
        main_page.click_order_button("top")

        order_page = PageOrder(driver)
        order_page.click_scooter_logo()

        assert order_page.is_url(MAIN_PAGE_URL)

    @allure.title("Логотип Яндекса открывает Дзен в новом окне")
    def test_click_yandex_logo_opens_dzen_in_new_window(self, driver):
        main_page = PageMain(driver)
        main_page.click_yandex_logo()
        main_page.switch_to_new_window()

        assert main_page.is_url_contains(DZEN_URL)
