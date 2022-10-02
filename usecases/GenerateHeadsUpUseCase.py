import os

import aiohttp
import asyncio

from usecases.utils import SERVER_URL, WeatherCode, fetch

POINT_GAP = 6


class GenerateHeadsUpUseCase:
    def __init__(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon

    async def execute(self):
        urls = make_urls_forecast(self.lat, self.lon)
        loop = asyncio.get_event_loop()
        async with aiohttp.ClientSession(loop=loop) as session:
            results = await asyncio.gather(
                *[loop.create_task(fetch(session, url)) for url in urls]
            )
            return forecast_to_str(results)


def forecast_to_str(results):
    results_to_codes = [x["code"] for x in results]
    a_day = results_to_codes[0:3]
    two_days = results_to_codes
    if a_day.count(WeatherCode.SNOW.value) >= 2:
        return "내일 폭설이 내릴 수도 있으니 외출 시 주의하세요."
    elif two_days.count(WeatherCode.SNOW.value) >= 2:
        return "눈이 내릴 예정이니 외출 시 주의하세요."
    elif a_day.count(WeatherCode.RAIN.value) >= 2:
        return "폭우가 내릴 예정이에요. 우산을 미리 챙겨두세요."
    elif two_days.count(WeatherCode.RAIN.value) >= 2:
        return "며칠동안 비 소식이 있어요."
    else:
        return "날씨는 대체로 평온할 예정이에요."


def make_urls_forecast(lat, lon):
    hours = [x * POINT_GAP for x in range(1, 9)]
    urls = [make_url_forecast(lat, lon, hour) for hour in hours]
    return urls


def make_url_forecast(lat, lon, hour_offset):
    return (
        SERVER_URL
        + "/forecast/hourly?lat="
        + str(lat)
        + "&lon="
        + str(lon)
        + "&hour_offset="
        + str(hour_offset)
        + "&api_key="
        + os.environ["AWS_API_KEY"]
    )
