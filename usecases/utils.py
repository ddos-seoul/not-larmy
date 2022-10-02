import os
from enum import Enum

SERVER_URL = "https://thirdparty-weather-api-v2.droom.workers.dev"


class WeatherCode(Enum):
    FINE = 0
    CLOUD = 1
    RAIN = 2
    SNOW = 3


class CurrentWeatherDescription(Enum):
    HEAVY_SNOW = "폭설이 내리고 있어요."
    LIGHT_SNOW = "눈이 포슬포슬 내립니다."
    HEAVY_RAIN = "폭우가 내리고 있어요."
    LIGHT_RAIN = "비가 오고 있습니다."
    LIGHT_CLOUD = "날씨가 약간은 칙칙해요."
    SHINY = "따사로운 햇살을 맞으세요."
    COLD = "날이 참 춥네요."
    FINE = "날씨가 참 맑습니다."


class ForeCastDescription(Enum):
    SNOW_TMR = "내일 폭설이 내릴 수도 있으니 외출 시 주의하세요."
    SNOW_SOON = "눈이 내릴 예정이니 외출 시 주의하세요."
    RAIN_TMR = "폭우가 내릴 예정이에요. 우산을 미리 챙겨두세요."
    RAIN_SOON = "며칠동안 비 소식이 있어요."
    FINE = "날씨는 대체로 평온할 예정이에요."


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


# TODO url 생성 통합함수 만들기 or 찾기
def make_url(lat, lon):
    return (
        SERVER_URL
        + "/current?lat="
        + str(lat)
        + "&lon="
        + str(lon)
        + "&api_key="
        + os.environ["AWS_API_KEY"]
    )
