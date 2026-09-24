<!-- PR TARGET: https://github.com/wokumura-uhm/wade-okumura | Individual Research Paper -->
# Individual Research Paper — pre-deadline read

**What I read.** Every commit since my last read, as one diff — twelve files ·
`capabilities/economic-research/spec.md` in full · all five files in `data/raw/` · `data/README.md` ·
`scripts/01-collect-data.py` · `prompt-log.md`.

**What I did not open this pass.** `drafts/2026-09-10-draft.md`, which has not changed since the
commit that wrote it · your Case 1 files. If something in those changes an item below, say so and I
will look.

---

The three items I expected to be hardest are done, and done in the spec rather than in a commit
message. The window is three years, and the script carries it as constants. The YCC exit is a
structural break, analyzed on each side. The timing rule is written: "FOMC announcements occurring
after the Tokyo market close will be assigned to the next Tokyo trading day. BOJ announcements
occurring during Tokyo trading hours will be assigned to the same Tokyo trading day." Investing.com,
Stooq and Yahoo Finance are gone from Market Data. Outputs and the acceptance test are filled, and
the hypothesis test is written before the data, which is the order that makes it a test.

**The FOMC event list is item 1, and the recommendation will be read off it.** `fomc-events.csv`
holds twenty-five meetings, a `source` column reading "Federal Reserve," and a retrieval date. Your
prompt log records where the rows came from — "List every FOMC meeting from September 2023
through…," answered by Copilot — and the script hard-codes that answer in
`collect_fomc_events` rather than fetching anything. So the source column names a source nobody
opened. Logging it is exactly right; it is how I know, and it is the row where your own habit of
flagging AI output for verification earns its keep. Every date and every `policy_action` label needs
checking against the Federal Reserve's FOMC calendar and each meeting's statement. I have not done
that check either, and I am not going to be the second unverified reader. A wrong date puts a window
on the wrong day; a wrong label goes straight into the treasurer's recommendation. Once each row is
checked, put the calendar URL and the check date in `source` or `data/README.md`; until then the
column should say what it is.

**The data files are set up but still empty.** You have built the scaffolding well — the raw folder
has a file waiting for each series, with the columns already named, and `data/README.md` already
describes the processed files that will come out of the pipeline. What is missing is the data itself.
Four series to pull, each with an obvious public home: the JGB 10-year yield from the Ministry of
Finance's historical yield-curve data, into `jgb10y.csv`; the US 10-year Treasury yield from FRED
(series DGS10), into `us10y.csv`; the USD/JPY spot rate from FRED (series DEXJPUS), into `usdjpy.csv`;
and the BOJ Monetary Policy Meeting dates from the Bank of Japan's own meeting calendar and
statements, into `boj-events.csv`, verified the same way as the FOMC rows. Record the retrieval date
for each. Analysis, Recommendation and the chart all sit on these four, so this is the afternoon's
work that unlocks everything after item 1.

**The pre-break sample is a handful of meetings.** Your window opens in September 2023 and the YCC
exit falls a few months into it, so by your own list only the first few FOMC rows sit before the
break. A mean absolute change on that side rests on very few observations. The structural-break
decision is right; the spec should say what you will do with a pre-break side that small — report it
as context rather than as a test, or extend the window back far enough to make it one.

**"Exceeds" by any amount passes.** The spec reports means, standard deviations and the difference,
and then declares the hypothesis supported if one mean exceeds the other. State a minimum difference
now — relative to the pooled standard deviation, or a simple two-sample test at a stated level —
so that a difference of a fraction of a basis point cannot confirm the paper.

**The treasurer's action is still a placeholder.** Outputs and the acceptance test both promise "a
recommendation for a corporate treasurer" and neither says what kind. A treasurer's recommendation
is a calendar: which announcements to hedge into, which to sit through, and by how much. Write it now
as a conditional — if FOMC reactions exceed BOJ reactions by the threshold, then this — and let the
data fill in the branch.

**The draft describes the design the spec abandoned.** Its analysis window is still ten trading days
either side, and its fourth open question asks which window to use, which the spec has now answered.
Update it last, once the data is in.

**In order:**

1. Verify every FOMC row against the Federal Reserve's calendar and statements; record the source and
   check date; rename the `source` column's contents until you have.
2. Pull the JGB, Treasury and USD/JPY series and the BOJ events, with retrieval dates.
3. Set the minimum difference that counts as support.
4. Decide how the pre-break side is reported.
5. Write the treasurer's recommendation as a conditional.
6. Update the draft's window and open questions to match the spec.
