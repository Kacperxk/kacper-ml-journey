from .models import WeatherData


class WeatherAnalyzer:
    """Computes stats and comparisons across a collection of WeatherData records."""

    def __init__(self, records: list[WeatherData]) -> None:
        self.records = records

    def min_temperature(self) -> WeatherData:
        return min(self.records, key=lambda x: x.temperature_c)

    def max_temperature(self) -> WeatherData:
        return max(self.records, key=lambda x: x.temperature_c)

    def average_temperature(self, city: str | None = None) -> float:
        try:
            if not city:
                return sum(x.temperature_c for x in self.records) / len(self.records)
            else:
                return sum(
                    x.temperature_c for x in self.records if x.city == city
                ) / len([x for x in self.records if x.city == city])
        except ZeroDivisionError as e:
            raise ValueError(f"List with WeatherData's is empty: {e}") from e

    def compare_cities(self) -> dict[str, float]:
        return {
            city: self.average_temperature(city=city)
            for city in {x.city for x in self.records}
        }


dik1 = {
    "city": "skibidi",
    "date": "21-01",
    "temperature_c": 10.0,
    "humidity_pct": 1.0,
    "wind_speed_kmh": 20.0,
    "precipitation_mm": 30.0,
}

dik3 = {
    "city": "skibidi",
    "date": "21-01",
    "temperature_c": 20.0,
    "humidity_pct": 1.0,
    "wind_speed_kmh": 20.0,
    "precipitation_mm": 30.0,
}

dik2 = {
    "city": "jakarta",
    "date": "22-02",
    "temperature_c": 50.0,
    "humidity_pct": 3.0,
    "wind_speed_kmh": 7.0,
    "precipitation_mm": 6.0,
}
test1 = WeatherData.from_dict(dik1)
test2 = WeatherData.from_dict(dik2)
test3 = WeatherData.from_dict(dik3)

miasta = [test1, test2, test3]

analyze = WeatherAnalyzer(miasta)
ob = analyze.compare_cities()
print(ob)
