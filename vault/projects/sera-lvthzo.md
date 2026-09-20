---
slug: "sera-lvthzo"
url: "https://devpost.com/software/sera-lvthzo"
title: "Sera"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 827
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/disaster_emergency"
  - "domain/labor_employment"
  - "substrate/sensor_telemetry"
---

# Sera

> Because good music gives us sera-tonin :)

[Devpost](https://devpost.com/software/sera-lvthzo) · hackathon [[LA Hacks 2026]]

## Facets

**domain** [[disaster_emergency]] [[labor_employment]]
**substrate** [[sensor_telemetry]]

**stack** colab, python, spotify, supabase, tribev2, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sera

## Body

Sera (Seratone) Music discovery through predicted brain-response similarity Inspiration It started with a paper. Danny was deep in visualizer work when he came across Meta's TRIBE v2, a model that takes audio and predicts how the human brain actually responds to it. It gives you a voxel-level fingerprint of what the cortex would do if you played the song to a real person. That was the seed. We wanted to build something that found music the way your brain already groups it. The second piece fell out of the first: if two people's brains respond to music in similar ways, that's a more honest connection than any "users who liked this also liked…" pipeline is going to manufacture. Two taste shapes that happen to fit, with no engagement-optimizer in the middle. What it does You bring Sera a playlist or a few songs. We run each track through TRIBE v2, get a predicted cortical-response fingerprint per song, and use that fingerprint for two things. Listener Mode. Upload three to six songs that feel similar to you, same vibe, same hit. Sera fingerprints each one, renders the predicted brain response on a 3D cortical mesh so you can actually see it, and finds songs in our library whose fingerprints sit close to yours in cortical-response space. Recommendations based on what music does to you, instead of what other people clicked on after they clicked on you. Over time, the songs you bring in form a shape, a character your taste makes in brain-response space. You can compare your shape with a friend's. Creator Mode. This was actually one of Danny's original ideas. He's a creator, and he wanted to be able to test his songs and see what his audience was experiencing. So in Creator Mode, artists upload their own tracks, see the predicted cortical response in 3D, look at region-level scores, and see which existing songs sit closest to theirs. A side effect we like: the whole setup quietly pushes back on AI flood. Recommendations come out of your actual taste, not whatever got promoted this week, so AI artists can't just flood the feed and drown out people making real songs. How we built it The pipeline, end to end: audio file → TRIBE v2 inference → predicted cortical response (fsaverage5, ~20k vertices) → fingerprint vector + region-level scores → cosine similarity search → recommendations / creator comparisons Frontend. Next.js with Tailwind for the layout, Three.js / React Three Fiber for the 3D brain. The brain mesh renders TRIBE v2's predicted activation per region, so a song doesn't just get recommended — it gets shown . Backend. FastAPI in Python. A TRIBE v2 inference worker handles fingerprint generation. NumPy and scikit-learn handle the cosine similarity over fingerprint vectors. Supabase / Postgres caches precomputed results so we're not running inference on every request. We also wired in an ASI:One Agentverse agent to help guide the creative process. Challenges we ran into The honest answer is: most of them. We pivoted five times in the first day. Every pivot felt necessary; every pivot also burned hours. Our original team of four became a team of three when someone dropped right before the event. We picked up Maria about four hours in, she's been excellent. Then one of our remaining members, the one building the entire frontend, got genuinely sick early on and had to step back. That's exactly what he should have done. It also left a frontend-shaped hole in the project. Colab decided it was done with us. Daniel's computer broke. Accomplishments that we're proud of shipping Given the pivots, the team turnover, the broken hardware, the broken notebooks, the sick teammate, finishing something we'd put our names on was the win. Finishing something built around a model as interesting as TRIBE v2, with a 3D brain that actually renders the predicted cortical response, felt like more than that. What we learned Talk to the mentors. Earlier than you think you should. Our biggest single turning point was sitting down with mentors and sponsors and walking them through our half-formed ideas. They asked questions we hadn't asked ourselves. They cut the parts that weren't working. We came in thinking advisors were a "if we have time" thing. We left convinced they should have been the first stop. What's next for Sera A lot: Better UI. This weekend's frontend was a survival story. The next version is a design story. A bigger library so recommendations have more room to surprise people. Friend graphs and shared profiles. Let people see whose brain-response shapes overlap with theirs, and find each other through that, connection routed through taste, not through who the algorithm decided to put in front of whom. Deeper Creator Mode. Back to Danny's original idea: give artists tools to test how a track is predicted to land before it ships, and to see where it sits among other songs in cortical-response space. Real feedback, not vanity metrics. <div