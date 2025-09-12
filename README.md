Project 2

Описание:
Project 2 - проект представляет собой учебное ядро интернет-магазина, построенное на принципах объектно-ориентированного программирования. Обновлены все модули.

Функциональность:

### Абстрактный базовый класс
- Создан абстрактный базовый класс `BaseProduct`
- Определен общий интерфейс для всех продуктов
- Классы `Product`, `Smartphone` и `LawnGrass` наследуются от `BaseProduct`

### Класс-миксин
- Реализован класс-миксин `LogCreationMixin` для логирования создания объектов
- При создании объекта выводится информация о классе и параметрах
- Реализован метод `__repr__` для удобного представления объектов

Структура проекта:
Project 2
├── data
│ └── products.json
├── htmlcov
│ └── index.html
├── logs
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
В проекте реализованы автоматические тесты с использованием pytest и фикстур. Добавлены тесты (loader.py и models.py).

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
