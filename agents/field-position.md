# Agent: where does my idea sit in this field?

Run this BEFORE you build, on the corpus you collected. It kills ideas cheaply.

---

You have {{N}} submission descriptions in {{CORPUS}}. I am considering building
{{IDEA}}. Tell me how crowded that is, and be unflattering.

1. Write regexes for each PILLAR of the idea — the separable claims it rests on
   (e.g. "creates a tool at runtime", "withholds a field structurally", "a write
   waits for a person"). Count how many entries match each.
2. Widen each pattern until it hurts. Report the narrow AND the wide count, and
   say which phrasings the narrow one missed. A pattern that only matches your
   own vocabulary is measuring you, not the field.
3. Count every PAIR and every TRIPLE of pillars. How many entries hold two
   together? Three? The combination is usually the only thing that is actually
   rare.
4. Run MY OWN description through the identical patterns and report the result
   as data, not as a claim. Note that match count scales with description
   length — report how it scores on a {{SHORT}}-char excerpt too, so the
   comparison is like-for-like.
5. Read the top ~20 nearest entries in full. For each: does it defeat my claim,
   partially or entirely? Quote the sentence that decides it.
6. State the single strongest argument that my idea is NOT distinctive.

DELIVER a table of counts, the pair/triple table, the named near-neighbours with
the deciding sentence for each, and a one-paragraph verdict. Do not flatter.
