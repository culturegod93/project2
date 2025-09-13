import pytest

from src.models import Category, Product, ZeroQuantityError


class TestProductValidation:
    """Тесты для валидации создания продукта"""

    def test_product_creation_with_zero_quantity(self):
        """Тест создания продукта с нулевым количеством"""
        with pytest.raises(ZeroQuantityError) as exc_info:
            Product("Test Product", "Test Description", 100.0, 0)

        assert "Товар с нулевым количеством не может быть добавлен" in str(
            exc_info.value
        )

    def test_product_creation_with_positive_quantity(self):
        """Тест создания продукта с положительным количеством"""
        product = Product("Test Product", "Test Description", 100.0, 5)
        assert product.quantity == 5

    def test_new_product_with_missing_fields(self):
        """Тест new_product с отсутствующими полями"""
        data = {
            "name": "Test Product"
            # нет обязательных полей price и quantity
        }
        with pytest.raises(Exception):
            Product.new_product(data)


class TestCategoryMiddlePrice:
    """Тесты для метода middle_price категории"""

    def test_middle_price_with_products(self):
        """Тест расчета средней цены с товарами в категории"""
        product1 = Product("Product 1", "Desc 1", 100.0, 5)
        product2 = Product("Product 2", "Desc 2", 200.0, 3)
        category = Category("Test Category", "Test Description", [product1, product2])

        assert category.middle_price() == 150.0  # (100 + 200) / 2 = 150

    def test_middle_price_empty_category(self):
        """Тест расчета средней цены для пустой категории"""
        category = Category("Test Category", "Test Description", [])

        assert category.middle_price() == 0

    def test_middle_price_single_product(self):
        """Тест расчета средней цены для категории с одним товаром"""
        product = Product("Product", "Desc", 100.0, 5)
        category = Category("Test Category", "Test Description", [product])

        assert category.middle_price() == 100.0


class TestCategoryAddProduct:
    """Тесты для добавления продуктов в категорию с обработкой исключений"""

    def test_add_product_with_zero_quantity(self, capsys):
        """Тест добавления товара с нулевым количеством в категорию"""
        category = Category("Test Category", "Test Description", [])
        # Создаем продукт с положительным количеством
        product = Product("Test Product", "Test Description", 100.0, 1)
        # Вручную изменяем количество на 0 (так как нет сеттера с проверкой)
        product.quantity = 0

        category.add_product(product)

        captured = capsys.readouterr()
        assert "Ошибка при добавлении товара" in captured.out
        assert "Нельзя добавить товар с нулевым количеством" in captured.out
        assert "Обработка добавления товара завершена" in captured.out

    def test_add_valid_product(self, capsys):
        """Тест добавления валидного товара в категорию"""
        category = Category("Test Category", "Test Description", [])
        product = Product("Test Product", "Test Description", 100.0, 5)

        category.add_product(product)

        captured = capsys.readouterr()
        assert "Товар успешно добавлен" in captured.out
        assert "Обработка добавления товара завершена" in captured.out
        assert len(category._products) == 1

    def test_add_valid_product_stdout(self, capsys):
        """Тест вывода сообщения при успешном добавлении товара"""
        category = Category("Test Category", "Test Description", [])
        product = Product("Test Product", "Test Description", 100.0, 5)

        category.add_product(product)

        captured = capsys.readouterr()
        assert "Товар успешно добавлен" in captured.out
        assert "Обработка добавления товара завершена" in captured.out


class TestLogCreationMixin:

    def test_repr_method_with_actual_product(self):
        """Тест метода __repr__ для реального продукта"""
        product = Product("Test Product", "Test Description", 100.0, 5)
        repr_str = repr(product)
        assert "Product" in repr_str
        assert "name='Test Product'" in repr_str
        assert "description='Test Description'" in repr_str
        # Проверим, что приватные поля не отображаются
        assert "_price" not in repr_str
