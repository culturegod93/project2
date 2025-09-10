from __future__ import annotations

from typing import Union


class Product:
    """
    Класс для описания продукта.
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        if price <= 0:
            raise ValueError("Цена должна быть положительной")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Product) -> float:
        """
        Складываем стоимость товаров (цена * количество).
        """
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только продукты")
        return self.price * self.quantity + other.price * other.quantity

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return False
        return (
            self.name == other.name
            and self.description == other.description
            and self.price == other.price
            and self.quantity == other.quantity
        )

    @classmethod
    def new_product(
        cls, data: dict[str, Union[str, float, int]], products_list: list[Product]
    ) -> Product:
        """
        Создаёт продукт или увеличивает количество, если он уже есть.
        """
        for product in products_list:
            if (
                product.name == data["name"]
                and product.description == data["description"]
            ):
                product.quantity += int(data["quantity"])
                product.price = float(data["price"])  # обновляем цену
                return product
        return cls(
            str(data["name"]),
            str(data["description"]),
            float(data["price"]),
            int(data["quantity"]),
        )


class Category:
    """
    Класс для описания категории товаров.
    """

    name: str
    description: str
    __products: list[Product]

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Union[Product, tuple[str, str, float, int]]],
    ) -> None:
        self.name = name
        self.description = description
        self.__products: list[Product] = []

        for product in products:
            if isinstance(product, Product):
                self.__products.append(product)
            elif isinstance(product, tuple):
                title, description, price, quantity = product
                self.__products.append(
                    Product(str(title), str(description), float(price), int(quantity))
                )
            else:
                raise TypeError("Продукты должны быть Product или tuple")

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {len(self.__products)}"

    @property
    def products(self) -> str:
        return "\n".join(str(p) for p in self.__products)

    @property
    def products_list(self) -> list[Product]:
        return self.__products
