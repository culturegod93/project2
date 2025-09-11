import json
from typing import List

from src.models import Category, Product


def load_from_json(path: str) -> List[Category]:
    """
    Загружает данные из JSON-файла и создает список категорий с продуктами.

    Args:
        path: Путь к JSON-файлу

    Returns:
        List[Category]: Список объектов Category
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Файл {path} не найден")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле {path}")
        return []

    categories: List[Category] = []
    for item in data:
        products = []
        for p in item.get("products", []):
            try:
                product_data = {
                    "name": str(p["name"]),
                    "description": str(p.get("description", "")),
                    "price": float(str(p["price"])),
                    "quantity": int(str(p["quantity"])),
                }
                products.append(Product.new_product(product_data))
            except (KeyError, ValueError, TypeError) as e:
                print(f"Ошибка при создании продукта: {e}")
                continue

        try:
            categories.append(
                Category(str(item["name"]), str(item.get("description", "")), products)
            )
        except (KeyError, ValueError, TypeError) as e:
            print(f"Ошибка при обработке данных категории: {e}")
            continue

    return categories
