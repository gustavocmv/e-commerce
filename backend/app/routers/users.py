from typing import List

from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.fake_db import seed_users
from app.models import User
from app.schemas import UserSchema
from app.dependencies import get_db


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/seed", response_model=List[UserSchema])
async def create_seed_users(db: Session = get_db):
    users = []
    for user in seed_users:
        user = User(
            name=user["name"],
            email=user["email"],
            password=user["password"],
            is_admin=user["is_admin"],
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        users.append(user)

    return users
