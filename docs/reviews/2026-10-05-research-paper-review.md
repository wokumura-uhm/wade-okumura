# Wade Okumura — feedback, sweep of 2026-10-05

## Research paper review — pre-deadline read

The test now has a verdict, and it is in the files where I can find it. The last row of your results file reads "Post-Exit, Hypothesis Test, JGB10Y," a difference of −0.004211 and "Not Supported," and the draft's recommendation follows the branch your spec set out for that result. The exit meeting is treated as the break and kept out of both regimes, and you ran the sensitivity with it included: the verdict holds. Every number I checked traces, from the 3.02 bp and 2.60 bp averages to the event counts on each side.

**What does the result mean for the treasurer?** Three questions sit on the same −0.42 bp.

1. First, your spec measures USD/JPY too, and the treasurer manages currency risk as well as rates. The results file shows post-exit average absolute USD/JPY moves of 1.84 on Fed days against 1.40 on BOJ days. What does that row say, and should the recommendation treat rates and FX the same way?
2. Second, a larger average BOJ move can mean BOJ decisions matter more, or that they surprised markets more. Does a bigger move show the BOJ has "regained control," which is the question in your title?
3. Third, your draft asks how large a typical two-day JGB move is on a day with no meeting. Against that, how should a reader weigh −0.42 bp next to your 5 bp threshold?

**Redraw the test as its own figure and put it in the draft.** This is still open from my last read. The draft shows Figure 1 and both Figure 2 panels; `figure-03-event-study-comparison.png` exists but is unchanged and not in the draft. Redraw it in basis points with the threshold line, rename the "Pre-YCC" label in the second Figure 2 panel, and add Figure 3 to the draft.

**Say where the sample ends.** The draft says the sample runs "between September 2023 and September 2026," but `data/raw/jgb10y.csv` ends on August 31, 2026, while the event lists include the September 2026 FOMC and BOJ meetings. State the JGB end date and which events drop out, or extend the series past August 31 so the two September meetings come in.

**In order:**

1. Answer in the text what the USD/JPY row says, whether a bigger BOJ move means control or surprise, and how −0.42 bp compares with a typical move on a day with no meeting.
2. Redraw Figure 3 in basis points with the threshold line, rename "Pre-YCC" in the second Figure 2 panel, and add Figure 3 to the draft.
3. State the JGB end date and the events it drops, or extend the series to bring them in.
