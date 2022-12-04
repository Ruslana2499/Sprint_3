import pytest as pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# импортировали пакет Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from test_locators import ElementsLocators, UrlLocators


@pytest.fixture
def create_driver_instance():
    driver = webdriver.Chrome()
    # полноэкранный режим
    driver.maximize_window()
    return driver


@pytest.fixture
def open_registration_form(create_driver_instance):
    # открыть страницу
    driver = create_driver_instance
    driver.get(UrlLocators.HOME_PAGE)

    # Найди элемент и кликнуть по нему
    account_link = driver.find_element(*ElementsLocators.INDEX_PAGE_ACCOUNT_LINK)
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(account_link))
    account_link.click()
    registration_link = driver.find_element(*ElementsLocators.LOGIN_FORM_REGISTRATION_LINK)
    registration_link.click()
    #Найти поля имя, email, пароль
    input_name = driver.find_element(*ElementsLocators.REGISTRATION_FORM_INPUT_NAME)
    input_email = driver.find_element(*ElementsLocators.REGISTRATION_FORM_INPUT_EMAIL)
    input_password = driver.find_element(*ElementsLocators.REGISTRATION_FORM_INPUT_PASSWORD)
    # Найди элемент
    submit_button = driver.find_element(*ElementsLocators.FORM_SUBMIT_BUTTON)
    return {
        'driver': driver,
        'input_name': input_name,
        'input_email': input_email,
        'input_password': input_password,
        'submit_button': submit_button
    }


@pytest.fixture
def switching_to_an_account(create_driver_instance):
    # открыть страницу
    driver = create_driver_instance
    driver.get(UrlLocators.HOME_PAGE)
    # Найди элемент и кликнуть по нему
    account_link = driver.find_element(*ElementsLocators.INDEX_PAGE_ACCOUNT_LINK)
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(account_link))
    account_link.click()
    # Найти поля email, пароль
    driver.find_element(*ElementsLocators.LOGIN_FORM_INPUT_EMAIL).send_keys('ruslanamanbatchurina05098@yandex.ru')
    driver.find_element(*ElementsLocators.LOGIN_FORM_INPUT_PASSWORD).send_keys('12345!2"№324')
    driver.find_element(*ElementsLocators.FORM_SUBMIT_BUTTON).click()
    account_link = driver.find_element(*ElementsLocators.INDEX_PAGE_ACCOUNT_LINK)
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(account_link))
    account_link.click()
    WebDriverWait(driver, 15).until(expected_conditions.url_to_be(UrlLocators.ACCOUNT_PAGE))
    return driver
