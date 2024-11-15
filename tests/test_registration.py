import pytest
import allure
from tests.page_objects.main_page import MainPage
from tests.page_objects.registration_page import RegistrationPage
from tests.page_objects.login_page import LoginPage
from tests.data import BASE_URL, REGISTRATION_DATA


@allure.feature('Регистрация')
class TestRegistration:
    """Тесты для функциональности создания аккаунта"""
    
    @allure.title('Создание аккаунта')
    @allure.description('Нажать кнопку «Создать аккаунт», заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт». Проверить переход на страницу авторизации и отображение формы авторизации.')
    def test_create_account(self, driver):
        """Тест создания аккаунта"""
        main_page = MainPage(driver)
        main_page.navigate_to(BASE_URL)
        main_page.click_create_account_button()
        
        registration_page = RegistrationPage(driver)
        registration_page.fill_registration_form(
            REGISTRATION_DATA["first_name"],
            REGISTRATION_DATA["last_name"],
            REGISTRATION_DATA["username"],
            REGISTRATION_DATA["email"],
            REGISTRATION_DATA["password"]
        )
        registration_page.click_submit_button()
        
        login_page = LoginPage(driver)
        assert login_page.is_login_form_visible(), "Форма авторизации не отображается"
        assert login_page.is_login_page(), "Не произошел переход на страницу авторизации"

