from typing import List

import sqlalchemy as sa
from fastapi import APIRouter, HTTPException, Path

from app.config import settings
from app.dependencies import get_current_user, get_db
from app.fake_db import seed_users
from app.models import User
from app.schemas import UserSchema
from app.schemas.user import CreateUserSchema
from app.security import hash_password

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/seed", response_model=List[UserSchema])
def create_seed_users(db: sa.orm.Session = get_db):
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
        users.append(user)

    return users


@router.post("", response_model=UserSchema)
def create_user(
    user: CreateUserSchema,
    db: sa.orm.Session = get_db,
) -> UserSchema:
    """
    Create new user.
    """
    try:
        user = User(
            name=user.name,
            email=user.email,
            password=hash_password(user.password),
        )
        db.add(user)
        db.commit()

    except sa.exc.IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="A user with this email already exists.",
        )

    # if settings.EMAILS_ENABLED and user.email:
    #     send_new_account_email(
    #         email_to=user.email,
    #         username=user.email,
    #         password=user.password
    #     )

    return user


@router.get("/me", response_model=UserSchema)
def read_user_me(
    current_user: UserSchema = get_current_user,
) -> UserSchema:
    """
    Get current user.
    """
    return current_user


@router.get("/{user_id}", response_model=UserSchema)
def read_user_by_id(
    user_id: int = Path(...),
    db: sa.orm.Session = get_db,
) -> UserSchema:
    """
    Get a specific user by id.
    """
    return db.get(User, user_id)
