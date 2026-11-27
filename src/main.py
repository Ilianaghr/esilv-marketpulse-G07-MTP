from pathlib import Path
import argparse
import csv
import json

from analytics import (
    align_series,
    calculate_base_100,
    calculate_period_return,
    calculate_relative_performance,
)
from providers.bloomberg_provider import fetch_approved_sample_prices


DATA_DIR = Path("data/sample")

# These starter values mirror config/settings.yml.
# settings.yml is a human-readable configuration contract in the CORE.
# Parsing YAML is optional and is not required by the 18-hour lab sequence.
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"
BLOOMBERG_SAMPLE_LABEL = "Bloomberg stage - APPROVED_SAMPLE"
YAHOO_LABEL = "Yahoo Finance via yfinance"


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return [normalize_price_row(row) for row in csv.DictReader(file)]


def normalize_price_row(row):
    return {
        "date": row["date"],
        "ticker": row["ticker"],
        "open": float(row["open"]),
        "high": float(row["high"]),
        "low": float(row["low"]),
        "close": float(row["close"]),
        "volume": int(row["volume"]),
    }


def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]


def get_first_date(prices):
    return prices[0]["date"]


def get_last_date(prices):
    return prices[-1]["date"]


def get_first_close(prices):
    return prices[0]["close"]


def get_last_close(prices):
    return prices[-1]["close"]


def display_market_summary(asset, prices, show_currency=True):
    first_close = get_first_close(prices)
    last_close = get_last_close(prices)

    print(f"{asset['ticker']} - {asset['name']}")
    print(f"Market       : {asset['market']}")
    print(f"Observations : {len(prices)}")
    print(f"First date   : {get_first_date(prices)}")
    print(f"Last date    : {get_last_date(prices)}")

    if show_currency:
        print(f"First close  : {first_close:.2f} {asset['currency']}")
        print(f"Last close   : {last_close:.2f} {asset['currency']}")
    else:
        print(f"First close  : {first_close:.2f}")
        print(f"Last close   : {last_close:.2f}")


def build_market_snapshot(provider="bloomberg"):
    """Acquire and compare the two series for terminal and dashboard consumers."""
    instruments = load_instruments()

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    tickers = (instrument["ticker"], benchmark["ticker"])
    if provider == "bloomberg":
        prices = fetch_approved_sample_prices(tickers)
        provider_label = BLOOMBERG_SAMPLE_LABEL
    elif provider == "yahoo":
        from providers.yahoo_provider import fetch_yahoo_prices

        prices = {ticker: fetch_yahoo_prices(ticker) for ticker in tickers}
        provider_label = YAHOO_LABEL
    else:
        raise ValueError(f"Unsupported provider: {provider}")

    aligned_instrument, aligned_benchmark = align_series(
        prices[instrument["ticker"]], prices[benchmark["ticker"]]
    )
    if not aligned_instrument:
        raise ValueError("No common dates between the instrument and benchmark.")

    instrument_return = calculate_period_return(aligned_instrument)
    benchmark_return = calculate_period_return(aligned_benchmark)
    return {
        "provider": provider_label,
        "lookback": LOOKBACK_LABEL,
        "interval": INTERVAL_LABEL,
        "instrument": instrument,
        "benchmark": benchmark,
        "instrument_prices": aligned_instrument,
        "benchmark_prices": aligned_benchmark,
        "instrument_return": instrument_return,
        "benchmark_return": benchmark_return,
        "relative_performance": calculate_relative_performance(
            instrument_return, benchmark_return
        ),
        "instrument_base_100": calculate_base_100(aligned_instrument),
        "benchmark_base_100": calculate_base_100(aligned_benchmark),
    }


def display_market_snapshot(snapshot):
    instrument = snapshot["instrument"]
    benchmark = snapshot["benchmark"]
    instrument_base_100 = snapshot["instrument_base_100"]
    benchmark_base_100 = snapshot["benchmark_base_100"]

    print("=== MarketPulse ===")
    print()

    print("Market configuration")
    print(f"Provider : {snapshot['provider']}")
    print(f"Period   : {snapshot['lookback']}")
    print(f"Interval : {snapshot['interval']}")
    print()

    print("Instrument")
    display_market_summary(
        instrument,
        snapshot["instrument_prices"],
        show_currency=True,
    )
    print(f"Period return: {snapshot['instrument_return']:.2f}%")

    print()

    print("Benchmark")
    display_market_summary(
        benchmark,
        snapshot["benchmark_prices"],
        show_currency=False,
    )
    print(f"Period return: {snapshot['benchmark_return']:.2f}%")

    print()
    print("Relative performance")
    print(
        f"{instrument['ticker']} vs {benchmark['ticker']} : "
        f"{snapshot['relative_performance']:+.2f} percentage points"
    )

    print()
    print("Base 100")
    print(
        f"{instrument['ticker']} : "
        f"{instrument_base_100[0]['value']:.2f} -> {instrument_base_100[-1]['value']:.2f}"
    )
    print(
        f"{benchmark['ticker']} : "
        f"{benchmark_base_100[0]['value']:.2f} -> {benchmark_base_100[-1]['value']:.2f}"
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description="Compare the MarketPulse series.")
    parser.add_argument(
        "--provider",
        choices=("bloomberg", "yahoo"),
        default="bloomberg",
        help="use the approved Bloomberg sample (default) or Yahoo Finance",
    )
    args = parser.parse_args(argv)
    try:
        snapshot = build_market_snapshot(args.provider)
    except ValueError as error:
        raise SystemExit(str(error)) from error
    display_market_snapshot(snapshot)


if __name__ == "__main__":
    main()
