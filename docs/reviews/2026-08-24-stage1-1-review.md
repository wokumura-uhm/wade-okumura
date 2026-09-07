<!-- PR TARGET: https://github.com/wokumura-uhm/wade-okumura | Stage 1.1 -->
# Stage 1.1 review — engagement brief

**Brief:** [`docs/briefs/perfect-competition-brief.md`](https://github.com/wokumura-uhm/wade-okumura/blob/main/docs/briefs/perfect-competition-brief.md)

> Re-graded 2026-09-07 against your revisions of 4 and 7 September. Both of the things the last review asked for arrived: the hypothesis now carries the reasoning behind it, and every falsification condition now carries a number.

| Criterion | Where it stands |
|---|---|
| Problem restated in your own voice | Unchanged and solid. The objective, the resources, the one-shot commitment and the cost structure are all stated properly, and the point that the plan cannot be changed mid-season is the one most briefs leave out. The case table is still transcribed rather than read, which is what keeps this short of everything this criterion asks for — the prose around it is yours, but the table itself is the case's. |
| Hypothesis names a specific mix | 10 tomato, 20 carrot, 30 mesclun, with the remaining beds deliberately left unplanted if the marginal bed stops paying. Specific, feasible, and committed. Unchanged from the last pass because it was already complete. |
| Economic mechanism | This is where the revision landed, and it is a real improvement. The hypothesis now puts the three forces side by side — revenue per bed, labor input, fertilizer cost — and names the diminishing-returns rate for each crop with its number, then says which way each force pushes. That is the argument, and it was implicit before. What is still open is the same sentence it has always been: "approximately 10 beds to tomatoes" is asserted, not derived. Nothing on the page computes what the tenth tomato bed costs, or what the eleventh would cost, or where those figures sit against $8,800. |
| Falsifiability and process | All three conditions now carry a number, and the first one is the right shape: fewer than 5 or more than 15 tomato beds is a two-sided band, so being slightly off and being badly wrong are no longer the same verdict. The third is the best of them — "if more than 500 labor hours remain unused" turns a vague claim about the binding constraint into something you can read off a cell. Sequence and path are clean. |

### What moved, and why

The last review named two things. Both are done.

The hypothesis used to say tomatoes would stay below their cap and carrots and mesclun would run to theirs, without saying what made that true. It now names the three cost dimensions and the compounding rates, and it explains the direction of each. Falsification used to be three directional statements with no thresholds in them; all three now have numbers, and one of them is two-sided.

That is what acting on a review looks like, and it is worth saying that you did it by strengthening the argument rather than by softening the prediction — the mix is unchanged.

### The one thing still missing is an arithmetic line, and it belongs in the model now

"Approximately 10" is the only unsupported number left in the brief, and I am deliberately not asking you to fix it here. The brief is committed and dated, and it should stay as it is.

Carry the question into the model instead. The tomato labor requirement for q beds is q x 2.50 x 36 x 1.10^q, so a single bed is 99 hours and the schedule climbs fast. Build the marginal cost of each successive tomato bed, put $8,800 next to it, and find where the two cross. If it crosses at 10, your brief was right and you will have shown why. If it crosses somewhere else, that is the more interesting outcome and it is what the analysis stage asks you to explain.

### Your Stage 1.2 is the urgent one

Your specification at capabilities/marginal-analysis/spec.md is still a general template for analysing a company through the perfect-competition model, with a data table whose values all read "To be supplied" and a company field that says "To be selected." There is no model.xlsx in the folder at all.

The distinction that is doing the damage is capability versus engagement. A capability is the reusable method — marginal analysis, written once, used on anything. An engagement is this farm: 64 beds, three crops, 36 weeks, these prices and these compounding rates. What you have written is a good capability document. What the stage grades is the engagement model.

The specification it wants names the actual inputs with their actual values, the sheets the workbook must contain, the labor function q x hours x 36 x (1 + rate)^q, how the farmer's 720 hours and the temporary pool are consumed, the Solver setup, and a set of validation rules with tolerances — for example that one tomato bed must come to 99.0 hours within 0.01. Then you build the workbook from that document.

Keep the template. It is genuinely reusable and it belongs in your repository. It is just not this deliverable.

### On your question about the breakdown

You asked whether the per-criterion breakdown could be sent to you, because the pull request has it and Lamaku does not.

It is the other way round, and I should have said so more clearly. The breakdown lives in the Lamaku comment — this text, under HOW THE SCORE BREAKS DOWN, with each criterion, what it was worth and what it earned. The pull request deliberately carries the written review and the criterion table with no numbers in them at all, because your repository is public and your grade is not. So the pull request is the version that is missing something, on purpose.

If the Lamaku comment is being truncated on your end, tell me in the thread and I will send the whole thing by email instead.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your brief into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then write the changes yourself.** For a brief, this matters more than usual: a hypothesis you did not generate cannot be honestly compared against your model in Stage 3, and that comparison is the entire point of writing the brief first.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*One standing rule for this stage: do not revise your hypothesis to match what your model later tells you. If the model contradicts the brief, that is a finding, not an error — Stage 3 asks you to explain the gap, and a brief quietly edited to be right afterwards has nothing left to explain.*

*Your score and the per-criterion breakdown are in your Lamaku comment, not here — this repository is public.*

— Adam
