import dataclasses

from fastapi import APIRouter, HTTPException

from usecases.GenerateSummaryUseCase import GenerateSummaryUseCase

router = APIRouter()


@router.get("/")
async def weather_summary(lat: float, lon: float):
    try:
        if not (validate_args(lat, lon)):
            raise HTTPException(status_code=400, detail="파라미터 값을-위도와 경도를- 확인해주세요.")
        summary_generator = GenerateSummaryUseCase(lat, lon)
    except Exception as e:
        raise HTTPException(status=500, detail="Internal Server Error")
    return dataclasses.asdict(await summary_generator.execute())


def validate_args(lat, lon):
    return lat >= -90 & lat <= 90 & lon > -180 & lon < 180
