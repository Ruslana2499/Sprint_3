from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_locators import ElementsLocators, UrlLocators


def test_successful_registration(switching_to_an_account): #тест переход по клику на «Конструктор» из личного кабинета
    driver = switching_to_an_account
    driver.find_element(*ElementsLocators.HEADER_CONSTRUCTOR_LINK).click()
    assert WebDriverWait(driver, 5).until(expected_conditions.url_to_be(UrlLocators.HOME_PAGE))
    # закрыть браузер
    driver.quit()


def test_successful_registration(switching_to_an_account): #тест переход по клику на логотип Stellar Burgers из личного кабинета
    driver = switching_to_an_account
    driver.find_element(*ElementsLocators.HEADER_LOGO_LINK).click()
    assert WebDriverWait(driver, 5).until(expected_conditions.url_to_be(UrlLocators.HOME_PAGE))
    # закрыть браузер
    driver.quit()