# The WebMCP Challenge — what one full run produced

Sep 2–4, 2026. Deadline Sep 4 01:00 PDT. Gallery never published.

## The field

| | |
| --- | ---: |
| Registered participants (public) | 7,085 |
| Participants enumerated | 6,944 (98.0%) |
| Public profiles fetched | 6,943 |
| Unique project slugs seen | 9,087 |
| **Confirmed submissions — participant route** | **2,402** |
| **Confirmed submissions — search route** | **2,396** |
| Best estimate of the true total | ~2,450 (band 2,400–2,520) |

Two independent routes, six apart. The search route's own header said
*"1–24 of 2484"* across 104 pages.

**The first corpus had 868 and was treated as the field for a day and a half** —
28–36% of it. Of the 1,524 later found: 834 created after the snapshot (the real
last-36-hours surge), **690 already existed and were simply never fetched**
because the sweep stopped at page 26.

Measured index gap: 20 of 868 known entries appear nowhere in a complete
enumeration of the query that names the hackathon — **2.3%**. Search is a lower
bound, always.

Conversion looks impossible until you check team size: 94% of teams were one
person, so 2,402 submissions came from ~2,605 people (37.5% of registrants).

## Quality distribution

12 slices × ~200, one blind LLM judge each, identical rubric.

| band | count | share |
| --- | ---: | ---: |
| 80+ | 216 | 9.0% |
| 70–79 | ~585 | 24% |
| 60–69 | ~757 | 32% |
| 50–59 | ~475 | 20% |
| under 50 | ~358 | 15% |

Per-slice 80+ counts ranged **4 to 35** under the same rubric — calibration
drift is large, normalise before comparing across slices.

## Top of the field (blind text triage)

| | | |
| ---: | ---: | --- |
| 1 | 91 | placard · mace · mandate-0bmige |
| 4 | 90 | office-of-kaiju-affairs |
| 5 | 89 | aic-risk · agentperf · out-of-service · hubit · substrate · ninthtool · blindfold · cedarfield · release-airlock |
| 14 | 88 | spatialize · living-evidence · ferrule · vouchsafe · concord · review-gate · recall-me-maybe |

## The same entry, judged four ways

Our own submission, `warrant-4ywaz2`:

| judge | corpus | score | placing |
| --- | --- | ---: | --- |
| deep source verification | 868 | 92 | 10th |
| deep source verification (blind, rerun) | 2,392 | 92 | — |
| ten-minute judge (blind) | 2,392 | 93 | "top ten, without hesitation" |
| slice triage (blind, text only) | 2,392 | **83** | ~115th, top 4.8% |

The spread is the finding. **Text-only triage cannot see a test suite**, so
Execution fell 23→19 and Impact 21→18 on identical work. If your strength only
appears when someone runs something, most judging will not see it.

And the estimate moved every time the denominator did:

```
868 corpus, source-verified      →  92, 10th      (denominator was 36% of real)
~2,450, sampled                  →      20–50th
2,392, blind full-field triage   →  83, ~115th    (denominator finally correct)
```

Three estimates, all wrong in the same direction, all for the same reason.

## Inter-rater spread

One slice was accidentally judged twice. Nine entries, identical text and rubric:

| entry | A | B | Δ |
| --- | ---: | ---: | ---: |
| ferrule | 88 | 86 | +2 |
| grenz | 83 | 82 | +1 |
| genevault | 85 | 83 | +2 |
| foodloop | 80 | 76 | +4 |
| fitcheck | 83 | 77 | +6 |
| groundplan | 82 | 76 | +6 |
| handback | 84 | 74 | +10 |
| haggle | 87 | 76 | +11 |
| gildongmu | 83 | 70 | +13 |

**Mean +6.1, worst +13.** Wider than most gaps in the top 100. Quote a band.

## What the field converged on

Independently, many entries reached the same idea: **a tool that does not exist
is stronger than a tool that refuses.** `getTools()` as the enforcement surface —
mace (motions), placard (hazmat), hubit (checkout), track-record (award),
careers-webmcp (`grep -c` returns 0), cedarfield (a tool that needs a physical
human act to exist).

The other convergence: **declared tool metadata can lie, so enforce at runtime** —
ninthtool found Chrome silently dropping 13 of 20 spec promises; lapse found
225 schema violations in 299 probes against Chrome's own reference demos;
grenz wraps `registerTool` itself; trustwright audits other sites and signs a
revocable badge.

## Files

| | |
| --- | --- |
| `data/results.tsv` | 195 scored entries — chunk, slug, per-criterion, total |
| `data/dist.tsv` | per-slice band counts (the calibration drift) |
| `data/census.json` | participant-route census with its own caveats |
| `data/new_submissions_since_freeze.json` | the 1,539 the first corpus missed |
| `data/new_scored.json` | signal scores over the new set |
| `corpus/chunk_*.json.gz` | all 2,392 entries as judged — the input, gzipped |
