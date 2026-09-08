<!-- PR TARGET: https://github.com/wokumura-uhm/wade-okumura | Stage 1.2 -->
# Stage 1.2 review — spec, build, audit

> **Hurricane Lowell.** If you are boarding up, packing, or hauling the patio furniture indoors, put this review down — it will keep, and nothing in it needs you today. And if you are reading a review while a hurricane bears down on the islands: I am writing one in the same weather, so there is no judgement coming from this end. :) Look after your people first — the coursework will survive whatever Lowell does.

**Spec:** [`capabilities/marginal-analysis/spec.md`](https://github.com/wokumura-uhm/wade-okumura/blob/main/capabilities/marginal-analysis/spec.md)

> Re-graded 2026-09-08 against the specification and workbook you committed. The last pass was a hold with almost nothing at the graded path. This one lands the published profit to the cent, and your Checks sheet does something no other workbook in this cohort does — it counts its own errors instead of asserting it has none.

| Criterion | Where it stands |
|---|---|
| Spec completeness — inputs, structure, calculation flow | Twenty-six named inputs with unit and source, the derived rates given as derivations, and carrot hours carried at full precision with a note that the case displays the rounded value. Five sheets, each described by what it must contain. Complete and buildable. |
| Spec validation rules | Structural checks and acceptance criteria are both there and both stated before the build, with a tolerance on the profit figure. Thinner than the strongest specs here: the Solver path-independence test and the Farm Profit Lab cross-check are both things you ran, but neither was written down as a rule in advance. |
| Workbook satisfies the contract | Lands $42,761.66 and 5,277.2161 labor hours — exact against my model. Formulas reference named ranges throughout. Been through Excel, so the cached values are real. The acceptance checks are gated behind a RUN control so they report NOT EVALUATED rather than falsely failing before Solver runs, which is a genuinely good idea. |
| Audit note | Full marks. Six findings, each with an explicit statement of what the check would catch, both Solver starting points recorded, an independent cross-check, an input-perturbation test, and the marginal-cost dip observed with its explanation deliberately reserved for the next stage. |

### The cell that actually checks

Checks!C2 contains a SUMPRODUCT over ISERROR across four named ranges spanning three sheets, and reports the count. If a #REF! appeared anywhere in those ranges tomorrow, that cell would change and the row would fail.

This sounds like a small thing. It is not. The most common way a validation sheet fails is by containing a row that cannot fail — a cell holding a literal zero compared against zero, reporting PASS because it was told to rather than because anything was examined. I have found that pattern in this cohort's workbooks more than once, including in the strongest one.

You also counted formula cells and constant cells with array formulas, so "every calculated cell contains a formula" is a measurement rather than a claim. That is the right instinct and it is the difference between a checklist and an audit.

### What changed since the last pass

The previous pass could find a specification at the graded path and essentially nothing else. What is there now is a complete, precise, buildable document and a workbook that satisfies it.

The single decision that made the difference is in your input table: CAR_HRS carried as 0.833333333333333 with the note that the case displays 0.833, and both wage rates given as derivations from the salaries rather than as the printed $34.72 and $17.36.

Three other students hit a $13 gap against the published profit and only one of them closed it. You never opened it, because you wrote the exact values into the contract before you built. That is the whole reason your profit lands on $42,761.66 rather than near it.

### Where the remaining marks are

Your validation-rules section lists what the workbook must satisfy. What it does not do is say what happens when a rule fails.

Compare two of your own audit findings. You ran Solver from 0/0/0 and 20/0/0 and both converged — but nothing in the spec said to run it twice, or what to do if the two runs had disagreed. You cross-checked bed 10 against the Farm Profit Lab and found a $1 display difference — but nothing in the spec said to cross-check, or what size of difference would have been a finding rather than rounding.

You did both of the right things. The specification just does not know you did. Write those two as rules with their tolerances and their failure responses, and the spec-side criteria are essentially full.

### One observation to carry forward

Your last audit finding records that tomato marginal cost decreases around six beds before increasing again, and explicitly reserves the cause for the analysis stage.

That is exactly the right boundary between building and explaining, and you are one of the few people who drew it deliberately rather than by running out of time. Hold on to the observation — the mechanism behind it is the most interesting result in this model, and the next stage asks for it directly.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your spec into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then correct the spec, not the workbook.** This is the rule that makes the stage work: when a check fails, you fix the specification and regenerate, so the document keeps describing what was actually built.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*Your score and the per-criterion breakdown are in your Lamaku comment, not here — this repository is public.*

— Adam
