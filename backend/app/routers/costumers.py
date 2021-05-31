from fastapi import APIRouter
from ..fake_db import customers
from ..models.customer import Customer


router = APIRouter(
    prefix="/customers",
    tags=["customers"],
)

@router.get("/seed")
async def create_seed_customers(
    db: Session = get_db_dep()
):
    customer = customers[0]
    db_obj = Customer(
        name=customer["name"],
        email=customer["email"],
        password=customer["password"]
        is_admin=customer["is_admin"]
    )
