from typing import Optional, List

from pydantic import BaseModel, EmailStr

# Shared properties
class UserBaseSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    is_admin: Optional[bool] = True


# Properties to receive via API on creation
class CreateUserSchema(UserBaseSchema):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UpdateUserSchema(UserBaseSchema):
    password: Optional[str] = None


class UserInDBBaseSchema(UserBaseSchema):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class UserSchema(UserInDBBaseSchema):
    pass


# Additional properties stored in DB
class UserInDBSchema(UserInDBBaseSchema):
    password: str
