---
type: spec
capability: marginal-analysis
engagement: perfect-competition
date: 2026-08-31
status: draft            # draft | built | audited
built_with: "Copilot Code, from this file"
---

# <Capability> — model specification

## Purpose
This spec defines a reproducible scenario for Bus 620 where Copilot analyzes the ideal number of crops to plant to maximize profits for a farm.

## Inputs — the named contract
| Name | Value | Unit | Source |
|---|---|---|---|
| `TOM_PRICE` | 8800 | USD per bed | Case scenario, crop table |
| `TOM_HRS`   | 2.5  | hours per week per bed | Case scenario, crop table |
| `TOM_MAXBEDS`   | 20  | max beds used for crop | Case scenario, crop table |
| `TOM_FERTPRICE`   | 880  | crop fertilizer price per bed | Case scenario, crop table |
| `TOM_DIMRET`   | 0.10  | diminishing returns per bed added per crop | Case scenario, crop table |
| `CAR_PRICE` | 2094 | USD per bed | Case scenario, crop table |
| `CAR_HRS`   | 0.83  | hours per week per bed | Case scenario, crop table |
| `CAR_MAXBEDS`   | 20  | max beds used for crop | Case scenario, crop table |
| `CAR_FERTPRICE`   | 440  | crop fertilizer price per bed | Case scenario, crop table |
| `CAR_DIMRET`   | 0.025  | diminishing returns per bed added per crop | Case scenario, crop table |
| `MES_PRICE` | 2700 | USD per bed | Case scenario, crop table |
| `MES_HRS`   | 1.25  | hours per week per bed | Case scenario, crop table |
| `MES_MAXBEDS`   | 30  | max beds used for crop | Case scenario, crop table |
| `MES_FERTPRICE`   | 880  | crop fertilizer price per bed | Case scenario, crop table |
| `MES_DIMRET`   | 0.0125  | diminishing returns per bed added per crop | Case scenario, crop table |

<!--
Every input gets a name, a value, a unit, and a source. You choose the names.
The requirement is that they exist and are used consistently below.
-->

## Structure
<!--
Each sheet or region, and what it is for.
-->

## Calculation logic
<!--
In named-range notation, never cell addresses:

  LABOR_HRS(q) = q x HRS_PER_BED x WEEKS x (1 + DIM_PCT)^q

"Column D times column E" is not a specification — it describes a spreadsheet
that does not exist yet.
-->

## Conventions
<!--
The rules that are not visible in the formulas: costing order, allocation basis,
rounding, what happens at the boundaries. State all of them. A convention you
leave out is a convention the builder invents.
-->

## Validation rules
<!--
The conditions the finished artifact must satisfy — check figures as acceptance
criteria, hand calculations, and structural rules ("every calculated cell
contains a formula", "no error cells").
-->

## Outputs
<!--
Each result the model reports, by name.
-->

## Audit findings
<!--
Added AFTER the build. For each check: what you checked, what you found, what
you did about it.
-->