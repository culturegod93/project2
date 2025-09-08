import pytest

from src.models import Category, Product


@pytest.fixture
def sample_products():
    p1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    p2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return [p1, p2]


@pytest.fixture
def sample_category(sample_products):
    return Category("Смартфоны", "Описание категории", sample_products)


def test_product_init(sample_products):
    p1, p2 = sample_products
    assert p1.name == "Samsung Galaxy S23 Ultra"
    assert p1.description == "256GB, Серый цвет, 200MP камера"
    assert p1.price == 180000.0
    assert p1.quantity == 5


def test_category_init(sample_category):
    cat = sample_category
    assert cat.name == "Смартфоны"
    assert cat.description == "Описание категории"
    assert len(cat.products.splitlines()) == 2  # геттер возвращает строки
    assert Category.product_count >= 2


def test_add_product(sample_category):
    new_product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    old_count = Category.product_count
    sample_category.add_product(new_product)
    assert len(sample_category.products.splitlines()) == 3
    assert Category.product_count == old_count + 1


def test_price_setter():
    p = Product("Test", "Desc", 1000.0, 1)
    p.price = 2000.0
    assert p.price == 2000.0

    # Проверка отрицательной цены (не изменяет)
    old_price = p.price
    p.price = -100
    assert p.price == old_price


def test_new_product_creates_or_merges():
    existing_products = [
        Product("Item1", "Desc1", 100.0, 5),
        Product("Item2", "Desc2", 200.0, 3),
    ]
    data = {"name": "Item1", "description": "Desc1", "price": 150.0, "quantity": 7}
    new_p = Product.new_product(data, products_list=existing_products)
    # Должно обновить количество и взять максимальную цену
    assert new_p.quantity == 12
    assert new_p.price == 150.0
