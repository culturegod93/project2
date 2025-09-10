import pytest

from src.models import Category, Product


def test_product_creation():
    p = Product("Test", "Desc", 100.0, 5)
    assert p.name == "Test"
    assert str(p) == "Test, 100.0 руб. Остаток: 5 шт."


def test_product_invalid_price():
    with pytest.raises(ValueError):
        Product("Bad", "Desc", -10.0, 5)


def test_product_invalid_quantity():
    with pytest.raises(ValueError):
        Product("Bad", "Desc", 100.0, -1)


def test_product_addition():
    p1 = Product("A", "DescA", 100.0, 2)  # 200
    p2 = Product("B", "DescB", 50.0, 4)  # 200
    assert p1 + p2 == 400.0


def test_product_equality():
    p1 = Product("X", "Desc", 10.0, 1)
    p2 = Product("X", "Desc", 10.0, 1)
    p3 = Product("Y", "Desc", 10.0, 1)
    assert p1 == p2
    assert p1 != p3


def test_new_product_creates_or_merges():
    products = [Product("Item1", "Desc1", 100.0, 5)]
    data = {"name": "Item1", "description": "Desc1", "price": 150.0, "quantity": 7}
    updated = Product.new_product(data, products)
    assert updated.quantity == 12
    assert updated.price == 150.0


def test_category_creation_with_products_and_tuples():
    p1 = Product("Phone", "Smartphone", 1000.0, 2)
    c = Category(
        "Electronics",
        "Devices",
        [
            p1,
            ("Laptop", "Gaming", 2000.0, 1),
        ],
    )
    assert "Phone" in c.products
    assert "Laptop" in c.products
    assert len(c.products_list) == 2
