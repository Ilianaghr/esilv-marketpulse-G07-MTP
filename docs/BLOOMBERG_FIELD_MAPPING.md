# Bloomberg Field Mapping

## Access mode

`APPROVED_SAMPLE`. The [sample](../data/sample/bloomberg_reference_sample.json) contains teaching data derived from the local prices CSV. Live Bloomberg connectivity remains unverified. The TD09 brief cites `docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md`; the tables below use the two JSON files supplied in this repository.

## Market instruments

| Role | MarketPulse ticker | Bloomberg identifier | Observations |
|---|---|---|---:|
| Instrument | `AAPL` | `AAPL US Equity` | 21 |
| Benchmark | `SP500` | `SPX Index` | 21 |

## Field mapping

Each entry in `series` identifies one instrument and contains its `observations` array. The observation keys below belong to the teaching sample. Live Bloomberg field mnemonics remain unverified.

| MarketPulse field | Source in the sample | Canonical value |
|---|---|---|
| `date` | observation → `observation_date` | String in `YYYY-MM-DD` format |
| `ticker` | series → `canonical_ticker` | `AAPL` or `SP500`, as mapped above |
| `open` | observation → `open_value` | Float |
| `high` | observation → `high_value` | Float |
| `low` | observation → `low_value` | Float |
| `close` | observation → `close_value` | Float |
| `volume` | observation → `volume_value` | Integer, including zero |

## TD10 handoff

Both series cover the same 21 dates from 2026-09-01 through 2026-09-30. All required fields are present and populated. Preserve the zero volume recorded for every SP500 observation.

For each observation, carry the parent series’ canonical ticker into the output row. Compare the resulting 42 rows with the `rows` array in the [expected canonical result](../data/sample/bloomberg_reference_expected.json).
