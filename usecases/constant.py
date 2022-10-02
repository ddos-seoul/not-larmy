from enum import Enum

SERVER_URL = "https://thirdparty-weather-api-v2.droom.workers.dev"


class WeatherCode(Enum):
    FINE = 0
    CLOUD = 1
    RAIN = 2
    SNOW = 3
