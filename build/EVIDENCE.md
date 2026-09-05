# Making claims a stranger can check

The single highest-leverage thing in a written submission is that a judge can
re-derive a number without your machine, your key, or your model. Everything
here is about that.

## Tier your claims and publish the tiering

`evidence/CLAIMS.template.md` is the shape:

- **REPRODUCIBLE** — one command in your repo re-derives it, no key, no model.
- **MEASURED** — measured once, transcript checked in; replayed, not re-sampled.
- **DESIGNED** — follows from how the code is written; nothing counts it.
- **NOT CLAIMED** — what a reader might reasonably assume that you do *not*
  assert.

That last section is the one that earns trust. Every judge in this exercise
independently said an entry naming its own weakness reads as stronger.

## Audit yourself before a reader does

`evidence/self-audit.py` checks the write-up against the repository:

- every file the write-up cites is actually tracked in git
- the test count stated in prose equals what `npm test` prints
- figures stated in the write-up appear in `CLAIMS.md`
- nothing is sitting unpushed

It was written *after* a reader found exactly these drifts. Run it in CI.

**Its own weakness, worth fixing when you port it:** the CLAIMS cross-check
splits `"21 of 24"` and searches only for `21`, so six of eleven checks pass on
a one- or two-digit substring. Match the full string.

## Every command in your write-up must run on someone else's machine

Three of twelve documented commands failed on a clean checkout because they
defaulted to `http://localhost:5173` — one had it hardcoded with no override.
In a submission whose thesis is *a claim you cannot run is not evidence*, that
is the most expensive kind of bug.

→ Default every check to the **deployed** URL. Take `--url` to override. Then
run the whole list from a fresh clone with no dev server anywhere.

`evidence/reproduce.sh` should run **everything** the write-up lists. Ours ran 7
of 12, and the 5 it skipped were exactly the ones that failed.

## Public no-key APIs are worth more than better numbers

Reproducible beats impressive. These all answer with no account:

| Source | What it gives |
| --- | --- |
| US BLS OEWS (`api.bls.gov/publicAPI/v2`) | employment by occupation — sizes an audience |
| Eurostat (`ec.europa.eu/eurostat/api/dissemination`) | EU labour force, for a non-US bracket |
| Have I Been Pwned (`/api/v3/breaches`) | breach counts by exposed data class |
| eCFR / data.gov / open-data portals | the actual regulation or dataset you cite |

`evidence/population.py` is a worked example: it asks BLS for five occupations
live, sums them, and **prints its own caveat** — that an occupation count is an
upper bound on an audience, not a count of people who need the thing.

Two federal programs count the same occupation differently (1,532,400 vs
1,373,680 bookkeepers). Cite the one a stranger can re-derive in one command and
say why you chose it. Disclosing the disagreement scores better than picking the
bigger number.

## An ablation is the strongest single artifact

Delete your safety/policy layer, re-run the identical questions, and count what
leaks. `0 vs 1552` is checkable, survives paraphrase, and no amount of prose
competes with it. Fewer than 2% of entries in the field had one.

State what it does *not* prove: an ablation shows the check runs, not that the
classification behind it is right.
