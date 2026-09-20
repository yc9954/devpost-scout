---
slug: "peersuade"
url: "https://devpost.com/software/peersuade"
title: "Peersuade"
hackathon: "UNIHACK 2026, funded by the European Union"
organization: "UNIHACK"
winner: true
words: 648
team_size: 6
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/civic_government"
  - "domain/education"
  - "user/legal_professional"
  - "substrate/code_repository"
  - "substrate/transcript_audio"
---

# Peersuade

> A real-time 1v1 debate game where two players compete to win a fictional Australian election by out-arguing each other in front of AI-simulated voters.

[Devpost](https://devpost.com/software/peersuade) · hackathon [[UNIHACK 2026- funded by the European Union]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[vision_ocr]] [[voice_speech]]
**domain** [[civic_government]] [[education]]
**user** [[legal_professional]]
**substrate** [[code_repository]] [[transcript_audio]]

**stack** agora-rtc, express.js, flash, gemini, groq-whisper, next.js-15, react-19, socket.io, tailwind-css-v4, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we faced
- accomplishments we're proud of
- what we learned
- what's next for peersuade

## Body

Main lobby Topic Live transcription during debate Objection feature Final voting results Agent vote reasoning GIF Party mode Peersuade: Turning Political Apathy into a Party Game Inspiration Western democracies are facing a growing crisis of political disengagement. The numbers are stark: Globally, 55% of Gen Z voters feel their political systems do not care about their voices. In Australia, around 47% of Gen Z voters in the 2022 federal election admitted their primary motivation was simply avoiding the fine — not because they cared about any policy. Traditional political debates are inaccessible, jargon-heavy, and frankly boring. Meanwhile, party games like Jackbox prove that the right format can get a room of strangers laughing, arguing, and deeply invested within minutes. We asked: what if political engagement felt like that? What if instead of watching politicians dodge questions on TV, you and your friend were the ones at the podiums — getting cheered on, called out, and judged by a live AI jury? What It Does Peersuade is a real-time, browser-based 1v1 debate game. Two players connect from separate devices, receive generated candidate profiles and debate randomised policy topics — both serious and absurd — in front of 5 AI-simulated voters. Players can slam an OBJECTION! button mid-speech to steal the floor. After two rounds, the jury votes and delivers their verdict. How We Built It Layer Technology Frontend Next.js 15, React 19, Tailwind v4 Realtime Socket.io over Express.js Voice Agora RTC + Groq Whisper (speech-to-text) AI Voters Gemini Flash The architecture is fully server-authoritative — all game state lives on the Express server and is pushed to clients via WebSocket events. This was essential for keeping two players in sync across separate devices with no shared state. Challenges We Faced Designing fair AI voters was harder than expected. Without careful prompt design, the AI jury often favored the candidate who spoke last or the one who gave longer answers, even if those answers weren’t stronger. We wanted the system to be balanced such that each candidate would have an equal chance of winning. Achieving that took many iterations of the voter personality prompts and the scoring guidelines. Real-time voice transcription latency was another bottleneck. Debates are time-pressured, so a 3–4 second transcription delay broke immersion. We solved this by streaming audio chunks to Groq Whisper in parallel rather than waiting for a full speech turn to complete. Multiplayer state sync on reconnect was a classic distributed systems problem — a player dropping and rejoining mid-debate had to seamlessly receive the full current game state without desynchronising the other player. Accomplishments We're Proud Of The full game loop works end-to-end — lobby, debate, live transcription, AI judging, and winner reveal — in real time across two separate devices. The AI voters each have distinct personalities and deliver genuinely funny, sometimes scathing rationales for their votes. The Jackbox-style visual polish makes it feel like a real party game, not a civics lesson. The objection mechanic creates real tension and laugh-out-loud moments. What We Learned "The right format can make anything engaging — even a debate about the Emu War." Server-authoritative design is non-negotiable for multiplayer. Any client-side state that diverges from the server will eventually cause bugs that are nearly impossible to reproduce. Voice as input fundamentally changes how players engage. People are funnier, more expressive, and more committed when they have to actually speak their argument aloud. Prompt engineering is product design. The way you describe a voter's personality to an LLM determines the entire feel of the judging experience. Small wording changes produced wildly different (and sometimes hilarious) voter behaviour. What's Next for Peersuade Spectator/audience mode so a whole room can watch and react live. More topic packs covering different countries and political systems beyond Australia. A persistent leaderboard and ranked debate mode. Taking the game beyond the hackathon and into classrooms as a tool for political education. <div