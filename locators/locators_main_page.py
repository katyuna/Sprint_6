from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_ORDER_TOP = (By.XPATH, '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]')
    BUTTON_ORDER_BOTTOM = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]')

    QUESTION = (By.ID, "accordion__heading-{}")
    ANSWER = (By.ID, "accordion__panel-{}")
