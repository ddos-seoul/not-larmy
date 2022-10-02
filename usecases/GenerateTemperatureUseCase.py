import asyncio
import os

import aiohttp

from usecases.GenerateGreetingUseCase import make_url
from usecases.constant import SERVER_URL


class GenerateTemperatureUseCase:
    def __init__(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon

    async def execute(self):
        urls = make_urls_historical(self.lat, self.lon)
        loop = asyncio.get_event_loop()
        async with aiohttp.ClientSession(loop=loop) as session:
            results = await asyncio.gather(
                *[loop.create_task(fetch(session, url)) for url in urls]
            )
            return history_to_str(results)


def history_to_str(results: list):
    temps = list(map(lambda x: x["temp"], results))
    current = temps[0]
    day_ago = temps[4]
    diff_str = history_temp_diff_str(current, day_ago)
    min_max_str = temp_min_max_str(temps)
    return diff_str + " " + min_max_str


def history_temp_diff_str(now, before):
    diff = now - before
    if diff > 0:  # 온도가 올라간 경우
        if now >= 15:
            return "어제보다 " + str(diff) + "도 더 덥습니다."
        else:
            return "어제보다 " + str(diff) + "도 덜 춥습니다."
    elif diff < 0:  # 온도가 내려간 경우
        if now >= 15:
            return "어제보다 " + str(abs(diff)) + "도 덜 덥습니다."
        else:
            return "어제보다 " + str(abs(diff)) + "도 더 춥습니다."
    else:
        if now >= 15:
            return "어제와 비슷하게 덥습니다."
        else:
            return "어제와 비슷하게 춥습니다."


def temp_min_max_str(temps):
    return "최고기온은 " + str(max(temps)) + "도, 최저기온은 " + str(min(temps)) + "도 입니다."


async def fetch(session, url):
    # TODO make util
    async with session.get(url) as response:
        return await response.json()


def make_urls_historical(lat, lon):
    current = [make_url(lat, lon)]
    befores = list(
        map(
            lambda hour_offset: make_url_before(lat, lon, hour_offset),
            [-6, -12, -18, -24],
        )
    )
    return current + befores


def make_url_before(lat, lon, before):
    return (
        SERVER_URL
        + "/historical/hourly?lat="
        + str(lat)
        + "&lon="
        + str(lon)
        + "&hour_offset="
        + str(before)
        + "&api_key="
        + os.environ["AWS_API_KEY"]
    )
