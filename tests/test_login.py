import pytest
import allure
from tests.page_objects.main_page import MainPage
from tests.page_objects.login_page import LoginPage
from tests.page_objects.registration_page import RegistrationPage
from tests.data import BASE_URL


@allure.feature('Авторизация')
class TestLogin:
    """Тесты для функциональности авторизации"""
    
    @pytest.fixture(autouse=True)
    def setup_user(self, driver):
        """Фикстура для создания пользователя перед тестами"""
        from tests.data import get_registration_data, get_authorization_data
        
        user_data = get_registration_data()
        self.auth_data = get_authorization_data(user_data)
        
        main_page = MainPage(driver)
        main_page.navigate_to(BASE_URL)
        main_page.click_create_account_button()
        
        registration_page = RegistrationPage(driver)
        registration_page.wait_for_registration_form()
        
        registration_page.fill_registration_form(
            user_data["first_name"],
            user_data["last_name"],
            user_data["username"],
            user_data["email"],
            user_data["password"]
        )
        
        registration_page.click_submit_button()
        registration_page.accept_alert_if_present()
        registration_page.wait_for_url_contains("signin")
        
        yield
    
    @allure.title('Авторизация')
    @allure.description('Нажать кнопку «Войти», заполнить все поля формы авторизации и нажать кнопку «Войти». Проверить переход на главную страницу и отображение кнопки «Выход».')
    def test_login(self, driver):
        """Тест авторизации"""
        login_page = LoginPage(driver)
        login_page.navigate_to(f"{BASE_URL}signin")
        login_page.wait_for_login_form()
        
        login_page.fill_login_form(
            self.auth_data["username"],
            self.auth_data["password"]
        )
        
        login_page.click_submit_button()
        login_page.accept_alert_if_present()
        login_page.wait_for_url_not_contains("signin")
        
        main_page_after_login = MainPage(driver)
        assert main_page_after_login.is_logout_button_visible(), \
            "Кнопка 'Выход' не отображается после авторизации"
        assert main_page_after_login.is_main_page(), \
            "Не произошел переход на главную страницу"

