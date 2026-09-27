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
RESULTS_FILE = PROCESSED_DIR / "event-study-results.csv"

def load_market_data(file_path):
    df = pd.read_csv(file_path)

    df["date"] = pd.to_datetime(df["date"])

    return df.sort_values("date").reset_index(drop=True)

def get_event_window(df, event_date):
    """
    Return the last available trading observation before the event date
    and the first available trading observation after the event date.
    """
    event_date = pd.to_datetime(event_date)

    before = df[df["date"] < event_date]
    after = df[df["date"] > event_date]

    if before.empty or after.empty:
        return None

    t_minus_1 = before.iloc[-1]
    t_plus_1 = after.iloc[0]

    return {
        "t_minus_1_date": t_minus_1["date"],
        "t_minus_1_value": t_minus_1["value"],
        "t_plus_1_date": t_plus_1["date"],
        "t_plus_1_value": t_plus_1["value"],
    }

def build_event_rows(events_df, market_df, series_name):
    rows = []

    for _, event in events_df.iterrows():

        window = get_event_window(
            market_df,
            event["event_date"]
        )

        if window is None:
            print(
                f"[WARNING] Unable to build {series_name} event window | "
                f"{event['event_type']} | "
                f"{event['event_date']} | "
                f"series range: "
                f"{market_df['date'].min().date()} to "
                f"{market_df['date'].max().date()}"
            )
            continue

        rows.append({
            "event_name": event["event_name"],
            "event_date": event["event_date"],
            "event_type": event["event_type"],
            "policy_action": event["policy_action"],
            "series": series_name,
            "t_minus_1_date": window["t_minus_1_date"],
            "t_minus_1_value": window["t_minus_1_value"],
            "t_plus_1_date": window["t_plus_1_date"],
            "t_plus_1_value": window["t_plus_1_value"],
            "change": window["t_plus_1_value"] - window["t_minus_1_value"],
            "absolute_change": abs(window["t_plus_1_value"] - window["t_minus_1_value"]),
        })

    return rows


def main():

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    # Load the raw data
    fomc = pd.read_csv(FOMC_FILE)
    boj = pd.read_csv(BOJ_FILE)

    us10y = load_market_data(US10Y_FILE)
    usdjpy = load_market_data(USDJPY_FILE)
    jgb10y = load_market_data(JGB10Y_FILE)

    rows = []

    # Generate event_dataset
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

    value_columns = [
        "t_minus_1_value",
        "t_plus_1_value",
        "change",
        "absolute_change",
    ]

    event_dataset[value_columns] = (
        event_dataset[value_columns].round(6)
    )

    event_dataset.to_csv(
        DATASET_FILE,
        index=False
    )

    print(
        f"Created {DATASET_FILE} "
        f"({len(event_dataset)} rows)"
    )

    # Generate event-study-results
    results = (
        event_dataset
        .groupby(["event_type", "series"])
        .agg(
            count=("change", "count"),
            mean_change=("change", "mean"),
            mean_absolute_change=("absolute_change", "mean"),
            std_change=("change", "std"),
            std_absolute_change=("absolute_change", "std"),
        )
        .reset_index()
    )

    numeric_columns = [
    "mean_change",
    "mean_absolute_change",
    "std_change",
    "std_absolute_change",
    ]

    results[numeric_columns] = (
        results[numeric_columns]
        .round(6)
    )

    results = results.sort_values(
        ["series", "event_type"]
    ).reset_index(drop=True)

    results.to_csv(
        RESULTS_FILE,
        index=False
    )

    print("\nEvent Study Results")
    print(results)

    print(
        f"Created {RESULTS_FILE} "
        f"({len(results)} rows)"
    )

if __name__ == "__main__":
    main()
