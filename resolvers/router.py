from fastapi import APIRouter
from resolvers.weather import summary_resolver

api_router = APIRouter()
api_router.include_router(summary_resolver.router, prefix="/summary")
