import pytest
import allure
from tests.page_objects.main_page import MainPage
from tests.page_objects.login_page import LoginPage
from tests.page_objects.recipe_page import RecipePage
from tests.page_objects.registration_page import RegistrationPage
from tests.data import BASE_URL, RECIPE_DATA


@allure.feature('Создание рецепта')
class TestRecipe:
    """Тесты для функциональности создания рецепта"""
    
    @pytest.fixture(autouse=True)
    def setup_user_and_login(self, driver):
        """Фикстура для создания пользователя и авторизации"""
        from tests.data import get_registration_data, get_authorization_data
        
        user_data = get_registration_data()
        auth_data = get_authorization_data(user_data)
        
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
        
        login_page = LoginPage(driver)
        login_page.navigate_to(f"{BASE_URL}signin")
        login_page.wait_for_login_form()
        
        login_page.fill_login_form(
            auth_data["username"],
            auth_data["password"]
        )
        
        login_page.click_submit_button()
        login_page.accept_alert_if_present()
        login_page.wait_for_url_not_contains("signin")
        
        yield
    
    @allure.title('Создание рецепта')
    @allure.description('Авторизоваться и перейти на таб «Создать рецепт». Заполнить все поля формы создания рецепта и нажать кнопку «Создать рецепт». Проверить отображение карточки созданного рецепта и название, которое заполняли при создании.')
    def test_create_recipe(self, driver):
        """Тест создания рецепта"""
        main_page = MainPage(driver)
        main_page.navigate_to(BASE_URL)
        main_page.click_create_recipe_tab()
        
        recipe_page = RecipePage(driver)
        recipe_page.wait_for_recipe_form()
        
        image_path = recipe_page.get_file_path(RECIPE_DATA["image_path"])
        
        recipe_page.fill_recipe_form(
            RECIPE_DATA["name"],
            RECIPE_DATA["description"],
            image_path,
            RECIPE_DATA["ingredient"]
        )
        
        recipe_page.enable_submit_button()
        recipe_page.click_submit_button()
        recipe_page.accept_alert_if_present()
        recipe_page.wait_for_url_not_contains("create", timeout=10)
        
        assert recipe_page.is_recipe_card_visible(), \
            "Карточка созданного рецепта не отображается"
        
        recipe_name = recipe_page.get_recipe_name()
        assert RECIPE_DATA["name"] in recipe_name, \
            f"Название рецепта не совпадает. Ожидалось: {RECIPE_DATA['name']}, получено: {recipe_name}"

