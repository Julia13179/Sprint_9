# Установка Allure для генерации отчетов

## macOS (через Homebrew)

Если у вас установлен Homebrew:
```bash
brew install allure
```

Если Homebrew не установлен, установите его:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Альтернативная установка (без Homebrew)

1. Скачайте Allure с GitHub:
   - Перейдите на https://github.com/allure-framework/allure2/releases
   - Скачайте `allure-2.x.x.tgz` для macOS

2. Распакуйте архив:
```bash
tar -xzf allure-2.x.x.tgz
sudo mv allure-2.x.x /usr/local/allure
```

3. Добавьте в PATH:
```bash
echo 'export PATH="/usr/local/allure/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

4. Проверьте установку:
```bash
allure --version
```

## После установки

Сгенерируйте отчет:
```bash
allure generate allure-results -o allure-report --clean
```

Откройте отчет:
```bash
allure open allure-report
```

Или просто откройте `allure-report/index.html` в браузере.

