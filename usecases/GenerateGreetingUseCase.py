import os
from enum import Enum

import requests

from usecases.constant import SERVER_URL


class GenerateGreetingUseCase:
    def __init__(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon

    async def execute(self):
        forecast_current = requests.get(
            SERVER_URL
            + "/current?lat="
            + str(self.lat)
            + "&lon="
            + str(self.lon)
            + "&api_key="
            + str(os.environ["AWS_API_KEY"])
        )
        return weather_to_str(forecast_current.json())


def weather_to_str(weather):
    # TODO num 을 타입으로 가지는 weather 객체 선언
    if weather["code"] == WeatherCode.SNOW.value and weather["rain1h"] >= 100:
        return "폭설이 내리고 있어요."
    elif weather["code"] == WeatherCode.SNOW.value:
        return "눈이 포슬포슬 내립니다."
    elif weather["code"] == WeatherCode.RAIN.value and weather["rain1h"] >= 100:
        return "폭우가 내리고 있어요."
    elif weather["code"] == WeatherCode.RAIN.value:
        return "비가 오고 있습니다."
    elif weather["code"] == WeatherCode.CLOUD.value:
        return "날씨가 약간은 칙칙해요."
    elif weather["code"] == WeatherCode.FINE.value and weather["temp"] >= 30:
        return "따사로운 햇살을 맞으세요."
    elif weather["temp"] <= 0:
        return "날이 참 춥네요."
    return "날씨가 참 맑습니다."


class WeatherCode(Enum):
    FINE = 0
    CLOUD = 1
    RAIN = 2
    SNOW = 3
