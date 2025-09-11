from src.models import Category, LawnGrass, Product, Smartphone

if __name__ == "__main__":
    # Создаем смартфоны
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    smartphone2 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )
    smartphone3 = Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий",
    )

    # Выводим информацию о смартфонах
    print("=== ИНФОРМАЦИЯ О СМАРТФОНАХ ===")
    print(smartphone1)
    print(smartphone2)
    print(smartphone3)

    # Создаем газонную траву
    grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    grass2 = LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )

    # Выводим информацию о газонной траве
    print("\n=== ИНФОРМАЦИЯ О ГАЗОННОЙ ТРАВЕ ===")
    print(grass1)
    print(grass2)

    # Демонстрация сложения товаров одного типа
    print("\n=== СЛОЖЕНИЕ ТОВАРОВ ОДНОГО ТИПА ===")
    smartphone_sum = smartphone1 + smartphone2
    print(f"Суммарная стоимость смартфонов: {smartphone_sum} руб.")

    grass_sum = grass1 + grass2
    print(f"Суммарная стоимость газонной травы: {grass_sum} руб.")

    # Демонстрация ошибки при сложении товаров разных типов
    print("\n=== ПОПЫТКА СЛОЖЕНИЯ ТОВАРОВ РАЗНЫХ ТИПОВ ===")
    try:
        invalid_sum = smartphone1 + grass1
        print(f"Результат сложения: {invalid_sum} руб.")
    except TypeError as e:
        print(f"Ошибка: {e}")

    # Создаем категории
    print("\n=== СОЗДАНИЕ КАТЕГОРИЙ ===")
    category_smartphones = Category(
        "Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2]
    )
    category_grass = Category(
        "Газонная трава", "Различные виды газонной травы", [grass1, grass2]
    )

    # Добавляем продукты в категории
    category_smartphones.add_product(smartphone3)
    print("Продукты в категории 'Смартфоны':")
    print(category_smartphones.products)

    print(f"Общее количество продуктов: {Category.product_count}")

    # Демонстрация ошибки при добавлении не-продукта
    print("\n=== ПОПЫТКА ДОБАВЛЕНИЯ НЕ-ПРОДУКТА ===")
    try:
        category_smartphones.add_product("Not a product")  # type: ignore
        print("Не-продукт успешно добавлен")
    except TypeError as e:
        print(f"Ошибка: {e}")

    # Демонстрация работы с обычными продуктами
    print("\n=== РАБОТА С ОБЫЧНЫМИ ПРОДУКТАМИ ===")
    regular_product = Product("Обычный товар", "Просто товар", 1000.0, 10)
    print(regular_product)

    # Проверка сложения обычных продуктов
    regular_product2 = Product("Другой товар", "Еще товар", 500.0, 5)
    try:
        regular_sum = regular_product + regular_product2
        print(f"Сумма обычных товаров: {regular_sum} руб.")
    except TypeError as e:
        print(f"Ошибка при сложении обычных товаров: {e}")

    # Проверка, что нельзя сложить обычный товар и смартфон
    try:
        mixed_sum = regular_product + smartphone1
        print(f"Сумма обычного товара и смартфона: {mixed_sum} руб.")
    except TypeError as e:
        print(f"Ошибка при сложении разных типов: {e}")
