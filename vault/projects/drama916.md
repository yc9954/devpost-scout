---
slug: "drama916"
url: "https://devpost.com/software/drama916"
title: "drama916"
hackathon: "Global AI Hackathon Series with Qwen Cloud "
organization: "Alibaba Cloud"
winner: true
words: 650
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# drama916

> One logline in, a finished vertical drama out — written, storyboarded, critiqued before rendering, filmed and voiced by Qwen agents. With a real receipt for every cent of compute.

[Devpost](https://devpost.com/software/drama916) · hackathon [[Global AI Hackathon Series with Qwen Cloud]]

## Facets

**domain** [[finance_payments]]
**substrate** [[financial_record]] [[video_visual]]

**stack** alibaba-cloud, dashscope, ffmpeg, function-compute, python, qwen, qwen-cloud

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges
- what's next

## Body

Type one sentence — and ~10 minutes later you get a voiced, subtitled, 9:16 short film for a few dollars of compute. An autonomous showrunner on Qwen Cloud, with one human approval gate before any money is spent. Inspiration AI video tools render first and fix later — burning the most expensive step over and over. A real production locks the script and storyboard on paper first, then shoots once. We built that. What it does Trends → loglines: a live ribbon of trending topics, refreshed hourly, rewritten by the model into film ideas. Writes the screenplay ( qwen3.7-max ), plans every shot ( qwen3.7-plus ). Critic-before-render: a director-critic loop rewrites weak shots while everything is still text — ~$0.002 a round instead of ~$1 a re-render. Paints the storyboard ( qwen-image-2.0-pro ); a series bible keeps characters consistent across shots. Approval gate: redraw any frame with a note, reorder, drop — the only human step, before a single video credit is spent. The Film-it button shows the real price. Films, voices, cuts: each approved still becomes a happyhorse-1.1-i2v clip, every line gets a voice ( qwen3-tts-flash ), ffmpeg cuts the film — with a caption and hashtags ready to post. Cost ledger: every API call is metered; the price on the premiere screen is the real total, not an estimate. How we built it A zero-framework Python service on Alibaba Function Compute drives the whole pipeline over DashScope. One glass page: composer → live studio stream (script → board → critic → storyboard) → premiere. Challenges Image moderation false-positives ("hug") → G-rated symbolic staging; still blocked → shown honestly with a Regenerate button. The video model can "succeed" with an all-black clip → an ffmpeg luma guard catches it, retries once, then refuses honestly. Voice longer than its 5s clip → the cut holds the shot until the line finishes. What's next Shareable per-film pages, music/SFX bed, and a series mode with recurring characters.Type one sentence — and ~10 minutes later you get a voiced, subtitled, 9:16 short film for a few dollars of compute. An autonomous showrunner on Qwen Cloud, with one human approval gate before any money is spent. Inspiration AI video tools render first and fix later — burning the most expensive step over and over. A real production locks the script and storyboard on paper first, then shoots once. We built that. What it does Trends → loglines: a live ribbon of trending topics, refreshed hourly, rewritten by the model into film ideas. Writes the screenplay ( qwen3.7-max ), plans every shot ( qwen3.7-plus ). Critic-before-render: a director-critic loop rewrites weak shots while everything is still text — ~$0.002 a round instead of ~$1 a re-render. Paints the storyboard ( qwen-image-2.0-pro ); a series bible keeps characters consistent across shots. Approval gate: redraw any frame with a note, reorder, drop — the only human step, before a single video credit is spent. The Film-it button shows the real price. Films, voices, cuts: each approved still becomes a happyhorse-1.1-i2v clip, every line gets a voice ( qwen3-tts-flash ), ffmpeg cuts the film — with a caption and hashtags ready to post. Cost ledger: every API call is metered; the price on the premiere screen is the real total, not an estimate. How we built it A zero-framework Python service on Alibaba Function Compute drives the whole pipeline over DashScope. One glass page: composer → live studio stream (script → board → critic → storyboard) → premiere. Challenges Image moderation false-positives ("hug") → G-rated symbolic staging; still blocked → shown honestly with a Regenerate button. The video model can "succeed" with an all-black clip → an ffmpeg luma guard catches it, retries once, then refuses honestly. Voice longer than its 5s clip → the cut holds the shot until the line finishes. What's next Shareable per-film pages, music/SFX bed, and a series mode with recurring characters. <div