from src.loader import load_from_json
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

    # Демонстрация новых возможностей
    print("=== ДЕМОНСТРАЦИЯ МАГИЧЕСКИХ МЕТОДОВ ===")

    # Выводим строковое представление категории
    print("Строковое представление категории:")
    print(category1)
    print()

    # Выводим строковое представление продукта
    print("Строковое представление продукта:")
    print(product1)
    print()

    # Демонстрация сложения продуктов
    print("Сложение продуктов (общая стоимость):")
    total_value = product1 + product2
    print(f"Суммарная стоимость {product1.name} и {product2.name}: {total_value} руб.")
    print()

    # Демонстрация итерации по категории
    print("Итерация по продуктам категории:")
    for product in category1:
        print(f"  - {product}")
    print()

    # Выводим список товаров категории через геттер
    print("Список товаров категории через геттер:")
    print(category1.products)

    # Добавляем новый продукт через метод add_product
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print("После добавления нового продукта:")
    print(category1.products)
    print(f"Общее количество продуктов: {Category.product_count}")
    print(f"Количество категорий: {Category.category_count}")

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
    print(new_product)

    # Тестируем сеттер цены
    print("\nИзменяем цену продукта:")
    new_product.price = 800
    print(f"Новая цена: {new_product.price} руб.")

    # Попытка установить отрицательную цену
    new_product.price = -100
    print(f"Цена после попытки установить -100: {new_product.price} руб.")
    new_product.price = 0
    print(f"Цена после попытки установить 0: {new_product.price} руб.")

    # Демонстрация загрузки из JSON
    print("\n=== ДЕМОНСТРАЦИЯ ЗАГРУЗКИ ИЗ JSON ===")
    try:
        categories = load_from_json("data/products.json")
        for category in categories:
            print(category)
            for product in category:
                print(f"  - {product}")
    except Exception as e:
        print(f"Ошибка при загрузке из JSON: {e}")
        print("Создайте файл data/products.json для тестирования этой функции")
