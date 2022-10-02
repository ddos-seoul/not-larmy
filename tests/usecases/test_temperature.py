import random
import unittest

from usecases.GenerateTemperatureUseCase import temp_min_max_str, history_temp_diff_str

SOME_COLD_TEMP = -100
SOME_HOT_TEMP = 100
SOME_RANDOM_NUMBER = random.randrange(0, 10)


class MinMaxTest(unittest.TestCase):
    def test_min_max(self):
        temps = [random.randrange(-30, 30) for _ in range(0, 5)]
        result = temp_min_max_str(temps)
        self.assertEqual(
            result,
            "최고기온은 " + str(max(temps)) + "도, 최저기온은 " + str(min(temps)) + "도 입니다.",
        )


class HistoryStrTest(unittest.TestCase):
    def test_hotter_than_yesterday(self):
        now = random.randrange(15, SOME_HOT_TEMP)
        before = now - SOME_RANDOM_NUMBER
        diff = now - before
        result = history_temp_diff_str(now, before)
        self.assertEqual(result, "어제보다 " + str(diff) + "도 더 덥습니다.")

    def test_less_cold_than_yesterday(self):
        now = random.randrange(SOME_COLD_TEMP, 15)
        before = now - SOME_RANDOM_NUMBER
        diff = now - before
        result = history_temp_diff_str(now, before)
        self.assertEqual(result, "어제보다 " + str(diff) + "도 덜 춥습니다.")

    def test_less_hot_than_yesterday(self):
        now = random.randrange(16, SOME_HOT_TEMP)
        before = now + SOME_RANDOM_NUMBER
        diff = now - before
        result = history_temp_diff_str(now, before)
        self.assertEqual(result, "어제보다 " + str(abs(diff)) + "도 덜 덥습니다.")

    def test_colder_than_yesterday(self):
        now = random.randrange(SOME_COLD_TEMP, 15)
        before = now + SOME_RANDOM_NUMBER
        diff = now - before
        result = history_temp_diff_str(now, before)
        self.assertEqual(result, "어제보다 " + str(abs(diff)) + "도 더 춥습니다.")

    def test_hot(self):
        now = random.randrange(15, SOME_HOT_TEMP)
        before = now
        result = history_temp_diff_str(now, before)
        self.assertEqual(result, "어제와 비슷하게 덥습니다.")

    def test_cold(self):
        now = random.randrange(SOME_COLD_TEMP, 15)
        before = now
        result = history_temp_diff_str(now, before)
        self.assertEqual(result, "어제와 비슷하게 춥습니다.")


if __name__ == "__main__":
    unittest.main()
