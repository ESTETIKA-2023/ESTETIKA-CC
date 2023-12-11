from fastapi import APIRouter, FastAPI
from .endpoints import users
from .endpoints import predict
from .endpoints import batik_article
from app.core.config import settings

APIRouter = APIRouter()

def CreateApp():
    app = FastAPI()

    app.include_router(
        users.router,
        prefix = f"{settings.API_PATH}",
        tags = ["Users"]
    )

    app.include_router(
        predict.router,
        prefix = f"{settings.API_PATH}",
        tags = ["Predict"]
    )

    app.include_router(
        batik_article.router,  # Include batik_article router
        prefix=f"{settings.API_PATH}",
        tags=["Batik Article"]
    )
    # app.include_router(
    #     batikshops.router,
    #     prefix = f"{settings.API_PATH}",
    #     tags = ["Batik Shops"]
    # )

    # app.include_router(
    #     batikvillages.router,
    #     prefix = f"{settings.API_PATH}",
    #     tags = ["Batik Villages"]
    # )
    
    # app.include_router(
    #     articles.router,
    #     prefix = f"{settings.API_PATH}",
    #     tags = ["Articles"]
    # )

    return app