from fastapi import FastAPI, Path, HTTPException
from .fake_db import products


app = FastAPI()


@app.get('/products')
async def get_products():
    return products

@app.get('/products/{product_id}')
async def get_product(product_id: int = Path(...)):
    for product in products:
        if product["_id"] == product_id:
            return product
    raise HTTPException(404, "Product not found.")
    
