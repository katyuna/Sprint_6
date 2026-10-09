import allure

from locators.locators_cookie_floating_footer import CookieLocators
from pages.base_page import BasePage


class PageCookieFloatingFooter(BasePage):

    @allure.step("Проверить, показан ли баннер cookie")
    def is_cookie_displayed(self):
        return bool(self.find_elements(CookieLocators.BUTTON_COOKIE))

    @allure.step("Закрыть баннер cookie")
    def click_cookie(self):
        self.click_element(CookieLocators.BUTTON_COOKIE)
