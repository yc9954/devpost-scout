---
slug: "voicezero"
url: "https://devpost.com/software/voicezero"
title: "VoiceZero"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 963
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "user/small_business"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# VoiceZero

> We build websites by conversation

[Devpost](https://devpost.com/software/voicezero) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[developer_tools]]
**user** [[small_business]]
**substrate** [[transcript_audio]] [[video_visual]] [[web_dom]]

**stack** angular.js, docker, express.js, node.js, snowflake, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that we're proud of
- what i learned
- what's next for voicezero

## Body

VoiceZero: Your website, by conversation Inspiration The inspiration for VoiceZero came not from a tech blog, but from direct conversations with small business owners in my city. I spoke with the owners of local coffee shops, and other small businesses. Despite having fantastic services and products, most lacked an online presence. The reason was always the same: existing "no-code" tools were still too complex. They required them to think like designers, learn new interfaces, or even write effective prompts. This led me to a critical insight: the problem wasn't just about code, it was about complexity. So, I asked: What if creating a website was as simple and natural as having a conversation? I confirmed a clear gap in the market. While AI could assist in website creation, no platform was truly voice-first . I was inspired to build that platform, using the most intuitive interface of humans to empower local businesses. What it does VoiceZero is a web application that empowers small business owners to build a professional website simply by talking to an AI assistant. It eliminates the need for technical skills, design experience, or even typing. Start with a Click: The user visits the site and clicks a single button to start a conversation. Guided Conversation: The AI assistant guides the user with questions about their business, services, brand style, and contact information. It's not about writing prompts; it's about answering simple questions. Real-Time Build: As the user speaks, the website builds itself in a live preview pane. When they describe their services, a new section appears. When they mention their brand colors, the theme updates instantly. On-Demand Visuals: Based on user feedback, VoiceZero now generates contextual images on the fly. If you're a coffee shop describing your "Artisanal Espresso," the platform creates and places a relevant, high-quality image for you. The result is a small business owner going from idea to a deployed, visually-rich website in minutes, all through an effortless conversation. How I built it For this hackathon, my focus was on demonstrating momentum. I moved beyond the initial MVP to build features that prove VoiceZero can scale and learn from its users. My two primary achievements during this sprint were: Building a Conversation Analytics Dashboard with Snowflake: To deeply understand user needs, I integrated Snowflake with the conversations data. Using the snowflake-sdk for JavaScript, every conversation is now logged. I used Snowflake's AI SQL functions to analyze the data directly: AI_SENTIMENT helps gauge the overall user feeling at different points in the conversation. AI_COMPLETE classifies user messages into categories like 'confused', 'satisfied', or 'excited'. This dashboard isn't just a feature; it's the engine for our product development, allowing us to pinpoint exactly where the user experience is succeeding or failing. Shipping On-Demand Image Generation: One of the first pieces of feedback I received from my initial users was the need for visuals. During this hackathon, I built and integrated a feature that generates images based on the conversational context, creating a more complete and professional-looking website without any extra effort from the user. Challenges I ran into The main challenge during this sprint was integrating the Snowflake backend and building the analytics dashboard within the tight 72-hour timeframe. This involved quickly learning the Snowflake JavaScript SDK, architecting the data pipeline for for transcription logging, and applying AI_COMPLETE prompts to get consistently accurate classifications of user sentiment. It was a race to move from raw data to actionable insights, but this process was critical for proving our ability to build a data-driven product. Accomplishments that we're proud of This hackathon was about proving we could execute and generate real pull from the market. First Users Onboarded: I moved beyond a prototype by onboarding my first users on-site, the very coffee shop owners who inspired the project. Their feedback was invaluable and led directly to the new image generation feature. We have testimonials and proof of utility from real businesses now. Shipped a Data-Driven Engine: Building the Snowflake analytics dashboard in a weekend is a major technical accomplishment. We are no longer guessing what users want; we have a system to measure it. Organic Waitlist Growth: Without any marketing spend, our waitlist is growing organically, signaling strong market demand for a simpler solution to website creation. Most of all, I'm proud of transitioning VoiceZero from an idea into a user-validated tool with a clear and data-informed path forward. What I learned My biggest learning from this hackathon is the power of turning feedback into quantitative data. It's one thing to hear a user say, "I was a bit confused there." It's another to see a "Confused" spike on a dashboard tied to a specific point in the conversational session. By using Snowflake to analyze conversations, I learned that technology should not just adapt to humans, but also learn from them at scale. The true power of AI here is not just in generating a website, but in understanding the user's journey. This human-centric, and data-driven approach could be the key to making VoiceZero truly empowering. What's next for VoiceZero The analytics dashboard is now our compass. Our roadmap is no longer based on assumptions but will be directly guided by the insights we gather from every user conversation. Our immediate next steps are: Refine the Onboarding Flow: Use the dashboard to identify and eliminate points of friction or confusion for new users. Expand Creative Capabilities: Analyze what types of businesses are signing up to inform new, industry-specific layouts and features. Activate the Waitlist: Begin onboarding users from our growing waitlist, continuing to gather data and iterate rapidly. I envision VoiceZero becoming the go-to platform for any small business that needs a powerful online presence without the technical headache. We're not just building websites; we're building confidence for entrepreneurs. <div