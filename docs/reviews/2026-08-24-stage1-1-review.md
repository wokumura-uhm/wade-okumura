<!-- PR TARGET: https://github.com/wokumura-uhm/wade-okumura | Stage 1.1 (2.5 pts) -->
# Stage 1.1 review — engagement brief · **80 / 100** (B-) · 2.00 / 2.5 pts

**Brief:** [`docs/briefs/perfect-competition-brief.md`](https://github.com/wokumura-uhm/wade-okumura/blob/main/docs/briefs/perfect-competition-brief.md)

> Re-graded 2026-09-02 against your 1 September revision. Half of what you changed is a clear improvement and half of it went backwards, and the two roughly cancel. Scores never go down in a re-grade, so 80 stands — but I want to be straight with you about which half is which, because the thing you removed is the thing this stage is scored on.

| Criterion | Earned | Notes |
|---|---|---|
| Problem restated in your own voice | 27 / 30 | Up from 20, and this is a real gain. The factual error is gone — you no longer say you will not know the prices, and you now state the farm's costs properly: $20,000 fixed, the farmer at $50,000 for 720 field hours, temporary workers at $25,000 each for 1,440 hours. You added the constraint that matters most and stated it plainly: "The planting decision must be made at the beginning of the season and cannot be changed during the growing cycle." Three points off because the section is now half case table, and a transcribed table is not a restatement. |
| Hypothesis names a specific mix | 8 / 25 | Down from 20, and this is the whole problem. Your previous brief said 22 tomato / 21 carrot / 21 mesclun — three integers, committed, and specific enough that a model could contradict them. The tomato figure was above the cap, which cost five points. The new version says a "larger share" may go to carrots and that the plan is "expected to favor carrots over tomatoes, subject to profitability and labor constraints." There are no numbers in it. The eight points are for a stated direction; a direction is not a mix. |
| Economic mechanism | 18 / 25 | Up from 16. The reasoning is cleaner than before and it is correct in direction: carrots have the lowest labor hours, the lowest fertilizer, and a low compounding rate, so they can absorb more beds before the marginal bed stops paying; tomatoes have the highest of all three and so stop early despite the price. You also dropped the even-split conclusion, which contradicted this reasoning. Seven points off because nothing is quantified — the rates are named, never used. |
| Falsifiability and process | 0 / 20 | Still no section. Unchanged from last time, and still the largest block of points available to you on this stage for a three-sentence job. Nothing in the brief names a result that would show the reasoning was wrong, so no model outcome can contradict it. |
| **Final** | **80 / 100** | unchanged — see note |

> Raw total 53, down from 56. Your previous 80 came from the floor, and the floor applies to a committed brief that restates the problem in your own words and names a specific mix. The brief no longer names a mix, so it no longer meets the second condition — but re-grades are generosity-only in this course and no score is ever lowered, so the 80 stands.

### Put the numbers back, and keep everything else you did

I think I know what happened. My last review said 22 tomato beds is above the 20-bed cap and a prediction that violates a stated constraint cannot be compared against a model that enforces it. The fix for that is to change 22 to a number at or under 20. It is not to remove the numbers.

"Expected to favor carrots over tomatoes" cannot be wrong. Any model output with more carrots than tomatoes confirms it, and the case is built so that almost any sensible allocation does. A prediction that survives every outcome tells you nothing in Stage 3, which is where you are asked to explain the gap between what you expected and what the model said. There has to be a gap for that to be writable.

Everything else in the revision should stay. The cost data, the price correction, the committed-for-the-season line, the cleaner mechanism — all of it is better than what was there.

### The arithmetic that will give you the numbers

You have the rates. Use them once and the mix writes itself.

One tomato bed takes 2.50 × 36 = 90 hours for the season. Ten tomato beds do not take 900 — the compounding applies to the whole crop, so it is 10 × 2.50 × 36 × 1.1^10, about 2,334 hours. One mesclun bed takes 1.25 × 36 = 45 hours, and thirty mesclun beds take about 1,960 — barely more than ten tomato beds, for three times the acreage.

Now put a price on it. The farmer's 720 hours cost about $34.72 each and run out early; everything after that is temporary labor at about $17.36. So the marginal tomato bed late in the crop costs a few hundred hours of temp labor plus $880 of fertilizer, against $8,800 of revenue. Work out roughly where those cross and you have your tomato number. Carrots and mesclun compound so slowly that the question for them is whether anything stops them before their caps.

### What i would write, in order, and it is under an hour

- Three integers under Hypothesis. Tomatoes at or under 20, carrots at or under 20, mesclun at or under 30, summing to 64 or fewer. One paragraph on why those and not others, using the rates.

- A section called "How I would know I was wrong." Three sentences, each naming a number the model could return and the claim of yours it would break. This is worth 20 points and it is the cheapest 20 points on the page.

- Leave the rest alone. It is good now.

### One note on Stage 1.2, which is graded separately

You did both things I asked on the repository side — analysis/README.md and docs/README.md are in, and the specification moved to capabilities/marginal-analysis/spec.md with the old folder removed. That moved your Stage 0 from 94 to 96.

The separate Stage 1.2 review has the substantive point about that specification, and it is worth reading before you spend more time on it: the document at that path specifies how to analyse a company or market in general, not how to build this farm's model. That stage is due 6 September.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your brief into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then write the changes yourself.** For a brief, this matters more than usual: a hypothesis you did not generate cannot be honestly compared against your model in Stage 3, and that comparison is the entire point of writing the brief first.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*One standing rule for this stage: do not revise your hypothesis to match what your model later tells you. If the model contradicts the brief, that is a finding, not an error — Stage 3 asks you to explain the gap, and a brief quietly edited to be right afterwards has nothing left to explain.*

— Adam
