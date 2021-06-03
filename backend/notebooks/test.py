# %%
from sqlalchemy import select
from sqlalchemy.orm.exc import NoResultFound

from app.db.session import SessionLocal
from app.entities import User

from os import environ
print(environ['SQLALCHEMY_WARN_20'])


# %%
db = SessionLocal()

# %%
try:
    user = db.execute(select(User).where(User.id == 2)).scalars().one()
except NoResultFound:
    print('deu ruim')

# %%
try:
    user = db.execute(select(User).where(User.id == 1)).scalars()
except NoResultFound:
    print('deu ruim')


# %%
dir(user)
# %%
user.all()
# %%
# %%
print(db.query(User).filter(User.id == 1).first().name)
# %%
