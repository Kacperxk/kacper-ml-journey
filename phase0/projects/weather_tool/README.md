# CLI Weather Tool

Command-line tool that fetches current weather and multi-day forecasts from
the Open-Meteo API, saves results locally as JSON, and computes stats and
city comparisons across saved data. Full spec: `docs/phase0/projects.md`.

## Usage

```
python -m weather_tool.cli current Warsaw
python -m weather_tool.cli current Warsaw --save data.json
python -m weather_tool.cli forecast Warsaw --days 5 --save data.json
python -m weather_tool.cli stats data.json
python -m weather_tool.cli stats data.json --average --city Warsaw
python -m weather_tool.cli stats data.json --min --max --compare
```

`--save` appends to an existing file instead of overwriting, so records from
multiple cities and runs accumulate into one file for `stats` to compare.

## Structure

- `exceptions.py` — custom exception hierarchy (`WeatherError` and subclasses)
- `models.py` — `WeatherData`
- `fetcher.py` — `WeatherFetcher`, talks to the Open-Meteo API
- `analyzer.py` — `WeatherAnalyzer`, stats across records
- `storage.py` — save/load records as JSON
- `cli.py` — argparse entry point

## Errors

Bad city names, API/network failures, and missing or corrupted files all
raise typed exceptions (`exceptions.py`), caught once in `cli.py`'s `main()`
and printed as a clean one-line message — no raw tracebacks.

---

*Status: done — see `phase0/README.md`.*
