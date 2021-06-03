from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy import select
from sqlalchemy.orm import Session

from app import security
from app.config import settings
from app.db.session import SessionLocal
from app.models import User
from app.schemas import TokenPayloadSchema

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl=f"/login/access-token")


@Depends
def validate_token(token: str = Depends(reusable_oauth2)) -> TokenPayloadSchema:
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[security.ALGORITHM],
        )
        token_data = TokenPayloadSchema(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    return token_data


@Depends
def get_db() -> Generator[Session, None, None]:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@Depends
def get_current_user(
    db: Session = get_db, token_data: TokenPayloadSchema = validate_token
) -> User:
    user = db.get(User, token_data.sub)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    return user


# @Depends
# def get_current_admin(
#     user: User = get_current_user,
# ) -> User:
#     if not user.is_admin:
#         raise HTTPException(
#             status_code=400, detail="The user doesn't have enough privileges"
#         )
#     return user
