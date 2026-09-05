<!-- PR TARGET: https://github.com/wokumura-uhm/wade-okumura | Stage 1.1 -->
# Stage 1.1 review — engagement brief

**Brief:** [`docs/briefs/perfect-competition-brief.md`](https://github.com/wokumura-uhm/wade-okumura/blob/main/docs/briefs/perfect-competition-brief.md)

> Re-graded 2026-09-04 against your revision of 3 September. Your previous result sat on the floor rather than on a total you had earned. This one is earned on merit. You put the bed counts back and you added the section that had never existed.

| Criterion | Where it stands |
|---|---|
| Problem restated in your own voice | Unchanged and solid. The price error is long gone, the cost structure is stated properly, and the constraint that matters most is stated plainly: the plan is committed at the start of the season and cannot be changed during the growing cycle. What is still open is that half the section is the case table. |
| Hypothesis names a specific mix | "Approximately 10 tomato beds, 20 carrot beds, and 30 mesclun beds, with any remaining beds left unplanted if labor becomes the binding constraint." Three real integers, all inside their caps, and the idle beds accounted for rather than ignored. This is the criterion that went backwards last pass when the numbers came out; it is now the strongest one on the page. |
| Economic mechanism | Unchanged. The reasoning is correct in direction — carrots and mesclun have low labor, low fertilizer and shallow compounding so they run to their caps, while tomatoes stop short despite the price. What is still open is the same thing as before: the rates are named and never used. Nothing in the section works out where the tomato crossover falls, so the 10 is a judgement rather than a result. |
| Falsifiability and process | The section exists for the first time, and all three conditions name an observation and what it would mean about your reasoning. The third is the most interesting: "If the model leaves significant labor unused, then I have incorrectly identified labor as the primary constraint." That is a real test and — worth knowing in advance — it is one you are going to fail, which is a good thing. What is still open is that no condition carries a number or a tolerance: "close to 20 tomato beds" and "significant labor unused" both need a threshold. |

### You put the numbers back, which was the whole ask

Last pass the revision removed 22 / 21 / 21 and replaced it with a direction — carrots favoured over tomatoes — which no model output could contradict. The fix for a number that breaks a cap is a different number, not the absence of one, and you found that in a day.

10 / 20 / 30 is inside every cap, sums to 60 of 64, and accounts for the four idle beds. It is also the published optimum, which does not affect the grade — you are scored on committing to a specific claim with reasoning, not on being right — but it does mean your Stage 1.3 reflection will be about why your reasoning landed on the right answer, which is a harder and more interesting essay than it sounds.

### The condition you are going to fail, and why that is the best one

"If the model leaves significant labor unused, then I have incorrectly identified labor as the primary constraint."

The farm has 6,480 labor hours — the farmer's 720 plus four temporary workers at 1,440 each. At 10 / 20 / 30 the model uses about 5,277. So roughly 1,200 hours go unused, which is most of a whole worker, and by your own condition that means labor is not the primary constraint.

It is not. And that is the single most valuable thing in this case. Labor never runs out — it gets more expensive. A bed stops being worth planting because the hour that plants it costs more than the bed earns, not because there are no hours left. You wrote a test that will teach you that, in advance, without knowing the answer. Put a number on "significant" before the model runs — say, more than 500 hours — and the test becomes something you can point at in Stage 1.3.

### Stage 1.2 is due 6 september and it is the urgent one

The document at capabilities/marginal-analysis/spec.md specifies how to conduct a perfect-competition analysis of a company or market in general. It does not specify this farm's model — there are no bed counts, no prices, no labor function, and every value in its inputs table reads "To be supplied". There is no workbook.

The separate Stage 1.2 review sets out what the specification has to contain and gives a two-day sequence. Read that one first — it is worth considerably more than this stage is.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your brief into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then write the changes yourself.** For a brief this matters more than usual: a hypothesis you did not generate cannot be honestly compared against your model in Stage 3, and that comparison is the entire point of writing the brief first.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*One standing rule: do not revise your hypothesis to match what your model later tells you. If the model contradicts the brief, that is a finding, not an error.*

*Your score and the per-criterion breakdown are in your Lamaku comment, not here — this repository is public.*

— Adam
