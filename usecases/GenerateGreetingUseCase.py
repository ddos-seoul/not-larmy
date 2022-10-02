import aiohttp

from usecases.utils import WeatherCode, make_url, CurrentWeatherDescription


async def call_current(lat, lon):
    async with aiohttp.ClientSession() as session:
        async with session.get(make_url(lat, lon)) as response:
            return await response.json()


def weather_to_str(weather):
    # TODO num 을 타입으로 가지는 weather 객체 선언
    if weather["code"] == WeatherCode.SNOW.value and weather["rain1h"] >= 100:
        return CurrentWeatherDescription.HEAVY_SNOW
    elif weather["code"] == WeatherCode.SNOW.value:
        return CurrentWeatherDescription.LIGHT_SNOW
    elif weather["code"] == WeatherCode.RAIN.value and weather["rain1h"] >= 100:
        return CurrentWeatherDescription.HEAVY_RAIN
    elif weather["code"] == WeatherCode.RAIN.value:
        return CurrentWeatherDescription.LIGHT_RAIN
    elif weather["code"] == WeatherCode.CLOUD.value:
        return CurrentWeatherDescription.LIGHT_CLOUD
    elif weather["code"] == WeatherCode.FINE.value and weather["temp"] >= 30:
        return CurrentWeatherDescription.SHINY
    elif weather["temp"] <= 0:
        return CurrentWeatherDescription.COLD
    return CurrentWeatherDescription.FINE


class GenerateGreetingUseCase:
    def __init__(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon

    async def execute(self):
        response = call_current(self.lat, self.lon)
        return weather_to_str(await response)
