# ServiceNow AI Thesis Scripts

This folder contains the Python scripts used to collect, structure, evaluate, and report evidence for the ServiceNow AI thesis project.

## Purpose

The project tests the hypothesis that generative and agentic AI are enabling enterprises to build or automate workflow capabilities internally, reducing demand for commercial SaaS platforms such as ServiceNow.

The workflow is designed to distinguish evidence of AI-driven SaaS displacement from ordinary business factors such as seasonality, macroeconomic conditions, procurement timing, competition, and company-specific execution.

## Execution Order

Scripts should generally be run in the following order:

### 01-collect-evidence.py

Collects evidence relevant to the hypothesis.

Potential inputs include:

- ServiceNow earnings releases
- ServiceNow investor presentations
- ServiceNow earnings-call transcripts
- Customer announcements and disclosures
- Systems integrator and implementation partner commentary
- Comparable disclosures from Salesforce, Atlassian, Workday, Oracle, and SAP
- Credible reporting on internally developed enterprise AI systems

Potential outputs:

- Evidence source records
- Raw company metrics
- Management commentary
- Customer and partner observations
- Source metadata and retrieval dates

### 02-extract-signals.py

Extracts structured signals from the collected evidence.

Signals may include:

- Subscription revenue growth
- Current remaining performance obligations growth
- Total remaining performance obligations
- Net-new annual contract value, when disclosed
- Renewal and expansion commentary
- Large-contract activity
- Sales-cycle commentary
- Customer references to internal AI development
- Evidence of SaaS replacement or contract avoidance
- Alternative explanations for observed changes

Potential outputs:

- Structured evidence log
- Company KPI history
- Extracted qualitative signals
- Source-linked observations

### 03-score-hypothesis.py

Evaluates each evidence item against the project's hypothesis framework.

Evidence classifications include:

- Supports the hypothesis
- Contradicts the hypothesis
- Supports an alternative explanation
- Inconclusive

The script should preserve the distinction between:

- Observed facts
- Interpretations
- Causal evidence
- Unverified scenario claims

Potential outputs:

- Scored evidence log
- Hypothesis scorecard
- Evidence counts by classification
- Current confidence assessment

### 04-build-report.py

Generates the project's summary report from the structured and scored evidence.

Potential outputs:

- Executive summary
- Current hypothesis assessment
- Evidence timeline
- KPI scorecard
- Supporting evidence
- Contradictory evidence
- Alternative explanations
- Unresolved questions
- Tables and figures

## Design Principles

- Preserve raw evidence and source material unchanged.
- Record the source URL and retrieval date for every evidence item.
- Separate observed facts from interpretations.
- Do not treat stock-price movements as proof of operating performance.
- Do not treat slower ServiceNow growth alone as proof of AI-driven displacement.
- Require evidence connecting internal AI adoption to an actual SaaS purchasing decision.
- Evaluate credible alternative explanations.
- Keep scripts focused on a single responsibility.
- Make classifications and calculations reproducible.
- Retain contradictory and inconclusive evidence.

## Evidence Standard

The hypothesis should not be considered supported by a single earnings miss, management comment, customer anecdote, or stock-price movement.

Stronger evidence should establish the following chain:

1. An enterprise deploys an internally developed AI capability in production.
2. The capability replaces or materially reduces the need for commercial SaaS functionality.
3. The enterprise reduces, avoids, or declines to expand a commercial software contract.
4. The decision is reflected in customer disclosures, company metrics, partner commentary, or other credible evidence.
5. Similar behavior appears across multiple customers or software providers.

## Status

Script responsibilities and expected outputs have been defined.

Implementation is pending development of the evidence sources, data schema, scoring method, and report format.

## Script Organization

The project uses a small number of scripts that map directly to the research workflow:

1. Collect evidence
2. Extract structured signals
3. Score the evidence against the hypothesis
4. Build the research report

Additional scripts should only be introduced when the workflow becomes complex enough to justify separating responsibilities.

Current planned scripts:

- `01-collect-evidence.py`
- `02-extract-signals.py`
- `03-score-hypothesis.py`
- `04-build-report.py`

This structure favors transparency, reproducibility, and ease of review over a larger collection of narrowly scoped scripts.
