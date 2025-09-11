from __future__ import annotations

from typing import Dict, Iterator, List, Union


class Product:
    """
    Класс товара.
    Атрибуты:
        name: название
        description: описание
        _price: приватная цена (float)
        quantity: количество на складе (int)
    """

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name: str = name
        self.description: str = description
        self._price: float = float(price)
        self.quantity: int = int(quantity)

    @property
    def price(self) -> float:
        """Геттер приватного атрибута цены."""
        return self._price

    @price.setter
    def price(self, value: Union[float, int]) -> None:
        """
        Сеттер приватного атрибута цены.
        Если value <= 0, выводится сообщение и значение не меняется.
        """
        try:
            val = float(value)
        except (TypeError, ValueError):
            print("Цена должна быть числом")
            return

        if val <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        self._price = val

    @classmethod
    def new_product(cls, data: Dict[str, object]) -> Product:
        """
        Создать Product из словаря.
        Ожидаемые ключи: name, description, price, quantity
        """
        try:
            name = str(data["name"])
            description = str(data.get("description", ""))
            price = float(str(data["price"]))
            quantity = int(str(data["quantity"]))

            return cls(name, description, price, quantity)
        except (KeyError, ValueError, TypeError) as e:
            print(f"Ошибка при создании продукта: {e}")
            raise

    def __str__(self) -> str:
        """
        Формат вывода продукта:
        "Название продукта, X руб. Остаток: X шт."
        Цена форматируется без дробной части (как в условиях задания).
        """
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Product) -> float:
        """
        Сложение двух товаров — возвращает суммарную стоимость (price * quantity).
        Если other не Product — возвращает NotImplemented.
        """
        if not isinstance(other, Product):
            return NotImplemented
        return float(self.price * self.quantity + other.price * other.quantity)


class Category:
    """
    Класс категории.
    Класс-атрибуты:
        category_count: количество созданных категорий
        product_count: суммарное количество продуктов во всех категориях
    """

    category_count: int = 0
    product_count: int = 0

    def __init__(
        self, name: str, description: str, products: List[Product] | None = None
    ) -> None:
        self.name: str = name
        self.description: str = description
        self._products: List[Product] = []

        if products:
            for p in products:
                if not isinstance(p, Product):
                    raise TypeError("elements of products must be Product instances")
                self._products.append(p)

        Category.category_count += 1
        Category.product_count += len(self._products)

    def add_product(self, product: Product) -> None:
        """Добавить продукт в категорию (и увеличить product_count)."""
        if not isinstance(product, Product):
            raise TypeError("product must be Product")
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Геттер, возвращающий строку со всеми продуктами в формате:
        "Название продукта, X руб. Остаток: X шт.\n"
        """
        return "".join(
            f"{p.name}, {int(p.price)} руб. Остаток: {p.quantity} шт.\n"
            for p in self._products
        )

    def __str__(self) -> str:
        """Возвращает строку с подсчётом общего количества товаров в данной категории."""
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self) -> Iterator[Product]:
        """Возвращает итератор по продуктам категории."""
        return iter(self._products)


class CategoryIterator:
    """Итератор для перебора продуктов в категории."""

    def __init__(self, products: List[Product]) -> None:
        self.products = products
        self.index = 0

    def __iter__(self) -> CategoryIterator:
        return self

    def __next__(self) -> Product:
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        raise StopIteration
