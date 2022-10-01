from fastapi import APIRouter
from resolvers.weather import summary

api_router = APIRouter()
api_router.include_router(summary.router, prefix="/summary")
