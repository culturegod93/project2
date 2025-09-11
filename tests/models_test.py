import pytest

from src.models import Category, LawnGrass, Product, Smartphone


class TestSmartphone:
    """Тесты для класса Smartphone"""

    def test_smartphone_creation(self):
        """Тест создания смартфона"""
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
        assert smartphone.name == "Test Phone"
        assert smartphone.description == "Test Description"
        assert smartphone.price == 1000.0
        assert smartphone.quantity == 5
        assert smartphone.efficiency == 95.5
        assert smartphone.model == "Test Model"
        assert smartphone.memory == 256
        assert smartphone.color == "Black"

    def test_smartphone_str(self):
        """Тест строкового представления смартфона"""
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
        assert "Test Phone" in str(smartphone)
        assert "Test Model" in str(smartphone)
        assert "256" in str(smartphone)
        assert "Black" in str(smartphone)
        assert "1000" in str(smartphone)
        assert "5" in str(smartphone)


class TestLawnGrass:
    """Тесты для класса LawnGrass"""

    def test_lawn_grass_creation(self):
        """Тест создания газонной травы"""
        grass = LawnGrass(
            "Test Grass", "Test Description", 500.0, 10, "Russia", "7 days", "Green"
        )
        assert grass.name == "Test Grass"
        assert grass.description == "Test Description"
        assert grass.price == 500.0
        assert grass.quantity == 10
        assert grass.country == "Russia"
        assert grass.germination_period == "7 days"
        assert grass.color == "Green"

    def test_lawn_grass_str(self):
        """Тест строкового представления газонной травы"""
        grass = LawnGrass(
            "Test Grass", "Test Description", 500.0, 10, "Russia", "7 days", "Green"
        )
        assert "Test Grass" in str(grass)
        assert "Russia" in str(grass)
        assert "7 days" in str(grass)
        assert "Green" in str(grass)
        assert "500" in str(grass)
        assert "10" in str(grass)


class TestProductAddition:
    """Тесты для сложения продуктов"""

    def test_smartphone_addition(self):
        """Тест сложения смартфонов"""
        phone1 = Smartphone(
            "Phone 1", "Desc 1", 1000.0, 2, 90.0, "Model 1", 128, "Black"
        )
        phone2 = Smartphone(
            "Phone 2", "Desc 2", 1500.0, 3, 95.0, "Model 2", 256, "White"
        )
        result = phone1 + phone2
        expected = 1000.0 * 2 + 1500.0 * 3  # 2000 + 4500 = 6500
        assert result == expected

    def test_lawn_grass_addition(self):
        """Тест сложения газонной травы"""
        grass1 = LawnGrass("Grass 1", "Desc 1", 100.0, 5, "Russia", "7 days", "Green")
        grass2 = LawnGrass("Grass 2", "Desc 2", 150.0, 3, "USA", "5 days", "Dark Green")
        result = grass1 + grass2
        expected = 100.0 * 5 + 150.0 * 3  # 500 + 450 = 950
        assert result == expected

    def test_different_types_addition(self):
        """Тест попытки сложения разных типов продуктов"""
        phone = Smartphone("Phone", "Desc", 1000.0, 2, 90.0, "Model", 128, "Black")
        grass = LawnGrass("Grass", "Desc", 100.0, 5, "Russia", "7 days", "Green")

        with pytest.raises(TypeError):
            phone + grass  # Убрано присваивание result

    def test_product_and_smartphone_addition(self):
        """Тест попытки сложения Product и Smartphone"""
        product = Product("Product", "Desc", 100.0, 2)
        phone = Smartphone("Phone", "Desc", 1000.0, 2, 90.0, "Model", 128, "Black")

        with pytest.raises(TypeError):
            product + phone  # Убрано присваивание result

    def test_product_and_lawn_grass_addition(self):
        """Тест попытки сложения Product и LawnGrass"""
        product = Product("Product", "Desc", 100.0, 2)
        grass = LawnGrass("Grass", "Desc", 100.0, 5, "Russia", "7 days", "Green")

        with pytest.raises(TypeError):
            product + grass  # Убрано присваивание result


class TestCategoryAddProduct:
    """Тесты для добавления продуктов в категорию"""

    def test_add_smartphone_to_category(self):
        """Тест добавления смартфона в категорию"""
        category = Category("Test Category", "Test Description")
        phone = Smartphone("Phone", "Desc", 1000.0, 2, 90.0, "Model", 128, "Black")

        category.add_product(phone)
        assert len(list(category)) == 1

    def test_add_lawn_grass_to_category(self):
        """Тест добавления газонной травы в категорию"""
        category = Category("Test Category", "Test Description")
        grass = LawnGrass("Grass", "Desc", 100.0, 5, "Russia", "7 days", "Green")

        category.add_product(grass)
        assert len(list(category)) == 1

    def test_add_regular_product_to_category(self):
        """Тест добавления обычного продукта в категорию"""
        category = Category("Test Category", "Test Description")
        product = Product("Product", "Desc", 100.0, 2)

        category.add_product(product)
        assert len(list(category)) == 1

    def test_add_invalid_product_to_category(self):
        """Тест попытки добавления не-продукта в категорию"""
        category = Category("Test Category", "Test Description")

        with pytest.raises(TypeError):
            category.add_product("Not a product")
