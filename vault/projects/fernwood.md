---
slug: "fernwood"
url: "https://devpost.com/software/fernwood"
title: "Fernwood"
hackathon: "Backblaze Generative Media Hackathon: Build with Genblaze on B2"
organization: "Backblaze"
winner: true
words: 992
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/provenance_signing"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Fernwood

> Fernwood turns Backblaze into a brand's memory: every rejected attempt teaches the Campaign Brain, so each run scores higher and cuts a real multi-shot ad. It's a Campaign Studio for elite ad teams!

[Devpost](https://devpost.com/software/fernwood) · hackathon [[Backblaze Generative Media Hackathon- Build with Genblaze on B2]]

## Facets

**mechanism** [[benchmark_measured]] [[provenance_signing]] [[structural_withholding]]
**domain** [[developer_tools]] [[supply_logistics]]
**substrate** [[code_repository]] [[video_visual]]

**stack** backblaze-b2, deepgrseedream, fastapi, ffmpeg, genblaze, python, react, tailwindcss, tokenrouter, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next

## Body

Inspiration We started with a self-critiquing campaign generator: it makes a key visual, a voiceover and a copy suite, has a vision model score each one against the brief, and regenerates anything that fails. Every attempt — including the rejected ones — gets a SHA-256 manifest and lands in Backblaze B2. Then we noticed something uncomfortable. Every AI campaign tool generates assets. None of them actually learn anything after repeated attempts. That gap became the project: turn the storage layer into memory. What it does Give Fernwood a brand brief and it produces a campaign kit — key visual, voiceover, copy suite, and a cut multi-shot advertisement — with a Campaign Brain sitting behind it. The Brain has five lobes, each a real inference call with its own provenance manifest: Lobe What it does Recall Reads this brand's past rejected attempts back out of B2 Strategy Turns brief + learned laws into one directive all three tracks share Foresight Predicts the score and failure mode before spending any quota Audience Four synthetic personas from the brief react to the finished work Learning Distils new brand laws from this run's rejections and objections A brand law is a citation, not an opinion. Each one names the campaign, the attempt and the critique sentence that produced it — laws without evidence are discarded before they're saved. The advertisement isn't one still in motion. An LLM writes a storyboard, each shot gets its own generated first frame and camera move, the shots render in parallel, then ffmpeg cuts them together, lays the approved voiceover across the whole film, and closes on a branded end card. How we built it Genblaze is the orchestration and provenance spine. The key design call: one Pipeline.run() per attempt , not per asset. A Pipeline is declared then executed as a unit, and the retry prompt doesn't exist until the previous critique comes back — so one run per attempt means one manifest per attempt, which is the entire "attempt #1 rejected, attempt #2 approved" chain. Attempts link via from_result() , recording parent_run_id lineage. Both provider styles appear, chosen by the upstream API rather than by preference: images are synchronous ( SyncProvider ), video is a genuine task queue, so it subclasses BaseProvider and implements real submit / poll / fetch_output . That async lifecycle is what lets three ad shots render concurrently — six minutes of sequential waiting becomes two. Backblaze B2 holds campaigns, every manifest, and brains/{slug}/brain.json with an immutable snapshot per version. The versioning matters: "the brain improved" is only a checkable claim if the earlier brain still exists to compare against. The resonance score blends felt sentiment with stated intent: $$\text{resonance} = 0.6 \cdot \overline{\text{sentiment}} + 0.4 \cdot \overline{\text{intent}}$$ Intent is weighted lower deliberately — an audience that admires an ad without acting on it is a real and common outcome, and a single figure that can't tell the two apart flatters every campaign. We report population standard deviation alongside it, because 50/100 from a lukewarm panel and 50/100 from a panel split down the middle are different problems. Challenges we ran into The ffmpeg mux hung forever. Laying the voiceover over the cut looks trivial. -shortest alone truncates the picture to the length of the narration — silently deleting the end card. Adding apad fixes that, but apad pads infinitely ; combined with -shortest and a filtergraph output, ffmpeg never sees an end-of-stream and runs until killed. It surfaced as a 300-second timeout per mux, not an error. The fix is bounding the output with an explicit -t of the video's own duration. A model that looked healthy and wasn't. gemini-3.5-flash returns HTTP 200 with empty content on multimodal requests. Checking the status code alone would have degraded every critique to a heuristic fallback with no error anywhere. Our startup probe now requires non-empty, parseable JSON before trusting a model. A free tier that couldn't carry the load. We trialled a free LLM for all text work. Measured live, it capped at 8 requests per minute and took over two minutes per structured call — against a pipeline that makes ~20 text calls per campaign. We benchmarked six candidates on a real Campaign Brain prompt and chose on evidence. What survived the experiment is a client-side rate limiter that paces any *-free model under its cap and is inert for everything else. Image models letter hex codes into the frame. Passing #1E3A2B produced posters with colour swatches labelled "E3AB" painted into the image — which the critique then correctly failed for containing text. We convert hex to words ("deep forest green") and sanitize every string that reaches an image model. Our own UI lied. The results page had a hardcoded CRITIQUE VERDICT: PASSED badge sitting directly above a provenance log listing failed attempts. For a project whose entire premise is honest reporting, that was the worst bug in the codebase. It now derives from actual asset status and reads CRITIQUE: 3/4 PASSED with the shortfall named. What we learned Storage is not a cost centre. Every failure this studio produces is training data for the next campaign — the rejected attempts turned out to be worth more than the approved ones, because they're the only place a brand's boundaries are written down. We also learned to make our claims falsifiable. The improvement panel refuses to report a trend from a single run. The demo flag that caps the first image critique is compensated for, so we never measure our own harness. And the advertisement's provenance record states plainly that the generated motion was never scored by any model — because overstating what you verified is worse than a modest claim. What's next Cross-brand law transfer (what a coffee brand learned that a bakery could use), critique of the generated motion itself, and letting a brand manager promote or veto a law by hand — human feedback as another evidence source the Brain reasons over. <div