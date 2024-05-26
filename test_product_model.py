from app.models.product import Product

def test_create_product():
    product_data = {
        "name": "Test Product",
        "price": 10.0,
        "description": "Test description"
    }
    product = Product(**product_data)
    assert product.name == "Test Product"
    assert product.price == 10.0
    assert product.description == "Test description"
