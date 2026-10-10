# Wade Okumura — feedback, sweep of 2026-10-09

## Research paper review — last read before grading

**What I read.** `drafts/2026-10-09-draft.md` in full · `data/processed/event-study-results.csv` and the start of `data/processed/event-dataset.csv` · the start of `data/raw/jgb10y.csv` · the commits since my last read.

**What I did not open this pass.** The figure images · `analysis/research-paper.pdf`, which I did not compare with the draft · `scripts/` · `prompt-log.md`. If something in those changes an item below, say so and I will look.

---

This is my last read before the paper is graded.

Most of my last read is done. The JGB series now runs daily through the end of the study, so no events drop out, and the difference is −0.38 bp, which checks against your results file: 3.02 bp after BOJ announcements against 2.64 bp after the Fed. USD/JPY is in, "1.84 yen around Federal Reserve announcements and 1.40 yen around BOJ," and the paper now allows that the gap "could also mean that BOJ decisions surprised markets more." Figure 3 is added.

**Which source produced the numbers?** The draft says the JGB series is FRED IRLTLT01JPM156N and cites OECD (2026). That series is monthly, and a window from the day before to the day after an announcement needs daily data. The committed `data/raw/jgb10y.csv` is daily and names the Japan Ministry of Finance as its source. Which one produced your results, and do the Methodology and the reference list say so?

**How many BOJ events?** The draft says "25 Federal Reserve … and 25 Bank of Japan policy announcements." Your results file counts 25 for the Fed but 24 for the BOJ, with March 19, 2024 excluded. Which count is right for each table, and does the text say why one was left out?

**How big is a typical day?** The paper names the benchmark itself, "It should also be evaluated against the typical two-day JGB movement," and lists it under Open Questions. The daily data to compute it are already in `data/raw/jgb10y.csv`. Is −0.38 bp large or small against an ordinary two-day move with no meeting?

Lamaku holds the graded copy; right now it has no upload from you.

**In order:**

1. Upload the PDF to Lamaku.
2. Answer which JGB source produced the numbers, and make the Methodology and references match.
3. Answer how many BOJ events each table uses.
4. Decide whether to compute the typical two-day move and compare −0.38 bp with it.
