from helpers.helpers import wait_for_element
from locators.locators_cookie_floating_footer import CookieLocators


class PageCookieFloatingFooter(CookieLocators):

    def __init__(self, driver):
        self.driver = driver

    def is_cookie_displayed(self):
        return bool(self.driver.find_elements(*self.BUTTON_COOKIE))

    def click_cookie(self):
        wait_for_element(self.driver, self.BUTTON_COOKIE).click()