from sqlalchemy import Boolean, Column, Integer, Text, DateTime, false, func

from app.db.base_class import Base


class Customer(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, index=True, nullable=False)
    email = Column(Text, unique=True, index=True, nullable=False)
    password = Column(Text, nullable=False)
    is_admin = Column(Boolean, server_default=false(), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
