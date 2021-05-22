from fastapi import FastAPI
from .fake_db import products


app = FastAPI()


@app.get('/products')
async def get_products():
    return products

