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

- FRED (USD/JPY)
- BOJ Statistical Data
- Japan Ministry of Finance Yield Curve Data

## Analysis Window

For each policy event the events will be measured using Tokyo trading days rather than calendar days.

The event window will be limited to one or two Tokyo trading days surrounding each announcement in order to isolate the market reaction and avoid overlap with other central-bank meetings.

The analysis will map each policy announcement to the Tokyo trading session in which market participants could first react.

FOMC announcements occurring after the Tokyo market close will be assigned to the next Tokyo trading day.

BOJ announcements occurring during Tokyo trading hours will be assigned to the same Tokyo trading day.

All event windows will be measured relative to that assigned Tokyo trading day.

## Sample Design Considerations

The proposed sample overlaps the final period of Bank of Japan Yield Curve Control (YCC) and the subsequent policy transition.

Because YCC may affect observed 10-year Japanese government bond yield movements, the YCC exit will be treated as a structural break. Market reactions before and after the Bank of Japan's exit from Yield Curve Control will be analyzed separately to evaluate whether policy transmission changed following normalization.

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

The hypothesis will be considered supported if the mean absolute 1-day change in the Japanese 10-year government bond yield around Federal Reserve announcements exceeds the mean absolute 1-day change around Bank of Japan announcements.

The analysis will report:

- Mean absolute yield change for FOMC events
- Mean absolute yield change for BOJ events
- Standard deviation of each event group
- Difference between group means

The hypothesis will be rejected if:

- BOJ event reactions exceed FOMC event reactions, or
- JGB yields move independently of U.S. Treasury yields.

## Success Criteria

The analysis will:

- Identify major monetary-policy events during the sample period.
- Measure market responses in JGB yields and USD/JPY.
- Evaluate the hypothesis using the predefined criteria.
- Provide a recommendation for a corporate treasurer responsible for managing interest-rate and foreign-exchange risk exposure.

## Outputs

1. Event dataset
2. Treasury yield dataset
3. JGB yield dataset
4. USD/JPY dataset
5. Event-study figures
6. Final research paper
7. Corporate treasury recommendation

## Acceptance Test Procedure

The capability passes if:

1. All FOMC and BOJ events are collected.
2. Tokyo trading-day windows are correctly assigned.
3. JGB yield changes are calculated for all events.
4. Mean and standard deviation are reported.
5. The hypothesis is evaluated using the predefined threshold.
6. A recommendation for a corporate treasurer is provided.
7. The final recommendation is logically supported by the empirical findings.

## Audit findings

To be completed after the build.
