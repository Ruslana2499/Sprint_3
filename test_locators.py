from selenium.webdriver.common.by import By


class ElementsLocators:
    INDEX_PAGE_LOGIN_ACCOUNT_BUTTON = By.XPATH, '//*[contains(@class, "button_button__33qZ0")]' #кнопка «Войти в аккаунт» на главной странице
    INDEX_PAGE_ACCOUNT_LINK = By.LINK_TEXT, 'Личный Кабинет' #кнопка «Личный Кабинет» на главной странице

    ACCOUNT_PAGE_LOGOUT_BUTTON = By.CLASS_NAME, "Account_button__14Yp3" #кнопка «Выйти» в личном кабинете

    LOGIN_FORM_INPUT_EMAIL = By.NAME, "name" #поле ввода email на странице «Вход»
    LOGIN_FORM_INPUT_PASSWORD = By.NAME, "Пароль" #поле ввода пароля на странице «Вход»
    LOGIN_FORM_REGISTRATION_LINK = By.LINK_TEXT, 'Зарегистрироваться' #кнопка «Зарегистрироваться» на странице «Вход»

    FORM_SUBMIT_BUTTON = By.XPATH, '//*[contains(@class, "button_button__33qZ0")]'# кнопка «Войти» на странице «Вход»
    FORM_LOGIN_LINK = By.LINK_TEXT, 'Войти' #ссылка "Войти" на страницах: «Регистрация», «Восстановление пароля»

    HEADER_CONSTRUCTOR_LINK = By.XPATH, '//*[contains(@class, "AppHeader_header__link__3D_hX")]' #ссылка Конструктор (переход на главную страницу)
    HEADER_LOGO_LINK = By.CSS_SELECTOR, '.AppHeader_header__logo__2D0X2 a' #логотип Stellar Burgers (переход на главную страницу)

    REGISTRATION_FORM_INPUT_ERROR = By.CLASS_NAME, 'input__error' #блок с ошибкой
    REGISTRATION_FORM_INPUT_EMAIL = By.CSS_SELECTOR, "fieldset + fieldset input" #поле ввода email страница «Регистрация»
    REGISTRATION_FORM_INPUT_NAME = By.NAME, "name" #поле ввода имени страница «Регистрация»
    REGISTRATION_FORM_INPUT_PASSWORD = By.NAME, "Пароль" #поле ввода пароля страница «Регистрация»

    CONSTRUCTOR_SECTION_BUNS = By.XPATH, '//*[contains(@class, "tab_tab__")][1]' # первый элемент конструктора «Булки»
    CONSTRUCTOR_SECTION_SAUCES = By.XPATH, '//*[contains(@class, "tab_tab__")][2]' #второй элемент конструктора «Соусы»
    CONSTRUCTOR_SECTION_FILLINGS = By.XPATH, '//*[contains(@class, "tab_tab__")][3]' #третий элемент конструктора «Начинки»


class UrlLocators:
    HOME_PAGE = 'https://stellarburgers.nomoreparties.site/' # главная страница
    REMIND_PASSWORD_PAGE = 'https://stellarburgers.nomoreparties.site/forgot-password' # страница "Восстановление пароля"
    REGISTRATION_PAGE = 'https://stellarburgers.nomoreparties.site/register' # страница "Регистрация"
    LOGIN_PAGE = 'https://stellarburgers.nomoreparties.site/login' # страница "Вход"
    ACCOUNT_PAGE = 'https://stellarburgers.nomoreparties.site/account/profile' # личный кабинет
