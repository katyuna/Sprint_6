import allure
from selenium.webdriver.common.keys import Keys

from locators.locators_order_page import OrderPageLocators
from pages.base_page import BasePage


class PageOrder(BasePage):

    @allure.step("Заполнить форму «Для кого самокат» и нажать «Далее»")
    def fill_customer_form(self, name, surname, address, phone):
        self.fill_input_field(OrderPageLocators.INPUT_NAME, name)
        self.fill_input_field(OrderPageLocators.INPUT_SURNAME, surname)
        self.fill_input_field(OrderPageLocators.INPUT_ADDRESS, address)
        self.click_element(OrderPageLocators.OPTIONS_METRO)
        self.click_element(OrderPageLocators.OPTION_METRO)
        self.fill_input_field(OrderPageLocators.INPUT_PHONE, phone)
        self.click_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step("Заполнить форму «Про аренду» и нажать «Заказать»")
    def fill_rent_form(self, date, color, comment):
        self.fill_input_field(OrderPageLocators.INPUT_DATE, date + Keys.ENTER)
        self.click_element(OrderPageLocators.DROPDOWN_RENTAL_PERIOD)
        self.click_element(OrderPageLocators.OPTION_RENTAL_PERIOD)
        self.click_element(self.format_locator(OrderPageLocators.CHECKBOX_COLOR, color))
        self.fill_input_field(OrderPageLocators.INPUT_COMMENT, comment)
        self.click_element(OrderPageLocators.BUTTON_ORDER_IN_FORM)

    @allure.step("Подтвердить заказ: нажать «Да»")
    def confirm_order(self):
        self.click_element(OrderPageLocators.BUTTON_CONFIRM_YES)

    @allure.step("Проверить, что появилось окно «Заказ оформлен»")
    def is_order_placed_modal_displayed(self):
        return self.is_element_displayed(OrderPageLocators.MODAL_ORDER_PLACED)
