from tests.page_objects.base_page import BasePage
from tests.locators import LoginPageLocators


class LoginPage(BasePage):
    """Page Object для страницы авторизации"""
    
    # Локаторы
    EMAIL_INPUT = LoginPageLocators.EMAIL_INPUT
    PASSWORD_INPUT = LoginPageLocators.PASSWORD_INPUT
    SUBMIT_BUTTON = LoginPageLocators.SUBMIT_BUTTON
    LOGIN_FORM = LoginPageLocators.LOGIN_FORM
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def fill_login_form(self, username: str, password: str):
        """Заполнение формы авторизации"""
        self.send_keys(self.EMAIL_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
    
    def click_submit_button(self):
        """Клик по кнопке входа"""
        self.click_element(self.SUBMIT_BUTTON)
    
    def is_login_form_visible(self) -> bool:
        """Проверка видимости формы авторизации"""
        return self.is_element_visible(self.LOGIN_FORM)
    
    def is_login_page(self) -> bool:
        """Проверка что находимся на странице авторизации"""
        current_url = self.get_current_url()
        return "/signin" in current_url or "/login" in current_url
    
    def wait_for_login_form(self):
        """Ожидание загрузки формы авторизации"""
        self.wait_for_element(self.EMAIL_INPUT)

