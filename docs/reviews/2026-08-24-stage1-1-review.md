<!-- PR TARGET: https://github.com/wokumura-uhm/wade-okumura | Stage 1.1 (2.5 pts) -->
# Stage 1.1 review — engagement brief · **80 / 100** (B-) · 2.00 / 2.5 pts

**Brief:** [`docs/briefs/perfect-competition-brief.md`](https://github.com/wokumura-uhm/wade-okumura/blob/main/docs/briefs/perfect-competition-brief.md)

> Graded 2026-08-31, first pass on this brief — your previous result on this stage was a hold, because the file was empty. There is a real brief there now and it is entered. Your raw came to 56 and the floor is carrying the rest; two of the four criteria are near zero and both are fixable in an evening.

| Criterion | Earned | Notes |
|---|---|---|
| Problem restated in your own voice | 20 / 30 | What is there is genuinely yours and one phrase in it is better than anything else in the paragraph: "The resources consist of 64 beds, one pair of hands, and the budget for up to 4 temporary workers." One pair of hands is the constraint stated the way an operator would state it. You also catch the thing that makes this a brief worth writing: "The plan must be committed for the entire season" — one decision, no revisions. Ten points off for two reasons. It is two sentences where the stage asks for half a page to a page, and it contains a factual error: "I will not know the prices." The prices are given — $8,800, $2,094, and $2,700 per bed — and they are the crux of the case. What you cannot do is change them. That is what price taker means, and it is a different claim from not knowing them. |
| Hypothesis names a specific mix | 20 / 25 | 22 tomato, 21 carrot, 21 mesclun — three integers summing to 64, specific and committed, which is what this criterion is for. Five points off because 22 tomato beds is above the tomato cap of 20, so the mix cannot be planted. A prediction that violates a stated constraint cannot be compared against a model that enforces it. |
| Economic mechanism | 16 / 25 | The mechanism you name is the right one: "labor requirements increase as more beds of a single crop are planted, so concentrating too heavily on any one crop may cause diminishing returns to outweigh the additional revenue." That is correct and it is the whole engine of the case. What it does not survive is your own conclusion. A balanced 22 / 21 / 21 split only follows if the three crops behave similarly, and the case says they do not — the rates are 10 percent, 2.5 percent, and 1.25 percent, an eightfold spread, against prices that differ fourfold. Spreading evenly across three crops with rates that far apart is the one allocation the mechanism argues against. |
| Falsifiability and process | 0 / 20 | There is no section. Nothing in the brief names a result that would show the reasoning was wrong, so no model outcome can contradict it. This is the largest single block of points available to you on this stage and it is a three-sentence job. |
| **Raw total** | **56 / 100** | — |
| **Floor applied** | **+24** | 80% floor: a committed brief that states the problem and names a specific mix |
| **Final** | **80 / 100** | floored |

### The one question to answer before you rewrite

Your prediction says spread the beds evenly. Your mechanism says concentration is punished. Those are compatible only if the punishment is roughly the same for every crop. It is not.

So the question to sit with is: if tomatoes are punished eight times as fast as mesclun per additional bed, but earn more than three times as much per bed, which effect wins first — and at what bed count? You do not need the model to reason about it. One tomato bed takes 2.5 x 36 = 90 labor hours for the season; the tenth tomato bed brings the crop's requirement to 10 x 2.5 x 36 x 1.1 to the tenth, which is about 2,334 hours, not 900. One mesclun bed takes 1.25 x 36 = 45 hours, and thirty mesclun beds take about 1,960 — not far off ten tomato beds, for three times the acreage.

Whatever you conclude from that, it will not be an even split. That is the argument the brief is asking you for, and once you have it the falsification section writes itself.

### What I'd fix first

- Bring the tomato figure inside the 20-bed cap.

- Correct the line about not knowing the prices. They are given; you cannot change them.

- Expand the problem statement: what is fixed, what you choose, what limits the choice, and what happens if you choose badly. You already have the last one in the season-commitment sentence.

- Add "How I would know I was wrong." Three sentences, each naming a result the model could produce and the claim it would break. If the model comes back concentrated rather than balanced, your even-split reasoning was wrong. If it leaves beds empty, your assumption that all 64 should be planted was wrong.

### A note on sequence

Your Stage 1.2 specification work is the largest anyone in this cohort had written a week ago — and it is at capabilities/perfect-competition/, which is not the graded path, while capabilities/marginal-analysis/spec.md holds a stub. Details in your Stage 0 comment.

Worth saying here: fix the brief before the spec. The spec is where you write down what the model must do; the brief is where you decide what you think the answer is. Doing them in the other order means the specification quietly becomes the prediction, and Stage 3 has nothing to compare.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your brief into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then write the changes yourself.** For a brief, this matters more than usual: a hypothesis you did not generate cannot be honestly compared against your model in Stage 3, and that comparison is the entire point of writing the brief first.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*One standing rule for this stage: do not revise your hypothesis to match what your model later tells you. If the model contradicts the brief, that is a finding, not an error — Stage 3 asks you to explain the gap, and a brief quietly edited to be right afterwards has nothing left to explain.*

— Adam
