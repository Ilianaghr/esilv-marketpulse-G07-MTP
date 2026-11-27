"""Normalize the approved Bloomberg teaching sample using the TD09 mapping."""

import json
from pathlib import Path


BLOOMBERG_IDENTIFIERS = {"AAPL": "AAPL US Equity", "SP500": "SPX Index"}
REFERENCE_SAMPLE = (
    Path(__file__).resolve().parents[2] / "data/sample/bloomberg_reference_sample.json"
)


def load_bloomberg_reference_sample(path=REFERENCE_SAMPLE):
    with open(path, encoding="utf-8") as file:
        payload = json.load(file)

    if (
        payload.get("access_mode") != "approved_sample"
        or payload.get("is_live_bloomberg_output") is not False
    ):
        raise ValueError("Expected an approved Bloomberg teaching sample.")
    return payload["series"]


def normalize_reference_series(series):
    canonical_ticker = series["canonical_ticker"]
    return [
        {
            "date": observation["observation_date"],
            "ticker": canonical_ticker,
            "open": float(observation["open_value"]),
            "high": float(observation["high_value"]),
            "low": float(observation["low_value"]),
            "close": float(observation["close_value"]),
            "volume": int(observation["volume_value"]),
        }
        for observation in series["observations"]
    ]


def fetch_approved_sample_prices(tickers):
    """Load the sample once and return canonical rows for each requested ticker."""
    series_by_identifier = {
        series["provider_identifier"]: series
        for series in load_bloomberg_reference_sample()
    }
    prices_by_ticker = {}
    for ticker in tickers:
        if ticker not in BLOOMBERG_IDENTIFIERS:
            raise ValueError(f"Unsupported Bloomberg ticker: {ticker}")
        identifier = BLOOMBERG_IDENTIFIERS[ticker]
        series = series_by_identifier.get(identifier)
        if series is None or series["canonical_ticker"] != ticker:
            raise ValueError(f"Approved Bloomberg series not found for {ticker}: {identifier}")
        rows = normalize_reference_series(series)
        if not rows:
            raise ValueError(f"Approved Bloomberg series has no observations for {ticker}.")
        prices_by_ticker[ticker] = rows
    return prices_by_ticker
