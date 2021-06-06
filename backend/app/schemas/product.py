from base64 import b64encode
from decimal import Decimal
from typing import Optional, Union
from filetype import guess_mime

from pydantic import BaseModel, validator


# Shared properties
class ProductBaseSchema(BaseModel):
    name: Optional[str] = None
    author: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    price: Optional[Decimal] = None
    # stock: Optional[int] = None
    # rating: Optional[float] = None
    # reviews: Optional[int] = None

    @validator("image", pre=True)
    def cast_to_base64(cls, image: Union[bytes, str, None]):
        if image is None:
            return
        if isinstance(image, bytes):
            image = (
                f"data:{guess_mime(image)};base64,{b64encode(image).decode('utf-8')}"
            )
        return image


# Properties to receive via API on creation
class CreateProductSchema(ProductBaseSchema):
    name: str
    author: str
    category: str
    description: str
    price: Decimal


# Properties to receive via API on update
class UpdateProductSchema(ProductBaseSchema):
    stock: Optional[int] = None
    rating: Optional[float] = None
    reviews: Optional[int] = None


class ProductInDBBaseSchema(ProductBaseSchema):
    id: Optional[int] = None
    stock: Optional[int] = None
    rating: Optional[float] = None
    reviews: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class ProductSchema(ProductInDBBaseSchema):
    stock: Optional[int] = None
    rating: Optional[float] = None
    reviews: Optional[int] = None


# Additional properties stored in DB
class ProductInDBSchema(ProductInDBBaseSchema):
    pass
