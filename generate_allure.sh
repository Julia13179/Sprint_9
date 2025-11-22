#!/bin/bash
# Скрипт для генерации Allure отчета

if [ ! -d "allure-results" ]; then
    echo "Директория allure-results не найдена. Запустите тесты сначала."
    exit 1
fi

allure generate allure-results -o allure-report --clean
echo "Allure отчет сгенерирован в директории allure-report"

