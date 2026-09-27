# Data

This folder contains the sourced inputs and generated datasets used in the economic-research event study.

## Folder Structure

```text
data/
├── raw/
│   ├── fomc-events.csv
│   ├── boj-events.csv
│   ├── us10y.csv
│   ├── jgb10y.csv
│   └── usdjpy.csv
│
├── processed/
│   ├── event-dataset.csv
│   └── event-study-results.csv
│
└── README.md
```

## Raw Data

Raw datasets replicate source systems without transformation.

- us10y.csv = FRED DGS10
- usdjpy.csv = FRED DEXJPUS series, quoted as Japanese yen per U.S. dollar
- jgb10y.csv = Ministry of Finance Japan 10-year government bond yield series

## Processed Data

Processed datasets contain transformations used for analysis.
Examples:

- Event windows merged with market series
- Event-window change calculations
