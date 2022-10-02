import asyncio
from models.summary import Summary
from usecases.GenerateGreetingUseCase import GenerateGreetingUseCase
from usecases.GenerateHeadsUpUseCase import GenerateHeadsUpUseCase
from usecases.GenerateTemperatureUseCase import GenerateTemperatureUseCase


class GenerateSummaryUseCase:
    def __init__(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon
        self.greeting_maker = GenerateGreetingUseCase(lat, lon)
        self.temperature_maker = GenerateTemperatureUseCase(lat, lon)
        self.heads_up_maker = GenerateHeadsUpUseCase(lat, lon)

    async def execute(self):
        greeting, temperature, heads_up = await asyncio.gather(
            self.greeting_maker.execute(),
            self.temperature_maker.execute(),
            self.heads_up_maker.execute(),
        )
        return Summary(greeting, temperature, heads_up)
