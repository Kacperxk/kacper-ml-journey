class WeatherError(Exception):
    """Base exception for all errors raised by this tool."""

    pass


class APIError(WeatherError):
    """Raised when a request to the Open-Meteo API fails (network error, timeout, non-2xx response)."""


class CityNotFoundError(WeatherError):
    """Raised when a city name can't be resolved to coordinates via geocoding."""


class ParseError(WeatherError):
    """Raised when an API response is missing expected fields or can't be parsed into a WeatherData."""
