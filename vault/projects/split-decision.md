---
slug: "split-decision"
url: "https://devpost.com/software/split-decision"
title: "Split Decision"
hackathon: "Global AI Hackathon Series with Qwen Cloud "
organization: "Alibaba Cloud"
winner: true
words: 1134
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/accessibility"
  - "domain/civic_government"
  - "domain/education"
  - "domain/legal_justice"
  - "domain/media_journalism"
  - "user/educator_student"
  - "user/government_staff"
  - "user/legal_professional"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# Split Decision

> Nine AI judges argue real Supreme Court cases, live on Alibaba Cloud. Two AI journalists cover the fight. Convene the panel yourself and watch it think.

[Devpost](https://devpost.com/software/split-decision) · hackathon [[Global AI Hackathon Series with Qwen Cloud]]

## Facets

**mechanism** [[benchmark_measured]] [[deterministic_policy]] [[multi_agent]] [[provenance_signing]] [[realtime_stream]] [[structural_withholding]]
**domain** [[accessibility]] [[civic_government]] [[education]] [[legal_justice]] [[media_journalism]]
**user** [[educator_student]] [[government_staff]] [[legal_professional]] [[researcher]]
**substrate** [[code_repository]] [[structured_db]] [[transcript_audio]] [[web_dom]]

**stack** alibaba-cloud, python, qwen, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for split decision

## Body

Inspiration I make radio for a living, and I've spent the last year watching everyone (including me) bolt multiple AI agents together and just assume the committee is smarter than the individual. Nobody I asked could show me numbers. Agents also have a bad habit: put them in a group and they start agreeing with each other, fast. So I wanted a judgment task that's genuinely hard, where the answers are public, formal, and can't be argued with. Supreme Court outcomes are exactly that. The Court tells you who won, and it tells you the vote. And because I'm a radio person, I couldn't resist the other half of the idea: if machine minds are going to argue, you should be able to listen to them do it. What it does Split Decision is two-agent societies. The first is a court: nine AI judges, each committed in writing to a real judicial philosophy — a Textualist, a Pragmatist, an Originalist, a Precedent Maximalist, and five more. They read a briefing memo on a real Supreme Court case, cast secret ballots, argue in rounds, and file a verdict with dissents. The second society is a newsroom: two AI journalist anchors who cover the deliberation and turn every case into a podcast episode, playing verbatim clips from the argument. Everything runs off one event log per case. The podcast, the pixel-art courtroom replay (watch the vote board flip in real time), the live transcript panel, and the scoreboard all read the same file. Juror words are never paraphrased. Then it grades itself. Every case is scored against the real Court three ways: one model asked directly, nine judges voting silently, and the full deliberation. There's a fourth arm — nine neutral analysts with no philosophies — as a control. The panel has also filed public predictions on three cases the Court hasn't decided yet, so reality gets to grade it later. And there's a live bench where you can convene a real deliberation yourself, on the deployed server, nothing cached: https://split-decision.tarikmoody.com How we built it Everything reasons on Qwen Cloud. The nine jurors run on qwen3.7-plus; the foreperson and the clerk (who writes the bench memo) run on qwen3.7-max. The twelve distinct voices — nine judges, a foreperson, two anchors — were created with Qwen's Voice Design and synthesized with qwen3-tts. Episode art comes from wan2.6-t2i. The pipeline is Python; audio is assembled with ffmpeg; the courtroom is Phaser 3 + TypeScript. Case data comes from CourtListener, Oyez, and the Supreme Court Database. It's deployed on an Alibaba Cloud Simple Application Server (nginx serving the app, systemd running the pipeline, a small stdlib HTTP service powering the live bench) with OSS holding the podcast feed and episodes. The spine is a JSON-schema-validated event log. Every utterance, secret ballot, vote flip, and verdict is one line in events.jsonl, validated at emission. The deliberation protocol is a state machine built to resist sycophancy: private ballots before anyone speaks, personas re-injected every round, and each judge carrying a written trigger for when it's allowed to change its vote. Flips have to be argued, never just announced. Challenges we ran into The benchmark was the hard part, and it fought back twice. First, contamination: these models have memorized legal history. On pre-2025 cases the solo model scores 96–100% — even on obscure ones no law student has heard of. So the scoreboard only counts cases decided after training ended, and I published the memorization curve as its own exhibit. Second, my own math. My first published result said debate cost the panel ten points of accuracy. A mock-judging pass I ran on the project caught it: I was comparing different case pools. Paired on the identical 24 cases, the silent jury and the debating court both score 66.7%. I rewrote the findings page and left the correction on it, on purpose. Smaller fights: Alibaba's OSS default endpoint force-downloads HTML, so the web app had to move to nginx on the server. The TTS model I'd planned on turned out to be Beijing-region-only, which is how I ended up on Voice Design (better anyway). Content moderation killed a deliberation mid-round once — now moderation blocks fail fast and only transient errors retry. And when a model reply comes back malformed, the engine used to quietly fill in a vote; now every synthesized fallback is flagged in the log and rendered with a warning marker, because an immutable record you quietly patch isn't immutable. Accomplishments that we're proud of The honest result. Deliberation didn't make the panel more accurate — it made it more articulate. Debate corrected two cases and spoiled two (sign test p=1.0). On brand-new cases, nothing beat the dumbest baseline, always guess "reverse" (75%, because the Court reverses most cases it takes). I published all of it, including the correction of my own earlier overclaim. The control arm settles what the personas actually do: nine neutral analysts scored exactly the same 66.7% — but they herded, reaching unanimous verdicts on half the cases in about 1.5 rounds, while the ideologues argued for ~3 rounds with flips that tracked philosophy almost perfectly (the cautious Minimalist flipped 21 times, the immovable Textualist once). Ideology shapes the debate; the model sets the score. And the June 29 double-header. The real Court decided two presidential removal cases the same morning, in opposite directions — fired the FTC commissioner (6–3), protected the Fed governor (5–4). The panel, blind to both outcomes, split the pair the same way: reverse 7–2, affirm 8–1. Its dissents even came from the philosophically matching corners. What we learned If you're building agents that discuss before deciding, measure it — paired, against a naive baseline, on data the model can't have memorized. Every one of those three words did real work here, and skipping any of them would have let me ship a wrong headline. Also: multi-agent debate buys you richer arguments, in-character persuasion, and a complete record of who convinced whom. Those are real products. Accuracy wasn't one of them, at this scale, and knowing which one you're paying for is the whole game. What's next for Split Decision Three predictions are on the record for cases the Court hasn't decided: Suncor v. Boulder County, Younge v. Fulton County DA, and Air Force v. Prutehi Guahan. Every time the real Court rules, the season scoreboard updates in public — win or lose. After that: a listener-request docket (pick a case, the pipeline deliberates it overnight and it's in the podcast feed by morning), landmark re-litigation specials (the panel already re-argued Plessy v. Ferguson and upheld it 7–2, which says something uncomfortable about faithfully applied philosophies), and a bigger sample — 24 cases was enough to kill my headline, and about 50 would be enough to say something firm. <div