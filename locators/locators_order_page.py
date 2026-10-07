from selenium.webdriver.common.by import By
from locators.locators_cookie_floating_footer import CookieLocators


class OrderPageLocators(CookieLocators):

    INPUT_NAME = (By.XPATH, '//input[@placeholder="* Имя"]')
    INPUT_SURNAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    INPUT_ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    INPUT_PHONE = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')

    OPTIONS_METRO = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    OPTION_METRO = (By.XPATH, '(//li[@class="select-search__row"])[1]')

    BUTTON_NEXT = (By.XPATH, '//button[text()="Далее"]')

    INPUT_DATE = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    DROPDOWN_RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-control")
    OPTION_RENTAL_PERIOD = (By.XPATH, '(//div[@class="Dropdown-option"])[1]')
    CHECKBOX_BLACK = (By.ID, "black")
    CHECKBOX_GREY = (By.ID, "grey")
    INPUT_COMMENT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    BUTTON_ORDER_IN_FORM = (By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[text()="Заказать"]')

    BUTTON_CONFIRM_YES = (By.XPATH, '//button[text()="Да"]')
    MODAL_ORDER_PLACED = (By.XPATH, '//div[contains(@class, "Order_ModalHeader") and contains(text(), "Заказ оформлен")]')
