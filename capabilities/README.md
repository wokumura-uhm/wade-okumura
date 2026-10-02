# Capabilities

This folder contains reusable capabilities developed and demonstrated through applied economics projects. Each capability is organized in its own subfolder and includes the specification and supporting deliverables used to build, validate, analyze, and document the work.

## Purpose

The capabilities in this folder demonstrate a structured, specification-driven approach to economic analysis. Across projects, the work emphasizes:

- Clear problem definition
- Specification-driven development
- Reproducible analysis
- Validation and auditability
- Documentation of assumptions and decisions
- Translation of analytical results into practical recommendations

## Folder Structure

Each capability subfolder may contain:

- `README.md` - Overview of the capability, project purpose, results, and deliverables
- `spec.md` - Requirements, methodology, assumptions, constraints, and audit findings
- Analytical models, datasets, reports, or other supporting artifacts

```text
capabilities/
├── README.md
├── economic-research/
│   ├── README.md
│   └── spec.md
└── marginal-analysis/
    ├── README.md
    ├── spec.md
    ├── model.xlsx
    ├── perfect-competition-analysis.md
    └── perfect-competition-memo.md
```

## Existing Capabilities

### Economic Research

Supports the collection, processing, analysis, and validation of economic and financial data using a reproducible, specification-driven research workflow.

The current project examines whether Federal Open Market Committee announcements have a larger impact on Japanese government bond yields than Bank of Japan announcements. It also evaluates reactions in U.S. Treasury yields and the USD/JPY exchange rate.

**Exercised in:** Economic Research - Stage 2: Spec, Build, Audit

**Status:** Data collection and event-study analysis in progress

**Key deliverable:**

- `spec.md` - Model specification and audit findings

### Marginal Analysis

Analyzes marginal cost, marginal revenue, labor utilization, and profit optimization for crop-allocation decisions under diminishing returns.

The current project determines the profit-maximizing allocation of tomato, carrot, and mesclun beds using nonlinear labor requirements, labor constraints, land constraints, and cost structures.

**Exercised in:**

- Perfect Competition - Stage 2: Spec, Build, and Audit
- Perfect Competition - Stage 3: Analyze and Report Findings

**Key deliverables:**

- `spec.md` - Model specification and audit findings
- `model.xlsx` - Completed optimization workbook
- `perfect-competition-analysis.md` - Economic analysis and figures
- `perfect-competition-memo.md` - Executive planting recommendation

## Documentation Approach

The README in each capability subfolder provides a concise description of the capability, its purpose, deliverables, application, and results.

The `spec.md` file serves as the primary reference for the project's requirements, methodology, assumptions, constraints, validation criteria, and audit findings.

When project work changes, the documentation describing that work should be updated with the related implementation changes to keep the repository consistent, reproducible, and auditable.
