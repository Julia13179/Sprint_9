from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
from pathlib import Path
import os


class BasePage:
    """Базовый класс для Page Object"""
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        # Увеличиваем таймаут для CI окружения (GitHub Actions)
        timeout = 20 if os.getenv('CI') else 10
        self.wait = WebDriverWait(driver, timeout)
    
    def find_element(self, locator: tuple):
        """Поиск элемента с ожиданием"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator: tuple):
        """Поиск элементов с ожиданием"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click_element(self, locator: tuple):
        """Клик по элементу с ожиданием кликабельности"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        self._handle_alert()
    
    def send_keys(self, locator: tuple, text: str):
        """Ввод текста в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator: tuple) -> str:
        """Получение текста элемента"""
        element = self.find_element(locator)
        return element.text
    
    def is_element_visible(self, locator: tuple) -> bool:
        """Проверка видимости элемента"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def wait_for_element(self, locator: tuple, timeout: int = 10):
        """Ожидание появления элемента"""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located(locator))
    
    def get_file_path(self, filename: str) -> str:
        """Получение абсолютного пути к файлу"""
        app_dir = Path(__file__).parent.parent.parent
        file_path = app_dir / filename
        return str(file_path.absolute())
    
    def _handle_alert(self):
        """Обработка alert'ов"""
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass
        except Exception:
            pass
    
    def navigate_to(self, url: str):
        """Переход на URL"""
        self.driver.get(url)
    
    def get_current_url(self) -> str:
        """Получение текущего URL"""
        return self.driver.current_url
    
    def wait_for_url_change(self, timeout: int = 10):
        """Ожидание изменения URL"""
        initial_url = self.driver.current_url
        self.wait.until(lambda d: d.current_url != initial_url)
    
    def wait_for_url_contains(self, text: str, timeout: int = 10):
        """Ожидание, что URL содержит текст"""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda d: text in d.current_url)
    
    def wait_for_url_not_contains(self, text: str, timeout: int = 10):
        """Ожидание, что URL не содержит текст"""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda d: text not in d.current_url)
    
    def execute_script(self, script: str, *args):
        """Выполнение JavaScript"""
        return self.driver.execute_script(script, *args)
    
    def find_elements_by_xpath(self, xpath: str):
        """Поиск элементов по XPath (для внутреннего использования в page objects)"""
        return self.driver.find_elements(By.XPATH, xpath)
    
    def accept_alert_if_present(self):
        """Принимает alert, если он присутствует"""
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            return True
        except NoAlertPresentException:
            return False
        except Exception:
            return False
    
    def wait_for_element(self, locator: tuple, timeout: int = 10):
        """Ожидание появления элемента"""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located(locator))

