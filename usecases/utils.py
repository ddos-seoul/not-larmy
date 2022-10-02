import os
from enum import Enum

SERVER_URL = "https://thirdparty-weather-api-v2.droom.workers.dev"


class WeatherCode(Enum):
    FINE = 0
    CLOUD = 1
    RAIN = 2
    SNOW = 3


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
