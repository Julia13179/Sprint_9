# Инструкция по генерации Allure отчета

## Способ 1: Установка Allure CLI (рекомендуется)

### macOS:
```bash
brew install allure
```

### Linux:
```bash
# Скачайте Allure с https://github.com/allure-framework/allure2/releases
# Или используйте пакетный менеджер вашего дистрибутива
```

После установки:
```bash
allure generate allure-results -o allure-report --clean
```

## Способ 2: Использование Docker

```bash
docker run --rm \
  -v "$(pwd)/allure-results:/app/allure-results" \
  -v "$(pwd)/allure-report:/app/allure-report" \
  frankescobar/allure-docker-service:latest \
  allure generate /app/allure-results -o /app/allure-report --clean
```

## Способ 3: Использование готового образа

```bash
# Скачайте образ
docker pull frankescobar/allure-docker-service

# Сгенерируйте отчет
docker run --rm \
  -v "$(pwd)/allure-results:/app/allure-results" \
  -v "$(pwd)/allure-report:/app/allure-report" \
  frankescobar/allure-docker-service \
  allure generate /app/allure-results -o /app/allure-report --clean
```

## После генерации

Отчет будет в директории `allure-report/`. Эту директорию нужно закоммитить в репозиторий.

Для просмотра отчета локально:
```bash
allure open allure-report
```

Или просто откройте файл `allure-report/index.html` в браузере.

