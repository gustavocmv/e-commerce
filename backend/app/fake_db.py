from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

seed_users = [
    {
        "name": "Gustavo",
        "email": "admin@example.com",
        "password": pwd_context.hash("1234"),
        "is_admin": True,
    },
    {
        "name": "John",
        "email": "john@example.com",
        "password": pwd_context.hash("1234"),
        "is_admin": False,
    },
]

products = [
    {
        "_id": 1,
        "name": "O Jardim das Aflições",
        "author": "Olavo de Carvalho",
        "image": "/images/jardim.jpg",
        "rating": 4.3,
        "numReviews": 3,
        "price": 49.90,
        "description": "An awesome book.",
        "countInStock": 15,
    },
    {
        "_id": 2,
        "name": "O Mínimo que Você Precisa Saber para não Ser um Idiota",
        "author": "Olavo de Carvalho",
        "image": "/images/jardim.jpg",
        "rating": 4.3,
        "numReviews": 3,
        "price": 39.90,
        "description": "An awesome book.",
        "countInStock": 10,
    },
    {
        "_id": 3,
        "name": "Os 4 Temperamentos",
        "author": "Ítalo Marsili",
        "image": "/images/jardim.jpg",
        "rating": 4.3,
        "numReviews": 3,
        "price": 49.90,
        "description": "An awesome book.",
        "countInStock": 0,
    },
    {
        "_id": 4,
        "name": "As Crônicas de Nárnia",
        "author": "C. S. Lewis",
        "image": "https://flxt.tmsimg.com/assets/p90695_p_v10_ab.jpg",
        "rating": 3.3,
        "numReviews": 3,
        "price": 109.90,
        "description": "An awesome bosok.",
        "countInStock": 0,
    },
]
