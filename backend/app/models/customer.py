from typing import Optional, List

from pydantic import BaseModel, EmailStr
from sqlalchemy import Boolean, Column, Integer, Text, DateTime, false, func

from app.db.base_class import Base


class Customer(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, index=True, nullable=False)
    email = Column(Text, unique=True, index=True, nullable=False)
    password = Column(Text, nullable=False)
    is_admin = Column(Boolean, server_default=false(), nullable=False)
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )


# Shared properties
class CustomerBaseModel(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    is_admin: Optional[bool] = True


# Properties to receive via API on creation
class CustomerCreateModel(CustomerBaseModel):
    email: EmailStr
    password: str


# Properties to receive via API on update
class CustomerUpdateModel(CustomerBaseModel):
    password: Optional[str] = None


class CustomerInDBBaseModel(CustomerBaseModel):
    id: Optional[int] = None

    class ConfigModel:
        orm_mode = True


# Additional properties to return via API
class CustomerModel(CustomerInDBBaseModel):
    pass


class CustomersModel(BaseModel):
    customers: List[CustomerModel]


# Additional properties stored in DB
class CustomerInDBModel(CustomerInDBBaseModel):
    hashed_password: str
