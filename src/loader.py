import json
from typing import List
from src.models import Product, Category


def load_from_json(path: str) -> List[Category]:
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []
    for item in data:
        products = [
            Product(p["name"], p["description"], p["price"], p["quantity"])
            for p in item.get("products", [])
        ]
        categories.append(Category(item["name"], item["description"], products))
    return categories
