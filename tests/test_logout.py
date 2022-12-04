from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_locators import ElementsLocators, UrlLocators


def test_successful_registration(switching_to_an_account): #тест выход из аккаунта
    driver = switching_to_an_account
    driver.find_element(*ElementsLocators.ACCOUNT_PAGE_LOGOUT_BUTTON).click()
    assert WebDriverWait(driver, 5).until(expected_conditions.url_to_be(UrlLocators.LOGIN_PAGE))
    # закрыть браузер
    driver.quit()