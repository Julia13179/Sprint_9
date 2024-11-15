from tests.page_objects.base_page import BasePage
from tests.locators import MainPageLocators


class MainPage(BasePage):
    """Page Object для главной страницы"""
    
    # Локаторы
    CREATE_ACCOUNT_BUTTON = MainPageLocators.CREATE_ACCOUNT_BUTTON
    LOGIN_BUTTON = MainPageLocators.LOGIN_BUTTON
    LOGOUT_BUTTON = MainPageLocators.LOGOUT_BUTTON
    CREATE_RECIPE_TAB = MainPageLocators.CREATE_RECIPE_TAB
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_create_account_button(self):
        """Клик по кнопке создания аккаунта"""
        self.click_element(self.CREATE_ACCOUNT_BUTTON)
    
    def click_login_button(self):
        """Клик по кнопке входа"""
        self.click_element(self.LOGIN_BUTTON)
    
    def is_logout_button_visible(self) -> bool:
        """Проверка видимости кнопки выхода"""
        return self.is_element_visible(self.LOGOUT_BUTTON)
    
    def click_create_recipe_tab(self):
        """Клик по табу создания рецепта"""
        self.click_element(self.CREATE_RECIPE_TAB)
    
    def is_main_page(self) -> bool:
        """Проверка что находимся на главной странице"""
        from tests.data import BASE_URL
        current_url = self.get_current_url()
        return BASE_URL in current_url or current_url.endswith("/")

