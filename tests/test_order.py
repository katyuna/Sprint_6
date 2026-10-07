import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers import data
from helpers.helpers import wait_for_element
from helpers.urls import MAIN_PAGE_URL, DZEN_URL
from locators.locators_main_page import MainPageLocators
from locators.locators_order_page import OrderPageLocators
from pages.page_main import PageMain

class TestOrder:

    def test_is_order_button_displayed(self, driver):
        button = wait_for_element(driver, MainPageLocators.BUTTON_ORDER_TOP)
        assert button.is_displayed()

    @pytest.mark.parametrize(
        "order_button, name, surname, address, phone, color, comment",
        [
            (MainPageLocators.BUTTON_ORDER_TOP, data.ORDER_NAME_1, data.ORDER_SURNAME_1, data.ORDER_ADDRESS_1,
             data.ORDER_PHONE_1, OrderPageLocators.CHECKBOX_BLACK, data.ORDER_COMMENT_1),
            (MainPageLocators.BUTTON_ORDER_BOTTOM, data.ORDER_NAME_2, data.ORDER_SURNAME_2, data.ORDER_ADDRESS_2,
             data.ORDER_PHONE_2, OrderPageLocators.CHECKBOX_GREY, data.ORDER_COMMENT_2),
        ],
        ids=["top_button", "bottom_button"]
    )
    def test_create_order(self, driver, order_button, name, surname, address, phone, color, comment):
        page = PageMain(driver)
        page.click_button(order_button)

        page.fill_input_field(OrderPageLocators.INPUT_NAME, name)
        page.fill_input_field(OrderPageLocators.INPUT_SURNAME, surname)
        page.fill_input_field(OrderPageLocators.INPUT_ADDRESS, address)
        page.choose_option(OrderPageLocators.OPTIONS_METRO, OrderPageLocators.OPTION_METRO)
        page.fill_input_field(OrderPageLocators.INPUT_PHONE, phone)
        page.click_button(OrderPageLocators.BUTTON_NEXT)

        page.fill_input_field(OrderPageLocators.INPUT_DATE, data.DELIVERY_DATE + Keys.ENTER)
        page.choose_option(OrderPageLocators.DROPDOWN_RENTAL_PERIOD, OrderPageLocators.OPTION_RENTAL_PERIOD)
        page.click_button(color)
        page.fill_input_field(OrderPageLocators.INPUT_COMMENT, comment)
        page.click_button(OrderPageLocators.BUTTON_ORDER_IN_FORM)
        page.click_button(OrderPageLocators.BUTTON_CONFIRM_YES)

        assert wait_for_element(driver, OrderPageLocators.MODAL_ORDER_PLACED).is_displayed()

    def test_click_scooter_logo_opens_main_page(self, driver):
        page = PageMain(driver)
        page.click_button(MainPageLocators.BUTTON_ORDER_TOP)
        page.click_button(MainPageLocators.LOGO_SCOOTER)

        assert WebDriverWait(driver, 5).until(EC.url_to_be(MAIN_PAGE_URL))

    def test_click_yandex_logo_opens_dzen_in_new_window(self, driver):
        page = PageMain(driver)
        page.click_button(MainPageLocators.LOGO_YANDEX)

        WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[-1])

        assert WebDriverWait(driver, 30).until(EC.url_contains(DZEN_URL))
