import pytest

from src.models import Category, CategoryIterator, Product


class TestProduct:
    """Тесты для класса Product"""

    def test_product_creation(self):
        """Тест создания продукта"""
        product = Product("Test Product", "Test Description", 100.0, 10)
        assert product.name == "Test Product"
        assert product.description == "Test Description"
        assert product.price == 100.0
        assert product.quantity == 10

    def test_product_str(self):
        """Тест строкового представления продукта"""
        product = Product("Test Product", "Test Description", 100.0, 10)
        expected = "Test Product, 100 руб. Остаток: 10 шт."
        assert str(product) == expected

    def test_product_addition(self):
        """Тест сложения продуктов"""
        product1 = Product("Product 1", "Desc 1", 100.0, 5)
        product2 = Product("Product 2", "Desc 2", 200.0, 3)
        result = product1 + product2
        expected = 100.0 * 5 + 200.0 * 3  # 500 + 600 = 1100
        assert result == expected

    def test_product_addition_invalid_type(self):
        """Тест сложения продукта с неверным типом"""
        product = Product("Product", "Desc", 100.0, 5)
        # Прямой вызов __add__ для проверки возврата NotImplemented
        result = product.__add__("invalid")
        assert result is NotImplemented

    def test_price_setter_valid(self):
        """Тест установки корректной цены"""
        product = Product("Product", "Desc", 100.0, 5)
        product.price = 150.0
        assert product.price == 150.0

    def test_price_setter_invalid(self, capsys):
        """Тест установки некорректной цены"""
        product = Product("Product", "Desc", 100.0, 5)
        product.price = -50.0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 100.0  # Цена не изменилась

    def test_new_product_classmethod(self):
        """Тест создания продукта через classmethod"""
        data = {
            "name": "New Product",
            "description": "New Description",
            "price": 200.0,
            "quantity": 7,
        }
        product = Product.new_product(data)
        assert product.name == "New Product"
        assert product.description == "New Description"
        assert product.price == 200.0
        assert product.quantity == 7

    def test_new_product_classmethod_invalid_data(self):
        """Тест создания продукта с неверными данными"""
        data = {
            "name": "New Product",
            # Пропущены обязательные поля
        }
        with pytest.raises(Exception):
            Product.new_product(data)


class TestCategory:
    """Тесты для класса Category"""

    def test_category_creation(self):
        """Тест создания категории"""
        product = Product("Test Product", "Test Description", 100.0, 10)
        category = Category("Test Category", "Test Description", [product])

        assert category.name == "Test Category"
        assert category.description == "Test Description"
        # Исправлено: используем публичный интерфейс вместо приватного атрибута
        assert len(list(category)) == 1

    def test_category_str(self):
        """Тест строкового представления категории"""
        product1 = Product("Product 1", "Desc 1", 100.0, 5)
        product2 = Product("Product 2", "Desc 2", 200.0, 3)
        category = Category("Test Category", "Test Description", [product1, product2])

        expected = "Test Category, количество продуктов: 8 шт."
        assert str(category) == expected

    def test_add_product(self):
        """Тест добавления продукта в категорию"""
        product = Product("Test Product", "Test Description", 100.0, 10)
        category = Category("Test Category", "Test Description", [])

        category.add_product(product)
        # Исправлено: используем публичный интерфейс вместо приватного атрибута
        assert len(list(category)) == 1

    def test_add_product_invalid_type(self):
        """Тест добавления неверного типа в категорию"""
        category = Category("Test Category", "Test Description", [])

        with pytest.raises(TypeError):
            category.add_product("invalid product")

    def test_products_property(self):
        """Тест свойства products"""
        product1 = Product("Product 1", "Desc 1", 100.0, 5)
        product2 = Product("Product 2", "Desc 2", 200.0, 3)
        category = Category("Test Category", "Test Description", [product1, product2])

        expected = (
            "Product 1, 100 руб. Остаток: 5 шт.\nProduct 2, 200 руб. Остаток: 3 шт.\n"
        )
        assert category.products == expected

    def test_category_iterator(self):
        """Тест итерации по категории"""
        product1 = Product("Product 1", "Desc 1", 100.0, 5)
        product2 = Product("Product 2", "Desc 2", 200.0, 3)
        category = Category("Test Category", "Test Description", [product1, product2])

        product_names = [product.name for product in category]
        assert product_names == ["Product 1", "Product 2"]

    def test_category_count(self):
        """Тест подсчета количества категорий"""
        # Сбросим счетчики для чистоты теста
        initial_count = Category.category_count
        product = Product("Test Product", "Test Description", 100.0, 10)
        # Используем _ для неиспользуемой переменной
        _ = Category("Test Category", "Test Description", [product])

        assert Category.category_count == initial_count + 1

    def test_product_count(self):
        """Тест подсчета количества продуктов"""
        # Сбросим счетчики для чистоты теста
        initial_count = Category.product_count
        product1 = Product("Product 1", "Desc 1", 100.0, 5)
        product2 = Product("Product 2", "Desc 2", 200.0, 3)
        # Используем _ для неиспользуемой переменной
        _ = Category("Test Category", "Test Description", [product1, product2])

        assert Category.product_count == initial_count + 2


class TestCategoryIterator:
    """Тесты для класса CategoryIterator"""

    def test_iterator_creation(self):
        """Тест создания итератора"""
        product = Product("Test Product", "Test Description", 100.0, 10)
        iterator = CategoryIterator([product])

        assert iterator.products == [product]
        assert iterator.index == 0

    def test_iterator_iteration(self):
        """Тест итерации по продуктам"""
        product1 = Product("Product 1", "Desc 1", 100.0, 5)
        product2 = Product("Product 2", "Desc 2", 200.0, 3)
        iterator = CategoryIterator([product1, product2])

        products = list(iterator)
        assert products == [product1, product2]

    def test_iterator_stop_iteration(self):
        """Тест остановки итерации"""
        product = Product("Test Product", "Test Description", 100.0, 10)
        iterator = CategoryIterator([product])

        next(iterator)  # Первый вызов
        with pytest.raises(StopIteration):
            next(iterator)  # Второй вызов - должно вызвать исключение
