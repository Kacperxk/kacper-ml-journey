from .exceptions import APIError, CityNotFoundError, ParseError
from .models import WeatherData
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

            if not data.get("results"):
                raise CityNotFoundError(f"Couldn't find city named: {city}")

            lat = data["results"][0]["latitude"]
            lon = data["results"][0]["longitude"]

            return lat, lon
        except requests.RequestException as e:
            raise APIError(f"API request failed: {e}") from e

    def get_current(self, city: str) -> WeatherData:
        try:
            lat, lon = self.geocode(city)
            response = requests.get(
                self.weather_url,
                params={
                    "latitude": lat,
                    "longitude": lon,
                    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation",
                },
                timeout=5,
            )
            response.raise_for_status()
            data = response.json()
            current = data["current"]
            weather_dict = {
                "city": city,
                "date": current["time"],
                "temperature_c": current["temperature_2m"],
                "humidity_pct": current["relative_humidity_2m"],
                "wind_speed_kmh": current["wind_speed_10m"],
                "precipitation_mm": current["precipitation"],
            }
            return WeatherData.from_dict(weather_dict)
        except requests.RequestException as e:
            raise APIError(f"API request failed: {e}") from e
        except KeyError as e:
            raise ParseError(f"Missing expected field in response: {e}") from e

    def get_forecast(self, city: str, days: int = 3) -> list[WeatherData]:
        try:
            lat, lon = self.geocode(city)
            response = requests.get(
                self.weather_url,
                params={
                    "latitude": lat,
                    "longitude": lon,
                    "daily": "temperature_2m_mean,relative_humidity_2m_mean,wind_speed_10m_max,precipitation_sum",
                    "timezone": "auto",
                    "forecast_days": days,
                },
                timeout=5,
            )
            response.raise_for_status()
            data = response.json()
            days_data = data["daily"]
            weathers = []
            for time, temperature, humidity, wind, precipitation in zip(
                days_data["time"],
                days_data["temperature_2m_mean"],
                days_data["relative_humidity_2m_mean"],
                days_data["wind_speed_10m_max"],
                days_data["precipitation_sum"],
            ):
                weather_data_dict = {
                    "city": city,
                    "date": time,
                    "temperature_c": temperature,
                    "humidity_pct": humidity,
                    "wind_speed_kmh": wind,
                    "precipitation_mm": precipitation,
                }
                weathers.append(WeatherData.from_dict(weather_data_dict))
            return weathers
        except requests.RequestException as e:
            raise APIError(f"API request failed: {e}") from e
        except KeyError as e:
            raise ParseError(f"Missing expected field in response: {e}") from e
