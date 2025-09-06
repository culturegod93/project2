Project 2

Описание:
Project 2 - проект.

Структура проекта:
Project 2
├── data
│ └── products.json
├── htmlcov
│ └── index.html
├── src
│ ├── init.py
│ ├── loader.py
│ └── models.py
├── tests
│ ├── init.py
│ ├── loader_test.py
│ └── models_test.py
├── .coverage
├── .flake8
├── main.py
├── README.md
├── poetry.lock
└── poetry.toml

Тестирование:
В проекте реализованы автоматические тесты с использованием pytest. Добавлены тесты (loader.py и models.py).

1. Запуск тестов:
poetry run pytest
2. Проверка покрытия:
poetry run pytest --cov=src

Тестируемые модули: loader.py, models.py.

Ссылка:
https://github.com/culturegod93/project2

Установка:
1. Клонируйте репозиторий:
git clone https://github.com/culturegod93/project2
2. Установите зависимости:
poetry install

Документация:
Дополнительная информация о проекте в README.md.

Разработчик:
Дмитрий Смирнов.

Лицензия:
Проект лицензирован по лицензии MIT.
