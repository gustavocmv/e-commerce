from fastapi import APIRouter, Path, HTTPException

from app.fake_db import products


router = APIRouter(
    prefix="/products",
    tags=["products"],
)


@router.get("/products")
async def get_products():
    return products


@router.get("/products/{product_id}")
async def get_product(product_id: int = Path(...)):
    for product in products:
        if product["_id"] == product_id:
            return product
    raise HTTPException(404, "Product not found.")
