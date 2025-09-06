Project 2
Описание:
Project 2 - ... .

Структура проекта:
Project 1 ├── data │ ├── transactions.csv │ ├── transactions_excel.xlsx │ └── operations.json ├── htmlcov │ └── index.html ├── logs ├── src │ ├── init.py │ ├── decorators.py │ ├── external_api.py │ ├── file_readers.py │ ├── filters.py │ ├── generators.py │ ├── main.py │ ├── masks.py │ ├── processing.py │ ├── utils.py │ └── widget.py ├── tests │ ├── init.py │ ├── conftest.py │ ├── decorators_test.py │ ├── external_api_test.py │ ├── file_readers_test.py │ ├── filters_test.py │ ├── generators_test.py │ ├── masks_test.py │ ├── processing_test.py │ ├── utils_test.py │ └── widget_test.py ├── .coverage ├── .env.template ├── .flake8 ├── .gitignore ├── README.md ├── poetry.lock └── poetry.toml

Тестирование:
В проекте реализованы автоматические тесты с использованием pytest. Добавлены тесты (models.py и loader.py).

Запуск тестов:
poetry run pytest
Проверка покрытия:
poetry run pytest --cov=src
Тестируемые модули: models.py, loader.py.

Ссылка:
GitHub

Установка:
Клонируйте репозиторий:
git clone https://github.com/culturegod93/project2
Установите зависимости:
poetry install
Документация:
Дополнительная информация о проекте в README.md.

Разработчик:
Дмитрий Смирнов.

Лицензия
Проект лицензирован по лицензии MIT.
