---
slug: "impulse-kit"
url: "https://devpost.com/software/impulse-kit"
title: "Impulse Kit"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 474
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/health_clinical"
  - "domain/security_privacy"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/video_visual"
---

# Impulse Kit

> Tap the good, ignore the bad, learn fast.

[Devpost](https://devpost.com/software/impulse-kit) · hackathon [[Kiroween]]

## Facets

**mechanism** [[deterministic_policy]]
**domain** [[health_clinical]] [[security_privacy]]
**user** [[educator_student]] [[researcher]]
**substrate** [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** css, html, javascript, kiro

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into & what's next

## Body

Swipe on water, ignore soda Pick water Ignore trading traps Train visual recognition Learn French articles Pick out the correct options Inspiration Impulse Kit started with me watching TV. I saw a feature about Swiss neuroscientists who were testing a new method to help people break bad habits. The idea was brilliant: borrow the psychology of advertising, but reverse it. Instead of training the brain to crave something through repetition, they trained the brain to avoid it, using a simple Go/No-Go game where you tap healthy items and stay completely still for unhealthy ones. That idea stuck with me. I loved the elegance of it: fast reactions, instinct over analysis, subconscious learning. I immediately wondered, what else could you train this way? Could you build intuition for grammar? For pattern recognition? For trading? For anything that requires a gut feeling? This became the seed for Impulse Kit. What it does Impulse Kit is a cognitive training engine built around the Go/No-Go principle. Different themes plug into the same skeleton framework, allowing users to train their instincts across many domains. The prototype includes three examples: Sugar Habit Breaker 🧃 Healthy drinks appear - swipe them into your cart. Sugary drinks appear - do nothing. A fast, neuroscience-inspired training loop for impulse control. Language Gender Reflex Trainer 🌐 A noun flashes with an article. If it’s correct, tap; if it's wrong, resist. It helps learners develop the “native speaker gut feeling” for grammatical gender. Trading Pattern Instincts 📈 Candlestick patterns appear. Buy signals require a tap; fake-outs must be ignored. It trains both fast pattern recognition and the discipline to not act impulsively. Impulse Kit turns all of these into quick, repeatable rounds designed to rewire instinctive reactions. How we built it I built Impulse Kit using Kiro as the foundation: I started by describing the Go/No-Go mechanism conversationally with Kiro and generating the base gameplay loop. It defined a skeleton spec that describes the timing, scoring, state machine, and reaction logic. After I was satisfied with one example, I moved to the next two. Each game is just a small override layer: new images, new rules, new “good vs bad” classifications. Challenges we ran into & What's next Finding universal examples wasn’t easy. Many instinctive-skill domains aren’t visually simple enough to display as flash cards (ER triage, mushroom identification, etc.). So maybe a more sophisticated version of the game should be made. Here are some ideas of how this project can be continued: More instinct modules: driving hazards, phishing email spotting, emotional tone recognition, food label scanning, etc. Personalized difficulty curves that adapt to user performance. A research mode that collects anonymized reflex-time data for behavioral science. User-generated instinct packs, allowing anyone to create their own Go/No-Go training sets directly from the GUI. Overall, lots of things to explore! Hope you like it! <3 <div