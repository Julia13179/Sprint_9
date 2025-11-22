"""Тестовые данные для тестов"""
import random
import string

BASE_URL = "https://foodgram-frontend-1.prakticum-team.ru/"

def generate_random_string(length=12):
    """Генерация случайной строки"""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def generate_random_email():
    """Генерация случайного email для тестов"""
    random_string = generate_random_string(12)
    return f"test_user_{random_string}@example.com"

def generate_test_data():
    """Генерация уникальных тестовых данных"""
    random_string = generate_random_string(12)
    email = generate_random_email()
    return {
        "first_name": "Тестовый",
        "last_name": "Пользователь",
        "username": f"test_user_{random_string}",
        "email": email,
        "password": "TestPassword123"
    }

def get_registration_data():
    """Получить уникальные данные для регистрации (генерирует новые каждый раз)"""
    return generate_test_data()

def get_authorization_data(registration_data):
    """Получить данные для авторизации на основе данных регистрации"""
    return {
        "username": registration_data["username"],
        "password": registration_data["password"]
    }

# Для обратной совместимости - генерируем данные один раз
_registration_data = generate_test_data()
REGISTRATION_DATA = _registration_data.copy()
AUTHORIZATION_DATA = {
    "username": REGISTRATION_DATA["username"],
    "password": REGISTRATION_DATA["password"]
}

# Данные для создания рецепта
RECIPE_DATA = {
    "name": "Тестовый рецепт",
    "description": "Описание тестового рецепта",
    "image_path": "assets/test_image.jpg",
    "ingredient": "булка"
}

