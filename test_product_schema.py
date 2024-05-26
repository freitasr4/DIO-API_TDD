from app.schemas.product_schema import ProductSchema

def test_product_schema():
    product_data = {
        "name": "Test Product",
        "price": 10.0,
        "description": "Test description"
    }
    product_schema = ProductSchema(**product_data)
    assert product_schema.name == "Test Product"
    assert product_schema.price == 10.0
    assert product_schema.description == "Test description"
