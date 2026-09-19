<!-- PR TARGET: https://github.com/wokumura-uhm/wade-okumura | Individual Research Paper -->
# Research paper review — pre-deadline read

**What I read.** `docs/briefs/research-brief.md` · `capabilities/economic-research/spec.md` ·
`capabilities/economic-research/README.md` · `drafts/2026-09-07-draft.md` ·
`drafts/2026-09-10-draft.md` · the repository file tree and commit history.

**What I did not open this pass.** `prompt-log.md` · your Case 1 files. If something in those changes
an item below, say so and I will look.

---

Your falsification section is the strongest thing you have pushed — five conditions, each of which
would actually change your mind, including the one that matters most: "Japanese yields move
independently of Treasury yields." That is a test, not a gesture at one.

What stands between you and a paper is data, not thinking. The spec is still `status: draft`,
`## Outputs` and `## Acceptance Test Procedure` are empty headings, and no series has been pulled.

**Shorten the event window — and define it in Tokyo trading days.** You specified ten trading days
either side. Over twelve months the Fed meets eight times and the BOJ eight times, so a twenty-one-day
window is four calendar weeks and your Fed and BOJ events will sit inside each other repeatedly; where
they overlap you cannot say which central bank moved the yield. Use the announcement window, one or two
days, and extend the sample to three years for 48 events instead of sixteen.

The time zones are the trap, and they run against you. The FOMC announces around 2pm Eastern, roughly
3am in Tokyo — the JGB response lands on the *next* Tokyo trading day. The BOJ announces mid-session and
shows up partly in the same day's close. A naively defined window therefore measures the two central
banks differently, and the asymmetry inflates the BOJ's apparent effect, which is exactly your null.
Define the window in Tokyo trading days relative to each announcement and say so in the spec. This is
the item most likely to sink the paper at review, and a narrow window makes it more dangerous, not less.

**Yield curve control, and a choice to make deliberately.** The BOJ pinned the ten-year JGB under YCC
from 2016 until its exit, so across much of a recent three-year sample JGB movement around *both* Fed
and BOJ announcements was mechanically suppressed. Your falsification condition — Japanese yields moving
independently of Treasuries — could be satisfied for reasons that have nothing to do with monetary
independence. Two ways to handle it: confine the sample to the post-YCC period, or treat the exit as a
natural experiment and compare pass-through before and after. The second is a considerably more
interesting paper and costs no extra data.

**Say what counts as an answer, in numbers.** "Compare the magnitude of market reactions" is an
activity, not a criterion. Write the threshold before you look: *the hypothesis holds if the mean
absolute one-day change in the JGB ten-year around FOMC decisions exceeds the change around BOJ
decisions.* Report the spread alongside the means — with two dozen events per group, a gap between two
averages can be noise, and the paper should not claim a difference it cannot support.

**Two of your sources will not survive a reader.** FRED and the BOJ's own statistics are primaries;
Investing.com, Stooq and Yahoo Finance are conveniences that invite the question of where the numbers
really came from. FRED carries USD/JPY daily as `DEXJPUS`. It does not carry a daily JGB series — its
Japanese ten-year is monthly, useless for an event study — so the Ministry of Finance's daily JGB
yield-curve file is the source. Note retrieval dates.

**You have no recommendation, and Recommendation is thirty percent of the rubric.** Nothing in the
brief, spec or draft hints at one, and it decides which results you foreground. Who is it for — the BOJ,
told its independence is narrower than it believes? A corporate treasurer, told to hedge around FOMC
dates rather than BOJ ones? Pick the audience and the recommendation falls out of the finding.

`capabilities/economic-research/README.md` is still the template, titled "Marginal Analysis" with
Purpose and Results empty. Two minutes.

**In order:**

1. Shorten the window, define it in Tokyo trading days, and extend the sample to three years.
2. Decide whether the sample is post-YCC only or spans the exit as a comparison.
3. Decide who the recommendation is for.
4. Pull the two series — JGB curve from MOF, USD/JPY from FRED (`DEXJPUS`). Note retrieval dates.
5. Write the threshold and the dispersion reporting into the spec, before looking at the data.
6. Fill in the README.
