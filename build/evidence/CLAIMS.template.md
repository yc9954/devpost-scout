# Every claim in this submission, and what backs it

Sorted by what kind of evidence there is, not by how good the claim sounds. A
claim you cannot check is worth less than a smaller one you can, so the weaker
tiers are here in full rather than left out.

**REPRODUCIBLE** — a command in this repository re-derives it, on your machine,
with no key and no model call.
**MEASURED** — it was measured once and the transcript is checked in; the number
is replayed, not re-sampled.
**DESIGNED** — it follows from how the code is written and you can read the code,
but nothing counts it.
**NOT CLAIMED** — things a reader might reasonably assume from the above, which
this project does not assert.

Run everything at once with `sh bench/reproduce.sh`.

## REPRODUCIBLE

| Claim | Command | Result |
| --- | --- | --- |
| The policy, drift and host-contract layers hold under 80 assertions | `npm test` | 80 passed |
| The deployed site does what the walkthrough says, step by step: a refusal in place, a demonstration recorded as two operations, eight edge cases judged, `registerTool` taking the surface 7 → 8, a period nobody demonstrated, a result with no names in it, and the tool withdrawing itself when a field is reclassified | `python3 bench/live-check.py` | 21 of 21 against `warrant-gray.vercel.app` |
| 0 identifiers reach a tool result; 1552 do with the policy layer deleted | `sed -n '/ABLATION/,/Without it/p' bench/ablation.txt` | printed per question, and they sum to 1552 |
| An agent never told the tool exists reaches for it on the question it was made for: 21 of 24 | `python3 bench/tool-choice.py` | 21/24 on the covered question, 0/24 on aggregates, 5/48 adversarial |
| Between about sixty and a hundred and twenty of the other 868 entries describe creating a tool at runtime | `cd webmcp-evaluator && python3 field_position.py` | 19 on the narrow pattern, 116 widened, 62 on an outside reading — every widening cost this project something |
| The identifiers on the screen are masked in the DOM itself, not just in tool output | `python3 bench/dom-check.py` | `national_id` renders `363••••••••` |
| Thirteen host-budget limits are respected | `python3 bench/host-check.py` | 13 of 13 |
| Thirteen direct attempts to extract an identifier through the tool surface | `python3 bench/direct-attack.py` | 0 leaks |
| The page holds 1,680 rows across eight controls | open the workbench, or `python3 bench/live-check.py` | the count is on the screen and asserted live |
| The five named roles are countable: **5,996,610** US wage and salary jobs | `python3 bench/population.py` — BLS OEWS 2025 over api.bls.gov, no key | An upper bound on the occupations, not a count of people who need this. The script prints that caveat itself. Self-employed are excluded, which is why the Occupational Outlook Handbook separately puts bookkeepers at **1,532,400** where OEWS says 1,373,680 — two federal programs counting one occupation. That figure is cited, not re-derived here. |

## MEASURED

| Claim | Evidence | Note |
| --- | --- | --- |
| 108 agent runs across two model families, half written to get a name out, produced no names | `bench/agent-suite*.md` and 96 transcripts in `bench/` | The runs happened once against real models. `tool-choice.py` replays the transcripts; re-running the models needs a key and would be a fresh sample, not this one. |
| OpenAI's Codex, given only the page's published tools, proposed a tool the page then validated | `bench/codex-chat.txt`, `public/agent-proposal.json` | One real multi-turn session, recorded. |
| Of the 116 entries that describe runtime tool creation, **three** have a non-developer decide the tool's shape | `webmcp-evaluator/authorship.md` | A reading, not a regex, done without knowing which row was this project. It said one until a reader found Understudy, which the selecting pattern could not see; widening it surfaced XACT FOUNDRY as well. Every entry's deciding sentence is written down so a reader can disagree. |

## DESIGNED

- **A field marked `pii` has no code path to a tool result.** The policy layer is
  derived from the page's field declaration rather than written beside it, so
  there is no branch to forget. The ablation above shows the check is wired in;
  it cannot show the classification is right.
- **A tool withdraws itself when its structure fingerprint stops matching** —
  removed from `getTools()`, not refused at call time. `npm test` covers the
  fingerprint and the withdrawal; `live-check.py` sees the count fall on the
  deployed site.
- **A write suspends inside the page until a person answers**, and a decline
  returns `declined_by_human` with nothing written.
- **A minted tool can be sent as a link and is revalidated by the receiving page**
  against its own declaration before it registers there.

## NOT CLAIMED

- **Not that the classification is right.** The counterfactual compares this page
  with a copy of itself with the checks removed. That proves the checks run. A
  field wrongly marked non-sensitive leaks exactly as it would have. What the
  design does about being wrong is withdraw every tool whose fingerprint no
  longer matches when the classification changes.
- **Not that this is the only entry doing any one of these things.** Runtime tool
  creation, structural withholding, drift handling and human-gated writes are
  each claimed by others — 204 entries describe a write that waits for a person.
  `docs/field-position.md` counts each pillar against the field and is
  deliberately unflattering.
- **Not that 108 runs is a benchmark.** It is 108 runs on one page against two
  model families. It is evidence that the surface held on those runs, not a
  general claim about agents.
- **Not that any number here came from a judge, a user study or a third party.**
  Everything measured was measured by this project about itself, except the
  corpus counts, which are over other people's published text.
- **Not that the submission window is unambiguous.** The organisers' two pages
  disagree: the rules give the Submission Period as ending *"September 3rd, 2026
  (1:00 pm Pacific Time)"*, and the hackathon's own landing page counts down to
  *"Sep 4, 2026 @ 1:00am PDT"* — twelve hours later. This project's first commit
  is 2026-09-03 09:17 PT, inside either reading; most of its commits fall in the
  twelve hours between the two. It was built to the countdown, because that is
  what closes the form, and it is recorded here rather than left for a reader to
  notice.
- **Not that the live site has been load-tested, audited, or run by anyone but
  its author and the agents in `bench/`.**
