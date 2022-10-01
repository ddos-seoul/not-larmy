import dataclasses

from fastapi import APIRouter

from usecases.GenerateSummaryUseCase import GenerateSummaryUseCase

router = APIRouter()


@router.get("/")
async def weather_summary(lat: float, lon: float):
    summary_generator = GenerateSummaryUseCase(lat, lon)
    # 400,
    # 500,

    return dataclasses.asdict(await summary_generator.execute())
