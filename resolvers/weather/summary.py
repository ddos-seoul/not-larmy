from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def weather_summary():
    return "Hello"
