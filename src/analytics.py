"""Compare price series that use the canonical market-data fields."""


def index_by_date(prices):
    return {row["date"]: row for row in prices}


def align_series(instrument_prices, benchmark_prices):
    instrument_by_date = index_by_date(instrument_prices)
    benchmark_by_date = index_by_date(benchmark_prices)
    common_dates = sorted(instrument_by_date.keys() & benchmark_by_date.keys())

    aligned_instrument = [instrument_by_date[date] for date in common_dates]
    aligned_benchmark = [benchmark_by_date[date] for date in common_dates]
    return aligned_instrument, aligned_benchmark


def calculate_period_return(prices):
    """Return the percentage change from the first to the last aligned close."""
    first_close = prices[0]["close"]
    last_close = prices[-1]["close"]
    return (last_close / first_close - 1) * 100


def calculate_base_100(prices):
    """Rebase every close to the first observation in the aligned series."""
    first_close = prices[0]["close"]
    return [
        {
            "date": row["date"],
            "ticker": row["ticker"],
            "value": row["close"] / first_close * 100,
        }
        for row in prices
    ]


def calculate_relative_performance(instrument_return, benchmark_return):
    """Return the difference in percentage points."""
    return instrument_return - benchmark_return
