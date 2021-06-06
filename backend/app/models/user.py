import sqlalchemy as sa

from app.db.base_class import Base


class User(Base):
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    name = sa.Column(sa.Text, index=True, nullable=False)
    email = sa.Column(sa.Text, unique=True, index=True, nullable=False)
    password = sa.Column(sa.Text, nullable=False)
    is_admin = sa.Column(sa.Boolean, server_default=sa.false(), nullable=False)
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
        return f"User - ID: {self.id} - Name: {self.name} - Email: {self.email}"

    @classmethod
    def get_by_email(cls, db, email):
        return db.execute(sa.select(User).where(User.email == email)).scalars().first()
