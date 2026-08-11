from .fetcher import WeatherFetcher
from .analyzer import WeatherAnalyzer
from .models import WeatherData
from .storage import save_records, load_records
from pathlib import Path
import argparse


def save_or_append(records: list[WeatherData], path: str) -> None:
    if Path(path).exists():
        saved_data = load_records(path)
        saved_data.extend(records)
        save_records(saved_data, path)
    else:
        save_records(records, path)


def main():
    fetcher = WeatherFetcher()

    parser = argparse.ArgumentParser(description="Does something useful")
    subparsers = parser.add_subparsers(dest="command")

    current_parser = subparsers.add_parser("current")
    forecast_parser = subparsers.add_parser("forecast")
    stats_parser = subparsers.add_parser("stats")

    current_parser.add_argument("city")
    current_parser.add_argument("--save")

    forecast_parser.add_argument("city")
    forecast_parser.add_argument("--days", type=int, default=3)
    forecast_parser.add_argument("--save")

    stats_parser.add_argument("path")
    stats_parser.add_argument("--city")
    stats_parser.add_argument("--min", action="store_true")
    stats_parser.add_argument("--max", action="store_true")
    stats_parser.add_argument("--average", action="store_true")
    stats_parser.add_argument("--compare", action="store_true")

    args = parser.parse_args()
    if args.command == "current":
        current_data = fetcher.get_current(args.city)
        if args.save:
            save_or_append([current_data], args.save)
        print(current_data.to_dict())
    elif args.command == "forecast":
        forecast_data = fetcher.get_forecast(args.city, args.days)
        if args.save:
            save_or_append(forecast_data, args.save)
        print([x.to_dict() for x in forecast_data])
    elif args.command == "stats":
        stored_data = load_records(args.path)
        analyzer = WeatherAnalyzer(stored_data)
        if not any([args.min, args.max, args.average, args.compare]):
            args.min = args.max = args.average = args.compare = True
        if args.min:
            min_record = analyzer.min_temperature()
            print(min_record.to_dict())
        if args.max:
            max_record = analyzer.max_temperature()
            print(max_record.to_dict())
        if args.average:
            print(analyzer.average_temperature(args.city))
        if args.compare:
            print(analyzer.compare_cities())


if __name__ == "__main__":
    main()
