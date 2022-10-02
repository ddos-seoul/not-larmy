import unittest

from usecases.GenerateHeadsUpUseCase import forecast_to_str
from usecases.utils import WeatherCode, ForeCastDescription

SNOW_CODE = WeatherCode.SNOW.value
FINE_CODE = WeatherCode.FINE.value
RAIN_CODE = WeatherCode.RAIN.value


class HeadsUpTest(unittest.TestCase):
    def test_snow_tomorrow(self):
        more_than_two_in_24_hours = [dict(code=SNOW_CODE) for x in range(0, 8)]
        result = forecast_to_str(more_than_two_in_24_hours)
        self.assertEqual(result, ForeCastDescription.SNOW_TMR)

    def test_snow_soon(self):
        more_than_two_in_48_hours = [dict(code=FINE_CODE) for x in range(0, 4)] + [
            dict(code=SNOW_CODE) for x in range(0, 4)
        ]
        result = forecast_to_str(more_than_two_in_48_hours)
        self.assertEqual(result, ForeCastDescription.SNOW_SOON)

    def test_rain_tomorrow(self):
        more_than_two_in_24_hours = [dict(code=RAIN_CODE) for x in range(0, 8)]
        result = forecast_to_str(more_than_two_in_24_hours)
        self.assertEqual(result, ForeCastDescription.RAIN_TMR)

    def test_rain_soon(self):
        more_than_two_in_48_hours = [dict(code=FINE_CODE) for x in range(0, 4)] + [
            dict(code=RAIN_CODE) for x in range(0, 4)
        ]
        result = forecast_to_str(more_than_two_in_48_hours)
        self.assertEqual(result, ForeCastDescription.RAIN_SOON)

    def test_fine(self):
        once = [dict(code=FINE_CODE) for x in range(0, 7)] + [dict(code=SNOW_CODE)]
        result = forecast_to_str(once)
        self.assertEqual(result, ForeCastDescription.FINE)


if __name__ == "__main__":
    unittest.main()
