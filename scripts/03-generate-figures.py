"""
03-generate-figures.py

Generate figures for the Economic Research project.

Outputs
-------
analysis/figures/figure-01-us10y-vs-jgb10y.png
analysis/figures/figure-02-usdjpy-vs-yield-spread.png
analysis/figures/figure-02b-usdjpy-vs-yield-spread-by-period.png
analysis/figures/figure-03-event-study-comparison.png
"""


import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Set path vars
PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data" / "raw"
DATAP_DIR = PROJECT_ROOT / "data" / "processed"
FIGURES_DIR = PROJECT_ROOT / "analysis" / "figures"

US10Y_FILE = DATA_DIR / "us10y.csv"
JGB10Y_FILE = DATA_DIR / "jgb10y.csv"
USDJPY_FILE = DATA_DIR / "usdjpy.csv"

FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# Load data
us10y = pd.read_csv(US10Y_FILE)
jgb10y = pd.read_csv(JGB10Y_FILE)
usdjpy = pd.read_csv(USDJPY_FILE)

# Convert dates
us10y["date"] = pd.to_datetime(us10y["date"])
jgb10y["date"] = pd.to_datetime(jgb10y["date"])
usdjpy["date"] = pd.to_datetime(usdjpy["date"])

# Figure 1: U.S. 10-Year Treasury Yield vs Japan 10-Year Government Bond Yield

# Create figure
plt.figure(figsize=(12, 6))

# Plot series
plt.plot(
    us10y["date"],
    us10y["value"],
    label="U.S. 10-Year Treasury Yield",
    linewidth=1.5,
)

plt.plot(
    jgb10y["date"],
    jgb10y["value"],
    label="Japan 10-Year Government Bond Yield",
    linewidth=1.5,
)

# YCC Exit reference line
plt.axvline(
    pd.Timestamp("2024-03-19"),
    color="red",
    linestyle="--",
    linewidth=1,
    label="BOJ YCC Exit",
)

# Labels
plt.title(
    "U.S. 10-Year Treasury Yield and Japan 10-Year Government Bond Yield"
)
plt.xlabel("Date")
plt.ylabel("Yield (%)")

plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.text(
    pd.Timestamp("2024-03-19"),
    plt.ylim()[1] - 0.05,
    "BOJ YCC Exit",
    rotation=90,
    verticalalignment="top",
    fontsize=10,
)

# Save figure
plt.savefig(
    FIGURES_DIR / "figure-01-us10y-vs-jgb10y.png",
    dpi=300,
    bbox_inches="tight",
)

plt.close()

print(
    f"Created {FIGURES_DIR / 'figure-01-us10y-vs-jgb10y.png'}"
)

# Figure 2: USD/JPY Exchange Rate vs U.S.-Japan Yield Spread
# Merge datasets
df = (
    us10y.rename(columns={"value": "us10y"})
    .merge(
        jgb10y.rename(columns={"value": "jgb10y"}),
        on="date",
        how="inner",
    )
    .merge(
        usdjpy.rename(columns={"value": "usdjpy"}),
        on="date",
        how="inner",
    )
)

# Calculate yield spread
df["yield_spread"] = df["us10y"] - df["jgb10y"]

# Create figure
fig, ax1 = plt.subplots(figsize=(12, 6))

# USDJPY (left axis)
ax1.plot(
    df["date"],
    df["usdjpy"],
    color="blue",
    linewidth=1.5,
    label="USD/JPY Exchange Rate",
)

ax1.set_xlabel("Date")
ax1.set_ylabel("USD/JPY", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

# Yield spread (right axis)
ax2 = ax1.twinx()

ax2.plot(
    df["date"],
    df["yield_spread"],
    color="green",
    linewidth=1.5,
    label="US-Japan Yield Spread",
)

ax2.set_ylabel(
    "Yield Spread (%)",
    color="green",
)
ax2.tick_params(axis="y", labelcolor="green")

# BOJ YCC Exit Line
ax1.axvline(
    pd.Timestamp("2024-03-19"),
    color="red",
    linestyle="--",
    linewidth=1,
)

ax1.text(
    pd.Timestamp("2024-03-19"),
    ax1.get_ylim()[1] * 0.98,
    "BOJ YCC Exit",
    rotation=90,
    va="top",
)

# Title
plt.title(
    "USD/JPY Exchange Rate and U.S.-Japan Yield Spread"
)

# Combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()

ax1.legend(
    lines1 + lines2,
    labels1 + labels2,
    loc="upper left",
)

plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "figure-02-usdjpy-vs-yield-spread.png",
    dpi=300,
    bbox_inches="tight",
)

plt.close()

print(
    f"Created {FIGURES_DIR / 'figure-02-usdjpy-vs-yield-spread.png'}"
)

# Figure 2B: USD/JPY vs U.S.-Japan Yield Spread by Period

df["period"] = "2025"

df.loc[df["date"] < "2024-03-19", "period"] = "Pre-Exit"
df.loc[
    (df["date"] >= "2024-03-19")
    & (df["date"] < "2025-01-01"),
    "period",
] = "2024"

df.loc[
    (df["date"] >= "2025-01-01")
    & (df["date"] < "2026-01-01"),
    "period",
] = "2025"

df.loc[df["date"] >= "2026-01-01", "period"] = "2026"

colors = {
    "Pre-Exit": "red",
    "2024": "blue",
    "2025": "green",
    "2026": "orange",
}

plt.figure(figsize=(10, 7))

for period, color in colors.items():
    subset = df[df["period"] == period]

    plt.scatter(
        subset["yield_spread"],
        subset["usdjpy"],
        alpha=0.6,
        color=color,
        label=period,
    )

plt.title(
    "USD/JPY Exchange Rate vs U.S.-Japan Yield Spread"
)

plt.xlabel("U.S.-Japan Yield Spread (%)")
plt.ylabel("USD/JPY")

plt.legend(title="Period")
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "figure-02b-usdjpy-vs-yield-spread-by-period.png",
    dpi=300,
    bbox_inches="tight",
)

plt.close()

print(
    f"Created {FIGURES_DIR / 'figure-02b-usdjpy-vs-yield-spread-by-period.png'}"
)

# Figure 3: Event Study Comparison

results = pd.read_csv(
    DATAP_DIR / "event-study-results.csv"
)

boj = results[
    (results["sample"] == "Post-Exit")
    & (results["event_type"] == "Bank of Japan")
    & (results["series"] == "JGB10Y")
]["mean_absolute_change"].iloc[0] * 100

fed = results[
    (results["sample"] == "Post-Exit")
    & (results["event_type"] == "Federal Reserve")
    & (results["series"] == "JGB10Y")
]["mean_absolute_change"].iloc[0] * 100

plt.figure(figsize=(8, 5))

plt.bar(
    ["BOJ", "Federal Reserve"],
    [boj, fed],
    color=["blue", "orange"]
)

plt.axhline(
    y=5,
    color="red",
    linestyle="--",
    label="5 bp threshold"
)

bars = plt.bar(
    ["BOJ", "Federal Reserve"],
    [boj, fed],
    color=["blue", "orange"]
)

# Bar labels
for bar in bars:
    h = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        h + 0.05,
        f"{h:.2f} bp",
        ha="center",
        va="bottom",
        fontweight="bold"
    )

# Difference annotation
difference = fed - boj

plt.text(
    0.5,
    3.6,
    f"Difference = {difference:.2f} bp\nVerdict: Not Supported",
    ha="center",
    bbox=dict(facecolor="white", alpha=0.8)
)

plt.ylabel("Average Absolute Change (basis points)")
plt.title("Post-Exit JGB10Y Event Study Comparison")
plt.legend()

plt.tight_layout()
plt.savefig(
    FIGURES_DIR / "figure-03-event-study-comparison.png",
    dpi=300,
    bbox_inches="tight",
)

plt.close()

print(
    f"Created {FIGURES_DIR / 'figure-03-event-study-comparison.png'}"
)
