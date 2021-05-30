from sqlalchemy import Boolean, Column, Integer, Text, DateTime
from sqlalchemy.sql import func

from app.db.base_class import Base


class Costumer(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, index=True, nullable=False)
    email = Column(Text, unique=True, index=True, nullable=False)
    password = Column(Text, nullable=False)
    is_admin = Column(Boolean, server_default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_onupdate=func.now())
