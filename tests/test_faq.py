from helpers import data
from locators.locators_main_page import MainPageLocators
from pages.page_main import PageMain


class TestFaq:

    def test_question_price_shows_answer(self, driver):
        main_page = PageMain(driver)
        main_page.click_question(MainPageLocators.QUESTION_PRICE)
        assert main_page.get_answer_text(MainPageLocators.ANSWER_PRICE) == data.ANSWER_PRICE

    def test_question_several_scooters_shows_answer(self, driver):
        main_page = PageMain(driver)
        main_page.click_question(MainPageLocators.QUESTION_SEVERAL_SCOOTERS)
        assert main_page.get_answer_text(MainPageLocators.ANSWER_SEVERAL_SCOOTERS) == data.ANSWER_SEVERAL_SCOOTERS

    def test_question_rental_time_shows_answer(self, driver):
        main_page = PageMain(driver)
        main_page.click_question(MainPageLocators.QUESTION_RENTAL_TIME)
        assert main_page.get_answer_text(MainPageLocators.ANSWER_RENTAL_TIME) == data.ANSWER_RENTAL_TIME

    def test_question_order_today_shows_answer(self, driver):
        main_page = PageMain(driver)
        main_page.click_question(MainPageLocators.QUESTION_ORDER_TODAY)
        assert main_page.get_answer_text(MainPageLocators.ANSWER_ORDER_TODAY) == data.ANSWER_ORDER_TODAY

    def test_question_prolongate_or_return_shows_answer(self, driver):
        main_page = PageMain(driver)
        main_page.click_question(MainPageLocators.QUESTION_PROLONGATE_OR_RETURN)
        assert main_page.get_answer_text(MainPageLocators.ANSWER_PROLONGATE_OR_RETURN) == data.ANSWER_EXTEND_OR_RETURN

    def test_question_charger_shows_answer(self, driver):
        main_page = PageMain(driver)
        main_page.click_question(MainPageLocators.QUESTION_CHARGER)
        assert main_page.get_answer_text(MainPageLocators.ANSWER_CHARGER) == data.ANSWER_CHARGER

    def test_question_cancel_order_shows_answer(self, driver):
        main_page = PageMain(driver)
        main_page.click_question(MainPageLocators.QUESTION_CANCEL_ORDER)
        assert main_page.get_answer_text(MainPageLocators.ANSWER_CANCEL_ORDER) == data.ANSWER_CANCEL_ORDER

    def test_question_outside_mcad_shows_answer(self, driver):
        main_page = PageMain(driver)
        main_page.click_question(MainPageLocators.QUESTION_OUTSIDE_MCAD)
        assert main_page.get_answer_text(MainPageLocators.ANSWER_OUTSIDE_MCAD) == data.ANSWER_OUTSIDE_MCAD
