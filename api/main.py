from fastapi import FastAPI
from api.core.settings import settings

from api.db.session import engine
from api.db.base_class import Base
from api.base import api_router


app = FastAPI(title=settings.TITLE, version=settings.VERSION)


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_api():
    api = FastAPI(title=settings.TITLE, version=settings.VERSION)
    create_tables()
    api.include_router(api_router)
    return api


app = start_api()
