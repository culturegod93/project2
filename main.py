from src.models import Category, Product, ZeroQuantityError

if __name__ == "__main__":
    # Тестирование обработки исключения при создании продукта с нулевым количеством
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ZeroQuantityError as e:
        print(f"Возникла ошибка ZeroQuantityError: {e}")
    else:
        print(
            "Не возникла ошибка ZeroQuantityError при попытке добавить продукт с нулевым количеством"
        )

    # Создание обычных продуктов
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создание категории и расчет средней цены
    category1 = Category(
        "Смартфоны", "Категория смартфонов", [product1, product2, product3]
    )
    print(
        f"Средняя цена в категории '{category1.name}': {category1.middle_price()} руб."
    )

    # Тестирование пустой категории
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(f"Средняя цена в пустой категории: {category_empty.middle_price()} руб.")

    # Демонстрация добавления товаров с обработкой исключений
    print("\n=== ДЕМОНСТРАЦИЯ ДОБАВЛЕНИЯ ТОВАРОВ ===")

    # Попытка добавить валидный товар
    product4 = Product("Новый товар", "Описание", 50000.0, 3)
    category1.add_product(product4)

    # Попытка добавить не-продукт (добавляем аннотацию type: ignore для обхода проверки mypy)
    category1.add_product("не товар")  # type: ignore

    # Попытка добавить товар с нулевым количеством
    try:
        product_zero = Product("Товар с нулем", "Описание", 1000.0, 0)
    except ZeroQuantityError as e:
        print(f"Не удалось создать товар: {e}")
