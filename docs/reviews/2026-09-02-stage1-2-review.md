<!-- PR TARGET: https://github.com/wokumura-uhm/wade-okumura | Stage 1.2 (8 pts) -->
# Stage 1.2 review — spec, build, audit

**Spec-side 17 out of 62.5 — held, not entered. The stage is not due until 6 September and there is no workbook, so there is nothing to compute a total against yet.**

**Spec:** [`capabilities/marginal-analysis/spec.md`](https://github.com/wokumura-uhm/wade-okumura/blob/main/capabilities/marginal-analysis/spec.md)

> Graded 2026-09-02, first pass. You did the file move I asked for on 31 August — the specification is now at capabilities/marginal-analysis/spec.md and the duplicate perfect-competition folder is gone — and I confirmed the content moved intact. That fixed your Stage 0. What it also revealed is a problem I should have caught last time and did not: the document is a general template for analysing a company, not a specification of this farm's model. I judged it by its length before and that was my error.

| Criterion | Earned | Notes |
|---|---|---|
| Spec completeness — inputs, structure, calculation flow | 9 / 37.5 | The document is well organised and the process it describes is sound — separate observations from assumptions, state units and price basis, label model illustrations, do not silently infer missing values. What it does not contain is this model. The Data Inputs table has fourteen rows and every Value cell is blank with the source listed as "To be supplied": market_name, price_observed, quantity_observed, marginal_cost, average_variable_cost. None of the case's numbers are in it — not the 64 beds, the three crops, the $8,800, the 2.50 hours per bed-week, the 10 percent compounding, the 20-bed cap, the $20,000 fixed cost, the farmer's 720 hours. There is no labor function, no sheet structure, no named ranges, and no statement of what the workbook computes. Nine points for the framework, which is real; a builder cannot build a workbook from it because it does not describe one. |
| Spec validation rules | 8 / 25 | Ten rules and several are genuinely good ones: units and price basis must be consistent, total revenue must reconcile to price times quantity, sensitivity analysis must identify which assumptions change the conclusion, and re-running from documented inputs must reproduce the reported outputs. That last one is the definition of reproducibility and most people in this cohort did not write it. Eight points because none of them can fail against this model — there is no hand-check anchor, no published check figure, no tolerance, and nothing that names a quantity this workbook would produce. |
| Workbook satisfies the contract | 0 / 25 | No workbook. You removed the xlsx files on 31 August. None was due, so nothing is lost — but the stage is due 6 September and the specification it is meant to be built from does not exist yet. |
| Audit note | 0 / 12.5 | No audit section, which is correct with no build behind it. |
| **Spec-side subtotal** | **17 / 62.5** | the part that can be earned before a workbook exists |

> Spec-side 17 of 62.5. Held, not entered — the stage is not due until 6 September and this is recoverable in the time available.

### The distinction that matters here, and it is not a small one

There are two different documents you could write and they have almost the same name.

One is a methodology: how a perfect-competition analysis should be conducted in general, what has to be sourced, what has to be labelled an assumption, what makes a conclusion defensible. That is what you have written, and it is a decent piece of writing.

The other is a build contract: this specific model, with these specific inputs and their values, this labor function, these sheets, these named ranges, these acceptance figures. Someone who has never seen the case should be able to open it and produce a workbook that agrees with yours to the cent. That is what Stage 1.2 grades, and it is what your workbook has to be built from.

The test is concrete: hand your document to somebody who has not read the case and ask them to build the model. Right now they cannot start, because the first thing they need is a number and there are no numbers in it.

### What the specification has to contain, concretely

- Inputs, with values. WEEKS 36, TOTAL_BEDS 64, FIXED_COSTS $20,000, FARMER_SALARY $50,000, FARMER_FIELD_HRS 720, TEMP_COST_EACH $25,000, TEMP_HRS_EACH 1,440, MAX_TEMPS 4. Then per crop: cap, price per bed, labor hours per bed-week, fertilizer per bed, diminishing-returns rate. Every one a named range, every one with its source.

- The labor function, written out. LABOR_HRS(q) = q × hrs-per-bed-week × 36 × (1 + DIM)^q. The exponent on q is the thing most likely to be got wrong in this case, so say it explicitly.

- The costing order. The farmer's 720 hours are consumed first across all crops, then temporary labor covers the remainder. Rates are derived — 50,000/1,440 and 25,000/1,440 — not the rounded $34.72 and $17.36, because the rounding moves the answer.

- The sheet structure. Which sheets, what each holds, where the three decision cells live, and the Solver setup.

- Validation rules with numbers in them. LABOR_HRS(1) for tomatoes = 99 hours exactly. Optimal mix 10 / 20 / 30. Season profit $42,762 within $5. Standalone crossings 10 / 10 / 6. Each with a tolerance and a reason for the tolerance.

### What to keep from what you wrote

Do not throw the document away. Three of its rules belong in the new one almost verbatim: that units and price basis must be consistent and stated; that every figure identifies its source or is labelled a model illustration; and that re-running the calculation from the documented inputs must reproduce the reported outputs.

That third one is the whole stage in a sentence, and you wrote it before anyone told you to. Move it into a specification that has numbers in it and it becomes a rule you can actually test.

### Four days, in order

- Today: the inputs table with real values, and the labor function. That is the half of the specification that unblocks everything else.

- Tomorrow: structure, costing order, validation rules with the check figures in them. Commit it before you build anything — the commit order is part of what the stage is grading.

- Then build, run Solver from two different starting points, and write the audit.

Your Stage 1.1 brief needs a hypothesis with three numbers in it and a falsification section, and that is graded separately. If both stages at once is not realistic this week, tell me rather than disappearing on it — I would much rather work out a sequence with you now than grade a gap later.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your spec into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then correct the spec, not the workbook.** This is the rule that makes the stage work: when a check fails, you fix the specification and regenerate, so the document keeps describing what was actually built.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*Nothing here is final. Stage 1.2 is not due until 6 September, and the stage is re-graded from scratch at the deadline.*

— Adam
