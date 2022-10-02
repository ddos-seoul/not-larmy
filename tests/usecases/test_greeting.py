import random
import unittest

from usecases.GenerateGreetingUseCase import weather_to_str
from usecases.utils import CurrentWeatherDescription, WeatherCode

ANY_TEMP = random.randrange(-100, 100)
TEMP_30 = random.randrange(30, 100)
UNDER_ZERO = random.randrange(-100, 0)
OVER_ZERO = random.randrange(1, 30)
LESS_THAN_100_RAIN = random.randrange(0, 99)
MORE_THAN_100_RAIN = random.randrange(100, 3000)
ANY_RAIN = random.randrange(0, 3000)

SNOW = WeatherCode.SNOW.value
RAIN = WeatherCode.RAIN.value
CLOUD = WeatherCode.CLOUD.value
FINE = WeatherCode.FINE.value


class GreetingTest(unittest.TestCase):
    def test_heavy_snow(self):
        # TODO change to mock
        response = dict(code=SNOW, rain1h=MORE_THAN_100_RAIN, temp=ANY_TEMP)
        result = weather_to_str(response)
        self.assertEqual(result, CurrentWeatherDescription.HEAVY_SNOW)

    def test_light_snow(self):
        response = dict(code=SNOW, rain1h=LESS_THAN_100_RAIN, temp=ANY_TEMP)
        result = weather_to_str(response)
        self.assertEqual(result, CurrentWeatherDescription.LIGHT_SNOW)

    def test_heavy_rain(self):
        response = dict(code=RAIN, rain1h=MORE_THAN_100_RAIN, temp=ANY_TEMP)
        result = weather_to_str(response)
        self.assertEqual(result, CurrentWeatherDescription.HEAVY_RAIN)

    def test_light_rain(self):
        response = dict(code=RAIN, rain1h=LESS_THAN_100_RAIN, temp=ANY_TEMP)
        result = weather_to_str(response)
        self.assertEqual(result, CurrentWeatherDescription.LIGHT_RAIN)

    def test_light_cloud(self):
        response = dict(code=CLOUD, rain1h=ANY_RAIN, temp=ANY_TEMP)
        result = weather_to_str(response)
        self.assertEqual(result, CurrentWeatherDescription.LIGHT_CLOUD)

    def test_shiny(self):
        response = dict(code=FINE, rain1h=ANY_RAIN, temp=TEMP_30)
        result = weather_to_str(response)
        self.assertEqual(result, CurrentWeatherDescription.SHINY)

    def test_freezing_cold(self):
        response = dict(code=FINE, rain1h=ANY_RAIN, temp=UNDER_ZERO)
        result = weather_to_str(response)
        self.assertEqual(result, CurrentWeatherDescription.COLD)

    def test_else(self):
        response = dict(code=FINE, rain1h=ANY_RAIN, temp=OVER_ZERO)
        result = weather_to_str(response)
        self.assertEqual(result, CurrentWeatherDescription.FINE)


if __name__ == "__main__":
    unittest.main()
