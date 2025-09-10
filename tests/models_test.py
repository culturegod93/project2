from src.models import Category, Product


def test_product_price_setter(monkeypatch):
    p = Product("Test", "Desc", 100, 5)
    p.price = 200
    assert p.price == 200

    # проверка отрицательной цены
    p.price = -50
    assert p.price == 200  # должно остаться прежнее значение

    # проверка снижения цены с отменой
    monkeypatch.setattr("builtins.input", lambda _: "n")
    p.price = 150
    assert p.price == 200

    # подтверждение снижения
    monkeypatch.setattr("builtins.input", lambda _: "y")
    p.price = 150
    assert p.price == 150


def test_new_product():
    data = {"name": "Prod", "description": "Desc", "price": 100, "quantity": 5}
    p = Product.new_product(data)
    assert isinstance(p, Product)
    assert p.name == "Prod"
    assert p.description == "Desc"
    assert p.price == 100
    assert p.quantity == 5


def test_category_add_product():
    c = Category("Cat", "Desc")
    assert c.products == ""
    p = Product("Item", "Desc", 10, 1)
    c.add_product(p)
    assert "Item" in c.products
    assert Category.product_count >= 1
