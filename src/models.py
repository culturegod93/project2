from __future__ import annotations

from typing import List, Optional


class Product:
    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name: str = name
        self.description: str = description
        self._price: float = price  # приватный атрибут
        self.quantity: int = quantity

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self._price:
            confirm = input(
                f"Вы хотите снизить цену с {self._price} до {new_price}? (y/n): "
            )
            if confirm.lower() != "y":
                return
        self._price = new_price

    @classmethod
    def new_product(
        cls, data: dict[str, object], products_list: Optional[List[Product]] = None
    ) -> Product:
        name = str(data["name"])
        description = str(data["description"])

        price_raw = data["price"]
        quantity_raw = data["quantity"]

        if isinstance(price_raw, (int, float, str)):
            price = float(price_raw)
        else:
            raise TypeError(
                f"price должно быть float/int/str, получено {type(price_raw)}"
            )

        if isinstance(quantity_raw, (int, str)):
            quantity = int(quantity_raw)
        else:
            raise TypeError(
                f"quantity должно быть int/str, получено {type(quantity_raw)}"
            )

        if products_list is not None:
            for prod in products_list:
                if prod.name == name:
                    prod.quantity += quantity
                    if price > prod.price:
                        prod.price = price
                    return prod
        return cls(name, description, price, quantity)


class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(
        self, name: str, description: str, products: Optional[List[Product]] = None
    ) -> None:
        self.name: str = name
        self.description: str = description
        self._products: List[Product] = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self._products)

    def add_product(self, product: Product) -> None:
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        result = ""
        for prod in self._products:
            result += f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n"
        return result
