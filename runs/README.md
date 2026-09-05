# Runs

One directory per hackathon entered. Each holds what that run measured, so a
later run can be compared against it rather than started from nothing.

`FINDINGS.md` and `data/` are checked in. **`corpus/` is not** — the raw
submission pages and the judged chunks run to tens of megabytes and belong on
disk, not in git. `.gitignore` excludes `runs/*/corpus/`.

For the WebMCP run those local-only artifacts are:

| | |
| --- | --- |
| `corpus/submission-pages.tar.gz` | 1,539 fetched submission pages, 130MB → 35MB |
| `corpus/chunk_*.json.gz` | all 2,392 entries as the judges saw them |

Re-deriving them costs several hours of crawling, so keep a copy outside the
repo if the run still matters to you.
