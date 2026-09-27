"""
02-build-event-study.py

Build the event study for the Economic Research project.

Outputs
-------
data/processed/event-dataset.csv
data/processed/event-study-results.csv
"""

from pathlib import Path
import pandas as pd

# Paths
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

FOMC_FILE = RAW_DIR / "fomc-events.csv"
BOJ_FILE = RAW_DIR / "boj-events.csv"

US10Y_FILE = RAW_DIR / "us10y.csv"
USDJPY_FILE = RAW_DIR / "usdjpy.csv"
JGB10Y_FILE = RAW_DIR / "jgb10y.csv"

DATASET_FILE = PROCESSED_DIR / "event-dataset.csv"


def load_market_data(file_path):
    df = pd.read_csv(file_path)

    df["date"] = pd.to_datetime(df["date"])

    return df.sort_values("date").reset_index(drop=True)


def get_event_window(df, event_date):
    """
    Return T-1, T0, and T+1 observations for an event date.
    """

    event_date = pd.to_datetime(event_date)

    matches = df.index[df["date"] == event_date]

    if len(matches) == 0:
        return None

    idx = matches[0]

    if idx == 0 or idx == len(df) - 1:
        return None

    return {
        "t_minus_1": df.iloc[idx - 1]["value"],
        "event_day": df.iloc[idx]["value"],
        "t_plus_1": df.iloc[idx + 1]["value"],
    }


def build_event_rows(events_df, market_df, series_name):
    rows = []

    for _, event in events_df.iterrows():

        window = get_event_window(
            market_df,
            event["event_date"]
        )

        if window is None:
            continue

        rows.append({
            "event_name": event["event_name"],
            "event_date": event["event_date"],
            "event_type": event["event_type"],
            "policy_action": event["policy_action"],
            "series": series_name,
            "t_minus_1": window["t_minus_1"],
            "event_day": window["event_day"],
            "t_plus_1": window["t_plus_1"],
            "change": window["t_plus_1"] - window["t_minus_1"],
        })

    return rows


def main():

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    fomc = pd.read_csv(FOMC_FILE)
    boj = pd.read_csv(BOJ_FILE)

    us10y = load_market_data(US10Y_FILE)
    usdjpy = load_market_data(USDJPY_FILE)
    jgb10y = load_market_data(JGB10Y_FILE)

    rows = []

    for events in [fomc, boj]:

        rows.extend(
            build_event_rows(events, us10y, "US10Y")
        )

        rows.extend(
            build_event_rows(events, usdjpy, "USDJPY")
        )

        rows.extend(
            build_event_rows(events, jgb10y, "JGB10Y")
        )

    event_dataset = pd.DataFrame(rows)

    event_dataset.to_csv(
        DATASET_FILE,
        index=False
    )

    print(
        f"Created {DATASET_FILE} "
        f"({len(event_dataset)} rows)"
    )


if __name__ == "__main__":
    main()
