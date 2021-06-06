import sqlalchemy as sa

from app.db.base_class import Base


class Product(Base):
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    name = sa.Column(sa.Text, unique=True, index=True, nullable=False)
    author = sa.Column(sa.Text, nullable=False)
    category = sa.Column(sa.Text, nullable=False)
    description = sa.Column(sa.Text)
    image = sa.Column(sa.dialects.postgresql.BYTEA)
    # price = sa.Column(sa.dialects.postgresql.MONEY, nullable=False)
    price = sa.Column(sa.Numeric(precision=10, scale=2), nullable=False)
    stock = sa.Column(sa.Integer, nullable=False, server_default="0")
    rating = sa.Column(sa.Float)
    reviews = sa.Column(sa.Integer, nullable=False, server_default="0")

    created_at = sa.Column(
        sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
    )
    updated_at = sa.Column(
        sa.DateTime(timezone=True),
        server_default=sa.func.now(),
        onupdate=sa.func.now(),
        nullable=False,
    )

    def __repr__(self):
        return f"Product - ID: {self.id} - Name: {self.name}"

    @classmethod
    def get_by_name(cls, db, name):
        return (
            db.execute(sa.select(Product).where(Product.name == name)).scalars().first()
        )
