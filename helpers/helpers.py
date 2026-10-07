from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.urls import MAIN_PAGE_URL


def create_driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(MAIN_PAGE_URL)
    return driver

def wait_for_element(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

def wait_for_element_visible(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

def wait_for_element_clickable(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))