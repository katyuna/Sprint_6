from helpers.helpers import wait_for_element, wait_for_element_visible, wait_for_element_clickable
from locators.locators_main_page import MainPageLocators

class PageMain(MainPageLocators):

    def __init__(self, driver):
        self.driver = driver

    def click_question(self, question_locator):
        question = wait_for_element(self.driver, question_locator)
        # behavior: 'instant' — без плавной прокрутки, иначе клик попадает в картинку самоката
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'instant'});", question)
        wait_for_element_clickable(self.driver, question_locator).click()

    def get_answer_text(self, answer_locator):
        return wait_for_element_visible(self.driver, answer_locator).text

    def click_button(self, button_locator):
        button = wait_for_element_clickable(self.driver, button_locator)
        button.click()

    def fill_input_field(self, input_field_locator, input_field_text):
        input_field = wait_for_element(self.driver, input_field_locator)
        input_field.send_keys(input_field_text)

    def choose_option(self, options_locator, option_locator):
        wait_for_element(self.driver, options_locator).click()
        wait_for_element(self.driver, option_locator).click()

