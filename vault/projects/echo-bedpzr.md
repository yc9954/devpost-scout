---
slug: "echo-bedpzr"
url: "https://devpost.com/software/echo-bedpzr"
title: "Echo Reminder"
hackathon: "RevenueCat Shipaton 2025"
organization: "RevenueCat"
winner: true
words: 1218
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/deterministic_policy"
  - "mechanism/on_device_local"
  - "mechanism/voice_speech"
  - "domain/education"
  - "domain/transportation"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# Echo Reminder

> A voice-based reminder app with smart features for future-tasks, including web-search, research, and drafting emails.

[Devpost](https://devpost.com/software/echo-bedpzr) · hackathon [[RevenueCat Shipaton 2025]]

## Facets

**mechanism** [[benchmark_measured]] [[deterministic_policy]] [[on_device_local]] [[voice_speech]]
**domain** [[education]] [[transportation]]
**user** [[educator_student]] [[legal_professional]]
**substrate** [[structured_db]] [[transcript_audio]]

**stack** codex, cursor, expo.io, native, next.js, openai, perplexity, railway, react, react-native, supabase, tailwind, v0, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for echo reminder

## Body

Inspiration I (Luca) was thinking of making an app back in May of 2025. I asked myself, what’s the #1 app that I use that helps me in my day-to-day? I thought it was the Apple Reminders app. It's super simple, no over-complicated features, and just works. But one thing that annoyed me was having to always tap, scroll, and set the title, date, and time for each reminder. I tried using Siri, but it didn’t set reminders well; it literally transcribed my voice and created a reminder. It also couldn’t break down tasks into multiple reminders. So I sat on the idea for a bit and researched voice-based reminders. There were a few, but none of them stood out. While thinking about how to make the app, I decided to make a Mobbin purchase because it seemed useful. One day, I was scrolling through my Mobbin newsletter when I saw the announcement about Shipaton. More than the prize money, the Times Square billboard caught my eye. I thought, Why not do it? I was already doing a lot of research and was set on building an app. So the next day, I asked my girlfriend/teammate, Sydney, to film an intro. We walked outside and filmed in the park. That day, we posted day 1 of my 'Build an app with me' series, and I started vibe coding. What it does Echo lets users tap the microphone icon and say what they want to be reminded of. Echo will automatically set these details for the user, whether they say a single task, multiple tasks, or backtrack during their recording. My belief is that this strength, on its own, sets it apart from Apple Reminders + Siri. For the premium feature, which we put behind the RevenueCat paywall, users can enable web search or research capabilities for their tasks. For example, if a user sets a reminder for ‘How to study reinforcement learning?’, at the due date, Echo will remind you with a suggestion generated. We built this for our target audience: people in their early 20s who lack the time and capacity to immediately complete a task that pops up in their mind, who are on the move, and just want to speak it out first. How we built it I built the app as a cross‑platform Expo project with React Native and TypeScript. On the client side, I use Expo’s audio APIs to capture recordings, Expo Notifications for local scheduling, and SecureStore/AsyncStorage for a small offline cache. Styling is utility‑first with NativeWind/Tailwind. Supabase powers the database. I added a single “process‑audio” endpoint on an Express server (hosted on Railway) that handles both transcription and parsing. The server streams uploads with Multer, uses Whisper to transcribe speech, and calls OpenAI’s Responses API. For accuracy, parsing is done with structured tool calls to gpt‑5‑mini. A strict prompt/schema (title, schedule, repeat rules, checklist items) forces the model to return JSON instead of free‑form text. Then, I have code that repairs missing dates, propagates safe defaults, and deduplicates. On-device, I cache a stable user ID, AI summaries, and the OS notification schedule so reminders feel instant and still fire offline; when online, the app syncs with Supabase and reconciles changes. Design‑wise, my teammate Sydney sketched flows in Figma; I used v0 to translate those into initial components, then refined both the UI and parsing logic with Codex and Cursor. In the last stretch of Shipaton, I leaned heavily on OpenAI’s Codex to iterate quickly on prompts, structured outputs, and client polish. Challenges we ran into Firstly, this was our first time building and publishing an iOS app and wiring RevenueCat’s paywall, so we spent more time than expected on App Store Connect setup and paywall configuration. My teammate Sydney was also new to Figma, which slowed some iterations, so we relied a lot on Mobbin and v0 for speed and inspiration. Secondly, from a strategy perspective, there were a lot of disagreements between me and my partner due to the fact that we started this project without a specific target audience in mind. For example, do we target college students or young professionals? How would we then tailor our designs to fit this audience? We de-prioritized building the calendar view until we could validate who we were building for. Thirdly, parsing accuracy has been hard, and we're still figuring out how to handle this better for the long term. Since we use a lot of prompting, there are times when LLMs can behave more non-deterministically than other times. We fixed most of this by using tool-calls and forcing it to return structured outputs. The trade-off here is that latency goes up if you prompts become longer, but trimming the prompts can break some complex user queries. Keeping track of whether a change broke a test case became hard, so we tried setting up an eval/unit testing system where another LLM judges my app’s parsing decisions. It works, but it’s not fully automated yet. Accomplishments that we're proud of First and foremost, we're happy that we were able to publish our first app. We were expecting Echo to get rejected on the first submission, but it worked, and we're now pretty familiar with the process. Secondly, we're proud that we were able to vlog every day of the process on social media. To be honest, posting every day took a lot of time, and I was frustrated, and Sydney, who did a lot of the filming and editing, but now, looking back at my feed and the support we’ve gained, we're glad we pushed through. In terms of the app, we're satisfied that the voice functionality is at a state where users and I find it useful. For the most part, it is very accurate, and the fact that it can break down reminders and detect repeatability is a big differentiator compared to Apple Reminders, which we have set as a benchmark. What we learned We learned to pick a specific target audience early. We made a lot of decisions ourselves, based on assumptions of what a ‘user like us’ would find useful. There was a lot of feedback we got through building in public, which helped us notice small details we didn’t notice, and also helped us narrow down our priorities. However, getting feedback through social media also confused us in a sense, because the feedback varied a lot, and we received feedback from people who don’t use reminder apps on a daily basis. What's next for Echo Reminder Our goal is to keep working on adding features to Echo to differentiate it and strengthen its value. We plan on also updating my progress on social media, though not daily. In terms of features, we outlined in the near-term product roadmap that we’ll work on a simple calendar view, and then Google Calendar integration. In the long term, we want to make the voice feature even more powerful, like searching and deleting reminders and triggering integrations. Ideally, you’ll say “set up a meeting for 3 PM,” Echo will do it in the background, and then confirm before the meeting. From a marketing perspective, we want to focus more on TikTok (UGC marketing) and Reddit to get more users because we weren’t able to focus on this while developing the app. <div