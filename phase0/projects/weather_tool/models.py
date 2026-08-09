class WeatherData:
    """One weather observation or forecast point, for a single city and date."""

    def __init__(
        self,
        city: str,
        date: str,
        temperature_c: float,
        humidity_pct: float,
        wind_speed_kmh: float,
        precipitation_mm: float,
    ) -> None:
        self.city = city
        self.date = date
        self.temperature_c = temperature_c
        self.humidity_pct = humidity_pct
        self.wind_speed_kmh = wind_speed_kmh
        self.precipitation_mm = precipitation_mm

    @property
    def temperature_f(self) -> float:
        return (self.temperature_c * 1.8) + 32

    def to_dict(self) -> dict:
        return {
            "city": self.city,
            "date": self.date,
            "temperature_c": self.temperature_c,
            "humidity_pct": self.humidity_pct,
            "wind_speed_kmh": self.wind_speed_kmh,
            "precipitation_mm": self.precipitation_mm,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "WeatherData":
        return cls(**data)
