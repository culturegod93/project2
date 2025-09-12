import pytest

from src.models import (BaseProduct, Category, LawnGrass, LogCreationMixin,
                        Product, Smartphone)


class TestBaseProduct:
    """Тесты для абстрактного базового класса BaseProduct"""

    def test_base_product_is_abstract(self):
        """Тест, что BaseProduct является абстрактным классом"""
        with pytest.raises(TypeError):
            BaseProduct("Test", "Test", 100.0, 5)


class TestLogCreationMixin:
    """Тесты для миксина LogCreationMixin"""

    def test_log_creation_output(self, capsys):
        """Тест вывода информации при создании объекта"""

        class TestClass(LogCreationMixin):
            def __init__(self, name, value):
                super().__init__(name, value)
                self.name = name
                self.value = value
                self.__post_init__()

        _ = TestClass("Test", 123)
        captured = capsys.readouterr()

        assert "TestClass" in captured.out
        assert "'Test'" in captured.out
        assert "123" in captured.out

    def test_repr_method(self):
        """Тест метода __repr__"""

        class TestClass(LogCreationMixin):
            def __init__(self, name, value):
                super().__init__(name, value)
                self.name = name
                self.value = value

            def __post_init__(self):
                pass

        test_obj = TestClass("Test", 123)
        repr_str = repr(test_obj)

        assert "TestClass" in repr_str
        assert "name='Test'" in repr_str
        assert "value=123" in repr_str


class TestProductWithMixin:
    """Тесты для Product с миксином"""

    def test_product_creation_output(self, capsys):
        """Тест вывода информации при создании Product"""
        _ = Product("Test Product", "Test Description", 100.0, 5)
        captured = capsys.readouterr()

        assert "Product" in captured.out
        assert "'Test Product'" in captured.out
        assert "'Test Description'" in captured.out
        assert "100.0" in captured.out
        assert "5" in captured.out

    def test_product_repr(self):
        """Тест метода __repr__ для Product"""
        product = Product("Test Product", "Test Description", 100.0, 5)
        repr_str = repr(product)

        assert "Product" in repr_str
        assert "name='Test Product'" in repr_str
        assert "description='Test Description'" in repr_str
        assert "_price=100.0" not in repr_str  # Приватные поля не должны отображаться
        assert "quantity=5" in repr_str


class TestInheritanceWithMixin:
    """Тесты наследования с миксином"""

    def test_smartphone_creation_output(self, capsys):
        """Тест вывода информации при создании Smartphone"""
        _ = Smartphone(
            "Test Phone",
            "Test Description",
            1000.0,
            5,
            95.5,
            "Test Model",
            256,
            "Black",
        )
        captured = capsys.readouterr()

        assert "Smartphone" in captured.out
        assert "'Test Phone'" in captured.out

    def test_lawn_grass_creation_output(self, capsys):
        """Тест вывода информации при создании LawnGrass"""
        _ = LawnGrass(
            "Test Grass", "Test Description", 500.0, 10, "Russia", "7 days", "Green"
        )
        captured = capsys.readouterr()

        assert "LawnGrass" in captured.out
        assert "'Test Grass'" in captured.out

    def test_new_product_missing_fields(self):
        """Тест создания продукта с отсутствующими полями"""
        data = {
            "name": "Test Product"
            # Нет price и quantity
        }
        with pytest.raises(Exception):
            Product.new_product(data)

    def test_price_setter_negative(self, capsys):
        """Тест установки отрицательной цены"""
        product = Product("Test", "Desc", 100.0, 5)
        product.price = -50.0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 100.0

    def test_price_setter_zero(self, capsys):
        """Тест установки нулевой цены"""
        product = Product("Test", "Desc", 100.0, 5)
        product.price = 0.0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 100.0

    def test_price_setter_string(self, capsys):
        """Тест установки строки в качестве цены"""
        product = Product("Test", "Desc", 100.0, 5)
        product.price = "not a number"
        captured = capsys.readouterr()
        assert "Цена должна быть числом" in captured.out
        assert product.price == 100.0

    def test_addition_different_types(self):
        """Тест сложения продуктов разных типов"""
        product = Product("Product", "Desc", 100.0, 5)
        smartphone = Smartphone(
            "Smartphone", "Desc", 1000.0, 2, 90.0, "Model", 128, "Black"
        )

        with pytest.raises(TypeError):
            product + smartphone

    def test_add_non_product_to_category(self):
        """Тест добавления не-продукта в категорию"""
        category = Category("Test Category", "Test Description")

        with pytest.raises(TypeError):
            category.add_product("not a product")

    def test_product_repr(self):
        """Тест метода __repr__ для Product"""
        product = Product("Test Product", "Test Description", 100.0, 5)
        repr_str = repr(product)
        assert "Product" in repr_str
        assert "name='Test Product'" in repr_str
        assert "description='Test Description'" in repr_str

    def test_smartphone_repr(self):
        """Тест метода __repr__ для Smartphone"""
        smartphone = Smartphone(
            "Test Phone",
            "Test Description",
            1000.0,
            5,
            95.5,
            "Test Model",
            256,
            "Black",
        )
        repr_str = repr(smartphone)
        assert "Smartphone" in repr_str
        assert "name='Test Phone'" in repr_str

    def test_lawn_grass_repr(self):
        """Тест метода __repr__ для LawnGrass"""
        grass = LawnGrass(
            "Test Grass", "Test Description", 500.0, 10, "Russia", "7 days", "Green"
        )
        repr_str = repr(grass)
        assert "LawnGrass" in repr_str
        assert "name='Test Grass'" in repr_str
