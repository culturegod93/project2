from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Iterator, List, Union


class BaseProduct(ABC):
    """
    Абстрактный базовый класс для товаров.
    Определяет общий интерфейс для всех продуктов.
    """

    @abstractmethod
    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other) -> float:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, value: Union[float, int]) -> None:
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, data: Dict[str, object]) -> BaseProduct:
        pass


class LogCreationMixin:
    """
    Миксин для логирования создания объектов.
    """

    def __init__(self, *args, **kwargs):
        # Сохраняем аргументы для логирования
        self._init_args = args
        self._init_kwargs = kwargs

    def __post_init__(self):
        """Метод для логирования после инициализации"""
        class_name = self.__class__.__name__
        params = ", ".join(
            [
                f"'{arg}'" if isinstance(arg, str) else str(arg)
                for arg in self._init_args
            ]
        )
        print(f"{class_name}({params})")

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        params = ", ".join(
            [
                f"{key}={repr(value)}"
                for key, value in self.__dict__.items()
                if not key.startswith("_")
            ]
        )
        return f"{class_name}({params})"


class Product(LogCreationMixin, BaseProduct):
    """
    Класс товара.
    Наследуется от BaseProduct и LogCreationMixin.
    """

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        # Инициализируем BaseProduct
        BaseProduct.__init__(self, name, description, price, quantity)
        # Инициализируем LogCreationMixin
        LogCreationMixin.__init__(self, name, description, price, quantity)
        # Вызываем пост-инициализацию для логирования
        self.__post_init__()

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
        Если other не того же типа — выбрасывает TypeError.
        """
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных типов")
        return float(self.price * self.quantity + other.price * other.quantity)


class Smartphone(Product):
    """
    Класс Смартфон, наследник Product.
    Дополнительные атрибуты:
        efficiency: производительность
        model: модель
        memory: объем встроенной памяти
        color: цвет
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency: float = efficiency
        self.model: str = model
        self.memory: int = memory
        self.color: str = color

    def __str__(self) -> str:
        """Строковое представление смартфона."""
        return (
            f"{self.name}, {self.model}, {self.memory}GB, {self.color}, "
            f"{int(self.price)} руб. Остаток: {self.quantity} шт."
        )


class LawnGrass(Product):
    """
    Класс Трава газонная, наследник Product.
    Дополнительные атрибуты:
        country: страна-производитель
        germination_period: срок прорастания
        color: цвет
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country: str = country
        self.germination_period: str = germination_period
        self.color: str = color

    def __str__(self) -> str:
        """Строковое представление газонной травы."""
        return (
            f"{self.name}, {self.country}, {self.germination_period}, {self.color}, "
            f"{int(self.price)} руб. Остаток: {self.quantity} шт."
        )


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
            raise TypeError("Можно добавлять только объекты Product и его наследников")
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Геттер, возвращающий строку со всеми продуктами в формате:
        "Название продукта, X руб. Остаток: X шт.\n"
        """
        return "".join(f"{p}\n" for p in self._products)

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
