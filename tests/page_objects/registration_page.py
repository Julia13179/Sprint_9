from tests.page_objects.base_page import BasePage
from tests.locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    """Page Object для страницы регистрации"""
    
    # Локаторы
    FIRST_NAME_INPUT = RegistrationPageLocators.FIRST_NAME_INPUT
    LAST_NAME_INPUT = RegistrationPageLocators.LAST_NAME_INPUT
    USERNAME_INPUT = RegistrationPageLocators.USERNAME_INPUT
    EMAIL_INPUT = RegistrationPageLocators.EMAIL_INPUT
    PASSWORD_INPUT = RegistrationPageLocators.PASSWORD_INPUT
    SUBMIT_BUTTON = RegistrationPageLocators.SUBMIT_BUTTON
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def fill_registration_form(self, first_name: str, last_name: str, username: str, email: str, password: str):
        """Заполнение формы регистрации"""
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)
    
    def click_submit_button(self):
        """Клик по кнопке создания аккаунта"""
        self.click_element(self.SUBMIT_BUTTON)
    
    def wait_for_registration_form(self):
        """Ожидание загрузки формы регистрации"""
        self.wait_for_element(self.FIRST_NAME_INPUT)

