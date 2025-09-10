from src.models import Category, Product

if __name__ == "__main__":
    # Создаем продукты
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создаем категорию с продуктами
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    # Выводим список товаров категории через геттер
    print("Категория Смартфоны:")
    print(category1.products)

    # Добавляем новый продукт через метод add_product
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print("После добавления нового продукта:")
    print(category1.products)
    print(f"Общее количество продуктов: {Category.product_count}")

    # Создаем продукт через classmethod new_product
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    print("Создан новый продукт через new_product:")
    print(
        f"{new_product.name}, {new_product.description}, {new_product.price} руб., {new_product.quantity} шт."
    )

    # Тестируем сеттер цены
    print("\nИзменяем цену продукта:")
    new_product.price = 800
    print(f"Новая цена: {new_product.price} руб.")

    # Попытка установить отрицательную цену
    new_product.price = -100
    print(f"Цена после попытки установить -100: {new_product.price} руб.")
    new_product.price = 0
    print(f"Цена после попытки установить 0: {new_product.price} руб.")
