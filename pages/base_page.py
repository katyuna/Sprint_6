import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators_base_page import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def format_locator(locator, value):
        method, template = locator
        return method, template.format(value)

    def wait_for_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def wait_for_element_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def is_element_displayed(self, locator, timeout=5):
        return self.wait_for_element_visible(locator, timeout).is_displayed()

    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'instant'});", element)

    def click_element(self, locator):
        self.wait_for_element_clickable(locator).click()

    def fill_input_field(self, locator, text):
        self.wait_for_element(locator).send_keys(text)

    def get_element_text(self, locator):
        return self.wait_for_element_visible(locator).text

    def is_url(self, url, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    def is_url_contains(self, url_part, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.url_contains(url_part))

    @allure.step("Переключиться на новое окно браузера")
    def switch_to_new_window(self, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Нажать на логотип «Самоката» в шапке")
    def click_scooter_logo(self):
        self.click_element(BasePageLocators.LOGO_SCOOTER)

    @allure.step("Нажать на логотип Яндекса в шапке")
    def click_yandex_logo(self):
        self.click_element(BasePageLocators.LOGO_YANDEX)
