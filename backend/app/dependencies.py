from typing import Generator

from sqlalchemy import select
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from pydantic import ValidationError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm import Session

from app import security
from app.config import settings
from app.db.session import SessionLocal
from app.models import User
from app.schemas import TokenPayloadSchema


reusable_oauth2 = OAuth2PasswordBearer(tokenUrl=f"/login/access-token")


@Depends
def get_db() -> Generator[Session, None, None]:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@Depends
def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> User:
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
    try:
        user = db.execute(
            select(User)
            .where(User.id == token_data.sub)
        ).scalars().one()
        return user
    except NoResultFound:
        raise HTTPException(status_code=404, detail="User not found.")


@Depends
def get_current_admin(
    user: User = get_current_user,
) -> User:
    if not user.is_admin:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return user
