---
slug: "posthog-meeting-copilot"
url: "https://devpost.com/software/posthog-meeting-copilot"
title: "PostHog Meeting Copilot"
hackathon: "ElevenLabs x 16z Worldwide Hackathon"
organization: "ElevenLabs"
winner: true
words: 337
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "substrate/sensor_telemetry"
---

# PostHog Meeting Copilot

> The PostHog Meeting Copilot is a friendly voice assistant that joins your meetings, automatically summarizes your key PostHog dashboards and insights.

[Devpost](https://devpost.com/software/posthog-meeting-copilot) · hackathon [[ElevenLabs x 16z Worldwide Hackathon]]

## Facets

**mechanism** [[voice_speech]]
**substrate** [[sensor_telemetry]]

**stack** elevenlabs, fastapi, gpt-4o, lovable, python, react, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for posthog meeting copilot

## Body

Inspiration We know how important it is to keep an eye on our metrics, but it’s easy to skip them in standups or other meetings. Plus, if someone suddenly asks a “hey, what was our conversion rate last week?” kind of question, everyone ends up scrambling through different tabs and dashboards. What it does The PostHog Meeting Copilot is a friendly voice assistant that joins your meetings, automatically shares (and even summarizes) your key PostHog dashboards and insights. So, no more screen-sharing chaos or awkward silences trying to find that one data point—just smooth, data-driven discussions every time. Email parthgandhi@outlook.com or ishaan.shrivastava@gmail.com if you want to try it out. How we built it We integrated with the Posthog apis to get all insights/dashboards/embeds. We then used multiple gpt-4o calls to get relevant metrics, summarize them, and give a user-friendly output through the Elevenlabs voice agent. Challenges we ran into We underestimated how hard it would be to do an arbitrary HogQL generator. Google Meet/Zoom do not have good integrations for conversational agents. Along the way, we also discovered a bug in the Posthog client library: https://discord.com/channels/1066739690436313158/1342583407607283722/1343197902738165853 Accomplishments that we're proud of It works! We actually liked the problem we were solving for and face it regularly. We learnt at least 4-5 new tools/frameworks/technologies over the weekend. We were able to effectively prune our original vision to make sure we still have a minimum-lovable-product by submission time. What we learned How to effectively use the Elevenlabs conversational voice agent How to use lovable, and when to directly code or use an AI tool. How to solve interesting problems with the new modalities that have emerged What's next for PostHog Meeting Copilot We’ve also started working on a couple of additional features - Google meet and Zoom integration, so the bot can automatically join all your virtual meetings through calendar invites. An ad-hoc query generator that lets you ask arbitrary questions that are not in an existing insight. It generates and executes the right HogQL from user input. <div