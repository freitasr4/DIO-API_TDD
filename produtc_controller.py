from fastapi import APIRouter
from app.models.product import Product
from app.schemas.product_schema import ProductSchema

router = APIRouter()

@router.post("/products/")
async def create_product(product: ProductSchema):
    pass

# Implemente outros endpoints aqui
