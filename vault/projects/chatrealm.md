---
slug: "chatrealm"
url: "https://devpost.com/software/chatrealm"
title: "ChatRealm"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 1406
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/clinician"
  - "user/educator_student"
  - "user/researcher"
  - "user/social_worker"
---

# ChatRealm

> ChatRealm: Context-aware chat rooms powered by 5 AI agent bureaus and LinkedIn scraper service. Specialized rooms for D&D, AA, and therapy with intelligent, personalized moderation.

[Devpost](https://devpost.com/software/chatrealm) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[accessibility]] [[education]] [[health_clinical]] [[mental_health]]
**user** [[clinician]] [[educator_student]] [[researcher]] [[social_worker]]

**stack** anthropic-claude-api, asi-one, brightdata-api, docker, fastapi, fetch.ai-uagents, framer, javascript, nginx, phaser.js, postgresql, python, react, redis

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran through
- accomplishments that we're proud of
- what we learned
- what's next for chatrealm

## Body

Inspiration We started ChatRealm because we saw too many people suffering in silence. In online support groups, we watched quiet voices get drowned out. In therapy sessions, we saw people struggling to share their deepest fears. In recovery communities, we noticed how one person's courage to speak could inspire a whole room, but only if someone was there to hold space for them. Our north star was simple: uplift the people who are scared to speak up. We wanted to build something that amplifies voices that might otherwise go unheard, keeps the room engaged and supportive, and most importantly, keeps people calm and safe when they're sharing the things that frighten them most. Because everyone deserves to be heard, and no one should face their darkest moments alone. What it does ChatRealm is a safe space where AI doesn't replace human connection, it protects and nurtures it. Think of it as having a thoughtful friend in every conversation who notices when someone needs encouragement, steps in when things get heated, and celebrates every small victory. We built three specialized rooms where people need this support most: Dungeons & Dragons rooms aren't just about rolling dice. They're about shy players finding their voice through their characters, building confidence in a world where they can be heroes. Our AI Dungeon Master makes sure everyone gets their moment to shine. Alcoholics Anonymous rooms are sacred spaces where people share their struggles with addiction. Our AI recognizes when someone's celebrating "day one sober" and rallies the room to support them. When someone's struggling with temptation at 2 AM, it's there with resources and encouragement, buying time until human support arrives. Group Therapy rooms are where people work through trauma, anxiety, and depression. Our AI creates the calm, non-judgmental presence that helps people open up. It recognizes when someone's triggered and gently guides the conversation to safer ground, all while making sure quieter voices get heard. Here's what makes us different: our AI learns from your LinkedIn profile (if you choose to share it) to understand who you really are. It's not about stalking, it's about context. When you share your story, the AI knows whether you're a college student facing finals stress or a veteran dealing with PTSD. It tailors its support to meet you where you are. How we built it We knew from day one that this couldn't be a typical chatbot. People's mental health and recovery are too important to trust to a single AI making snap judgments. So we built something different: five specialized AI agents working together like a support team. The Response Coordinator is the team leader, deciding when to speak up and when to stay quiet. Sometimes the best support is silent presence. The Context Manager remembers everything. Not just what you said five minutes ago, but patterns over weeks. It knows if you're improving, struggling, or stuck. The Wellness Guardian is our safety net. It watches for crisis signals, words that suggest someone's in danger, and quietly alerts the system to provide immediate resources. The Emotion Tracker reads the room. It notices when someone's message seems cheerful but their word choice suggests they're masking pain. It picks up on the subtle cries for help. The Toxicity Detector is our bouncer. It keeps the space safe by catching harmful content before it derails someone's healing journey. Tech we used: FastAPI and Python for the backend brain React and TypeScript for the interface people see Socket.IO because conversations happen in real-time, not in turns Anthropic Claude for the AI that actually understands nuance and empathy Fetch.ai's uagents for coordinating our five-agent support team PostgreSQL and Redis for remembering every conversation and context BrightData API for optional LinkedIn profile understanding Docker to keep everything running smoothly We gave ChatRealm a retro pixel-art look on purpose. When you're about to share your deepest fear, a friendly pixel avatar feels less intimidating than a corporate interface. It's approachable while still taking your story seriously. Challenges we ran through Making AI actually empathetic was harder than we thought. Getting five AI agents to work together without tripping over each other required us to completely rethink our architecture. We failed. A lot. Our first version would timeout, crash, or give tone-deaf responses. We learned that real empathy comes from context, so we spent weeks teaching our AI to understand the difference between someone saying "I'm struggling" in a D&D game versus in an AA meeting. Building trust is everything. When someone's sharing that they relapsed, or that they had suicidal thoughts, the AI can't just spit out a generic response. It needs to understand the weight of that moment. We built a sophisticated context system that reads not just words, but the person behind them. LinkedIn integration helps, but so does remembering every interaction and learning from the community's patterns. Knowing when to intervene is an art, not a science. We wanted our AI to feel like a supportive friend, not a surveillance system. Too quiet and people feel abandoned. Too chatty and it drowns out human voices. We're still tuning this, but we built an intelligent intervention system that considers conversation flow, room energy, and individual needs. Sometimes the most supportive thing is silence. Real-time everything, always. Mental health crises don't wait for page refreshes. Someone saying "I can't do this anymore" needs immediate response. We built WebSocket connections, Redis caching, and background processing to ensure the AI is always listening and ready to help within milliseconds. Accomplishments that we're proud of Honestly? We're most proud of the moments our AI gets it right. When it notices someone's been quiet for 20 messages and gently asks, "Hey [name], what do you think?" That's amplifying a voice. When someone shares they hit 30 days sober and the AI celebrates with genuine warmth while encouraging others to share their own milestones. That's building community. When it detects crisis language and immediately provides suicide prevention resources while keeping the person engaged until human help arrives. That's saving lives. We built a five-agent AI system that actually works in production. We made it smart enough to know that "let's play" means something completely different in a D&D room versus a therapy session. We created an interface that feels like a game but holds space for the most serious conversations. But the real accomplishment? We built something that makes people feel safe enough to speak up. What we learned Technology is easy. Empathy is hard. We spent months on the technical architecture, but the real challenge was teaching AI to understand human pain and respond with genuine compassion. We learned that more context always beats smarter algorithms. Knowing someone's background, reading conversation history, and understanding room dynamics matters more than any fancy model. Silent support is still support. Our early versions talked too much. We learned that sometimes the AI's job is to just be present, ready to help, while humans connect with humans. The best moderation is invisible until it's needed. People want to be seen. The LinkedIn integration isn't about fancy tech. It's about making someone feel recognized. When the AI understands you're a nurse dealing with burnout, or a student facing academic pressure, its support becomes real instead of generic. Recovery isn't linear, and neither is conversation. Building room-specific AI taught us that every community has its own rhythm, vocabulary, and needs. One size fits nobody when it comes to supporting mental health and recovery. What's next for ChatRealm We want to keep building safe spaces: More communities that need support: Veterans with PTSD, LGBTQ+ youth, chronic pain sufferers, grief support groups, neurodivergent communities finding their people. Voice channels where people can talk instead of type, because sometimes speaking your truth out loud is what healing requires. Peer matching that connects you with others who've walked your path. Not random strangers, but people whose stories resonate with yours. Crisis response network that connects to real counselors when AI support isn't enough. We never want to replace human help, just make sure you have support while waiting for it. Long-term progress tracking so you can see how far you've come, even on days when it doesn't feel like it. Community building tools that help natural leaders emerge and peer support flourish. Most importantly, we want to keep listening. To the quiet voices, the scared voices, the voices that have been told to be silent. Because at ChatRealm, everyone gets heard. <div