import allure

from locators.locators_main_page import MainPageLocators
from pages.base_page import BasePage


class PageMain(BasePage):

    ORDER_BUTTONS = {
        "top": MainPageLocators.BUTTON_ORDER_TOP,
        "bottom": MainPageLocators.BUTTON_ORDER_BOTTOM,
    }

    @allure.step("Нажать на вопрос №{index} в разделе «Вопросы о важном»")
    def click_question(self, index):
        question = self.format_locator(MainPageLocators.QUESTION, index)
        self.scroll_to_element(question)
        self.click_element(question)

    @allure.step("Получить текст ответа на вопрос №{index}")
    def get_answer_text(self, index):
        return self.get_element_text(self.format_locator(MainPageLocators.ANSWER, index))

    @allure.step("Проверить, что кнопка «Заказать» в шапке видна")
    def is_order_button_top_displayed(self):
        return self.is_element_displayed(MainPageLocators.BUTTON_ORDER_TOP)

    @allure.step("Нажать кнопку «Заказать» ({position})")
    def click_order_button(self, position):
        button = self.ORDER_BUTTONS[position]
        self.scroll_to_element(button)
        self.click_element(button)
