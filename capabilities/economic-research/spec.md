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
| Policy Action | Rte change, forward guidance, QT, YCC adjustment, bond purchase change |
| Source | Official source |

## Data Sources

### Federal Reserve

- FOMC Statements
- FOMC Press Conferences
- Federal Reerve releases
- FRED

### Bank of Japan

- BOJ Monetary Policy Meeting statements
- BOJ bond purchase announcements
- BOJ statistics

### Market Data

- FRED
- BOJ
- Investing.com
- Stooq
- Yahoo Finance

## Analysis Window

For each policy event the events will be measured using Tokyo trading days rather than calendar days.

The vent window will be limited to one or two Tokyo trading days surrounding each announcement in order to isolate the market reaction and avoid overlap with other central-bank meetings.

The timing treatment for FOMC and BOJ announcements will be defined explicitly after mapping each announcement to the corresponding Tokyo trading session.

## Sample Design Considerations

The proposed sample overlaps the final period of Bank of Japan Yield Curve Control (YCC) and the subsequent policy transition.

Because YCC may affect observed 10-year Japanese government bond yield movements, the analysis will evaluate whether:

1. The sample should be restricted to post-YCC observations, or

2. The YCC exit should be treated as a structural break and analyzed separately.

This decision will be finalized before data collection and analysis.

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

Daily observations covering the 12-month analysis period.

Columns:

- Date
- US10 Yield
- Event Name (if applicable)
- Days From Event

Purpose: Evaluate whether major Federal Reserve events correspond to significant changes in Treasury yields.

### Sheet 3 - Japan 10-Year Government Bond Yield

Daily observations covering the 12-month analysis period.

Columns:

- Date
- JGB10Y Yield
- Event Name (if applicable)
- Days From Event

Purpose: Measure Japanese bond-market response to policy events.

### Sheet 4 - USDJPY Exchange Rate

Daily observations covering the 12-month analysis period.

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

## Success Criteria

The analysis will:

- Identify major monetary-policy events over the prior 12 months.
- Measure changes in JGB yields after Federal Reserve and BOJ actions.
- Measure changes in USD/JPY after Federal Reserve and BOJ actions.
- Compare the magnitude of market reactions.
- Determine whether evidence supports or rejects the hypothesis.
- Provide a recommendation supported by the analysis.

## Outputs

## Acceptance Test Procedure

## Audit findings

To be completed after the build.
