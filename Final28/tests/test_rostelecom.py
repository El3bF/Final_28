from pages.main_page import MainPage
from settings import *
from time import sleep


#  1) Заголовок "Авторизация" отображен на странице
def test_autorization_is_visible(driver):
    main_page = MainPage(driver)
    autorization = main_page.is_visible(MainPage.AUTORIZATION)
    assert autorization == True


#   2) Кнопка "Логин" кликабельна и по ее нажатию открывается форма авторизации с полем "Логин"
def test_login_is_clicable(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.LOGIN)
    login_button = main_page.is_visible(MainPage.USERNAME)
    assert login_button == True


#    3) Проверка позитивного сценария авторизации по почте
def test_valid_data_mail(driver):
    main_page = MainPage(driver)
    main_page.input_data(MainPage.USERNAME, valid_email)
    main_page.input_data(MainPage.PASSWORD, valid_password)
    sleep(10)  # чтобы ввести на случай необходимости вручную капчу
    main_page.find_element_and_click(MainPage.BUTTON)
    element = main_page.is_visible(MainPage.BUTTON_LOGOUT)
    assert element == True


#    4) Авторизация по валидной почте и невалидному паролю (негативный сценарий авторизации)
def test_invalid_pass_mail(driver):
    main_page = MainPage(driver)
    main_page.input_data(MainPage.USERNAME, valid_email)
    main_page.input_data(MainPage.PASSWORD, invalid_password)
    main_page.find_element_and_click(MainPage.BUTTON)
    error_button = main_page.is_visible(MainPage.ERROR)
    assert error_button == True


#    5) Авторизация по невалидной почте и валидному паролю (негативный сценарий авторизации)
def test_invalid_email(driver):
    main_page = MainPage(driver)
    main_page.input_data(MainPage.USERNAME, invalid_email)
    main_page.input_data(MainPage.PASSWORD, valid_password)
    main_page.find_element_and_click(MainPage.BUTTON)
    error_button = main_page.is_visible(MainPage.ERROR)
    assert error_button == True


#    6) Авторизация по невалидной почте и невалидному паролю (негативный сценарий авторизации)
def test_invalid_data(driver):
    main_page = MainPage(driver)
    main_page.input_data(MainPage.USERNAME, invalid_email)
    main_page.input_data(MainPage.PASSWORD, invalid_password)
    main_page.find_element_and_click(MainPage.BUTTON)
    error_button = main_page.is_visible(MainPage.ERROR)
    assert error_button == True


#    7) Кнопка "Зарегистрироваться" кликабельна и открывает форму "Регистрация"
def test_check_in(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    check = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert check == BaseUrl.CHECK_IN


#  8) Заполнение формы "Регистрация" и проверка кликабельности кнопки "Зарегистрироваться" (позитивный сценарий)
def test_check_in_and_registration(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME, name)
    main_page.input_data(MainPage.SURNAME, surname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL, email)
    main_page.input_data(MainPage.PASS, password)
    main_page.input_data(MainPage.PASS_CONFIRM, password)
    main_page.find_element_and_click(MainPage.BUTTON_REGIS)
    regist = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert regist == BaseUrl.CONFIRM_EMAIL


#    9) Заполнение формы "Регистрация" с невалидным мобильным телефоном (на 3 цифры больше, негативный сценарий)
def test_check_in_with_invalid_mobile(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME, name)
    main_page.input_data(MainPage.SURNAME, surname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL, invalid_mobile)
    main_page.input_data(MainPage.PASS, password)
    main_page.input_data(MainPage.PASS_CONFIRM, password)
    main_page.find_element_and_click(MainPage.BUTTON_REGIS)
    invalid_regist = main_page.get_text_of_element(MainPage.ERROR_MESSAGE)
    assert invalid_regist == BaseUrl.EMAIL_INVALID


#    10) Заполнение формы "Регистрация" с невалидным именем (менее 2 символов, негативный сценарий)
def test_check_in_with_invalid_name(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME, invalid_name)
    main_page.input_data(MainPage.SURNAME, surname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL, email)
    main_page.input_data(MainPage.PASS, password)
    main_page.input_data(MainPage.PASS_CONFIRM, password)
    main_page.find_element_and_click(MainPage.BUTTON_REGIS)
    invalid_regist_name = main_page.get_text_of_element(MainPage.ERROR_MESSAGE_NAME)
    assert invalid_regist_name == BaseUrl.NAME_INVALID


#    11) Заполнение формы "Регистрация" с валидным именем (2 символа кириллицей, позитивный сценарий)
def test_check_in_with_valid_name(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME, valid_name)
    main_page.input_data(MainPage.SURNAME, surname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL, email)
    main_page.input_data(MainPage.PASS, password)
    main_page.input_data(MainPage.PASS_CONFIRM, password)
    main_page.find_element_and_click(MainPage.BUTTON_REGIS)
    valid_regist_name = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert valid_regist_name == BaseUrl.CONFIRM_EMAIL


#    12) Заполнение формы "Регистрация" с валидным именем (30 символов кириллицей, позитивный сценарий)
def test_check_with_valid_name(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME, valid_name_max)
    main_page.input_data(MainPage.SURNAME, surname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL, email)
    main_page.input_data(MainPage.PASS, password)
    main_page.input_data(MainPage.PASS_CONFIRM, password)
    main_page.find_element_and_click(MainPage.BUTTON_REGIS)
    valid_regist_name = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert valid_regist_name == BaseUrl.CONFIRM_EMAIL


#    13) Заполнение формы "Регистрация" с валидным именем (31 символ кириллицей, негативный сценарий)
def test_check_with_invalid_name(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME, thirty_one_letters_name)
    main_page.input_data(MainPage.SURNAME, surname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL, email)
    main_page.input_data(MainPage.PASS, password)
    main_page.input_data(MainPage.PASS_CONFIRM, password)
    main_page.find_element_and_click(MainPage.BUTTON_REGIS)
    invalid_reg = main_page.get_text_of_element(MainPage.ERROR_MESSAGE_NAME)
    assert invalid_reg == BaseUrl.NAME_INVALID


#    14) Кнопка "Забыл пароль" кликабельна и открывает форму "Восстановление пароля"
def test_forgot_passwort(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.FORGOT_PASSWORD)
    fog_passw = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert fog_passw == BaseUrl.FOG_PASSWORD


#    15) Кнопка "VK" кликабельна, и открывает форму для регистрации через аккаунт ВКонтакте
def test_vk_is_available(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.VK)
    vk_avail = main_page.get_text_of_element(MainPage.LABLE_VK)
    assert vk_avail == BaseUrl.ENTRY_VK


#   16) Кнопка "ОК" кликабельна, и открывает форму для регистранции через аккаунт "Одноклассники"
def test_ok_is_available(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click((MainPage.OK))
    ok_avail = main_page.get_text_of_element(MainPage.LABLE_OK)
    assert ok_avail == BaseUrl.OK

###
### python -m pytest -v --driver Chrome --driver-path chromedriver.exe test_SF_RT.py
###

from time import sleep
from base_data import *
from settings import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


### тест RT-001 - общий вид формы (сохранить скриншот)
def test_001_vision(selenium):
    form = AuthForm(selenium)
    form.driver.save_screenshot('screen_003.jpg')


### тест RT-003 - проверка, что по-умолчанию выбрана форма авторизации по телефону
def test_003_by_phone(selenium):
    form = AuthForm(selenium)

    assert form.placeholder.text == 'Мобильный телефон'


### тест RT-004 - проверка автосмены "таб ввода"
def test_004_change_placeholder(selenium):
    form = AuthForm(selenium)

    # ввод телефона
    form.username.send_keys('+79037507041')
    form.password.send_keys('_')
    sleep(5)

    assert form.placeholder.text == 'Мобильный телефон'

    # очистка поля логина
    form.username.send_keys(Keys.CONTROL, 'a')
    form.username.send_keys(Keys.DELETE)

    # ввод почты
    form.username.send_keys('iqooks50@gmail.com')
    form.password.send_keys('_')
    sleep(5)

    assert form.placeholder.text == 'Электронная почта'

    # очистка поля логина
    form.username.send_keys(Keys.CONTROL, 'a')
    form.username.send_keys(Keys.DELETE)

    # ввод логина
    form.username.send_keys('MyLogin')
    form.password.send_keys('_')
    sleep(5)

    assert form.placeholder.text == 'Логин'


### тест RT-005 - проверка позитивного сценария авторизации по телефону
def test_005_positive_by_phone(selenium):
    form = AuthForm(selenium)

    # ввод телефона
    form.username.send_keys(valid_phone)
    form.password.send_keys(valid_pass)
    sleep(5)
    form.btn_click()

    assert form.get_current_url() != '/account_b2c/page'


### тест RT-006 - проверка негативного сценария авторизации по телефону
def test_006_negative_by_phone(selenium):
    form = AuthForm(selenium)

    # ввод телефона
    form.username.send_keys('+1234567890')
    form.password.send_keys('any_password')
    sleep(5)
    form.btn_click()

    err_mess = form.driver.find_element(By.ID, 'form-error-message')
    assert err_mess.text == 'Неверный логин или пароль'


### тест RT-007 - проверка позитивного сценария авторизации по почте
def test_007_positive_by_email(selenium):
    form = AuthForm(selenium)

    # ввод почты
    form.username.send_keys(valid_email)
    form.password.send_keys(valid_pass)
    sleep(5)
    form.btn_click()

    assert form.get_current_url() != '/account_b2c/page'


### тест RT-008 - проверка негативного сценария авторизации по почте
def test_008_negative_by_email(selenium):
    form = AuthForm(selenium)

    # ввод почты
    form.username.send_keys('aa@aa.aa')
    form.password.send_keys('any_password')
    sleep(5)
    form.btn_click()

    err_mess = form.driver.find_element(By.ID, 'form-error-message')
    assert err_mess.text == 'Неверный логин или пароль'


### тест RT-015 - проверка получения временного кода на телефон и открытия формы для ввода кода
def test_015_get_code(selenium):
    form = CodeForm(selenium)

    # ввод телефона
    form.address.send_keys(valid_phone)

    # длительная пауза предназначена для ручного ввода капчи при необходимости
    sleep(30)
    form.get_click()

    rt_code = form.driver.find_element(By.ID, 'rt-code-0')

    assert rt_code


### тест RT-019 - проверка перехода в форму восстановления пароля и её открытия
def test_019_forgot_pass(selenium):
    form = AuthForm(selenium)

    # клик по надписи "Забыл пароль"
    form.forgot.click()
    sleep(5)

    reset_pass = form.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    assert reset_pass.text == 'Восстановление пароля'


### тест RT-039 - проверка перехода в форму регистрации и её открытия
def test_039_register(selenium):
    form = AuthForm(selenium)

    # клик по надписи "Зарегистрироваться"
    form.register.click()
    sleep(5)

    reset_pass = form.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    assert reset_pass.text == 'Регистрация'


### тест RT-041 - проверка открытия пользовательского соглашения
def test_041_agreement(selenium):
    form = AuthForm(selenium)

    original_window = form.driver.current_window_handle
    # клик по надписи "Пользовательским соглашением" в подвале страницы
    form.agree.click()
    sleep(5)
    WebDriverWait(form.driver, 5).until(EC.number_of_windows_to_be(2))
    for window_handle in form.driver.window_handles:
        if window_handle != original_window:
            form.driver.switch_to.window(window_handle)
            break
    win_title = form.driver.execute_script("return window.document.title")

    assert win_title == 'User agreement'


### тест RT-043 - проверка перехода по ссылке авторизации пользователя через вконтакте
def test_043_auth_vk(selenium):
    form = AuthForm(selenium)
    form.vk_btn.click()
    sleep(5)

    assert form.get_base_url() == 'oauth.vk.com'


### тест RT-044 - проверка перехода по ссылке авторизации пользователя через одноклассники
def test_044_auth_ok(selenium):
    form = AuthForm(selenium)
    form.ok_btn.click()
    sleep(5)

    assert form.get_base_url() == 'connect.ok.ru'


### тест RT-045 - проверка перехода по ссылке авторизации пользователя через майлру
def test_045_auth_mailru(selenium):
    form = AuthForm(selenium)
    form.mailru_btn.click()
    sleep(5)

    assert form.get_base_url() == 'connect.mail.ru'


### тест RT-046 - проверка перехода по ссылке авторизации пользователя через google
def test_046_auth_google(selenium):
    form = AuthForm(selenium)
    form.google_btn.click()
    sleep(5)

    assert form.get_base_url() == 'accounts.google.com'


### тест RT-047 - проверка перехода по ссылке авторизации пользователя через яндекс
def test_047_auth_ya(selenium):
    form = AuthForm(selenium)
    form.ya_btn.click()
    sleep(5)

    assert form.get_base_url() == 'passport.yandex.ru'












