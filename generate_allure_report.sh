#!/bin/bash
# Скрипт для генерации Allure отчета

echo "Попытка генерации Allure отчета..."

# Проверка наличия allure-results
if [ ! -d "allure-results" ] || [ -z "$(ls -A allure-results)" ]; then
    echo "Ошибка: Директория allure-results пуста или не существует."
    echo "Сначала запустите тесты: pytest"
    exit 1
fi

# Способ 1: Использование Allure CLI (если установлен)
if command -v allure &> /dev/null; then
    echo "Используется Allure CLI..."
    allure generate allure-results -o allure-report --clean
    echo "✓ Отчет сгенерирован в allure-report/"
    exit 0
fi

# Способ 2: Использование Docker
if command -v docker &> /dev/null; then
    echo "Используется Docker..."
    docker run --rm \
        -v "$(pwd)/allure-results:/app/allure-results" \
        -v "$(pwd)/allure-report:/app/allure-report" \
        frankescobar/allure-docker-service:latest \
        allure generate /app/allure-results -o /app/allure-report --clean 2>/dev/null
    
    if [ $? -eq 0 ]; then
        echo "✓ Отчет сгенерирован в allure-report/"
        exit 0
    fi
fi

# Если ничего не сработало
echo "⚠ Allure CLI и Docker недоступны."
echo ""
echo "Для генерации отчета установите Allure CLI:"
echo "  macOS: brew install allure"
echo "  Linux: см. https://github.com/allure-framework/allure2/releases"
echo ""
echo "Или используйте Docker:"
echo "  docker pull frankescobar/allure-docker-service"
echo "  docker run --rm -v \$(pwd)/allure-results:/app/allure-results -v \$(pwd)/allure-report:/app/allure-report frankescobar/allure-docker-service allure generate /app/allure-results -o /app/allure-report --clean"
echo ""
echo "После установки запустите: ./generate_allure_report.sh"
exit 1

