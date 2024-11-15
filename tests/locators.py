"""Локаторы элементов для тестов"""
from selenium.webdriver.common.by import By


# Локаторы главной страницы
class MainPageLocators:
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(text(), 'Создать аккаунт')]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(text(), 'Выход')]")  # Это ссылка, а не кнопка
    CREATE_RECIPE_TAB = (By.XPATH, "//a[contains(text(), 'Создать рецепт')]")


# Локаторы страницы регистрации
class RegistrationPageLocators:
    FIRST_NAME_INPUT = (By.XPATH, "//input[@name='first_name']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@name='last_name']")
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")


# Локаторы страницы авторизации
class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    LOGIN_FORM = (By.XPATH, "//form")


# Локаторы страницы создания рецепта
class RecipePageLocators:
    # Поля не имеют name/id, используем порядок в форме
    NAME_INPUT = (By.XPATH, "//form//input[@type='text'][1]")  # Первое текстовое поле - название
    COOKING_TIME_INPUT = (By.XPATH, "//form//input[@type='text'][2]")  # Второе поле - время приготовления
    SERVINGS_INPUT = (By.XPATH, "//form//input[@type='text'][3]")  # Третье поле - количество порций
    DESCRIPTION_INPUT = (By.XPATH, "//form//textarea[1]")  # Первое textarea - описание
    IMAGE_INPUT = (By.XPATH, "//form//input[@type='file']")  # Поле загрузки файла
    INGREDIENT_INPUT = (By.XPATH, "//form//input[@type='text'][4]")  # Четвертое поле - ингредиент
    INGREDIENT_DROPDOWN_ITEM = (By.XPATH, "//*[contains(text(), 'булка') and (self::div or self::li or self::span or self::a) and contains(@class, 'ingredient')]")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать рецепт')]")
    RECIPE_CARD = (By.XPATH, "//div[contains(@class, 'recipe')] | //article | //div[contains(@class, 'card')]")
    RECIPE_NAME = (By.XPATH, "//div[contains(@class, 'recipe')]//h2 | //div[contains(@class, 'recipe')]//h1 | //article//h2 | //article//h1")

