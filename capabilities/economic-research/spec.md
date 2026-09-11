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

The goal is to determine whether Japanese markets remain primarily influenced by U.S. monetary policy despite the Bank of Japan’s recent policy normalization.

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

For each policy event:

- 10 trading days before event
- Event day
- 10 trading days after event

This creates a consistent event-study methodology.

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

Purpose:

Evaluate whether major Federal Reserve events correspond to significant changes in Treasury yields.

### Sheet 3 - Japan 10-Year Government Bond Yield

Daily observations covering the 12-month analysis period.

Columns:

- Date
- JGB10Y Yield
- Event Name (if applicable)
- Days From Event

Purpose:

Measure Japanese bond-market response to policy events.

### Sheet 4 - USDJPY Exchange Rate

Daily observations covering the 12-month analysis period.

Columns:

- Date
- USDJPY
- Event Name (if applicable)
- Days From Event

Purpose:

Measure currency-market response to policy events.

## Calculation logic

## Conventions

## Validation rules

## Outputs

## Acceptance Test Procedure

## Audit findings

To be completed after the build.
