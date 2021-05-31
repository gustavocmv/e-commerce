from fastapi import APIRouter

from app.fake_db import seed_customers
from app.models.customer import Customer, CustomersModel
from app.dependencies import get_db


router = APIRouter(
    prefix="/customers",
    tags=["customers"],
)


@router.get("/seed", response_model=CustomersModel)
async def create_seed_customers(db = get_db):
    customers = []
    for customer in seed_customers:
        customer = Customer(
            name=customer["name"],
            email=customer["email"],
            password=customer["password"],
            is_admin=customer["is_admin"],
        )
        db.add(customer)
        db.commit()
        db.refresh(customer)
        customers.append(customer)

    return customers
