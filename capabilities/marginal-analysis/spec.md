---
template: spec
purpose: "Technical specification for a BUS-620 perfect-competition analysis capability"
audience: student
fields_required: [title, author, date, version, company, scope, model_architecture, data_inputs, derived_inputs, formulas, validation, analysis_requirements, output_format, references]
naming_convention: "YYYY-MM-DD-{slug}.md"
course: BUS-620
---

# BUS-620 Perfect Competition Analysis Specification

**Author:** Wade Okumura  
**Date:** 2026-08-31 
**Version:** 1.0  
**Company:** To be selected; use a clearly identified company, market, or industry.

---

## 1. Scope & Objective

This specification defines a reproducible BUS-620 analysis of a selected company, market, or industry through the perfect-competition model. The analysis must identify its decision question, analytical period, geographic or market boundary, units, intended audience, assumptions, limitations, and evidence standard before work begins.

The objective is to assess how closely the selected case aligns with perfect-competition assumptions and to evaluate firm behavior, short-run production decisions, and long-run equilibrium. The work must distinguish observed data from assumptions, estimates, and model outputs and must not claim that a simplified model completely describes an operating business.

---

## Part A — Model Specification

### 2. Model Architecture

Store this capability and each engagement using the following structure:

```text
capabilities/perfect-competition/
docs/briefs/<specification>.md
data/<engagement>/
analysis/<engagement>/
analysis/figures/<engagement>/
docs/decisions/<engagement>-decision.md
```

The capability folder should contain the specification and model implementation. Each engagement should contain:

- `README.md`: question, status, owner, source list, and reproducibility instructions.
- `data/`: sourced inputs and provenance; do not overwrite original source files.
- `analysis/`: calculations, tables, and narrative findings.
- `analysis/figures/`: figures with descriptive filenames and source notes.
- `docs/decisions/`: recommendations and limitations written after analysis.

Separate the workflow into four layers:

1. **Inputs:** sourced observations and explicitly labeled assumptions.
2. **Calculations:** derived variables and formulas using named variables.
3. **Outputs:** tables, figures, model results, and sensitivity analysis.
4. **Interpretation:** findings, limitations, and recommendations tied to evidence.

Use consistent units within each model. Record currency, price basis, time period, quantity units, and whether values are nominal or inflation-adjusted. Every figure and table must identify its source or state that it is a model illustration.

### 3. Data Inputs

Complete this table before analysis. Values must be supplied from cited sources or explicitly labeled assumptions; the executor must not silently infer missing values.

| Named Input | Description | Source | Value | Unit |
|-------------|-------------|--------|-------|------|
| `market_name` | Market or industry analyzed | To be supplied | | Text |
| `company_name` | Focal company, if applicable | To be supplied | | Text |
| `analysis_period` | Fiscal year, quarter, or date range | To be supplied | | Date range |
| `price_observed` | Observed price or average revenue per unit | To be supplied | | Currency/unit |
| `quantity_observed` | Observed quantity sold or supplied | To be supplied | | Units |
| `total_revenue` | Revenue for the analysis period | To be supplied | | Currency |
| `total_explicit_cost` | Accounting costs for the analysis period | To be supplied | | Currency |
| `fixed_cost` | Costs that do not vary with modeled output | To be supplied | | Currency/period |
| `variable_cost` | Total variable cost at modeled output | To be supplied | | Currency |
| `marginal_cost` | Incremental cost of one additional unit | To be supplied | | Currency/unit |
| `average_total_cost` | Total cost per unit at modeled output | To be supplied | | Currency/unit |
| `average_variable_cost` | Variable cost per unit at modeled output | To be supplied | | Currency/unit |
| `market_price_competitive` | Competitive benchmark price | To be supplied | | Currency/unit |
| `market_quantity_competitive` | Competitive benchmark quantity | To be supplied | | Units |

### 4. Derived Inputs

Compute and label the following intermediate values:

| Named Derived Input | Formula |
|---------------------|---------|
| `accounting_profit` | `total_revenue - total_explicit_cost` |
| `total_cost_from_unit_costs` | `fixed_cost + variable_cost` |
| `average_revenue` | `total_revenue / quantity_observed` |
| `competitive_quantity_gap` | `quantity_observed - market_quantity_competitive` |
| `competitive_price_gap` | `price_observed - market_price_competitive` |

When a derived input cannot be calculated from supplied data, mark it `N/A` and explain why. Do not replace it with an estimate without documenting the assumption.

### 5. Model Definitions & Formulas

#### Perfect competition model

Use the competitive model only when its assumptions are stated and assessed. The baseline conditions to evaluate are many buyers and sellers, comparable products, limited individual price-setting power, and sufficiently low barriers to entry or exit.

| Measure | Formula or condition | Unit |
|---------|---------------------|------|
| Competitive firm output condition | `price_observed = marginal_cost` at the profit-maximizing output | Currency/unit |
| Short-run continue-production condition | `price_observed >= average_variable_cost` | Boolean/condition |
| Long-run zero-economic-profit condition | `price_observed = average_total_cost` | Currency/unit |
| Competitive price gap | `price_observed - market_price_competitive` | Currency/unit |
| Competitive quantity gap | `quantity_observed - market_quantity_competitive` | Units |

### 6. Validation Rules

The executor must verify:

- All monetary values use the same currency and price basis.
- All quantities and prices use compatible periods and units.
- `total_revenue` reconciles to `price_observed * quantity_observed` when both are intended to describe the same observation.
- `total_cost_from_unit_costs` reconciles to the applicable cost total or the difference is explained.
- Perfect-competition conclusions are not presented without an explicit assumption assessment.
- Modeled quantities, prices, and costs are nonnegative unless the model explicitly allows otherwise.
- The firm's output decision is checked against feasible quantity, capacity, shutdown, and break-even conditions.
- Every external claim, value, table, and figure has a source or is labeled as an assumption/model illustration.
- Sensitivity analysis identifies which assumptions materially change the conclusion.
- Re-running the calculation from the documented inputs reproduces the reported outputs.

---

## Part B — Analysis Specification

### 7. Analysis Requirements

For each engagement, address:

1. **Question:** What decision or economic relationship is being examined?
2. **Model choice:** Why is the selected model appropriate, and where does it simplify reality?
3. **Evidence:** Which observations support the analysis, and what are their sources and limitations?
4. **Results:** What do the calculations show, including units and uncertainty or sensitivity?
5. **Implications:** What does the result mean for the company, market, consumers, or other stakeholders?
6. **Limitations:** Which assumptions, missing data, or identification issues could change the conclusion?

Connect the model's assumptions to the observed market evidence. Explain how price-taking behavior, marginal cost, average cost, barriers to entry, and long-run adjustment interact. Avoid treating correlation as causation without a stated identification strategy.

### 8. Comparative Analysis

Compare the observed or selected case with the perfect-competition benchmark and at least two plausible sensitivity scenarios.

Explain whether a difference is driven by price, quantity, cost, barriers to entry, product differentiation, market concentration, or an assumption in the model.

### 9. Strategic Recommendations

Provide 3-5 recommendations only when the evidence supports action. Each recommendation must:

- Identify a specific decision or owner.
- State the economic mechanism it addresses.
- Cite the result or source supporting it.
- Identify an implementation constraint or risk.
- Include a measurable follow-up indicator where practical.

Recommendations must distinguish evidence-based conclusions from proposed actions and must not overstate the precision of the model.

### 10. Output Format

Each completed engagement should contain, in this order:

1. Title and decision question.
2. Executive summary of the finding.
3. Scope, period, units, and assumptions.
4. Sources and data provenance.
5. Model and formula definitions.
6. Validation checks.
7. Results tables and figures.
8. Sensitivity analysis.
9. Interpretation and limitations.
10. Strategic recommendations.
11. References.
12. Reproduction instructions.

Use concise professional prose for an instructor or business audience. Present formulas in named-variable notation and include units in table headings. Figures must have titles, axis labels, legends where needed, and source notes. Do not include unsupported statistics or claims.

---

## References

No external sources have been selected for this portfolio specification. Each engagement must add its actual references here and in its engagement README before analysis is considered complete. At minimum, document:

- Primary company filings, operating reports, or official market data, where applicable.
- Government, regulatory, or industry sources for market and policy facts.
- Course materials used for definitions or model assumptions.
- Any dataset, survey, forecast, or secondary source used in calculations.

Record the source title, publisher, publication date, URL or file path, access date, and the specific values or claims supported by the source.
