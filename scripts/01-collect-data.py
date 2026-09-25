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
from pandas_datareader import data as pdr

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
    "us10y": "FRED DGS10",
    "jgb10y": "Japan Ministry of Finance",
    "usdjpy": "FRED DEXJPUS",
    "copilot": "AI-generated event list",
}

# TODO
# - Collect FOMC event dates
# - Collect BOJ policy event dates
# - Download US 10Y Treasury yield series from FRED
# - Download USD/JPY exchange rate series from FRED
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
        "policy_action": "Rate Cut",
    },
    {
        "event_name": "FOMC Oct 2025",
        "event_date": "2025-10-29",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Cut",
    },
    {
        "event_name": "FOMC Dec 2025",
        "event_date": "2025-12-10",
        "event_type": "Federal Reserve",
        "policy_action": "Rate Cut",
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

    df["verified_source"] = ("Federal Reserve FOMC Calendar and Statements")

    df["verification_date"] = "2026-09-24"

    df = df[FOMC_COLUMNS]

    df.to_csv(FOMC_FILE, index=False)

    log(f"Created {FOMC_FILE}")

def collect_boj_events():
    """
    Create an empty BOJ events dataset.
    """

    events = [
    {
        "event_name": "BOJ Sep 2023",
        "event_date": "2023-09-22",
        "event_type": "Bank of Japan",
        "policy_action": "Policy Hold",
    },
    {
        "event_name": "BOJ Oct 2023",
        "event_date": "2023-10-31",
        "event_type": "Bank of Japan",
        "policy_action": "YCC Adjustment",
    },
    {
        "event_name": "BOJ Dec 2023",
        "event_date": "2023-12-19",
        "event_type": "Bank of Japan",
        "policy_action": "Policy Hold",
    },
    {
        "event_name": "BOJ Jan 2024",
        "event_date": "2024-01-23",
        "event_type": "Bank of Japan",
        "policy_action": "Policy Hold",
    },
    {
        "event_name": "BOJ Mar 2024",
        "event_date": "2024-03-19",
        "event_type": "Bank of Japan",
        "policy_action": "End YCC / Rate Increase",
    },
    {
        "event_name": "BOJ Apr 2024",
        "event_date": "2024-04-26",
        "event_type": "Bank of Japan",
        "policy_action": "Policy Hold",
    },
    {
        "event_name": "BOJ Jun 2024",
        "event_date": "2024-06-14",
        "event_type": "Bank of Japan",
        "policy_action": "Policy Hold",
    },
    {
        "event_name": "BOJ Jul 2024",
        "event_date": "2024-07-31",
        "event_type": "Bank of Japan",
        "policy_action": "Rate Increase / Bond Purchase Change",
    },
    {
        "event_name": "BOJ Sep 2024",
        "event_date": "2024-09-20",
        "event_type": "Bank of Japan",
        "policy_action": "Policy Hold",
    },
    {
        "event_name": "BOJ Oct 2024",
        "event_date": "2024-10-31",
        "event_type": "Bank of Japan",
        "policy_action": "Policy Hold",
    },
    {
        "event_name": "BOJ Dec 2024",
        "event_date": "2024-12-19",
        "event_type": "Bank of Japan",
        "policy_action": "Policy Hold",
    },
    {
        "event_name": "BOJ Jan 2025",
        "event_date": "2025-01-24",
        "event_type": "Bank of Japan",
        "policy_action": "Rate Increase",
    },
    {
        "event_name": "BOJ Mar 2025",
        "event_date": "2025-03-19",
        "event_type": "Bank of Japan",
        "policy_action": "Policy Hold",
    },
    {
        "event_name": "BOJ May 2025",
        "event_date": "2025-05-01",
        "event_type": "Bank of Japan",
        "policy_action": "Policy Hold",
    },
    {
        "event_name": "BOJ Jun 2025",
        "event_date": "2025-06-17",
        "event_type": "Bank of Japan",
        "policy_action": "Policy Hold",
    },
    {
        "event_name": "BOJ Jul 2025",
        "event_date": "2025-07-31",
        "event_type": "Bank of Japan",
        "policy_action": "Policy Hold",
    },
    {
        "event_name": "BOJ Sep 2025",
        "event_date": "2025-09-19",
        "event_type": "Bank of Japan",
        "policy_action": "Policy Hold",
    },
    {
        "event_name": "BOJ Oct 2025",
        "event_date": "2025-10-30",
        "event_type": "Bank of Japan",
        "policy_action": "Policy Hold",
    },
    {
        "event_name": "BOJ Dec 2025",
        "event_date": "2025-12-19",
        "event_type": "Bank of Japan",
        "policy_action": "Rate Increase",
    },
    {
        "event_name": "BOJ Jan 2026",
        "event_date": "2026-01-23",
        "event_type": "Bank of Japan",
        "policy_action": "Policy Hold",
    },
    {
        "event_name": "BOJ Mar 2026",
        "event_date": "2026-03-19",
        "event_type": "Bank of Japan",
        "policy_action": "Policy Hold",
    },
    {
        "event_name": "BOJ Apr 2026",
        "event_date": "2026-04-28",
        "event_type": "Bank of Japan",
        "policy_action": "Policy Hold",
    },
    {
        "event_name": "BOJ Jun 2026",
        "event_date": "2026-06-16",
        "event_type": "Bank of Japan",
        "policy_action": "Rate Increase",
    },
    {
        "event_name": "BOJ Jul 2026",
        "event_date": "2026-07-31",
        "event_type": "Bank of Japan",
        "policy_action": "Policy Hold",
    },
    {
        "event_name": "BOJ Sep 2026",
        "event_date": "2026-09-18",
        "event_type": "Bank of Japan",
        "policy_action": "Rate Increase",
    }
    ]

    df = pd.DataFrame(events)

    df["retrieval_date"] = RETRIEVAL_DATE

    df["original_source"] = SOURCES["copilot"]

    df["verified_source"] = ("Bank of Japan Official Announcements")

    df["verification_date"] = "2026-09-25"

    df = df[BOJ_COLUMNS]

    df.to_csv(BOJ_FILE, index=False)

    log(f"Created {BOJ_FILE}")

def collect_us10y():
    """
    Collect U.S. 10-Year Treasury yield data from FRED.
    """

    df = pdr.DataReader(
        "DGS10",
        "fred",
        ANALYSIS_START,
        ANALYSIS_END,
    )

    df = df.reset_index()

    df.columns = ["date", "value"]

    df = df.dropna(subset=["value"])

    df["source"] = SOURCES["us10y"]

    df["retrieval_date"] = RETRIEVAL_DATE

    df = df[US10Y_COLUMNS]

    df.to_csv(US10Y_FILE, index=False)

    log(f"Created {US10Y_FILE} ({len(df)} rows)")

def collect_jgb10y():
    """
    Create an empty Japan 10-Year Government Bond dataset.
    """

    df = pd.DataFrame(columns=JGB10Y_COLUMNS)

    df.to_csv(JGB10Y_FILE, index=False)

    log(f"Created {JGB10Y_FILE}")

def collect_usdjpy():
    """
    Collect USD/JPY exchange rate data from FRED.
    """

    df = pdr.DataReader(
        "DEXJPUS",
        "fred",
        ANALYSIS_START,
        ANALYSIS_END,
    )

    df = df.reset_index()

    df.columns = ["date", "value"]

    df = df.dropna(subset=["value"])

    # Convert JPYUSD -> USDJPY
    df["value"] = 1 / df["value"]

    df["source"] = "FRED DEXJPUS"

    df["retrieval_date"] = RETRIEVAL_DATE

    df = df[USDJPY_COLUMNS]

    df.to_csv(USDJPY_FILE, index=False)

    log(f"Created {USDJPY_FILE} ({len(df)} rows)")

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
