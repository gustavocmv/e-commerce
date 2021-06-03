from typing import Any

from sqlalchemy.orm import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def update(self, updated_self: dict):
        for attr, value in updated_self.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
