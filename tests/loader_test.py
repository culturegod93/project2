import json
import os
import tempfile

from src.loader import load_from_json


class TestLoader:
    """Тесты для функции load_from_json"""

    def test_load_from_json_valid(self):
        """Тест загрузки из корректного JSON файла"""
        # Создаем временный файл
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json_data = [
                {
                    "name": "Test Category",
                    "description": "Test Description",
                    "products": [
                        {
                            "name": "Test Product 1",
                            "description": "Test Description 1",
                            "price": 100.0,
                            "quantity": 5,
                        },
                        {
                            "name": "Test Product 2",
                            "description": "Test Description 2",
                            "price": 200.0,
                            "quantity": 3,
                        },
                    ],
                }
            ]
            json.dump(json_data, f)
            temp_path = f.name

        try:
            # Загружаем данные
            categories = load_from_json(temp_path)

            # Проверяем результат
            assert len(categories) == 1
            assert categories[0].name == "Test Category"
            assert categories[0].description == "Test Description"
            # Исправлено: используем публичный интерфейс вместо приватного атрибута
            assert len(list(categories[0])) == 2
            product_names = [product.name for product in categories[0]]
            assert "Test Product 1" in product_names
            assert "Test Product 2" in product_names
        finally:
            # Удаляем временный файл
            os.unlink(temp_path)

    def test_load_from_json_invalid_path(self, capsys):
        """Тест загрузки из несуществующего файла"""
        categories = load_from_json("nonexistent_file.json")
        captured = capsys.readouterr()

        assert "не найден" in captured.out
        assert categories == []

    def test_load_from_json_invalid_json(self, capsys):
        """Тест загрузки из некорректного JSON файла"""
        # Создаем временный файл с некорректным JSON
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write("invalid json content")
            temp_path = f.name

        try:
            categories = load_from_json(temp_path)
            captured = capsys.readouterr()
            assert "Ошибка декодирования JSON" in captured.out
            assert categories == []
        finally:
            os.unlink(temp_path)

    def test_load_from_json_missing_fields(self, capsys):
        """Тест загрузки из JSON с отсутствующими полями"""
        # Создаем временный файл с отсутствующими полями
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json_data = [
                {
                    "name": "Test Category",
                    "description": "Test Description",
                    "products": [
                        {
                            # Пропущено поле "name" (обязательное)
                            "description": "Test Description",
                            "price": 100.0,
                            "quantity": 5,
                        }
                    ],
                }
            ]
            json.dump(json_data, f)
            temp_path = f.name

        try:
            categories = load_from_json(temp_path)
            captured = capsys.readouterr()
            # Категория должна быть создана, но без продуктов из-за ошибки
            assert len(categories) == 1
            assert categories[0].name == "Test Category"
            # В категории не должно быть продуктов из-за ошибки
            assert len(list(categories[0])) == 0
            assert "Ошибка при создании продукта" in captured.out
        finally:
            os.unlink(temp_path)

    def test_load_from_json_invalid_category(self, capsys):
        """Тест загрузки из JSON с невалидными данными категории"""
        # Создаем временный файл с отсутствующим полем name у категории
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json_data = [
                {
                    # Пропущено поле "name"
                    "description": "Test Description",
                    "products": [],
                }
            ]
            json.dump(json_data, f)
            temp_path = f.name

        try:
            categories = load_from_json(temp_path)
            captured = capsys.readouterr()
            assert len(categories) == 0
            assert "Ошибка при обработке данных категории" in captured.out
        finally:
            os.unlink(temp_path)

    def test_load_from_json_invalid_product_data(self, capsys):
        """Тест загрузки из JSON с невалидными данными продукта"""
        # Создаем временный файл с продуктом, у которого отсутствует поле price
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json_data = [
                {
                    "name": "Test Category",
                    "description": "Test Description",
                    "products": [
                        {
                            "name": "Test Product",
                            "description": "Test Description",
                            # Пропущено price
                            "quantity": 5,
                        }
                    ],
                }
            ]
            json.dump(json_data, f)
            temp_path = f.name

        try:
            categories = load_from_json(temp_path)
            captured = capsys.readouterr()
            # Категория должна быть создана, но без продуктов
            assert len(categories) == 1
            assert len(list(categories[0])) == 0
            assert "Ошибка при создании продукта" in captured.out
        finally:
            os.unlink(temp_path)
