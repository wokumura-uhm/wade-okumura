---
type: spec
capability: economic-research
engagement: individual-research
date: 2026-09-07
status: draft            # draft | built | audited
built_with: "Copilot, from this file"
---

# Capability — model specification

## Purpose

The paper will evaluate whether recent Federal Reserve actions or Bank of Japan actions exert the greater influence on Japanese financial conditions.

The analysis will measure market reactions to major monetary policy events and evaluate their impact on:

- Japanese Government Bond (JGB) yields
- U.S. Treasury yields
- USD/JPY exchange rates

The goal is to determine whether Japanese markets remain primarily influenced by U.S. monetary policy despite the Bank of Japan’s recent policy normalization and to provide a recommendation for a corporate treasurer responsible for managing interest-rate and foreign-exchange risk exposure.

The intended audience is a corporate treasurer responsible for managing interest-rate and foreign-exchange risk exposure.

## Inputs — the named contract

### Named Events

One row per event.

| Name | Description |
| -------- | ------------- |
| Event Name | Name of policy event |
| Event Date | Date of event |
| Event Type | Federal Reserve or Bank of Japan |
| Policy Action | Rate change, forward guidance, QT, YCC adjustment, bond purchase change |
| Source | Official source |

## Data Sources

### Federal Reserve

- FOMC Statements
- FOMC Press Conferences
- Federal Reserve releases
- FRED

### Bank of Japan

- BOJ Monetary Policy Meeting statements
- BOJ bond purchase announcements
- BOJ statistics

### Market Data

- FRED DGS10 U.S. 10-Year Treasury Yield
- FRED DEXJPUS Exchange Rate
- Ministry of Finance Japan Interest Rate Data (10Y JGB)

## Analysis Window

For each policy event the events will be measured using Tokyo trading days rather than calendar days.

The event window will be limited to one or two Tokyo trading days surrounding each announcement in order to isolate the market reaction and avoid overlap with other central-bank meetings.

The analysis will map each policy announcement to the Tokyo trading session in which market participants could first react.

The analysis will use the recorded policy-announcement date as the event date. All event windows will be measured relative to the event date using Tokyo trading-day observations.

All event windows will be measured relative to the event date using the change from t-1 to t+1, where t-1 is the last available trading day before the event date and t+1 is the first available trading day after the event date.

## Sample Design Considerations

The proposed sample overlaps the final period of Bank of Japan Yield Curve Control (YCC) and the subsequent policy transition.

Because YCC may affect observed 10-year Japanese government bond yield movements, the YCC exit will be treated as a structural break. Market reactions before and after the Bank of Japan's exit from Yield Curve Control will be analyzed separately to evaluate whether policy transmission changed following normalization. Because the pre-exit sample contains relatively few observations, pre-exit results will be reported as descriptive context rather than used for formal hypothesis evaluation. The primary hypothesis test will be conducted using the post-exit sample.

## Structure

### Sheet 1 - Inputs

Contains all tracked events.

Columns:

- Event Name
- Event Date
- Event Type
- Policy Action
- Source

Contains no formulas.

### Sheet 2 - U.S. 10-Year Treasury Yield

Daily observations covering the three-year analysis period.

Columns:

- Date
- US10 Yield
- Event Name (if applicable)
- Days From Event

Purpose: Evaluate whether major Federal Reserve events correspond to significant changes in Treasury yields.

### Sheet 3 - Japan 10-Year Government Bond Yield

Daily observations covering the three-year analysis period.

Columns:

- Date
- JGB10Y Yield
- Event Name (if applicable)
- Days From Event

Purpose: Measure Japanese bond-market response to policy events.

### Sheet 4 - USDJPY Exchange Rate

Daily observations covering the three-year analysis period.

Columns:

- Date
- USDJPY
- Event Name (if applicable)
- Days From Event

Purpose: Measure currency-market response to policy events.

## Figures Planned

### Figure 1

US 10-Year Yield vs Japan 10-Year Yield

Question: Do Japanese yields move in response to U.S. yields?

### Figure 2

US/JPY vs Yield Spread

Question: Does a widening interest-rate differential weaken the yen?

### Figure 3

Event Study Chart

Overlay:

- Federal Reserve events
- Bank of Japan events
- JGB yield
- USD/JPY

Question: Which central bank generates the larger market reaction?

## Hypothesis Evaluation Criteria

The hypothesis will be considered supported only if:

1. The mean absolute two-trading-day change in the Japanese 10-year government bond yield measured from t-1 to t+1 around FOMC announcements exceeds the mean absolute two-trading-day change measured from t-1 to t+1 around BOJ announcements.

2. The difference is economically meaningful, defined as at least 5 basis points.

The analysis will report:

- Mean absolute JGB yield change for FOMC events
- Mean absolute JGB yield change for BOJ events
- Standard deviation of each event group
- Difference between group means

Differences smaller than 5 basis points will be reported but will not be treated as support for the hypothesis because they may lack practical significance for interest-rate risk management decisions.

## Success Criteria

The analysis will:

- Identify major monetary-policy events during the sample period.
- Measure market responses in JGB yields and USD/JPY.
- Evaluate the hypothesis using the predefined criteria.
- Provide a recommendation for a corporate treasurer responsible for managing interest-rate and foreign-exchange risk exposure.

If FOMC announcements generate average JGB yield reactions at least 5 basis points larger than BOJ announcements, corporate treasurers should prioritize interest-rate risk monitoring and hedging activity around FOMC announcement dates.

If no economically meaningful difference is observed, or if BOJ announcements generate larger reactions, treasurers should treat Federal Reserve and Bank of Japan announcements as having comparable relevance for Japanese interest-rate risk management.

## Outputs

1. Event dataset
2. Treasury yield dataset
3. JGB yield dataset
4. USD/JPY dataset
5. Event-study figures
6. Final research paper
7. Corporate treasury recommendation

## Citation and Reference Requirements

All external facts, statistics, historical events, policy actions, market-data descriptions, and academic claims must be supported by citations.

### Citation Style

Use APA 7th Edition for in-text citations and the References section.

### Source Requirements

The final paper should cite, as applicable:

- Federal Reserve publications and FOMC statements
- Bank of Japan policy statements and announcements
- Ministry of Finance Japan interest-rate data
- FRED data-series documentation
- Academic literature relevant to monetary-policy transmission, interest-rate differentials, and exchange-rate behavior

Use primary and authoritative sources whenever available.

### In-Text Citations

Every source discussed, quoted, paraphrased, or used to support a factual claim must have an appropriate in-text citation.

Every in-text citation must correspond to an entry in the References section.

### Use of AI

AI may be used for idea generation, coding assistance, data-processing assistance, editing, and feedback.

AI-generated information must be independently verified against authoritative sources before inclusion in the final paper.

AI interactions must be documented in the repository prompt log when they materially contribute to the research process or output.

### References

All sources cited in the paper must appear in a References section.

Each reference should include, as applicable:

- Author or organization
- Publication date
- Title
- Publisher or source
- URL or DOI

### Figures and Tables

Each figure and table must include:

- Figure or table number
- Descriptive title
- Data-source citation
- Notes describing transformations, calculations, definitions, or units when applicable

### Data Provenance Requirements

All source datasets must contain:

- Source
- Retrieval Date

Policy-event datasets must additionally contain:

- Original Source
- Verification Source
- Verification Date

## Acceptance Test Procedure

The capability passes if:

1. All FOMC and BOJ events are collected.
2. Event windows are correctly constructed using the nearest available trading days surrounding each event date.
3. JGB yield changes are calculated for all events.
4. Mean and standard deviation are reported.
5. The hypothesis is evaluated using the predefined threshold.
6. A recommendation for a corporate treasurer is provided.
7. The final recommendation is logically supported by the empirical findings.
8. All externally sourced claims, figures, tables, and datasets are cited, and every in-text citation corresponds to an entry in the References section.

## Audit findings

To be completed after the build.
