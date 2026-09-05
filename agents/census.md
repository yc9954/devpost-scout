# Agent: count the field via participants

The more complete of the two enumeration routes. Slow (hours). Run it in
parallel with the search sweep and compare the totals.

---

Produce a definitive census of {{HACKATHON}} submissions by walking the
PARTICIPANT list, not the gallery. The gallery at {{HOST}}/project-gallery is
{{GALLERY_STATUS}}, so it cannot be enumerated — but the participants page can,
and every submission belongs to a participant whose public portfolio lists it.

THE ROUTE — reuse the scripts in {{SCOUT}}/discover and {{SCOUT}}/verify, do not
rewrite them. Work in {{SCRATCH}}; do not overwrite anything in {{DATA_DIR}}.
Never run python with /tmp as cwd (a stray /tmp/inspect.py shadows the stdlib).

1. PARTICIPANTS. `discover/participants.py` reads the hackathon's own AJAX route
   `/participants?page=N` from inside a browser tab that already has the
   hackathon page open. Read the script for its arguments. Launch your OWN
   headless Chrome on a port nobody else is using. Page until exhausted. The
   page reports {{PARTICIPANT_COUNT}} — report what you actually retrieved.
2. PORTFOLIOS. `discover/portfolios.py` fetches each public profile over plain
   HTTP and extracts every `/software/<slug>` link, checkpointing as it goes.
3. MEMBERSHIP. `verify/membership_check.py` decides which of those slugs were
   actually submitted here, using the page's own `#submissions` block.
4. COMPARE against {{PRIOR_CORPUS}} if one exists. Match on EXACT SLUG only —
   Devpost appends random suffixes to duplicate titles, so `x-vmy83b` and
   `x-4ym0tq` are different projects.

WATCH FOR: the WAF answers concurrency with a 202 challenge page in a 200-shaped
body, which scores as "profile with zero projects" and silently under-counts. If
you see a run of empty profiles, stop, purge them, and re-crawl behind
`lib/fetch.py`. Four workers on project pages; search is a separate, harder
limit.

DELIVER:
- The headline number, with its holes stated plainly: how many participants of
  {{PARTICIPANT_COUNT}} you enumerated, how many profiles fetched, how many
  failed, and therefore what this is a floor on.
- A table: participants / profiles / unique slugs / confirmed submissions /
  new since {{PRIOR_DATE}}.
- The confirmed-new list as JSON, path reported.
- What fraction of the prior corpus this route independently re-derived — that
  is your coverage evidence.
- Anything you could not resolve.

Read-only throughout: log into nothing, change no account state, post nothing.
If a step is too slow, checkpoint and report exactly how far you got rather than
extrapolating silently.
