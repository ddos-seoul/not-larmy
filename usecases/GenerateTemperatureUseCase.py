from models.summary import Summary


class GenerateTemperatureUseCase:
    def __init__(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon

    async def execute(self):
        print(self.lat, self.lon)
        return "temperature"
