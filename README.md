# Sprint_9 - Автотесты для сервиса "Продуктовый помощник"

Проект содержит автотесты для учебного сервиса "Продуктовый помощник", написанные с использованием Selenium WebDriver, pytest и Allure.

## Структура проекта

```
Sprint_9/
├── tests/
│   ├── page_objects/      # Page Object классы
│   │   ├── __init__.py
│   │   ├── base_page.py
│   │   ├── main_page.py
│   │   ├── login_page.py
│   │   ├── registration_page.py
│   │   └── recipe_page.py
│   ├── __init__.py
│   ├── locators.py        # Локаторы элементов (вынесены для удобства)
│   ├── data.py            # Тестовые данные
│   ├── test_registration.py
│   ├── test_login.py
│   └── test_recipe.py
├── assets/                # Тестовые файлы (изображения и т.д.)
│   └── test_image.jpg
├── .github/
│   └── workflows/
│       └── ci.yml         # GitHub Actions workflow
├── conftest.py           # Конфигурация pytest и фикстуры
├── requirements.txt      # Зависимости проекта
├── pytest.ini           # Конфигурация pytest
├── Dockerfile           # Docker образ для тестов
├── docker-compose.yml   # Docker Compose конфигурация
├── browser.json        # Конфигурация браузеров для Selenoid
├── generate_allure.sh  # Скрипт для генерации Allure отчета
└── README.md           # Документация проекта
```

## Установка и запуск

### Локальный запуск

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Установите Allure (если еще не установлен):
```bash
# macOS
brew install allure

# Linux
# Следуйте инструкциям на https://docs.qameta.io/allure/
```

3. Запустите тесты:
```bash
pytest
```

4. Сгенерируйте Allure отчет:
```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

Или используйте скрипт:
```bash
./generate_allure.sh
allure open allure-report
```

### Запуск в Docker Compose

1. Убедитесь, что Docker и Docker Compose установлены

2. Запустите тесты с Selenoid:
```bash
docker-compose up --build
```

3. После завершения тестов, отчеты будут в директории `allure-results`

4. Для генерации отчета локально:
```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## Тесты

Проект содержит следующие тесты:

1. **test_registration.py** - Тесты создания аккаунта
   - Проверка создания аккаунта и перехода на страницу авторизации

2. **test_login.py** - Тесты авторизации
   - Проверка авторизации и перехода на главную страницу

3. **test_recipe.py** - Тесты создания рецепта
   - Проверка создания рецепта с загрузкой изображения и добавлением ингредиента

## Page Object Pattern

Проект использует паттерн Page Object для организации кода:
- Каждая страница имеет свой класс в `tests/page_objects/`
- Локаторы вынесены в отдельный файл `tests/locators.py` для удобства поддержки
- Базовый класс `BasePage` содержит общие методы для работы с элементами
- Тестовые данные вынесены в `tests/data.py`

## CI/CD

Проект настроен для работы с GitHub Actions. Файл `.github/workflows/ci.yml` содержит конфигурацию пайплайна, который:
- Запускает Selenoid в контейнере
- Устанавливает зависимости
- Запускает тесты
- Генерирует Allure отчет
- Сохраняет артефакты

## Требования

- Python 3.11+
- Chrome браузер (для локального запуска)
- Docker и Docker Compose (для запуска в контейнерах)
- Allure (для генерации отчетов)

## Особенности реализации

- Использование WebDriverWait для явных ожиданий
- Генерация случайного email для каждого запуска тестов
- Поддержка запуска как локально, так и через Selenoid
- Все тесты независимы друг от друга
- Тестовые данные вынесены в отдельный модуль
