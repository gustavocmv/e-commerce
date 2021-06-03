from datetime import timedelta
from typing import Any, Optional

import sqlalchemy as sa
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt

from app.config import settings
from app.dependencies import get_current_user, get_db
from app.models import User
from app.schemas import MsgSchema, TokenSchema, UserSchema
from app.security import create_access_token, verify_password

router = APIRouter(
    prefix="/login",
    tags=["login"],
)


@router.post("/access-token", response_model=TokenSchema)
def login_access_token(
    db: sa.orm.Session = get_db,
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = (
        db.execute(sa.select(User).where(User.email == form_data.username))
        .scalars()
        .first()
    )

    if user is None or not verify_password(user.password, form_data.password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.post("/test-token", response_model=UserSchema)
def test_token(current_user: User = get_current_user) -> UserSchema:
    """
    Test access token
    """
    return current_user


@router.post("/password-recovery/{email}", response_model=MsgSchema)
def recover_password(email: str, db: sa.orm.Session = get_db) -> MsgSchema:
    """
    Password Recovery
    """
    user = db.execute(query(User).where(User.email == email)).scalars().first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system.",
        )
    password_reset_token = generate_password_reset_token(email=email)
    send_reset_password_email(
        email_to=user.email, email=email, token=password_reset_token
    )
    return {"msg": "Password recovery email sent"}
