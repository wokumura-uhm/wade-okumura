"""
01-collect-data.py

Collect source data for the Economic Research project.

Outputs
-------
data/raw/fomc-events.csv
data/raw/boj-events.csv
data/raw/us10y.csv
data/raw/jgb10y.csv
data/raw/usdjpy.csv
"""

from pathlib import Path
from datetime import datetime
import pandas as pd

# Define path variables
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

RAW_DIR = PROJECT_ROOT / "data" / "raw"

# Define the analysis period and retrieval date
ANALYSIS_START = "2023-09-01"
ANALYSIS_END = "2026-09-23"
RETRIEVAL_DATE = datetime.now().date().isoformat()

# Output path constants
FOMC_FILE = RAW_DIR / "fomc-events.csv"
BOJ_FILE = RAW_DIR / "boj-events.csv"
US10Y_FILE = RAW_DIR / "us10y.csv"
JGB10Y_FILE = RAW_DIR / "jgb10y.csv"
USDJPY_FILE = RAW_DIR / "usdjpy.csv"

# CSV schema definitions
EVENT_COLUMNS = [
    "event_name",
    "event_date",
    "event_type",
    "policy_action",
    "original_source",
    "retrieval_date",
    "verified_source",
    "verification_date",
]

MARKET_COLUMNS = [
    "date",
    "value",
    "source",
    "retrieval_date",
]

FOMC_COLUMNS = EVENT_COLUMNS
BOJ_COLUMNS = EVENT_COLUMNS

US10Y_COLUMNS = MARKET_COLUMNS
JGB10Y_COLUMNS = MARKET_COLUMNS
USDJPY_COLUMNS = MARKET_COLUMNS

# Source definitions
SOURCES = {
    "fomc": "Federal Reserve",
    "boj": "Bank of Japan",
    "us10y": "FRED",
    "jgb10y": "Japan Ministry of Finance",
    "usdjpy": "FRED",
    "copilot": "AI-generated event list (unverified)",
}

# TODO
# - Collect FOMC event dates
# - Collect BOJ policy event dates
# - Download US 10Y Treasury yield series
# - Download USD/JPY exchange rate series
# - Download JGB 10Y yield series

def ensure_directories():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

def log(message: str):
    """
    Log a message to the console.
    """
    print(f"[INFO] {message}")

def collect_fomc_events():
    """
    Collect FOMC policy events.
    """

    events = [
    {
        "event_name": "FOMC Sep 2023",
        "event_date": "2023-09-20",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Hold",
    },
    {
        "event_name": "FOMC Nov 2023",
        "event_date": "2023-11-01",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Hold",
    },
    {
        "event_name": "FOMC Dec 2023",
        "event_date": "2023-12-13",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Hold",
    },
    {
        "event_name": "FOMC Jan 2024",
        "event_date": "2024-01-31",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Hold",
    },
    {
        "event_name": "FOMC Mar 2024",
        "event_date": "2024-03-20",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Hold",
    },
    {
        "event_name": "FOMC May 2024",
        "event_date": "2024-05-01",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Hold",
    },
    {
        "event_name": "FOMC Jun 2024",
        "event_date": "2024-06-12",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Hold",
    },
    {
        "event_name": "FOMC Jul 2024",
        "event_date": "2024-07-31",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Hold",
    },
    {
        "event_name": "FOMC Sep 2024",
        "event_date": "2024-09-18",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Cut",
    },
    {
        "event_name": "FOMC Nov 2024",
        "event_date": "2024-11-07",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Cut",
    },
    {
        "event_name": "FOMC Dec 2024",
        "event_date": "2024-12-18",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Cut",
    },
    {
        "event_name": "FOMC Jan 2025",
        "event_date": "2025-01-29",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Hold",
    },
    {
        "event_name": "FOMC Mar 2025",
        "event_date": "2025-03-19",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Hold",
    },
    {
        "event_name": "FOMC May 2025",
        "event_date": "2025-05-07",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Hold",
    },
    {
        "event_name": "FOMC Jun 2025",
        "event_date": "2025-06-18",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Hold",
    },
    {
        "event_name": "FOMC Jul 2025",
        "event_date": "2025-07-30",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Hold",
    },
    {
        "event_name": "FOMC Sep 2025",
        "event_date": "2025-09-17",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Hold",
    },
    {
        "event_name": "FOMC Oct 2025",
        "event_date": "2025-10-29",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Hold",
    },
    {
        "event_name": "FOMC Dec 2025",
        "event_date": "2025-12-10",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Hold",
    },
    {
        "event_name": "FOMC Jan 2026",
        "event_date": "2026-01-28",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Hold",
    },
    {
        "event_name": "FOMC Mar 2026",
        "event_date": "2026-03-18",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Hold",
    },
    {
        "event_name": "FOMC Apr 2026",
        "event_date": "2026-04-29",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Hold",
    },
    {
        "event_name": "FOMC Jun 2026",
        "event_date": "2026-06-17",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Hold",
    },
    {
        "event_name": "FOMC Jul 2026",
        "event_date": "2026-07-29",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Hold",
    },
    {
        "event_name": "FOMC Sep 2026",
        "event_date": "2026-09-16",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Increase",
    }
    ]

    df = pd.DataFrame(events)

    df["retrieval_date"] = RETRIEVAL_DATE

    df["original_source"] = SOURCES["copilot"]

    df["verified_source"] = ""

    df["verification_date"] = ""

    df = df[FOMC_COLUMNS]

    df.to_csv(FOMC_FILE, index=False)

    log(f"Created {FOMC_FILE}")

def collect_boj_events():
    """
    Create an empty BOJ events dataset.
    """

    df = pd.DataFrame(columns=BOJ_COLUMNS)

    df.to_csv(BOJ_FILE, index=False)

    log(f"Created {BOJ_FILE}")

def collect_us10y():
    """
    Create an empty U.S. 10-Year Treasury dataset.
    """

    df = pd.DataFrame(columns=US10Y_COLUMNS)

    df.to_csv(US10Y_FILE, index=False)

    log(f"Created {US10Y_FILE}")

def collect_jgb10y():
    """
    Create an empty Japan 10-Year Government Bond dataset.
    """

    df = pd.DataFrame(columns=JGB10Y_COLUMNS)

    df.to_csv(JGB10Y_FILE, index=False)

    log(f"Created {JGB10Y_FILE}")

def collect_usdjpy():
    """
    Create an empty USD/JPY dataset.
    """

    df = pd.DataFrame(columns=USDJPY_COLUMNS)

    df.to_csv(USDJPY_FILE, index=False)

    log(f"Created {USDJPY_FILE}")

def main():

    ensure_directories()

    log("Collecting FOMC events ...")
    collect_fomc_events()

    log("Collecting BOJ events...")
    collect_boj_events()

    log("Collecting U.S. 10-Year Treasury yield data ...")
    collect_us10y()

    log("Collecting Japan 10-Year Government Bond yield data ...")
    collect_jgb10y()

    log("Collecting USD/JPY data ...")
    collect_usdjpy()

    log("Data collection complete.")

if __name__ == "__main__":
    main()
