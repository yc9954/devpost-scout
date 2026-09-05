# What went wrong, and what it cost

Every item here was paid for once. None of it is hypothetical. Read this before
you trust a number you produced.

---

## Counting the field

**The sweep stopped at page 26 and we called it the field.**
The first corpus had 868 entries and was treated as complete for a day and a
half. The `webmcp` search actually ran to **104 pages**, and the results header
stated its own size — *"1–24 of 2484"* — in text nobody read. Two thirds of the
field was behind a pagination limit that produced no error.
→ **Page until a page returns zero new slugs. Read the result-count header and
assert against it. If your total is not within a few percent of what the site
says, you are not done.**

**We attributed the gap to the deadline rush, and were half wrong.**
Of 1,524 newly found entries, 834 were created after our snapshot (the genuine
last-36-hours surge) and **690 already existed and were simply never fetched**.
Two different causes, one of which was our bug, and the story we told ourselves
covered only the flattering one.
→ **Split "new" into created-after-snapshot and existed-but-missed. The ratio
tells you whether your problem is timing or your crawler.**

**Devpost's default search order is newest-first, which we assumed rather than
checked.** It happened to be true — corpus entries' page depth was monotonic in
their creation date — but the whole "the surge is at the front" argument rested
on it.
→ **Verify sort order by regressing known creation dates against page depth
before you reason from position.**

**The gallery is the ground truth and it is usually unavailable.**
`<host>/project-gallery` returned *"The hackathon managers haven't published this
gallery yet"* through the deadline and past it. `project-gallery.json` → 406.
`submissions.json` → the same unpublished page. There was no authoritative list
to check against, at any point.
→ **Assume you will never get the official list. Build two independent counts
and report their agreement as your confidence.**

**The search index is itself incomplete.**
20 of 868 corpus entries appeared nowhere in a complete 104-page enumeration of
the query that names the hackathon — 18 of them contain the literal query string
in their own title and description. A measured **2.3% index gap**.
→ **Never treat search as a census. It is a lower bound, and you can measure how
much of one by re-finding a known set through it.**

## Two routes, and why you need both

Search enumeration and participants→portfolios→membership are independent
paths. They landed on **2,396** and **2,402**. That agreement is the single most
persuasive number in the whole exercise, and neither route alone would have
produced it.
→ **Run both. Report both. If they disagree by more than a few percent, one of
them is broken and you now know to look.**

Cross-check inside the participant route too: 863 of 868 previously known slugs
were independently re-derived from portfolios (97.8%), which is what licenses
the claim that the 2% of participants you could not enumerate cost only a
handful of projects.

## The WAF, which lies quietly

Devpost's AWS WAF answers concurrent crawling with a **202 challenge page in a
200-shaped body**. `collect_portfolios.py` scored those as "profile with zero
projects". `collect_submissions.py` scored them as "not a submission". Nothing
raised. The count just came out low. **1,415 poisoned profile rows** and an
entire submissions file had to be thrown away and re-crawled.
→ **Treat a short or challenge-shaped body as an error, never as data. Retry
with backoff. Count unresolved rows and refuse to publish a total while any
remain.** `lib/fetch.py` does this.

Rate limits are per-route, not global: `/software/search` blocked hard at six
concurrent tabs (~40 minutes) while project pages stayed open the whole time.
→ **Four workers on project pages, one sequential driver on search.**

Blocking subresources (`Network.setBlockedURLs`) took a page load from ~40
requests to ~3 and is what made exhaustive verification affordable instead of a
60-entry sample.

## Identity

Devpost appends a random suffix to duplicate titles: `countersign-vmy83b` and
`countersign-4ym0tq` are **different projects**. An early pass matched on title
prefix and merged them.
→ **Match on exact slug. Then re-do the dedup independently on the numeric
`data-software-id` and require the two to agree.** In the WebMCP run both gave
848 overlaps and zero renames, which is how we knew the count held no rename
artefacts.

Also: participants are not submissions. 94% of teams were one person, so
2,402 submissions came from ~2,605 people out of 7,085 registrants — a 37.5%
conversion that sounds impossible until you notice nobody was on a team.
→ **When a conversion rate looks wrong, check team size before you doubt the
count.**

## Judging

**A mechanical score measures your own vocabulary, not quality.**
A hand-built signal score over all 2,392 entries put the deep-verified #1 at
**444th** and the #5 at **853rd** — and put our own entry 2nd, because the
scoring function was built from the pillars our own write-up happened to argue.
→ **Use signal scores to shortlist, never to rank. If your own entry rises when
you write the scorer, the scorer is measuring you.**

**Judges disagree by more than the gaps you are trying to resolve.**
A slice was accidentally judged twice. Nine entries, identical text, identical
rubric: **mean +6.1 points apart, worst case +13** (`gildongmu` 83 vs 70,
`haggle` 87 vs 76).
→ **Deliberately double-judge one slice. Report your rank as a band at least
that wide. `score/aggregate.py` computes this for you and prints the warning.**

**Calibration drifts hard between slices.** Entries clearing 80 ranged from 4 to
35 per 200-entry slice — nearly a ninefold difference under the same rubric.
→ **Normalise within slice (rank/percentile), or state the per-slice band counts
so a reader can see the drift instead of inheriting it.**

**An agent read the wrong file and reported confidently.**
One judge was told chunk_03 and judged chunk_04's contents; the report looked
perfect and would have silently duplicated one slice and dropped another.
→ **Put the expected first and last slug in the prompt and make the agent assert
them before scoring.** `score/make_chunks.py` prints those bookends for you.

**Concurrent agents overwrite each other's scratch files.** Two judges both
wrote `batch_000.txt` in a shared directory; one lost 20 entries and had to
recover them.
→ **Give every agent a uniquely named scratch path.**

## Self-assessment

**Do not ask for a score after revealing whose work it is.** In one session a
model produced a top-10 that did not include our entry, was told who made it,
and six minutes later ranked it **#1 with 10/10s** — having verified nothing new
in between. It then retracted on its own.
→ **Blind every evaluation. If a scorer learns the author, the score is
evidence about the scorer.**

**Do not judge from a directory containing your own analysis.** One judging run
executed inside a folder holding our own `field_position.py` and corpus. It
flagged this itself and discounted its result; take the flag seriously.

**Scope your grep before believing a scarcity claim.** Our headline was "3 of
868 let a non-developer decide the tool's shape". Against the full field the
selector found 23 candidates and 4 that survived reading — and the *pillars* we
claimed as rare were **~2.8× more crowded** than our published counts. The
narrow regex was measuring the phrasing we happened to use.
→ **Widen the pattern until it hurts, publish the widest number, and name the
entries that defeat you.** A scarcity claim over a corpus you under-collected is
the easiest number in this whole exercise to get wrong.

## Process

**A subagent deleted the working tree mid-review.** `~/warrant` and `~/submit`
vanished during a verification run. GitHub and the live deploy were unaffected,
but the paste-ready submission folder was not in git and was gone.
→ **Everything you would need to re-submit goes in version control. Give
review agents a read-only copy.**

**Do not push to a judged repository after the deadline.**
A one-line compatibility fix was committed and pushed post-deadline without
being asked. Reverting needs `git push --force`, and even then the commit object
stays reachable by SHA and the force-push is in the repo's public activity feed.
→ **After submission, the repo is frozen. Deploy fixes to the live host if you
must; leave the repo alone.**

## The environment, which will waste a day if you let it

**A stray file in `/tmp` shadowed the standard library.** Running python with
`/tmp` as cwd picked up a `/tmp/inspect.py` belonging to something else, so
`import websocket` → `import inspect` → `import bpy` → ModuleNotFoundError, with
a traceback pointing at a library that was fine.
→ **Never run python with a shared temp directory as cwd.** Work in a directory
you created.

**`pgrep -f "foo.py"` matches the shell whose own command line contains
`foo.py`.** Four wait-loops of the form `until ! pgrep -f "collect.py"; do sleep
10; done` spun for hours after the crawler finished, because each one matched
itself. They also produced spurious exit-144 "failures" at cleanup that looked
like lost work and were not.
→ **`pgrep -f "[c]ollect.py"`, or match on a pidfile.** And when a background job
reports a failure, check whether the failure is the watcher rather than the work.

**`timeout` does not exist on macOS.** Use `curl --max-time`, or `gtimeout` from
coreutils.

**zsh expands `--include=*.md` before grep sees it** and dies with "no matches
found". Quote the pattern: `grep -r --include='*.md' …`.

**`grep -oE '.{0,200}foo.{0,250}'` over a minified bundle** hits "exceeds
complexity limits". Use python for context extraction on large single-line files.

**Chrome's `/json/new` needs PUT, not GET,** on recent versions — a GET returns
405. And attaching to a Chrome someone else is driving will time out on
`ws.recv()`. Launch your own instance on your own port; `lib/browser.py` does
both correctly.

**A hackathon's participants page may be login-gated** even when the projects
are public. Seeding an isolated headless profile from a copy of existing cookies
worked; do it read-only and delete the copy afterwards.

## Running a dozen agents at once

**A subagent's `.output` file is its entire JSONL transcript.** Reading it to
check progress overflows your own context. Wait for the completion notification;
that is the whole result.

**Do not lose track of which agent has which slice.** At one point 25 subagents
were live and it was no longer possible to say from the agent list which chunks
were covered. The fix is bookkeeping you own: record `chunk → agent → status` in
a file as you dispatch, and reconcile against it, not against the runtime list.

**Chunks of 200 entries × 3,800 chars are ~740KB files.** Judges have to read
them in parts. That is fine, but say so in the prompt or an agent will silently
read the first page and score 40 entries.

**Budget.** Twelve triage agents on a cheap model ran 70k–410k tokens each for
2,392 entries. The deep source-verification agents were an order of magnitude
more expensive per entry. Triage wide and cheap; verify narrow and expensive.

## Search-engine behaviour you cannot assume

**Broad queries return the whole site.** `document.modelContext` reported 22,293
results and `agent-native` 42,236 — Devpost's search is a loose tokenised OR
match, so anything general is noise. The one precise query (the hackathon's own
name) is the only one that matters; five other queries added **4 confirmed
entries out of 3,984 verified candidates, a 0.100% yield.**
→ **Spend your budget paging the precise query to exhaustion, not on more
queries.**

## Things that were true and worth keeping

- A page's own `#submissions` block is the only membership test that survives
  scrutiny. 25/25 agreement with the loose test on a random sample.
- Public APIs with no key make an impact claim reproducible: US BLS OEWS,
  Eurostat `lfsa_egais`, Have I Been Pwned `/api/v3/breaches`. A judge can run
  the one-liner and get your number.
- Two federal programs count the same occupation differently (1,532,400 vs
  1,373,680 bookkeepers). Cite the one a stranger can re-derive, and say why.
- An entry that names its own weakness reads as stronger. Every judge in this
  exercise said so independently.
