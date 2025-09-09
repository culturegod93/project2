from __future__ import annotations

from typing import Any, Dict, List


class Product:
    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.__price = float(price)
        self.quantity = int(quantity)

    @property
    def price(self) -> float:
        """Геттер для приватного атрибута цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для цены: проверка на положительность"""
        if new_price > 0:
            self.__price = float(new_price)
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, data: Dict[str, Any]) -> Product:
        return cls(
            name=data["name"],
            description=data["description"],
            price=float(data["price"]),
            quantity=int(data["quantity"]),
        )

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Category:
    category_count = 0
    product_count = 0

    def __init__(
        self, name: str, description: str, products: List[Product] | None = None
    ) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = products or []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self) -> str:
        return "".join(
            [
                f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.\n"
                for p in self.__products
            ]
        )

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    def __str__(self) -> str:
        return f"{self.name} ({len(self.__products)} товаров)"
