import pytest
from helpers.helpers import create_driver
from pages.page_cookie_floating_footer import PageCookieFloatingFooter


@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def check_and_resolve_cookie_floating_footer(driver):
    cookie_page = PageCookieFloatingFooter(driver)
    if cookie_page.is_cookie_displayed():
        cookie_page.click_cookie()
