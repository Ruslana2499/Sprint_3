from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
from test_locators import ElementsLocators, UrlLocators


def test_successful_registration(open_registration_form): #тест успешной регистрации
    random_number = random.randrange(0, 999)
    if random_number < 10:
        random_number = '00' + str(random_number)
    elif random_number < 100:
        random_number = '0' + str(random_number)
    driver = open_registration_form['driver']
    open_registration_form['input_name'].send_keys('РусланаHeckfyf')
    open_registration_form['input_email'].send_keys('ruslanamanbatchurina05' + str(random_number) + '@yandex.ru')
    open_registration_form['input_password'].send_keys('12345!2"№324')
    open_registration_form['submit_button'].click()
    assert WebDriverWait(driver, 5).until(expected_conditions.url_to_be(UrlLocators.LOGIN_PAGE))
    # закрыть браузер
    driver.quit()


def test_password_two_characters_entered(open_registration_form): #тест ошибки для некорректного пароля
    driver = open_registration_form['driver']
    open_registration_form['input_name'].send_keys('Кусьло')
    open_registration_form['input_email'].send_keys('123@ya.ru')
    open_registration_form['input_password'].send_keys('12')
    open_registration_form['submit_button'].click()
    error_block = driver.find_element(*ElementsLocators.REGISTRATION_FORM_INPUT_ERROR)
    assert error_block.text == 'Некорректный пароль'
    # закрыть браузер
    driver.quit()


