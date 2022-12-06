from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_locators import UrlLocators


def test_successful_registration(switching_to_an_account): #тест переход в личный кабинет по клику на «Личный кабинет»
    driver = switching_to_an_account
    assert WebDriverWait(driver, 5).until(expected_conditions.url_to_be(UrlLocators.ACCOUNT_PAGE))
    # закрыть браузер
    driver.quit()