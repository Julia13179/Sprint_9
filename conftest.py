import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
import os


@pytest.fixture(scope='function')
def driver():
    """Фикстура для создания драйвера"""
    selenoid_url = os.getenv('SELENOID_URL')
    
    options = Options()
    options.unhandled_prompt_behavior = 'accept'  # Автоматически принимать alert'ы
    
    if selenoid_url:
        # Используем Selenoid
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "128.0")
        options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableVideo": False
        })
        driver = webdriver.Remote(
            command_executor=selenoid_url,
            options=options
        )
    else:
        # Локальный запуск для разработки
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        service = Service()
        driver = webdriver.Chrome(service=service, options=options)
    
    driver.maximize_window()
    yield driver
    driver.quit()

