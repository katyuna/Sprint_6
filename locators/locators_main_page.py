from selenium.webdriver.common.by import By

class MainPageLocators:
    BUTTON_ORDER_TOP = (By.XPATH, '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]')
    BUTTON_ORDER_BOTTOM = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]')

    QUESTION_PRICE = (By.ID, "accordion__heading-0")
    ANSWER_PRICE = (By.ID, "accordion__panel-0")

    QUESTION_SEVERAL_SCOOTERS = (By.ID, "accordion__heading-1")
    ANSWER_SEVERAL_SCOOTERS = (By.ID, "accordion__panel-1")

    QUESTION_RENTAL_TIME = (By.ID, "accordion__heading-2")
    ANSWER_RENTAL_TIME = (By.ID, "accordion__panel-2")

    QUESTION_ORDER_TODAY = (By.ID, "accordion__heading-3")
    ANSWER_ORDER_TODAY = (By.ID, "accordion__panel-3")

    QUESTION_PROLONGATE_OR_RETURN = (By.ID, "accordion__heading-4")
    ANSWER_PROLONGATE_OR_RETURN = (By.ID, "accordion__panel-4")

    QUESTION_CHARGER = (By.ID, "accordion__heading-5")
    ANSWER_CHARGER = (By.ID, "accordion__panel-5")

    QUESTION_CANCEL_ORDER = (By.ID, "accordion__heading-6")
    ANSWER_CANCEL_ORDER = (By.ID, "accordion__panel-6")

    QUESTION_OUTSIDE_MCAD = (By.ID, "accordion__heading-7")
    ANSWER_OUTSIDE_MCAD = (By.ID, "accordion__panel-7")
    LOGO_SCOOTER = (By.XPATH, '//a[contains(@class, "Header_LogoScooter")]')
    LOGO_YANDEX = (By.XPATH, '//a[contains(@class, "Header_LogoYandex")]')
