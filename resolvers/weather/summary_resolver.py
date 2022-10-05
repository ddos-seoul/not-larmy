import dataclasses
from xmlrpc.client import Boolean

from fastapi import APIRouter, HTTPException

from usecases.GenerateSummaryUseCase import GenerateSummaryUseCase

router = APIRouter()


@router.get("/")
async def weather_summary(lat: float, lon: float):
    if not(validate_args(lat,lon)):
        raise HTTPException(status_code=400, detail="arguments 확인 필요")
    try:
        summary_generator = GenerateSummaryUseCase(lat, lon)
        summary_dict = dataclasses.asdict(await summary_generator.execute())
        summary_dict["heads-up"] = summary_dict.pop("heads_up")
    except:
        raise HTTPException(status_code=500, detail="서버 에러입니다.")
    return summary_dict


def validate_args(lat: float, lon: float) -> Boolean:
    return (lat >= -90.0) & (lat <= 90.0) & (lon > -180.0) & (lon < 180.0)
