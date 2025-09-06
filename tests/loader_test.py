import json
import tempfile
from pathlib import Path

import pytest

from src.loader import load_from_json
from src.models import Category, Product


@pytest.fixture
def sample_json_file():
    """Создаёт временный JSON с тестовыми данными"""
    data = [
        {
            "name": "Смартфоны",
            "description": "Категория смартфонов",
            "products": [
                {
                    "name": "iPhone 15",
                    "description": "512GB",
                    "price": 210000.0,
                    "quantity": 5,
                },
                {
                    "name": "Samsung S23",
                    "description": "256GB",
                    "price": 180000.0,
                    "quantity": 3,
                },
            ],
        }
    ]
    tmp = tempfile.NamedTemporaryFile(
        delete=False, suffix=".json", mode="w", encoding="utf-8"
    )
    json.dump(data, tmp, ensure_ascii=False)
    tmp.close()
    yield tmp.name
    Path(tmp.name).unlink(missing_ok=True)


def test_load_from_json_returns_categories(sample_json_file):
    categories = load_from_json(sample_json_file)

    assert isinstance(categories, list)
    assert len(categories) == 1
    assert all(isinstance(cat, Category) for cat in categories)

    category = categories[0]
    assert category.name == "Смартфоны"
    assert category.description == "Категория смартфонов"
    assert len(category.products) == 2


def test_products_inside_category(sample_json_file):
    categories = load_from_json(sample_json_file)
    products = categories[0].products

    assert all(isinstance(p, Product) for p in products)
    assert products[0].name == "iPhone 15"
    assert products[0].price == 210000.0
    assert products[1].quantity == 3
