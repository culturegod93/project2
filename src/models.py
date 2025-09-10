from __future__ import annotations

from typing import List, Optional


class Product:
    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name: str = str(name)
        self.description: str = str(description)
        self._price: float = float(price)
        self.quantity: int = int(quantity)

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self._price:
            confirm = input(
                f"Вы действительно хотите снизить цену с {self._price} до {value}? (y/n): "
            )
            if confirm.lower() == "y":
                self._price = value
        else:
            self._price = value

    @classmethod
    def new_product(cls, data: dict) -> Product:
        return cls(
            name=str(data.get("name", "")),
            description=str(data.get("description", "")),
            price=float(data.get("price", 0)),
            quantity=int(data.get("quantity", 0)),
        )


class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(
        self, name: str, description: str, products: Optional[List[Product]] = None
    ) -> None:
        self.name: str = str(name)
        self.description: str = str(description)
        self._products: List[Product] = products if products else []

        Category.category_count += 1
        Category.product_count += len(self._products)

    def add_product(self, product: Product) -> None:
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        return "".join(
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.\n"
            for p in self._products
        )
