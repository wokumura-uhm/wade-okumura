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
- usdjpy.csv = FRED DEXJPUS
- jgb10y.csv = Source download

## Processed Data

Processed datasets contain transformations used for analysis.

Examples:
- USD/JPY converted to standard market convention
- Event windows merged with market series
- Return calculations
