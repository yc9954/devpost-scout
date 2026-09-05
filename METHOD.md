# The method, in order

Six stages. Stages 1–3 happen **before** you build; 4–5 while you build; 6 the
day before you submit.

---

## 1 · Enumerate the field

Two independent routes, because neither is complete and their agreement is your
confidence interval.

**A. Search sweep.** Devpost blocks plain clients on `/software/search`, so this
drives a real Chrome.

```sh
python3 discover/search_sweep.py --config config.json --out data/search.json
```

Page until a page returns zero new slugs. The results header states its own
total (*"1–24 of 2484"*) — assert against it. We once stopped at page 26 of 104
and lost two thirds of the field.

**B. Participants → portfolios.** More complete, much slower.

```sh
python3 discover/participants.py --config config.json --out data/participants.json
python3 discover/portfolios.py   --in data/participants.json --out data/portfolios.json
```

The participants list may be login-gated. Portfolios answer plain HTTP.

## 2 · Decide membership

A portfolio holds everything that person ever posted. Only some of it is in this
hackathon.

```sh
python3 verify/membership_check.py --config config.json \
    --in data/all_slugs.json --out data/confirmed.json --workers 4
```

This reads Devpost's own `#submissions` block rather than matching text anywhere
on the page. It reports `challenged` rows separately — **re-run those before
quoting a total.** Then fetch and parse the confirmed set:

```sh
python3 verify/parse_pages.py --in data/confirmed.json --out data/parsed.json
python3 verify/enrich.py      --in data/parsed.json    --out data/corpus.json
```

Compare the two routes' totals now. Ours: 2,396 and 2,402.

## 3 · Position your idea — before building

```sh
python3 position/field_position.py --config config.json --corpus data/corpus.json
python3 position/authorship_check.py --corpus data/corpus.json
```

Count each pillar narrowly and widely, then count pairs and triples: the
combination is what is actually rare, never a single pillar. Then run the
[field-position agent](agents/field-position.md) to read the twenty nearest
entries and name the ones that defeat you.

Run your own description through the identical patterns and publish that number,
including how it changes on a short excerpt — match count scales with length,
and a rarity claim that rests on you writing more than everyone else is not a
rarity claim.

Then choose what to build with [`position/IDEA-SELECTION.md`](position/IDEA-SELECTION.md):
five tests, fail one and the idea is dead. Six of ours died; the survivor is
what shipped. Do this before writing code, not after.

## 4 · Build the product

- [`build/FILM.md`](build/FILM.md) — the video, under the cap, with audio
- [`build/EVIDENCE.md`](build/EVIDENCE.md) — claims a stranger can re-derive
- [`build/WRITEUP.md`](build/WRITEUP.md) — the submission text
- [`build/SHIP.md`](build/SHIP.md) — deploy, host compatibility, the last 48 hours

Non-negotiables: every command in your write-up runs from a clean clone with no
dev server; `reproduce.sh` runs **all** of them; the ablation exists.

## 5 · Score the whole field

```sh
python3 score/signal_score.py --config config.json --corpus data/corpus.json --out data/signal.json
python3 score/make_chunks.py  --config config.json --in data/corpus.json \
        --out-dir judge/ --double-judge 4
```

`--double-judge 4` emits chunk 04 twice so you can measure judge disagreement.
Do not skip this; ours was **6.1 points on average, 13 at worst**, which is
wider than most of the gaps you are trying to resolve.

Fan out one [triage agent](agents/triage-slice.md) per chunk — cheap model,
identical rubric, and the first/last slug in the prompt as a sanity check (one
of ours judged the wrong file and reported confidently). Collect the reports
into `results.tsv` and `dist.tsv`, then:

```sh
python3 score/aggregate.py --results results.tsv --dist dist.tsv --me your-slug
```

Use `signal_score.py` only to shortlist. It ranks your own vocabulary.

## 6 · Judge yourself, blind, twice

```
agents/fast-judge.md    the ten-minute judge — how judging actually happens
agents/deep-verify.md   the source-verifying judge — clones, runs, adds up
```

Give neither the author, prior scores, or your session history. The fast judge's
complaints are the ones a real judge will have; the deep judge finds the defects
that would embarrass you. In our run they landed on 93 and 92 — and the deep one
found three of twelve documented commands failing on a clean machine.

Then fix what they found, and stop touching the repository.
