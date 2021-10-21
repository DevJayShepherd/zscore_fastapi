from fastapi import APIRouter

from api.routes import zscore_routes


api_router = APIRouter()

api_router.include_router(zscore_routes.router, prefix="/calculate", tags=["zscore"])
