---
type: spec
capability: marginal-analysis
engagement: perfect-competition
date: 2026-09-07
status: audited            # draft | built | audited
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
| `CAR_HRS` | 0.833333333333333 | hours per week per bed | Case scenario; displayed as 0.833 |
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
| `FARMER_SEASON_HRS` | 1440 | hours | Derived from case assumptions: 2 x FARMER_HOURS |
| `FARMER_SALARY` | 50000 | USD | Case scenario |
| `FARMER_RATE` | 34.7222222222 | USD per hour | Derived: FARMER_SALARY / FARMER_SEASON_HRS |
| `TEMP_COST_EACH` | 25000 | USD per worker per season | Case scenario |
| `TEMP_RATE` | 17.3611111111 | USD per hour | Derived: TEMP_COST_EACH / TEMP_WORKER_HOURS |
| `SEASON_WEEKS` | 36 | num weeks | Case scenario |

DIM_PCT values are stored as decimal percentages (10% = 0.10, 2.5% = 0.025, 1.25% = 0.0125).
Create workbook-level named ranges for every input listed in this section.

## Structure

Five sheets.

- Inputs
  - One row per named input in the Inputs section.
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
  - Columns: q, labor hours, labor cost, fertilizer cost, total cost, marginal cost, revenue, marginal revenue, and profit contribution.
  - For each crop schedule, labor cost(q) shall be calculated using the same farmer-first allocation logic used by the full model. The other two crops are held at zero beds.
  - BLENDED_LABOR_RATE shall not be used in schedule calculations.

- Optimization
  - Decision variables TOM_BEDS, CAR_BEDS, and MES_BEDS.
  - Objective function TOTAL_PROFIT.
  - Solver objective: Maximize TOTAL_PROFIT.
  - Solver changing cells: TOM_BEDS, CAR_BEDS, MES_BEDS.
  - Solver Method: GRG Nonlinear.
  - The workbook shall be delivered with decision variables set to zero and acceptance checks are evaluated only after Solver is executed.
  - All outputs listed in Section "Outputs" shall be implemented as workbook-level named ranges.
  - Constraint calculations for:
    - TOM_BEDS <= TOM_MAX_BEDS
    - CAR_BEDS <= CAR_MAX_BEDS
    - MES_BEDS <= MES_MAX_BEDS
    - TOM_BEDS + CAR_BEDS + MES_BEDS <= TOTAL_BEDS
    - TEMP_HOURS_USED <= MAX_TEMP_WORKERS x TEMP_WORKER_HOURS
    - All bed allocations are integers.

- Checks
  - One row per validation rule in the Validation rules section.
  - Columns: Validation Rule, Expected Result, Actual Result, PASS/FAIL.
  - Exact numeric acceptance targets shall be stored as numeric values in the Expected Result column. Explanatory text shall not be appended to exact-integer targets.

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
CEILING(TEMP_HOURS_USED / TEMP_WORKER_HOURS, 1)

FARMER_LABOR_COST = FARMER_HOURS_USED x FARMER_RATE

TEMP_LABOR_COST = TEMP_HOURS_USED x TEMP_RATE

TOTAL_LABOR_COST = FARMER_LABOR_COST + TEMP_LABOR_COST

BLENDED_LABOR_RATE =
IF(TOTAL_LABOR_HRS = 0, 0, TOTAL_LABOR_COST / TOTAL_LABOR_HRS)

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

Fixed costs are excluded from TOTAL_COST(q).

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
- The blended labor rate is a reporting metric only. Labor costs must always be calculated using the underlying labor source.

## Validation rules

Structural Checks

- No spreadsheet error cells (#n/A, #VALUE!, #DIV/0!, etc.).
- Every calculated cell contains a formula.
- Every input cell contains a constant value.
- Total allocated beds <= TOTAL_BEDS.
- Crop allocations <= crop maximums.

Acceptance Criteria

- Optimal mix = 10 tomatoes, 20 carrots, 30 mesclun.
- Season profit = $42,762 +/- $5.
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

## Acceptance Test Procedure

1. Run Solver using:
   - Objective: TOTAL_PROFIT
   - Changing Cells:
     - TOM_BEDS
     - CAR_BEDS
     - MES_BEDS
   - Method: GRG Nonlinear
   - Integer constraints on all bed variables
2. Recalculate the workbook.
3. Evaluate acceptance criteria.
4. Validation passes when:
   - TOM_BEDS = 10
   - CAR_BEDS = 20
   - MES_BEDS = 30
   - TOTAL_PROFIT = $42,762 ± $5
   - TOM_LABOR_HRS(1) = 99

## Audit findings

### Hand calculation at q = 1

**What I checked:** I calculated tomato labor hours for one bed by hand: 1 x 2.5 x 36 x 1.10 = 99 hours.

**What I found:** The workbook reports 99 hours for TOM_LABOR_HRS(1) on the MCSchedules, matching the hand calculation.

**What I did:** No workbook change was required.

**What this would catch:** This check would detect omission or incorrect placement of the exponential diminishing-returns term.

### Farm Profit Lab intermediate-value cross-check

**What I checked:** I compared the workbook's tomato marginal cost at q = 10 with the Farm Profit Lab.

**What I found:** The workbook reported $8,249, while the Farm Profit Lab reported $8,248. The difference was $1, which is attributable to rounding/display precision.

**What I did:** No model changes were required.

**What this would catch:** This check would identify errors inside the marginal-cost schedule even when the final optimization results appear correct.

### Solver path-dependence test

**What I checked:** I ran GRG Nonlinear with integer constraints from two starting allocations: 0/0/0 and 20/0/0.

**What I found:** Starting from 0/0/0 produced 10/20/30 beds and $42,762 profit. Starting from 20/0/0 produced 10/20/30 beds and $42,762 profit.

**What I did:** No model changes were required because Solver produced the same optimum from both starting points and no evidence of path dependence was observed.

**What this would catch:** This test would reveal a local optimum or starting-point dependence in the nonlinear optimization.

### Published Check Figures

**What I checked:** I compared the workbook results against the published acceptance figures.

**What I found:** After running Solver, the optimal allocation was 10 tomato beds, 20 carrot beds, and 30 mesclun beds. Total profit was $42,761.66, which is within the published acceptance range of $42,762 +/- $5.

I also reviewed the standalone marginal cost schedules. The tomato schedule crossed price at approximately 10 beds, the carrot schedule at approximately 10 beds, and the mesclun schedule at approximately 6 beds, which is consistent with the published references.

**What I did:** No model changes were required.

**What this would catch:** This check would identify errors in optimization logic, labor costing, revenue calculations, or constraint implementation even when individual formulas appear correct.

### Formula Inspection

**What I checked:** I spot-checked calculated cells in CostStructure, MCSchedules, and Optimization to verify that results were generated by formulas rather than pasted values.

**What I found:** The tested cells contained formulas referencing workbook named ranges including TOM_HRS, TOM_DIM_PCT, SEASON_WEEKS, FARMER_HOURS, FARMER_RATE, TEMP_RATE, TOTAL_REVENUE, TOTAL_VARIABLE_COST, and TOTAL_FIXED_COST.

I also verified that changing an input causes dependent calculations to update.

**What I did:** No model changes were required.

**What this would catch:** This check would identify hard-coded outputs that appear correct initially but fail when assumptions or inputs change.

### Tomato Marginal Cost Dip

**What I checked:** I reviewed the tomato marginal cost schedule.

**What I found:** Tomato marginal cost decreases around 6 beds before increasing again.

**What I did:** No model changes were required because the schedule follows the specified calculation logic.

**What this would catch:** This review would identify a flattened or incorrectly implemented marginal cost schedule.

The cause of the dip is reserved for Stage 3 analysis.