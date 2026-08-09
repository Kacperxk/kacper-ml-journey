from .exceptions import APIError, CityNotFoundError
import requests


class WeatherFetcher:
    """Fetches weather data from Open-Meteo API"""

    def __init__(
        self,
        weather_url: str = "https://api.open-meteo.com/v1/forecast",
        geocoding_url: str = "https://geocoding-api.open-meteo.com/v1/search",
    ) -> None:
        self.weather_url = weather_url
        self.geocoding_url = geocoding_url

    def geocode(self, city: str) -> tuple[float, float]:
        try:
            response = requests.get(
                self.geocoding_url,
                params={"name": city, "count": 1},
                timeout=5,
            )
            response.raise_for_status()
            data = response.json()

            if "results" not in data:
                raise CityNotFoundError(f"Couldn't find city named: {city}")

            lat = data["results"][0]["latitude"]
            lon = data["results"][0]["longitude"]

            return lat, lon
        except requests.RequestException as e:
            raise APIError(f"API request failed: {e}") from e

    def get_current(self, city: str) -> str:
        try:
            lat, lon = self.geocode(city)
            response = requests.get(
                self.weather_url,
                params={"latitude": lat, "longitude": lon, "hourly": "temperature_2m"},
            )
            response.raise_for_status()
            data = response.json()
            return data
        except requests.RequestException as e:
            raise APIError(f"API request failed: {e}") from e
