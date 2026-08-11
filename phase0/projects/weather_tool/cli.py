from .fetcher import WeatherFetcher
from .storage import save_records, load_records
import argparse


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

    args = parser.parse_args()
    if args.command == "current":
        current_data = fetcher.get_current(args.city)
        if args.save:
            save_records([current_data], args.save)
        print(current_data.to_dict())

    elif args.command == "forecast":
        forecast_data = fetcher.get_forecast(args.city, args.days)
        if args.save:
            save_records(forecast_data, args.save)
        print([x.to_dict() for x in forecast_data])


if __name__ == "__main__":
    main()
