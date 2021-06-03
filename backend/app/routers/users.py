from typing import List

import sqlalchemy as sa
from fastapi import APIRouter, HTTPException, Path

from app.dependencies import get_current_user, get_db
from app.models import User
from app.schemas import UserSchema
from app.schemas.user import CreateUserSchema, UpdateUserSchema
from app.security import hash_password

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


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


@router.put("/{user_id}", response_model=UserSchema)
def update_user(
    updated_user: UpdateUserSchema,
    user_id: int = Path(...),
    db: sa.orm.Session = get_db,
) -> UserSchema:
    """
    Update a user.
    """
    user = db.get(User, user_id)
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )

    updated_user = updated_user.dict(exclude_unset=True)
    try:
        updated_user["password"] = hash_password(updated_user["password"])
    except KeyError:
        pass

    user.update(updated_user)
    db.commit()

    return user
