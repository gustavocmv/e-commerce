# %%
import sqlalchemy as sa

from app.db.session import SessionLocal
from app.models import User
from app.schemas import CreateUserSchema
from app.security import hash_password

# %%
db: sa.orm.Session = SessionLocal()

# %%
user = CreateUserSchema(
    name="Gustavo Carvalho", email="cmv.gustavo@gmail.com", password="1234"
)

# %%
user = User(email=user.email, name=user.name, password=hash_password(user.password))

# %%
print(user.created_at)
print(user.is_admin)


# %%
db.add(user)

# %%
try:
    db.commit()
except sa.exc.IntegrityError as err:
    print(err)
    e = err
    db.rollback()


# %%
print(user.created_at)
print(user.is_admin)

# %%
db.refresh(user)

# %%
user = User(id=7)

# %%
user.name

# %%
db.add(user)

# %%

user = db.get(User, 4)

# %%
user

# %%
