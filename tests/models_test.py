from typing import Any, Dict

import pytest

from src.models import Category, Product


@pytest.fixture(autouse=True)
def reset_class_counters() -> None:
    """Сбрасываем счётчики перед каждым тестом, чтобы они не накапливались между тестами."""
    Category.category_count = 0
    Category.product_count = 0


def test_product_init() -> None:
    p = Product("Item1", "Desc1", 100.0, 5)
    assert p.name == "Item1"
    assert p.description == "Desc1"
    assert p.price == 100.0
    assert p.quantity == 5


def test_price_setter_positive_changes() -> None:
    p = Product("Item", "Desc", 100.0, 1)
    p.price = 150.0
    assert p.price == 150.0


def test_price_setter_non_positive_keeps_old_and_prints(
    capsys: pytest.CaptureFixture[str],
) -> None:
    p = Product("Item", "Desc", 100.0, 1)
    p.price = -10
    captured = capsys.readouterr().out
    assert "Цена не должна быть нулевая или отрицательная" in captured
    assert p.price == 100.0

    p.price = 0  # снова не должно примениться
    captured = capsys.readouterr().out
    assert "Цена не должна быть нулевая или отрицательная" in captured
    assert p.price == 100.0


def test_category_init_and_counters() -> None:
    p1 = Product("P1", "D1", 10.0, 1)
    p2 = Product("P2", "D2", 20.0, 2)
    cat = Category("Cat", "Desc", [p1, p2])

    assert cat.name == "Cat"
    assert Category.category_count == 1
    assert Category.product_count == 2

    # геттер products возвращает строку со списком товаров
    lines = cat.products.splitlines()
    assert len(lines) == 2
    assert "P1" in lines[0]
    assert "P2" in lines[1]
    assert "руб." in lines[0] and "Остаток:" in lines[0]


def test_category_add_product_increments_counter_and_shows_in_getter() -> None:
    cat = Category("Cat", "Desc", [])
    assert Category.product_count == 0

    p = Product("Phone", "256GB", 180000.0, 5)
    cat.add_product(p)

    assert Category.product_count == 1
    lines = cat.products.splitlines()
    assert len(lines) == 1
    assert "Phone" in lines[0]
    assert "руб." in lines[0]
    assert "Остаток:" in lines[0]


def test_new_product_creates_from_dict() -> None:
    data: Dict[str, Any] = {
        "name": "NewItem",
        "description": "NewDesc",
        "price": 99.9,
        "quantity": 3,
    }
    p = Product.new_product(data)
    assert isinstance(p, Product)
    assert p.name == "NewItem"
    assert p.description == "NewDesc"
    assert p.price == 99.9
    assert p.quantity == 3
