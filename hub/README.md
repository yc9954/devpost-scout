# The idea hub

Every hackathon Devpost lists, and the projects inside the ones worth reading —
in one SQLite file you can query before you decide what to build.

It answers two questions, both of which this project has previously got wrong by
guessing:

> **Has someone already built this, and did it win?**
> **Which hackathons are worth entering at all?**

## Why this is affordable when the project corpus was not

`discover/search_sweep.py` needs a real Chrome, gets rate-limited hard, and its
first run captured a third of the field. The hackathon index has none of those
problems:

| | `/api/hackathons` | `/software/search` |
| --- | --- | --- |
| transport | plain HTTP, JSON | CDP browser only |
| pagination ceiling | none — page 1538 of 1538 returns rows | capped |
| states its own total | `meta.total_count` | in prose, in the header |
| cost of a census | ~1,540 requests | hours, and a WAF fight |

Project galleries sit in between: plain HTTP, 24 a page, and — the reason they
matter — they carry a **`winner` ribbon**. A corpus of winners across many
hackathons is a better idea hub than a corpus of everything, because it is
pre-filtered by people who read the whole field.

## Collect

```sh
# 1. every hackathon (~1,540 requests, resumable, asserts against meta.total_count)
python3 hub/collect_hackathons.py --out data/hackathons.jsonl

# 2. the winners of the hackathons worth reading
python3 hub/collect_gallery.py --from-index data/hackathons.jsonl \
        --winners-only --min-prize 25000 --limit 200 --out data/projects.jsonl

# 3. one hackathon in full, when you are actually entering it
python3 hub/collect_gallery.py --host <host>.devpost.com --out data/projects.jsonl

# 4. build the hub
python3 hub/store.py build --hackathons data/hackathons.jsonl \
        --projects data/projects.jsonl --db data/ideas.db
```

Both collectors checkpoint after every unit and resume by skipping what is
already in the output file, so an interrupted run costs only the page it was on.

## Query

```sh
python3 hub/store.py stats
python3 hub/store.py orgs --min-prize 25000        # who runs hackathons, and how big
python3 hub/store.py search "agent browser tool"   # has this been built?
python3 hub/store.py search "food insecurity" --winners
```

**Search shortlists; it never ranks.** It is FTS over title and tagline, which
means it matches your vocabulary rather than the field's — the same failure that
put a deep-verified #1 entry at 444th in `score/signal_score.py`. Widen the query
until it hurts, then read the entries. A scarcity claim built on one keyword
query is the easiest wrong number in this repo.

Two more limits worth stating before quoting anything from here:

- **A gallery the managers never published yields nothing**, and is recorded as
  `gallery_unpublished` rather than as a hackathon with no projects. WebMCP's own
  gallery stayed unpublished through the deadline and past it.
- **Taglines are ~100 characters.** An idea whose distinguishing feature is in
  the body will not surface. For a hackathon you are actually entering, collect
  the full corpus through `discover/` + `verify/` and position against that.

## Schema

`hackathons` — id, title, host, url, **organization**, state, dates, **prize_usd**,
registrations, themes, winners_announced, gallery_url, featured, invite_only,
location.

`projects` — software_id, slug, url, title, tagline, host, hackathon_title,
organization, **is_winner**, members, gallery_page.

`projects_fts` — FTS5 external-content over title, tagline, hackathon_title.
Rebuild it with `INSERT INTO projects_fts(projects_fts) VALUES('rebuild')`;
a `DELETE` + re-`INSERT` corrupts the index.

## Feeding it into gbrain

The JSONL files are the interchange format. Each project row is one idea with a
stable `url` as its identity, so ingest is idempotent — re-running the collector
and re-ingesting will not duplicate. Keep `data/*.jsonl` as the source of truth
and treat `ideas.db` as a derived artifact you can always rebuild.

## Caveats you must carry into any claim

- **Prize amounts are self-reported and unvalidated.** The index contains a
  hackathon claiming $12,000,000 with 91 registrants and another claiming
  $10,000,000 with 7. Rank by `registrations` when you want *importance*; use
  prize only alongside it.
- **Eight currencies.** Devpost states the prize in the host's own currency
  (USD, CAD, INR, EUR, GBP, MXN, PKR). `prize_usd_approx` applies **static,
  approximate** rates and will drift; `prize_local` and `prize_currency` are
  stored so any figure can be re-derived. Summing raw amounts puts a ₹12.7M
  college hackathon above Google — that was the first version of this table.
- **`--winners-only` stops at the first page with no ribbon.** Devpost sorts
  winners first on every gallery checked, which makes winner collection two
  requests instead of four hundred. If a gallery ever orders differently this
  silently truncates — pass `--no-early-stop` when a result looks short.

## From rows to a graph you can think in

The collectors give you rows. These three turn them into a vault:

```sh
python3 hub/enrich_projects.py --in data/projects.jsonl --out data/projects_full.jsonl
python3 hub/extract.py         --in data/projects_full.jsonl --out data/facets.jsonl
python3 hub/vault.py           --in data/facets.jsonl --out vault/
python3 hub/gaps.py            --in data/facets.jsonl --vault vault/ --top 40
```

`enrich_projects.py` fetches each project page and parses the 2,000–8,000-word
body, its section headings, the stack, links and team — and saves the raw HTML to
`data/pages/`, which is also the directory `verify/parse_pages.py` has always read
and nothing previously wrote.

`extract.py` decomposes each write-up against `hub/taxonomy.json` into four
facets: **mechanism** (the move that makes it work), **domain**, **user**,
**substrate** (what it reads). Every hit is reported at two strengths — `strong`
(named in title/tagline, or repeated in the body) and `weak` — so a count can be
stated as a band rather than a number.

`vault.py` writes an Obsidian vault: one note per project, per facet, per
hackathon, wired with `[[wikilinks]]`. Facet notes are the graph hubs — open
`vault/` in Obsidian and the mechanism notes sit at the centre of every project
that used them.

`gaps.py` is the ideation engine. For every facet pair it computes the expected
co-occurrence under independence, `E = count(A)·count(B)/N`, and ranks the pairs
whose observed count sits furthest below it. Both halves proven, the combination
unoccupied.

### The taxonomy will lie to you if you let it

The first version reported that 54% of all projects were about
housing and homelessness. It was matching `rent` inside *current* and *inherent*,
`labor` inside *collaborated*, `frame` inside *framework*, `signed` inside
*designed*, `aging` inside *packaging*, `dom` inside *random*, and `url` inside
*curl*. Every bare stem under ~6 characters needs `\b` on both sides, and a stem
that is a common English substring should be deleted rather than bounded.

Audit before trusting a count — print the matched context, do not read the total:

```sh
python3 - <<'PY'
import json, re
tax = json.load(open('hub/taxonomy.json'))
rows = [json.loads(l) for l in open('data/projects_full.jsonl') if l.strip()]
rx = re.compile(tax['domain']['accessibility'], re.I)
for r in rows[:400]:
    t = f"{r.get('title')} {r.get('tagline')} {r.get('description')}"
    m = rx.search(t)
    if m: print('…', t[max(0, m.start()-30):m.end()+25].replace('\n', ' '), '…')
PY
```

### And an empty cell is a question, not an idea

From `position/IDEA-SELECTION.md`, paid for once already: **zero occupancy is not
evidence of a good idea. Nobody may have done it because it isn't attractive.**
Every gap note carries the five kill tests for exactly this reason. Run them.

## Generating candidates for one hackathon

```sh
python3 hub/ideate.py --config config.json --facets data/facets.jsonl --top 12
```

`gaps.py` asks what is missing *in general*. `ideate.py` asks what is missing
**for the hackathon you are entering**, and scores every candidate against that
hackathon's criteria verbatim — with the tiebreak criterion weighted up, because
Devpost's standard tie-break resolves on the first-listed criterion and that is
what decides placements once scores bunch at the top.

Rubric terms are IDF-weighted against the corpus. Weighting by criterion share
alone let generic words — *project*, *work*, *deliver*, *real* — dominate, and
every candidate came back with the same near-zero fit; rarity weighting is what
makes the distinctive rubric words carry the signal.

Two limits to state whenever you quote its output:

- **"Absent here" is only as good as your field data.** Without `--field`
  pointing at the target hackathon's own corpus, absence is measured against the
  whole brain, which is much weaker evidence. Run stage 2 of `/scout` first.
- **Combination candidates need a large brain.** At a few hundred projects almost
  no facet pair clears the expected-count floor, so the generator falls back to
  transfer candidates, which rank close to a global popularity list. Collect
  widely before trusting the ordering.

## One command

```sh
python3 scout.py "agents for humans"          # name it; get rubric, field, candidates
python3 scout.py "revenuecat shipaton 2026" --deep 120
```

`scout.py` chains resolve → rubric → field → decompose → candidates and prints one
brief. It degrades honestly: an unpublished gallery is reported as a real state
rather than as zero entries, and when the target field is unavailable the
candidate ordering **switches from absence to rubric fit** and says so, because
ranking by global frequency without field data just reproduces a popularity list.

### What the facet names do not capture

`revocation_withdrawal` matches a DeFi token-approval revoke and a clinical
consent withdrawal with equal confidence — the regex sees the verb, not the
stakes. Facets are a shortlist over the corpus, not a semantic model. Read the
exemplar write-ups in every candidate note before believing the pairing means
what you want it to mean.

## Empty cells are a small-corpus artifact

At 2,873 winners several `mechanism x domain` pairs were genuinely unoccupied and
the generator ranked them first. At 8,636 almost none are: every well-populated
pair picks up a few entrants, and a filter looking for zeros returns nothing.

That is not the field closing. It is sampling. The stable quantity is
**under-occupancy relative to independence** — `observed / expected` — which
survives the corpus tripling where "is it zero" does not. Both `gaps.py` and
`ideate.py` rank on it.

Two things follow whenever you quote this output:

- **A deficit is not automatically an opportunity.** `financial_record x
  education` sits 74 below independence because people do not put payment
  ledgers in classroom apps, not because nobody has thought of it. The generator
  cannot tell a gap from a non-sequitur; that is what reading the exemplars and
  running the five tests is for.
- **Report the ratio, not the absence.** "26 where independence predicts 48" is a
  claim that survives someone re-running it on a different corpus. "Nobody has
  done this" does not.
