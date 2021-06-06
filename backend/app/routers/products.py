from base64 import b64decode
from typing import List

import sqlalchemy as sa
from fastapi import APIRouter, HTTPException, Path

from app.dependencies import get_db, verify_admin
from app.fake_db import products
from app.models import Product
from app.schemas import CreateProductSchema, ProductSchema


router = APIRouter(
    prefix="/products",
    tags=["products"],
)


@router.get("", response_model=List[ProductSchema])
def get_products(db: sa.orm.Session = get_db) -> List[ProductSchema]:
    products = db.execute(sa.select(Product)).scalars().all()
    return products


@router.get("/{product_id}", response_model=ProductSchema)
def get_product(
    product_id: int = Path(...),
    db: sa.orm.Session = get_db,
) -> ProductSchema:
    product = db.get(Product, product_id)
    if product is None:
        HTTPException(404, "Product not found.")
    return product


@router.post("", response_model=ProductSchema, dependencies=[verify_admin])
def create_product(
    product: CreateProductSchema,
    db: sa.orm.Session = get_db,
) -> ProductSchema:
    """
    Create new Product.
    """
    product = product.dict(exclude_unset=True)
    if "image" in product:
        product["image"] = b64decode(product["image"])
    product = Product(**product)
    db.add(product)

    try:
        db.commit()
    except sa.exc.IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="A product with that name already exists.",
        )

    return product
