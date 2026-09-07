---
type: spec
capability: marginal-analysis
engagement: perfect-competition
date: 2026-09-07
status: draft            # draft | built | audited
built_with: "Copilot, from this file"
---

# Capability — model specification

## Purpose

This model determines the profit-maximizing allocation of tomato, carrot, and mesclun beds subject to labor availability, worker hiring limits, land availability, crop capacity limits, fertilizer costs, and diminishing returns.

The model must identify the optimal planting mix, expected profit, labor utilization, and worker requirements.

## Inputs — the named contract

| Name | Value | Unit | Source |
| --- | --- | --- | --- |
| `TOM_MAX_BEDS` | 20 | num beds | Case scenario, crop table |
| `TOM_PRICE` | 8800 | USD per bed | Case scenario, crop table |
| `TOM_HRS` | 2.5 | hours per week per bed | Case scenario, crop table |
| `TOM_FERT_COST` | 880 | USD per bed | Case scenario, crop table |
| `TOM_DIM_PCT` | 0.10 | percent per bed | Case scenario, crop table |
| `CAR_MAX_BEDS` | 20 | num beds | Case scenario, crop table |
| `CAR_PRICE` | 2094 | USD per bed | Case scenario, crop table |
| `CAR_HRS` | 0.833 | hours per week per bed | Case scenario, crop table |
| `CAR_FERT_COST` | 440 | USD per bed | Case scenario, crop table |
| `CAR_DIM_PCT` | 0.025 | percent per bed | Case scenario, crop table |
| `MES_MAX_BEDS` | 30 | num beds | Case scenario, crop table |
| `MES_PRICE` | 2700 | USD per bed | Case scenario, crop table |
| `MES_HRS` | 1.25 | hours per week per bed | Case scenario, crop table |
| `MES_FERT_COST` | 880 | USD per bed | Case scenario, crop table |
| `MES_DIM_PCT` | 0.0125 | percent per bed | Case scenario, crop table |
| `TOTAL_BEDS` | 64 | num beds | Case scenario |
| `FARMER_HOURS` | 720 | hours | Case scenario |
| `TEMP_WORKER_HOURS` | 1440 | max hours per worker | Case scenario |
| `MAX_TEMP_WORKERS` | 4 | max num workers | Case scenario |
| `BED_FIXED_COST` | 20000 | USD | Case scenario |
| `FARMER_SALARY` | 50000 | USD | Case scenario |
| `FARMER_RATE` | 34.72 | USD per hour | Case scenario |
| `TEMP_RATE` | 17.36 | USD per hour | Case scenario |
| `SEASON_WEEKS` | 36 | num weeks | Case scenario |

DIM_PCT values are stored as decimal percentages (10% = 0.10, 2.5% = 0.025, 1.25% = 0.0125).

## Structure

Five sheets.

- Inputs
  - One row per named input in Section 1.
  - Columns: Name, Value, Unit, Source.
  - Contains no formulas.

- CostStructure
  - Calculates total labor hours, farmer hours used, temporary labor hours used,
    temporary workers required, farmer labor cost, temporary labor cost,
    blended labor rate, fertilizer cost, fixed cost, and total cost at the
    current planting levels.

- MCSchedules
  - One block per crop (tomatoes, carrots, mesclun).
  - Quantity q = 0 through MAX_BEDS for that crop.
  - Columns: q, labor hours, labor cost, fertilizer cost, total cost,
    marginal cost, revenue, marginal revenue, and profit contribution.

- Optimization
  - Decision variables TOM_BEDS, CAR_BEDS, and MES_BEDS.
  - Objective function TOTAL_PROFIT.
  - Solver objective: Maximize TOTAL_PROFIT.
  - Solver changing cells: TOM_BEDS, CAR_BEDS, MES_BEDS.
  - Solver Method: GRG Nonlinear.
  - Constraint calculations for:
    - TOM_BEDS <= TOM_MAX_BEDS
    - CAR_BEDS <= CAR_MAX_BEDS
    - MES_BEDS <= MES_MAX_BEDS
    - TOM_BEDS + CAR_BEDS + MES_BEDS <= TOTAL_BEDS
    - TEMP_HOURS_USED <= MAX_TEMP_WORKERS x TEMP_WORKER_HOURS
    - All bed allocations are integers.

- Checks
  - One row per validation rule from Section 4.
  - Columns: Expected Result, Actual Result, PASS/FAIL.

## Calculation logic

TOM_LABOR_HRS(q) =
q × TOM_HRS × SEASON_WEEKS × (1 + TOM_DIM_PCT)^q

CAR_LABOR_HRS(q) =
q × CAR_HRS × SEASON_WEEKS × (1 + CAR_DIM_PCT)^q

MES_LABOR_HRS(q) =
q × MES_HRS × SEASON_WEEKS × (1 + MES_DIM_PCT)^q

TOTAL_LABOR_HRS =
TOM_LABOR_HRS(TOM_BEDS) +
CAR_LABOR_HRS(CAR_BEDS) +
MES_LABOR_HRS(MES_BEDS)

FARMER_HOURS_USED =
MIN(TOTAL_LABOR_HRS, FARMER_HOURS)

TEMP_HOURS_USED =
MAX(0, TOTAL_LABOR_HRS − FARMER_HOURS)

TEMP_WORKERS_USED =
CEILING(TEMP_HOURS_USED ÷ TEMP_WORKER_HOURS)

FARMER_LABOR_COST = FARMER_HOURS_USED x FARMER_RATE

TEMP_LABOR_COST = TEMP_HOURS_USED x TEMP_RATE

TOTAL_LABOR_COST = FARMER_LABOR_COST + TEMP_LABOR_COST

BLENDED_LABOR_RATE =
IF(TOTAL_LABOR_HRS = 0, 0, TOTAL_LABOR_COST ÷ TOTAL_LABOR_HRS)

TOM_REVENUE(q) =
q × TOM_PRICE

CAR_REVENUE(q) =
q × CAR_PRICE

MES_REVENUE(q) =
q × MES_PRICE

TOTAL_REVENUE =
TOM_REVENUE(TOM_BEDS) +
CAR_REVENUE(CAR_BEDS) +
MES_REVENUE(MES_BEDS)

TOTAL_FERTILIZER_COST =
(TOM_BEDS × TOM_FERT_COST) +
(CAR_BEDS × CAR_FERT_COST) +
(MES_BEDS × MES_FERT_COST)

TOTAL_FIXED_COST =
BED_FIXED_COST

TOTAL_VARIABLE_COST =
TOTAL_LABOR_COST +
TOTAL_FERTILIZER_COST

TOTAL_PROFIT =
TOTAL_REVENUE − TOTAL_VARIABLE_COST − TOTAL_FIXED_COST

For each crop schedule, the other two crops are held at zero beds.

TOTAL_COST(q) =
Crop_specific labor cost(q) +
Crop-specific fertilizer cost(q)

Fixed costs are excluded from TOTL_COST(q).

MC(q) =
TOTAL_COST(q) - TOTAL_COST(q-1)

MC(0) is blank.

TOTAL_LABOR_USED =
TOTAL_LABOR_HRS

TOTAL_LABOR_AVAILABLE =
FARMER_HOURS +
(MAX_TEMP_WORKERS × TEMP_WORKER_HOURS)

UNUSED_LABOR_HOURS =
TOTAL_LABOR_AVAILABLE − TOTAL_LABOR_USED

UNUSED_BEDS =
TOTAL_BEDS −
(TOM_BEDS + CAR_BEDS + MES_BEDS)

## Conventions

- Bed allocations must be whole integers.
- Negative bed allocations are not allowed.
- Total allocated beds may not exceed TOTAL_BEDS.
- Crop allocations may not exceed crop-specific maximums.
- Unused beds are permitted.
- Labor hours may remain unused.
- DIM_PCT compounds labor hours and does not reduce crop yield, price per bed, revenue per bed, or fertilizer cost per bed. Revenue and fertilizer cost are linear in bed quantity.
- All currency values are reported in USD.
- Labor hours are rounded to two decimal places for reporting only.
- Farmer labor hours are consumed before temporary worker hours.
- Temporary workers cover labor requirements beyond FARMER_HOURS.
- Labor costs are allocated to the P&L using the blended labor rate.

## Validation rules

Structural Checks

- No spreadsheet error cells (#n/A, #VALUE!, #DIV/0!, etc.).
- Every calculated cell contains a formula.
- Every input cell contains a constant value.
- Total allocated beds <= TOTAL_BEDS.
- Crop allocations <= crop maximums.

Acceptance Criteria

- Optimal mix = 10 tomatoes, 20 carrots, 30 mesclun.
- Season profit = $42,762 ± $5.
- LABOR_HRS(1) for tomatoes = 99.

## Outputs

OPT_TOM_BEDS
OPT_CAR_BEDS
OPT_MES_BEDS

TOTAL_REVENUE
TOTAL_VARIABLE_COST
TOTAL_FIXED_COST
TOTAL_PROFIT

TOTAL_LABOR_USED
TOTAL_LABOR_AVAILABLE
UNUSED_LABOR_HOURS

TEMP_WORKERS_USED
UNUSED_BEDS

## Audit findings

Added AFTER the build. For each check: what you checked, what you found, what
you did about it.
