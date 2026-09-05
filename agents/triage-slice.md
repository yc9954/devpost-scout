# Agent: triage one slice of the field

Fan this out one per chunk. Cheap model is fine (sonnet). Twelve of these
covered 2,392 entries. Substitute `{{...}}`.

---

You are judging entries in {{HACKATHON}}, a Devpost hackathon with {{N}}
submissions. You have one slice of the field. Score every entry in it and report
the best.

READ EXACTLY THIS FILE: {{CHUNK_PATH}} — a JSON array of {{ROWS}} rows. Sanity-
check before you start: its first slug is `{{FIRST_SLUG}}` and its last is
`{{LAST_SLUG}}`. If what you read does not match that, stop and say so. Do not
create scratch files with generic names another concurrent agent might
overwrite; if you need one, use a name containing `{{UNIQUE}}`.

Each row: slug, title, tagline, live (bool), repo (bool), video (bool), chars,
text (description, truncated to {{CAP}} chars). Read it in parts if large; skip
no rows.

OFFICIAL CRITERIA — four, equally weighted, 25 points each, 100 total:
1. {{CRITERION_1}}
2. {{CRITERION_2}}
3. {{CRITERION_3}}
4. {{CRITERION_4}}

CALIBRATION across {{N}} entries. Be harsh; the median entry is not good.
25 = best in the whole field on that axis, give it almost never. 22-24 = strong,
top ~2%. 19-21 = solid. 15-18 = competent but ordinary, where most working demos
land. 10-14 = thin wrapper. <10 = concept only, or the platform named but not
used.

HOW TO READ THE TEXT. You are scoring a written submission, not running code.
- Reward checkable specificity: named tools, exact counts, a described
  mechanism, a stated limitation, numbers with a method.
- Discount superlatives, roadmaps, "revolutionary/seamless" with nothing behind.
- live+repo+video all true is the baseline for Execution above 15, not evidence
  of quality — most entries have all three.
- What separates the top: {{WHAT_THE_PLATFORM_UNIQUELY_ENABLES}}, or a measured
  ablation or benchmark the entry ran on itself.
- An entry that names its own weakness is usually stronger than one that does not.

DELIVER, and nothing else:
1. Table of the TOP 15 in your slice, best first: slug | C1 | C2 | C3 | C4 |
   total | one sentence on what it actually does that earns the score.
2. One line: how the slice distributed — how many scored 80+, 70-79, 60-69,
   50-59, under 50.
3. Any entry you would argue belongs in the top 10 of the whole {{N}}, one
   sentence each. If none, say none.

Do not fetch anything from the network. Judge only the given text. Do not pad.
