from selenium import webdriver
from helpers.urls import MAIN_PAGE_URL


def create_driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(MAIN_PAGE_URL)
    return driver
