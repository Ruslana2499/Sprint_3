from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_locators import UrlLocators, ElementsLocators


def test_test_go_to_sauces_section(create_driver_instance):#тест клик по «Соусы»
    driver = create_driver_instance
    driver.get(UrlLocators.HOME_PAGE)
    sauces_tab_button = driver.find_element(*ElementsLocators.CONSTRUCTOR_SECTION_SAUCES)
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(sauces_tab_button))
    sauces_tab_button.click()
    assert 'tab_tab_type_current__' in sauces_tab_button.get_attribute('class')
    # закрыть браузер
    driver.quit()


def test_test_go_to_buns_section(create_driver_instance):#тест клик по «Булки»
    driver = create_driver_instance
    driver.get(UrlLocators.HOME_PAGE)
    sauces_tab_button = driver.find_element(*ElementsLocators.CONSTRUCTOR_SECTION_SAUCES)
    sauces_tab_button.click()
    buns_tab_button = driver.find_element(*ElementsLocators.CONSTRUCTOR_SECTION_BUNS)
    buns_tab_button.click()
    assert 'tab_tab_type_current__' in buns_tab_button.get_attribute('class')
    # закрыть браузер
    driver.quit()


def test_test_go_to_fillings_section(create_driver_instance):#тест клик по «Начинки»
    driver = create_driver_instance
    driver.get(UrlLocators.HOME_PAGE)
    fillings_tab_button = driver.find_element(*ElementsLocators.CONSTRUCTOR_SECTION_FILLINGS)
    fillings_tab_button.click()
    assert 'tab_tab_type_current__' in fillings_tab_button.get_attribute('class')
    # закрыть браузер
    driver.quit()