import json

import pytest

from src.loader import load_from_json
from src.models import Category


@pytest.fixture
def sample_json(tmp_path):
    data = [
        {
            "name": "Смартфоны",
            "description": "Описание категории",
            "products": [
                {
                    "name": "Samsung",
                    "description": "256GB",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {
                    "name": "Iphone",
                    "description": "512GB",
                    "price": 210000.0,
                    "quantity": 8,
                },
            ],
        }
    ]
    file_path = tmp_path / "data.json"
    file_path.write_text(json.dumps(data), encoding="utf-8")
    return file_path


def test_load_from_json(sample_json):
    categories = load_from_json(str(sample_json))
    assert isinstance(categories, list)
    assert all(isinstance(cat, Category) for cat in categories)
    cat = categories[0]
    assert cat.name == "Смартфоны"
    products_lines = cat.products.splitlines()
    assert len(products_lines) == 2
    assert "Samsung" in products_lines[0]
    assert "Iphone" in products_lines[1]
