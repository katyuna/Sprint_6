import allure

from helpers import data
from pages.page_main import PageMain


class TestFaq:

    @allure.title("Вопрос «Сколько это стоит? И как оплатить?» раскрывает ответ")
    def test_question_price_shows_answer(self, driver):
        main_page = PageMain(driver)
        main_page.click_question(0)
        assert main_page.get_answer_text(0) == data.ANSWER_PRICE

    @allure.title("Вопрос «Хочу сразу несколько самокатов!» раскрывает ответ")
    def test_question_several_scooters_shows_answer(self, driver):
        main_page = PageMain(driver)
        main_page.click_question(1)
        assert main_page.get_answer_text(1) == data.ANSWER_SEVERAL_SCOOTERS

    @allure.title("Вопрос «Как рассчитывается время аренды?» раскрывает ответ")
    def test_question_rental_time_shows_answer(self, driver):
        main_page = PageMain(driver)
        main_page.click_question(2)
        assert main_page.get_answer_text(2) == data.ANSWER_RENTAL_TIME

    @allure.title("Вопрос «Можно ли заказать самокат прямо на сегодня?» раскрывает ответ")
    def test_question_order_today_shows_answer(self, driver):
        main_page = PageMain(driver)
        main_page.click_question(3)
        assert main_page.get_answer_text(3) == data.ANSWER_ORDER_TODAY

    @allure.title("Вопрос «Можно ли продлить заказ или вернуть самокат раньше?» раскрывает ответ")
    def test_question_prolongate_or_return_shows_answer(self, driver):
        main_page = PageMain(driver)
        main_page.click_question(4)
        assert main_page.get_answer_text(4) == data.ANSWER_EXTEND_OR_RETURN

    @allure.title("Вопрос «Вы привозите зарядку вместе с самокатом?» раскрывает ответ")
    def test_question_charger_shows_answer(self, driver):
        main_page = PageMain(driver)
        main_page.click_question(5)
        assert main_page.get_answer_text(5) == data.ANSWER_CHARGER

    @allure.title("Вопрос «Можно ли отменить заказ?» раскрывает ответ")
    def test_question_cancel_order_shows_answer(self, driver):
        main_page = PageMain(driver)
        main_page.click_question(6)
        assert main_page.get_answer_text(6) == data.ANSWER_CANCEL_ORDER

    @allure.title("Вопрос «Я живу за МКАДом, привезёте?» раскрывает ответ")
    def test_question_outside_mcad_shows_answer(self, driver):
        main_page = PageMain(driver)
        main_page.click_question(7)
        assert main_page.get_answer_text(7) == data.ANSWER_OUTSIDE_MCAD
