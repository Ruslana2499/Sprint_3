from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_locators import ElementsLocators, UrlLocators


def test_login_account_using_login_to_account_button(create_driver_instance): #вход по кнопке «Войти в аккаунт» на главной
    driver = create_driver_instance
    driver.get(UrlLocators.HOME_PAGE)
    account_link = driver.find_element(*ElementsLocators.INDEX_PAGE_LOGIN_ACCOUNT_BUTTON)
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(account_link))
    account_link.click()
    driver.find_element(*ElementsLocators.LOGIN_FORM_INPUT_EMAIL).send_keys('ruslanamanbatchurina05098@yandex.ru')
    driver.find_element(*ElementsLocators.LOGIN_FORM_INPUT_PASSWORD).send_keys('12345!2"№324')
    button =driver.find_element(*ElementsLocators.FORM_SUBMIT_BUTTON)
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(button))
    button.click()
    assert WebDriverWait(driver, 15).until(expected_conditions.url_to_be(UrlLocators.HOME_PAGE))
    # закрыть браузер
    driver.quit()


def test_login_account_using_button_in_the_password_recovery_form(create_driver_instance): # тест вход через кнопку в форме восстановления пароля
    driver = create_driver_instance
    driver.get(UrlLocators.REMIND_PASSWORD_PAGE)
    driver.find_element(*ElementsLocators.FORM_LOGIN_LINK).click()
    driver.find_element(*ElementsLocators.LOGIN_FORM_INPUT_EMAIL).send_keys('ruslanamanbatchurina05098@yandex.ru')
    driver.find_element(*ElementsLocators.LOGIN_FORM_INPUT_PASSWORD).send_keys('12345!2"№324')
    driver.find_element(*ElementsLocators.FORM_SUBMIT_BUTTON).click()
    assert WebDriverWait(driver, 5).until(expected_conditions.url_to_be(UrlLocators.HOME_PAGE))
    # закрыть браузер
    driver.quit()


def test_login_account_using_Personal_Account_button(create_driver_instance): # тест вход через кнопку «Личный кабинет»
    driver = create_driver_instance
    driver.get(UrlLocators.HOME_PAGE)
    account_link = driver.find_element(*ElementsLocators.INDEX_PAGE_ACCOUNT_LINK)
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(account_link))
    account_link.click()
    driver.find_element(*ElementsLocators.LOGIN_FORM_INPUT_EMAIL).send_keys('ruslanamanbatchurina05098@yandex.ru')
    driver.find_element(*ElementsLocators.LOGIN_FORM_INPUT_PASSWORD).send_keys('12345!2"№324')
    driver.find_element(*ElementsLocators.FORM_SUBMIT_BUTTON).click()
    assert WebDriverWait(driver, 5).until(expected_conditions.url_to_be(UrlLocators.HOME_PAGE))
    # закрыть браузер
    driver.quit()


def test_login_account_using_button_in_registration_form(create_driver_instance): # вход через кнопку в форме регистрации
    driver = create_driver_instance
    driver.get(UrlLocators.REGISTRATION_PAGE)
    driver.find_element(*ElementsLocators.FORM_LOGIN_LINK).click()
    driver.find_element(*ElementsLocators.LOGIN_FORM_INPUT_EMAIL).send_keys('ruslanamanbatchurina05098@yandex.ru')
    driver.find_element(*ElementsLocators.LOGIN_FORM_INPUT_PASSWORD).send_keys('12345!2"№324')
    driver.find_element(*ElementsLocators.FORM_SUBMIT_BUTTON).click()
    assert WebDriverWait(driver, 5).until(expected_conditions.url_to_be(UrlLocators.HOME_PAGE))
    # закрыть браузер
    driver.quit()


