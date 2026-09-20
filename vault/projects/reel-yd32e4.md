---
slug: "reel-yd32e4"
url: "https://devpost.com/software/reel-yd32e4"
title: "Reel"
hackathon: "Backblaze Generative Media Hackathon: Build with Genblaze on B2"
organization: "Backblaze"
winner: true
words: 1200
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Reel

> A scene lives as words until someone spends real money to see if it works. Reel turns a screenplay scene into a fully previsualized cut — shots, stills, motion, and score — in minutes.

[Devpost](https://devpost.com/software/reel-yd32e4) · hackathon [[Backblaze Generative Media Hackathon- Build with Genblaze on B2]]

## Facets

**mechanism** [[human_in_the_loop]] [[provenance_signing]]
**domain** [[developer_tools]] [[education]] [[finance_payments]] [[health_clinical]] [[housing_homeless]] [[supply_logistics]] [[transportation]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[video_visual]] [[web_dom]]

**stack** backblaze-b2, boto3, fastapi, ffmpeg, flux, genblaze, kling, llama, musicgen, python, replicate, uvicorn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for reel

## Body

Logo Inspiration I'm a screenwriter. I have a feature called CARRIER — ninety-four pages of military horror — and like every writer, I keep hitting the same wall: a scene lives as words until someone spends real money to find out if it works. A location. A crew. A shoot day. Previsualization exists to solve exactly this, but it's slow and expensive, so writers almost never get it. The people who most need to see a scene before committing to it are the people who can least afford to. So I built the tool I wished existed, and pointed it at my own script first. What it does Reel turns a screenplay scene into a fully previsualized cut. Paste in a scene. Reel breaks it into shots the way a DP would — establishing, coverage, the beats — then generates a still for each shot, animates each still into a moving clip, scores the scene to match its dominant mood, and assembles everything into one continuous, watchable cut. Every asset lands in Backblaze B2 with a provenance record of exactly which model produced it, from which prompt, under which draft version. A writer can iterate — adjust the scene, regenerate, adjust again — until it feels right, then hand a director something that's already been visually pressure-tested. The thesis: shift discovery left. Move the expensive question ("does this scene work?") from the shoot day to the writer's desk. How we built it The pipeline runs on Genblaze for orchestration and Backblaze B2 for durable storage: Shot breakdown — an LLM reads the scene and returns a structured shot list (size, mood, time of day, camera move) as validated JSON. Stills — each shot description is composed into a prompt with a consistent "look bible" style anchor, so shots stay visually coherent across the scene, then rendered with Flux. Motion — each still is animated into a clip via image-to-video, so the movement matches the frame it came from rather than drifting. Score — the dominant mood across the shot list drives a generated underscore for the scene. Assembly — ffmpeg concatenates the clips in shot order and mixes the score underneath, producing a single scene.mp4. Backblaze B2 is the backbone, not an afterthought. Assets are organized hierarchically by project and draft version (reel/carrier/v26/sh01/...), each shot carries a provenance.json recording provider, model, prompt, and source hash, and the finished cut is stored alongside its parts. Because assets are versioned by draft, a v27 pass forks cleanly off v26 instead of overwriting it — you can compare how a scene looked across rewrites. The gallery UI reads directly from B2, proxying private assets through an authenticated server, so nothing is publicly exposed. It presents the assembled scene as a player plus the shot board beneath it. Challenges we ran into Model IDs were the single biggest time sink. Nearly every failure traced back to a model string that didn't resolve — names from documentation examples that didn't exist on the account, renamed versions, case sensitivity. I stopped guessing and started introspecting the installed SDK registries and reading provider model pages directly before writing any code against them. That discipline saved the build. Image-to-video needed a public URL. The video model requires a start_image its servers can actually fetch — and my B2 bucket is private by design. The fix was to hand the image generator's own public delivery URL directly to the video model (provider-to-provider), then persist the resulting clip to B2 myself. Chaining through private storage silently breaks; understanding why took a while. Non-official models need version objects, not version strings. The music model 404'd on both its bare name and a pinned name:hash string. Resolving the model and running its version object worked. Same class of problem as the model IDs — assumptions about how a reference is passed. Rate limiting under a low balance. The image provider throttles hard (burst of one) below a credit threshold, which silently killed multi-shot runs. I wrapped every call in retry-with-backoff so a full scene completes unattended. One provider consolidation. I started with a multi-provider architecture, then discovered mid-build that one provider's free tier was exhausted and its chat models were dedicated-instance billing (hourly GPU rental, not per-call). Collapsing to a single provider made the architecture simpler and the story cleaner. ObjectStorageSink with full manifest provenance. Clips and score are persisted with direct S3 calls, because the image-to-video stage must hand a PUBLICLY FETCHABLE start image to the video provider — private B2 URLs can't be fetched by the video model's servers — so that stage runs provider-to-provider and the output is persisted afterward. Accomplishments that we're proud of It works end to end, on my own feature. Screenplay text goes in; a scored, assembled, watchable scene comes out. Not a mockup or a single-model demo — the full chain, dogfooded on a real 94-page script I wrote. The provenance is real, not decorative. Every asset in the bucket can tell you which model made it, from which prompt, under which draft. That's the difference between "I generated some media" and "I have an auditable production pipeline." I shipped a finished cut, not a folder of assets. The ffmpeg assembly step was the difference between seven files and one watchable scene. That last mile is where most pipelines stop, and it's the whole reason the output feels like film instead of output. I debugged my way through five separate integration walls in a day — wrong model IDs, a private-storage handoff that silently broke image-to-video, a version-reference bug on a non-official model, a rate limiter that killed multi-shot runs, and a provider whose billing model didn't fit. Every one got diagnosed properly instead of patched around, and every fix is documented so it's repeatable. The tool solves my own problem. I'm not guessing at what a screenwriter needs from previs. I'm the user, and CARRIER is the test case. What we learned Verify, don't assume — every integration wrinkle in this build came from trusting a docstring example over the live API. Also: the most valuable features surface information the pipeline is already generating. Dialogue is already in the screenplay. Provenance is already in the generation metadata. The work is making it legible, not inventing new systems. What's next for Reel What's next for Reel Full-feature previs — running all 94 pages of CARRIER, which turns character consistency and cost management into the central problems. Voices and dialogue — screenplays already contain formatted dialogue; extracting it and casting consistent voices per character is the leap from "visual tool" to "feels like a film." Casting discovery — surfacing the character decisions the models make implicitly (age range, build, vocal register) as a structured casting brief a real casting director could work from. Human-in-the-loop approval gates — approve the stills before spending on video, the way a real production approves boards before it shoots. Cheaper and better. Other story inputs — the engine doesn't care that the input is a screenplay. A child's spoken story, song lyrics, or a novelist's own manuscript all become film through the same pipeline. University deployment — putting Reel in front of film and media students for real-world testing. <div