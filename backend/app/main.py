from fastapi import FastAPI, Path, HTTPException

from app.config import settings
from app.routers import (
    costumers,
    products,
)


app = FastAPI()

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app.include_router(costumers.router)
app.include_router(products.router)
