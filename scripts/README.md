# Scripts

This folder contains the Python scripts used to collect data, construct the event-study dataset, and generate figures for the economic research project.

## Purpose

The research workflow is designed to be reproducible. Raw source data is stored in `data/raw/`, processed datasets are stored in `data/processed/`, and all transformations are performed through scripts in this folder.

## Execution Order

Scripts should generally be run in the following order:

### 01-collect-data.py

Collects and prepares source datasets.

Inputs:

- Federal Reserve event data
- Bank of Japan event data
- U.S. 10-year Treasury yield data
- Japan 10-year government bond yield data
- USD/JPY exchange-rate data

Outputs:

- `data/raw/fomc-events.csv`
- `data/raw/boj-events.csv`
- `data/raw/us10y.csv`
- `data/raw/jgb10y.csv`
- `data/raw/usdjpy.csv`

### 02-build-event-study.py

Constructs the event-study dataset and applies event-window rules.

Responsibilities:

- Assign Tokyo trading days
- Calculate one-day and two-day event reactions
- Compute absolute yield changes
- Classify observations by event type
- Identify pre-YCC and post-YCC observations

Outputs:

- `data/processed/event-dataset.csv`

### 03-generate-figures.py

Generates summary tables and visualizations for the research paper.

Outputs:

- Research figures
- Summary statistics
- Event-study comparison results

## Design Principles

- Preserve raw source data unchanged.
- Record retrieval dates when collecting data.
- Ensure all calculations are reproducible.
- Prefer script-based transformations over manual spreadsheet edits.
- Keep scripts focused on a single responsibility.

## Status

Script interfaces and expected outputs have been defined.

Implementation is pending data collection and event-study analysis.

## Script Organization

The project intentionally uses a small number of scripts that map directly to the research workflow:

1. Collect source data
2. Build the event-study dataset
3. Generate figures and summary statistics

Additional scripts should only be introduced when complexity justifies further separation of responsibilities.

Current planned scripts:

- `01-collect-data.py`
- `02-build-event-study.py`
- `03-generate-figures.py`

This structure favors readability, reproducibility, and ease of review over a larger collection of narrowly scoped scripts.
