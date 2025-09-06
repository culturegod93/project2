import pytest
from src.models import Product, Category


@pytest.fixture
def sample_products():
    return [
        Product("Телефон", "Смартфон с OLED-экраном", 50000.0, 10),
        Product("Ноутбук", "Игровой ноутбук", 120000.0, 5),
    ]


def test_product_init():
    product = Product("Мышь", "Игровая мышь", 2500.0, 15)
    assert product.name == "Мышь"
    assert product.description == "Игровая мышь"
    assert product.price == 2500.0
    assert product.quantity == 15


def test_category_init(sample_products):
    category = Category("Электроника", "Гаджеты и устройства", sample_products)
    assert category.name == "Электроника"
    assert category.description == "Гаджеты и устройства"
    assert category.products == sample_products


def test_category_counters(sample_products):
    start_cat = Category.category_count
    start_prod = Category.product_count

    Category("Новая категория", "Описание", sample_products)

    assert Category.category_count == start_cat + 1
    assert Category.product_count == start_prod + len(sample_products)
