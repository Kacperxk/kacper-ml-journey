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
        matching = (
            self.records if not city else [x for x in self.records if x.city == city]
        )
        if not matching:
            if city:
                raise ValueError(f"No records found for the city: {city}")
            raise ValueError("No records to average")
        return sum(x.temperature_c for x in matching) / len(matching)

    def compare_cities(self) -> dict[str, float]:
        return {
            city: self.average_temperature(city=city)
            for city in {x.city for x in self.records}
        }
