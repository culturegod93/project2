import json
from typing import List

from src.models import Category, Product


def load_from_json(path: str) -> List[Category]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    categories: List[Category] = []
    for item in data:
        products = [
            Product(p["name"], p["description"], float(p["price"]), int(p["quantity"]))
            for p in item.get("products", [])
        ]
        categories.append(Category(item["name"], item["description"], products))
    return categories
