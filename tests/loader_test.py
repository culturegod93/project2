import json
from pathlib import Path

import pytest

from src.loader import load_from_json
from src.models import Category


@pytest.fixture
def sample_json(tmp_path: Path) -> Path:
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


def test_load_from_json(sample_json: Path):
    categories = load_from_json(str(sample_json))
    assert isinstance(categories, list)
    cat = categories[0]
    assert isinstance(cat, Category)
    products_lines = cat.products.splitlines()
    assert len(products_lines) == 2
    assert "Samsung" in products_lines[0]
    assert "Iphone" in products_lines[1]
