---
name: scout
description: Enter a Devpost hackathon to win it. Give a hackathon name or URL and this resolves the rules and rubric, enumerates the whole field, kills weak ideas before they cost you a build, researches an anchored impact claim, films the demo, writes the submission, and judges the result blind before a real judge does. Use whenever the user names a hackathon, asks what to build for one, asks how their entry stacks up, or wants a demo video, submission write-up, or impact numbers for a competition entry.
---

# scout

Enter a hackathon with evidence instead of optimism. Eight stages; each has a
gate. Do not skip a gate to be helpful — every gate here exists because skipping
it cost a real run something, priced in `PITFALLS.md`.

**Repo root is the working directory.** `pip install -r requirements.txt` first
(`websocket-client` is required and nothing else installs it).

## Read before acting

| when | read |
| --- | --- |
| always, before trusting any number you produce | `PITFALLS.md` |
| stage 1–2 | `METHOD.md` |
| stage 3 | `position/IDEA-SELECTION.md` |
| stage 5 | `write/IMPACT.md` |
| stage 6 | `build/EVIDENCE.md` |
| stage 7 | `build/FILM.md`, `build/TERMINAL.md` |
| stage 8 | `write/WINNING-WRITEUPS.md`, `build/WRITEUP.md` |
| stage 9 | `build/SHIP.md` |

Agent prompt templates live in `agents/*.md` with `{{PLACEHOLDER}}`s. Substitute
and dispatch them; do not rewrite them from memory.

## State

One directory per attempt: `runs/<slug>/`. Keep `STATE.md` there with the stage,
what is decided, and what is still open. Read it before doing anything; write to
it after every stage. `runs/*/corpus/` is gitignored; `data/` is scratch.

---

## 1 · Resolve the hackathon

```sh
python3 discover/hackathon.py --name "<what the user said>" --out config.json
```

Ambiguous names return a numbered list — show it and ask, never guess. Then
**report back to the user, before anything else**:

- the four-to-seven judging criteria **verbatim**, with weights
- **which criterion is the tiebreaker** (the first listed — Devpost's standard
  tie-break resolves on it, and at the top of a field scores bunch)
- the requirements that fail an entry outright: video cap, public URL, repo,
  language
- the deadline, and how long is left

If `criteria_source` is null, the parse failed: open the hackathon page yourself
and fill `config.json` by hand. **Everything downstream scores against these.
Never paraphrase them.**

## 2 · Enumerate the field

Two independent routes; their agreement is the confidence interval. Neither
alone is a census.

```sh
python3 discover/search_sweep.py <ws-url> "<query>" auto data/search.json
python3 discover/participants.py --output data/participants.json --ws-url <ws>
python3 discover/portfolios.py --participants data/participants.json --output data/portfolios.json
python3 verify/membership_check.py --config config.json --in data/all_slugs.json \
        --out data/confirmed.json --workers 4
```

**Gate:** page until a page returns zero new slugs, and assert your total against
the result header's own count. Report both routes' totals. Rows marked
`challenged` are unresolved, not negative — re-run them before quoting a total.
A sweep that stops early is the single most expensive error in this repo's
history: one stopped at page 26 of 104 and two-thirds of the field went missing
for a day and a half.

## 2.5 · Generate candidates out of every other hackathon

The brain (`hub/`) is thousands of winners across hundreds of hackathons,
decomposed into mechanism / domain / user / substrate. Two things to do with it
before the expensive field enumeration.

**Has this been built, and did it win?**

```sh
python3 hub/store.py search "<the idea, in the field's words>" --winners
python3 hub/store.py orgs --min-prize 25000        # which sponsors are worth entering
```

**What is proven elsewhere and absent here?** This is the generator:

```sh
python3 hub/ideate.py --config config.json --facets data/facets.jsonl --top 12
python3 hub/gaps.py   --facets data/facets.jsonl --vault vault/     # global combinations
```

`ideate.py` scores every candidate against **this hackathon's own criteria**,
verbatim, with extra weight on the tiebreak criterion from stage 1. It produces
two kinds:

- **transfer** — a mechanism with many wins across other fields that nobody here
  has used. The strongest kind: the move is already proven, only the setting is new.
- **combination** — a mechanism × domain pair whose halves are both well populated
  and whose intersection is empty.

Pass `--field <facets for this hackathon's own corpus>` once stage 2 has run;
without it "absent here" is measured against the whole corpus and is much weaker
evidence. Say which of the two you had.

**Every candidate is a question, not an idea.** Zero occupancy is not evidence of
a good idea — nobody may have done it because it is not attractive. Carry each one
into stage 3 and let the five tests kill it.

Build the hub first if `data/facets.jsonl` is missing — `hub/README.md`. Search
**shortlists, never ranks**: widen the query until it hurts before reporting that
nobody has built it, and read the entries rather than trusting the count.

## 3 · Kill the idea before building it

Run `position/IDEA-SELECTION.md`'s five tests. **Fail one and the idea is dead** —
not weakened. Six of seven candidates died in the run this came from.

Test 2 decides most of them: move the feature to a server API. Does it die? If it
survives, the platform is decoration and judges will see it.

Then dispatch `agents/field-position.md` against the corpus. Report the **wide**
occupancy count, not the flattering narrow one, and name the entries that defeat
the idea. **Gate: do not write code until an idea has passed all five and you
have said out loud which entries beat it.**

## 4 · Choose what wins on the rubric

Map the idea to each criterion, weighted, and put disproportionate effort on the
tiebreaker from stage 1. An entry strong on three criteria and absent on the
fourth loses to a balanced one — Devpost's judges name over-indexing explicitly.

## 5 · Anchor the impact claim

Follow `write/IMPACT.md`. **Never write an unanchored magnitude** ("millions of
people…"). Every impact claim sits on one of four anchors:

1. a cited public population (keyless API a judge can re-fetch)
2. a measurement you ran
3. a named institution that vouches
4. a concrete recurring instance

Anchor 4 is free and nearly as strong as 1 — two entries in the top 12 of a
2,392-entry field used nothing else. Decide the claimable population *before*
searching for a number, then state the caveat yourself in the same breath.

## 6 · Build, with evidence discipline

`build/EVIDENCE.md`. Tier every claim in `CLAIMS.md`; `reproduce.sh` must run
**all** of them from a clean clone with no dev server. Build the ablation —
delete the mechanism, re-run, count what breaks. Fewer than 2% of the field has
one, and it is the cheapest separation from the median.

## 7 · Film it

Terminal work → `build/TERMINAL.md` (VHS; the `.tape` is source, so the demo is a
build artifact). Browser app → `build/FILM.md` (shoot flat, draw camera after).
Respect the cap from stage 1 with four seconds of slack. The product must be
visibly working in the first 10–15 seconds; two of five Devpost judges start
here.

## 8 · Write it

`write/WINNING-WRITEUPS.md` has the measured patterns and the pre-submit
checklist. The load-bearing ones:

- the tagline is a falsifiable sentence with a number or citation in it
- headings name **claims**, not categories
- the whole argument in the first screen
- **a limitations section that names something that actually costs you** — every
  top entry has one, without exception, and the #1 entry in a 2,392-field spent
  more words attacking its own claim than describing its features

## 9 · Judge yourself, blind, twice

```
agents/fast-judge.md     the ten-minute judge — how judging actually happens
agents/deep-verify.md    clones, runs, adds up
```

**Gate — this one is absolute.** Give neither the author, prior scores, nor
session history. If a scorer learns whose work it is, the score is evidence about
the scorer: one model moved an entry from unranked to #1 with straight 10s in six
minutes, having verified nothing. Never judge from a directory holding your own
analysis. Give review agents a read-only copy — a subagent deleted the working
tree during one review.

Then fix what they found and **stop touching the repository**. After the deadline
the judged repo is frozen; deploy fixes to the live host instead.

## Scoring the field (optional, expensive)

```sh
python3 score/make_chunks.py --config config.json --in data/corpus.json \
        --out-dir judge/ --double-judge 4
python3 score/aggregate.py --results results.tsv --dist dist.tsv --me <slug>
```

Fan out `agents/triage-slice.md`, one per chunk, cheap model. **Always
`--double-judge`**: measured inter-rater spread was 6.1 points mean, 13 worst —
wider than the gaps you are trying to resolve. Quote rank as a band that wide.

Carry each chunk's first and last slug into the prompt as an assertion
(`make_chunks.py` prints them) — one judge read the wrong file and reported
confidently. Give every agent a unique scratch path. Track `chunk → agent →
status` in a file you own.

Signal scores (`score/signal_score.py`) **shortlist, never rank** — they measure
your own vocabulary and put the deep-verified #1 at 444th.

## Known rough edges

`METHOD.md` documents a config-driven CLI that several scripts do not implement
(positional `sys.argv`, hard-coded `data/` paths). Read a script's source before
running it. `verify/parse_pages.py` reads `data/pages/*.html` and **nothing here
writes that directory** — you must fetch and save the confirmed pages yourself
before it runs. See `CLAUDE.md` for the full tier list.
