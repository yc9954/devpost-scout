# devpost-scout

Tooling and playbooks for entering a Devpost hackathon with evidence instead of
optimism: enumerate the whole field, find where your idea actually sits in it,
build the product, film it, write it up, and score yourself blind before the
judges do.

Built during **The WebMCP Challenge** (Sep 2026, 2,392 submissions). Everything
here was used in anger; `PITFALLS.md` is the list of what it cost to learn.

## Read these first

| | |
| --- | --- |
| [`METHOD.md`](METHOD.md) | the pipeline, in order, with the commands |
| [`PITFALLS.md`](PITFALLS.md) | **every mistake and what it cost.** Read before trusting any number you produce |
| [`position/IDEA-SELECTION.md`](position/IDEA-SELECTION.md) | **five tests that kill an idea before you build it.** Six of ours died |
| [`build/`](build/) | the product: [film](build/FILM.md) · [evidence](build/EVIDENCE.md) · [write-up](build/WRITEUP.md) · [ship](build/SHIP.md) |
| [`agents/`](agents/) | reusable agent prompts, `{{placeholder}}`-parameterised |
| [`runs/webmcp-2026-09/`](runs/webmcp-2026-09/) | the full WebMCP dataset and findings |

## Porting to another hackathon

Copy `config.example.json` to `config.json` and change five things:

```json
{
  "hackathon_host":    "yourhack.devpost.com",
  "primary_query":     "the one word that names it",
  "membership_marker": "The Exact Hackathon Name",
  "criteria":          [ ...the official rubric, verbatim... ],
  "pillars":           { "your_claim": "regex", ... }
}
```

Find `membership_marker` by opening one known entry and reading the block
Devpost renders as *"Submitted to …"*. Everything else keys off the config;
nothing else in `discover/`, `verify/` or `score/` is WebMCP-specific.

Requirements: Python 3.9+, `websocket-client`, Google Chrome, and `ffmpeg` for
the film pipeline.

## The shape of it

```
discover/   enumerate the field two independent ways
verify/     decide which projects are actually in this hackathon
position/   count how crowded your idea's pillars are, before you build
score/      slice the corpus, fan out LLM judges, aggregate with error bars
build/      the product: film, evidence discipline, the write-up
agents/     the prompts that did the work
lib/        a CDP-driven Chrome and a WAF-aware fetch
runs/       what one full run produced
```

## Three things worth knowing before you start

**The official list is usually unavailable.** The project gallery stayed
unpublished through the deadline and past it. Build two independent counts and
report their agreement as your confidence — ours landed on 2,396 and 2,402 by
different routes, and that agreement is the most persuasive number in the whole
exercise.

**Your own scoring function measures your own vocabulary.** A mechanical score
built from the pillars our write-up argued put the deep-verified #1 entry at
444th and our own at 2nd. Use signal scores to shortlist. Never to rank.

**Blind every evaluation of your own work.** Told who made it, one model moved
an entry from unranked to #1 with 10/10s in six minutes, having verified nothing
new. If a scorer learns the author, the score is evidence about the scorer.
