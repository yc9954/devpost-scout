# What the top of a field actually writes

Read closely, not summarised: nine submission bodies at the top of two different
hackathons, plus what five Devpost judges say they do. This is the pattern that
survived reading all of them.

**A note on provenance, because it changes what these numbers mean.** Nine of
these entries are the top of the WebMCP field by *our own blind triage* of all
2,392 submissions (`runs/webmcp-2026-09/`), not official winners — that gallery
was never published. Five carry an actual Devpost **Winner** ribbon from Hack for
Social Impact 2025. Both sets are evidence; only the second set is a verdict.

| entry | field | score / status |
| --- | --- | --- |
| `placard` · `mace` · `mandate-0bmige` | WebMCP, 2,392 | 91, blind triage top-3 |
| `office-of-kaiju-affairs-webmcp` | WebMCP | 90, 4th |
| `aic-risk…` · `cedarfield-clinic` | WebMCP | 89, tied 5th |
| `libertas-innocence-asserted` · `haven-ur18b7` | Hack for Social Impact 2025 | **Winner ribbon** |

---

## 1 · The default sections are a floor, not a form

Devpost gives you Inspiration / What it does / How we built it / Challenges /
Accomplishments / What we learned / What's next. The field splits three ways and
**all three placed**:

| approach | who | what it looks like |
| --- | --- | --- |
| **Abandon them entirely** | `placard` (91, top of field) | 19 custom headings: *"The thing that should worry you"*, *"Try to break it, on the page"*, *"I attacked my own safety claim"*, *"Scope, stated plainly"* |
| **Keep them, front-load numbers** | `mace`, `aic-risk`, `kaiju` (89–91) | standard headings, but every section opens with a measured quantity |
| **Keep them, add two** | `kaiju`, `haven` | inserts *"Three citizen experiences"*, *"What our experiment found"*, *"Who built it"* between the defaults |

**The rule that actually holds:** a heading must name a *claim*, not a *category*.
"What it does" tells a judge nothing about whether to keep reading. "We scanned
every public WebMCP app" does. If you keep the default headings, the first
sentence under each has to do the work the heading isn't doing.

## 2 · The tagline is the whole submission

Every high scorer's tagline is a complete falsifiable sentence, not a slogan.

> **placard** — "Placard reads a chemical manifest and shows exactly which line of 49 CFR each pair breaks."
> **aic-risk** — "We scanned every public WebMCP app. 75 tools, 49 of them mutating, zero able to tell an agent which ones are dangerous."
> **mace** — "A clerk's bench for Robert's Rules where the WebMCP tool set IS the motion stack — an action that is out of order does not exist to be called."
> **libertas** — "…analyze parole transcripts, detect wrongful convictions against 3,400+ exonerations, identify bias, and generate legal forms, cutting review time from hours to minutes."

Structure they share: **[what it reads] → [what it produces] → [the specific
authority or number that makes it checkable]**. Three of the four put a number or
a citation *in the tagline itself*. Compare `haven`'s — "using AI to make intake
more human" — which won on other strengths and is the weakest line in the set.

Judges confirm the mechanism. Devpost's judge panel: *"Judges take only little
time to evaluate your solution and will skip you if they don't understand the use
case."* The tagline is where being skipped is decided.

## 3 · Impact: the top entries do not all use statistics — they all use a denominator

This is the finding that matters most, and it is the opposite of the usual advice.

| entry | how it sizes the problem | numbers? |
| --- | --- | --- |
| `placard` | 20,460 establishments; regulatory citations (49 CFR 177.848) | yes, cited |
| `kaiju` | 95 recorded trials; 41% accuracy decline; 2.4× context tokens | yes, self-measured |
| `aic-risk` | 75 tools scanned, 49 mutating; injection 0/3 vs 3/3 | yes, self-measured |
| `libertas` | "2% to 10% of all convicted people"; 3,400+ exonerations, **National Exoneration Registry**; partner freed 40 people / 500 years | yes, third-party cited |
| `haven` | **no statistics at all** — named partner: California Homeless Youth Project; 2-1-1 Sacramento; team member with foster-care background | no |
| `cedarfield` | **no statistics at all** — "Cancelled appointments go up at 8:00 and are gone by 8:01" | no |

`haven` won a social-impact hackathon with zero statistics. `cedarfield` placed in
the top 12 of 2,392 with zero statistics. So "add more numbers" is the wrong
lesson. What all six share is an **anchor a stranger can check**, and there are
exactly four kinds:

1. **A cited population** — a public dataset with a name and a number (`placard`, `libertas`)
2. **A measurement you ran** — trials, ablations, before/after (`kaiju`, `aic-risk`)
3. **A named institution that vouches** — a real partner org (`haven`, `libertas`)
4. **A recurring concrete instance** — a specific event, at a specific time, that repeats (`cedarfield`)

**What loses is an unanchored claim.** "Millions of people struggle with X" has no
anchor: no source, no measurement, no institution, no instance. It reads as
filler and every judge discounts it. If you cannot get anchor 1, get anchor 4 —
it is free and it is nearly as strong.

`cedarfield`'s sentence is the template for anchor 4, and it is worth memorising:

> "Cancelled appointments go up at 8:00 and are gone by 8:01. Course seats, visa
> slots, concert tickets, same story."
>
> "If you use a switch, a head pointer, or voice control, you lose that race every time."

Two sentences. A time, a mechanism, a named population, and a generalisation that
shows it is not one anecdote. No statistic anywhere.

## 4 · Every single top entry names its own limits — without exception

| entry | the sentence |
| --- | --- |
| `placard` | "No shipping-compliance officer has used this in production"; air and vessel modes excluded; "eCFR is an editorial compilation; only GPO editions have legal status" |
| `mace` | §49 board relaxations unmodeled; germaneness "non-computable, delegated to chair"; six motions documented as out of scope *in the code* |
| `aic-risk` | "A layer that marked all 16 critical would be unusable"; prior work separated from new work explicitly |
| `libertas` | scope limited to screening, not adjudication |

`placard`'s **longest section in the entire submission** is *"I attacked my own
safety claim"* — 19 adversarial review rounds, 59 defects found, documented. The
top-scoring entry in a 2,392-entry field spent more words attacking itself than
describing its features.

This matches the independent finding in `PITFALLS.md`: *every judge in this
exercise said, unprompted, that an entry naming its own weakness reads as
stronger.* Two separate lines of evidence, same conclusion. **Write the
limitations section first, not last.** It is the highest-yield paragraph in the
document and the one most people cut for space.

## 5 · The verifiability ladder

Ranked by what it costs a judge to check, cheapest first. High scorers stack
several; the field median has none.

| rung | what it is | who did it |
| --- | --- | --- |
| 0 | a claim in prose | everyone |
| 1 | a number with a stated method | `mace` (306 tests), `mandate` (34 tests) |
| 2 | a number with a public no-key source a judge can re-fetch | `placard` (eCFR), `libertas` (Exoneration Registry) |
| 3 | a command in your repo that re-derives it | `build/evidence/reproduce.sh` |
| 4 | **an ablation** — delete the mechanism, re-run, count what breaks | `aic-risk` (0/3 guarded vs 3/3 unguarded) |
| 5 | **an adversarial round against your own claim, published** | `placard` (19 rounds, 59 defects) |

`EVIDENCE.md` measured that fewer than 2% of the field had a rung-4 ablation. It
is the single cheapest way to separate from the median, and `aic-risk`'s version
is one table with two rows.

## 6 · What judges say, mapped to what the writing must do

From Devpost's five-judge panel, with the writing consequence:

| judge | what they said | what that means for the page |
| --- | --- | --- |
| Richard (Square) | watches the demo video first for context; penalises "over-indexing on one criterion" | the video, not the text, is the first impression — and the text must visibly touch all four criteria |
| Karen (Databricks) | *"Ambiguity is a red flag"*; polished presentation without detail or code scores badly | every adjective needs a number or a link beside it |
| Kelvin (Google) | prioritises visual appeal, then **plays** the project; cares less about code quality | the live URL is load-bearing; a broken one is fatal |
| Maria (NEAR) | judges "entrepreneurial mindset"; penalises recycled projects | say who pays and why this could not be a weekend script |
| Warren (Atlassian) | asks whether *he* would use the finished product; penalises "half-hearted" | one sentence answering "who uses this on Monday" |

Two of five say the **demo video is where judging starts**. The text is read
second, by someone who already has an opinion.

## 7 · Length, and where it breaks

- `kaiju`: ~5,000 words, scored 90.
- `placard`: 19 sections, longest in the sample, scored 91.
- `libertas` / `haven`: short, standard sections, won ribbons.

So length does not decide it. But our own run's ten-minute judge complained
specifically: *"the verification apparatus is longer than the idea, and the idea
is good enough to survive on one page."* That entry scored 93 and still lost the
reader's patience.

**The resolution:** long is fine when every section earns its place with a claim
a judge can check. Long is fatal when it is the same claim restated. Put the
whole argument in the first screen and let the rest be appendix — the reader who
stops after 200 words must already have the point.

## 8 · The checklist

Before you submit, the page must have:

- [ ] A tagline that is a falsifiable sentence with a number or a citation in it
- [ ] The full claim in the **first screen**, before any scrolling
- [ ] One of the four anchors, explicitly, for the impact claim — and never an unanchored "millions of people"
- [ ] At least one rung-4 ablation, in a two-row table
- [ ] A limitations section that names something that actually costs you
- [ ] Every adjective within a line of a number, link, or command
- [ ] A live URL that loads with no login, checked from a fresh browser
- [ ] Headings that name claims, not categories
- [ ] One sentence answering "who uses this on Monday, and what do they stop doing"
- [ ] Nothing in the text that the video contradicts

## Sources

Submission bodies read in full: [placard](https://devpost.com/software/placard) ·
[mace](https://devpost.com/software/mace) ·
[mandate](https://devpost.com/software/mandate-0bmige) ·
[office-of-kaiju-affairs](https://devpost.com/software/office-of-kaiju-affairs-webmcp) ·
[aic-risk](https://devpost.com/software/aic-risk-permissions-and-discovery-for-webmcp-apps) ·
[cedarfield-clinic](https://devpost.com/software/cedarfield-clinic) ·
[libertas](https://devpost.com/software/libertas-innocence-asserted) ·
[haven](https://devpost.com/software/haven-ur18b7).
Judge statements: [How to win a hackathon: advice from 5 seasoned judges](https://info.devpost.com/blog/hackathon-judging-tips) ·
[Understanding hackathon submission and judging criteria](https://info.devpost.com/blog/understanding-hackathon-submission-and-judging-criteria).
