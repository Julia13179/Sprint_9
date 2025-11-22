from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.page_objects.base_page import BasePage
from tests.locators import RecipePageLocators


class RecipePage(BasePage):
    """Page Object для страницы создания рецепта"""
    
    # Локаторы
    NAME_INPUT = RecipePageLocators.NAME_INPUT
    COOKING_TIME_INPUT = RecipePageLocators.COOKING_TIME_INPUT
    SERVINGS_INPUT = RecipePageLocators.SERVINGS_INPUT
    DESCRIPTION_INPUT = RecipePageLocators.DESCRIPTION_INPUT
    IMAGE_INPUT = RecipePageLocators.IMAGE_INPUT
    INGREDIENT_INPUT = RecipePageLocators.INGREDIENT_INPUT
    INGREDIENT_DROPDOWN_ITEM = RecipePageLocators.INGREDIENT_DROPDOWN_ITEM
    SUBMIT_BUTTON = RecipePageLocators.SUBMIT_BUTTON
    RECIPE_CARD = RecipePageLocators.RECIPE_CARD
    RECIPE_NAME = RecipePageLocators.RECIPE_NAME
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def fill_recipe_form(self, name: str, description: str, image_path: str, ingredient: str):
        """Заполнение формы создания рецепта"""
        from selenium.webdriver.common.keys import Keys
        
        # Заполняем название (первое текстовое поле)
        name_input = self.find_element(self.NAME_INPUT)
        name_input.clear()
        name_input.send_keys(name)
        
        # Находим все текстовые поля формы после заполнения названия
        text_inputs = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//form//input[@type='text']")))
        
        # Заполняем время приготовления (второе поле)
        text_inputs[1].clear()
        text_inputs[1].send_keys("30")
        
        # Заполняем количество порций (третье поле)
        text_inputs[2].clear()
        text_inputs[2].send_keys("4")
        
        # Заполняем описание
        description_input = self.find_element(self.DESCRIPTION_INPUT)
        description_input.clear()
        description_input.send_keys(description)
        
        # Загружаем изображение
        image_input = self.find_element(self.IMAGE_INPUT)
        image_input.send_keys(image_path)
        
        # Заполняем ингредиент (четвертое текстовое поле)
        ingredient_input = text_inputs[3]
        
        ingredient_input.click()
        ingredient_input.clear()
        ingredient_input.send_keys(ingredient[:3])
        
        ingredient_input.send_keys(Keys.ARROW_DOWN)
        ingredient_input.send_keys(Keys.ENTER)
    
    def is_submit_button_enabled(self) -> bool:
        """Проверка активности кнопки создания рецепта"""
        submit_btn = self.find_element(self.SUBMIT_BUTTON)
        return submit_btn.is_enabled()
    
    def enable_submit_button(self):
        """Принудительная активация кнопки через JavaScript"""
        submit_btn = self.find_element(self.SUBMIT_BUTTON)
        self.execute_script("arguments[0].removeAttribute('disabled');", submit_btn)
    
    def click_submit_button(self):
        """Клик по кнопке создания рецепта"""
        self.click_element(self.SUBMIT_BUTTON)
    
    def is_recipe_card_visible(self) -> bool:
        """Проверка видимости карточки рецепта"""
        return self.is_element_visible(self.RECIPE_CARD)
    
    def get_recipe_name(self) -> str:
        """Получение названия рецепта"""
        return self.get_text(self.RECIPE_NAME)
    
    def wait_for_recipe_form(self):
        """Ожидание загрузки формы создания рецепта"""
        self.wait_for_element(self.NAME_INPUT)

