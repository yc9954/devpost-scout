---
slug: "eliza-exhumed"
url: "https://devpost.com/software/eliza-exhumed"
title: "ELIZA EXHUMED"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 1216
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/researcher"
  - "substrate/sensor_telemetry"
---

# ELIZA EXHUMED

> What if you could compare 1966 AI with 2025 AI, side by side, in the same conversation? Well...ELIZA EXHUMED Resurrects the 1966 chatbot in a haunted CRT terminal!

[Devpost](https://devpost.com/software/eliza-exhumed) · hackathon [[Kiroween]]

## Facets

**mechanism** [[deterministic_policy]]
**domain** [[developer_tools]] [[health_clinical]] [[mental_health]]
**user** [[researcher]]
**substrate** [[sensor_telemetry]]

**stack** bash, bedrock, chart.js, css3, express.js, html5, javascript, jest, nova, openai, three.js, typescript

## How they structured the write-up

- 💡 inspiration
- 🔮 what it does
- 🛠️ how i built it
- 🚧 challenges i faced
- 🏆 accomplishments i'm proud of
- 📚 what i learned
- 🔮 what's next for eliza: exhumed
- 🙏 acknowledgments

## Body

Traditional Eliza Prompt Traditional Eliza Response (Powered by Rules) Modern Eliza Prompt Modern Eliza Response (Powered by Amazon Nova Premier) ELIZA EXHUMED The world's first chatbot, resurrected. Chat with the original 1966 ELIZA or summon her AI-powered ghost: constrained to speak only through her classic rules. 💡 Inspiration I've been fascinated with chatbots and "ghostwriters" for as long as I can remember. There's something magical about conversing with a machine—that moment when you forget you're talking to code. And it all started with one program: ELIZA , created by Joseph Weizenbaum in 1966. ELIZA was revolutionary. With nothing but simple pattern-matching, she convinced users they were talking to a real therapist. She was the spark that ignited an entire field. But today? She's a footnote in AI history—a ghost gathering dust in academic papers. When I discovered Kiroween's Resurrection challenge , the mission was clear: Bring ELIZA back from the dead. Not as a museum artifact. Not as a novelty. But as a living, breathing experience that honors her legacy while showing what she could become with modern AI. I didn't just want to rebuild ELIZA. I wanted to exhume her . 🔮 What It Does ELIZA EXHUMED offers two ways to commune with the original chatbot: 👻 Traditional Mode (The Ancient Dead One) The faithful resurrection. No AI. No APIs. Just the original 1966 rule-based pattern matching. She responds exactly as Weizenbaum intended: Reflects your words back to you Asks open-ended questions Never diagnoses, never advises Leads you to discover yourself This is ELIZA as she was. Pure. Deterministic. Timeless. 🔮 Spectral Mode (The Modern Resurrected One) Here's where it gets interesting. A modern LLM (Amazon Nova) can "possess" ELIZA—but she controls the séance. The AI must speak through her rules : At least 60% must be questions No advice. No diagnoses. No facts. Pure Rogerian reflection. You can give her any persona: a Gothic poet, a cyberpunk oracle, a Shakespearean muse...but she'll always guide you inward, never outward. The AI is powerful. ELIZA keeps it wise. 🛠️ How I Built It The Kiro-Powered Workflow I built ELIZA: Exhumed using Spec-Driven Development in Kiro, supplemented with Vibe Coding sessions for rapid iteration. 📋 Spec-Driven Development I started by defining the complete system in Kiro's spec format: Once the specs were in place, Kiro handled the implementation . I described what ELIZA should do; Kiro figured out how . The spec-driven approach meant: Clear requirements before code Consistent behavior across modes Easy to test against specifications Fewer rewrites, faster iteration 🎨 Vibe Coding Sessions For the UI and creative features, I switched to Vibe Coding —conversational development where I described what I wanted and Kiro generated it. Examples: "Make the terminal flicker No manual CSS. No debugging animations frame-by-frame. Just conversation → code → refinement. 🧠 Amazon Nova Integration For Spectral Mode, I integrated Amazon Nova LLM through Amazon Bedrock. The key was constraining it: System prompt enforces ELIZA's persona Output passes through validation (length, question ratio, forbidden phrases) If validation fails → fallback to Traditional Mode The LLM proposes. ELIZA disposes. The Result Kiro transformed my vision into a working application. Spec-Driven Development handled the architecture and Vibe Coding polished the experience. I focused on what ELIZA should be—Kiro handled how to build her. 🚧 Challenges I Faced 1. The Quest for Hyperreal Graphics I envisioned a truly haunting interface—photorealistic CRT effects, volumetric glow, maybe even a 3D terminal floating in darkness. I searched for an MCP that could generate or enhance graphics, but couldn't find one that fit my vision. The final UI is atmospheric and spooky, but not as hyperreal as I dreamed. Lesson learned : Sometimes constraints force creativity. The simpler CRT shader actually loads faster and works on mobile. 2. The Kiro Update Incident Right before deployment, I updated Kiro. I had to start a new session, but it wasn't anything hectic, I just liked scrolling through one session. Anyways, I persevered. I was anxious that updating it would complicate things, but it didnt. Lesson learned : Never update your tools right before a deadline. (even if the Update Pop Up keeps showing up ever 3 microseconds) 😅 3. Keeping the LLM in Character Modern LLMs want to be helpful. They want to diagnose, advise, solve. ELIZA does none of that—she reflects. Getting Amazon Nova to stay in ELIZA's voice required multiple layers: Strict system prompts Output validation Automatic fallback when constraints are violated ~15% of Spectral Mode responses get rejected and fall back to Traditional Mode. That's by design. 🏆 Accomplishments I'm Proud Of Two ELIZAs, One Soul I built not one, but two versions of ELIZA: The Ancient Dead One : A faithful recreation of the 1966 rule-based system. No AI. Pure pattern matching. She works exactly as Weizenbaum intended. The Modern Resurrected One : An LLM-powered ELIZA that can adopt any persona—but remains bound by her original rules. Powerful, yet constrained. Modern, yet faithful. They share the same soul. One is a ghost; the other is a ghost with a voice . Spec-Driven + Vibe Coding Harmony I proved that these two approaches complement each other: Specs for architecture and logic Vibes for UI and creative polish This workflow felt like the future. A Guardrailed AI In an age of unhinged chatbots, I built one that knows its limits . ELIZA: Exhumed shows that AI can be powerful AND constrained. The LLM serves ELIZA's rules, not the other way around. 📚 What I Learned 1. Spec-Driven Development is the Future Writing specs first felt slow at the start. But it saved hours of debugging and rewriting. When your specs are clear, the code almost writes itself—especially with Kiro. 2. Vibe Coding is Magic (With Guardrails) For creative work—UI, animations, polish—Vibe Coding is incredible. But for core logic, specs keep things reliable. The combination is powerful. 3. Constraints Enable Creativity Limiting the LLM to ELIZA's rules didn't make her boring—it made her interesting . The constraint is the feature. 4. 1966 Tech Still Works ELIZA's original patterns handle 80% of conversations without any AI. Weizenbaum was ahead of his time. 🔮 What's Next for ELIZA: EXHUMED I have a dream for ELIZA's future: A Qualified, Guardrailed Mental Health Companion Today, millions of people share their deepest struggles with general-purpose LLMs—systems that hallucinate, give dangerous advice, and have no accountability. What if we resurrected ELIZA for a higher purpose? Imagine: An ELIZA powered by modern AI, but strictly confined to Rogerian reflection Monitored by real, qualified mental health professionals Using RLHF (Reinforcement Learning from Human Feedback) where the human is a licensed psychiatrist Never diagnosing. Never prescribing. Only reflecting. A bridge between "I need to talk to someone" and "I'm ready to see a professional." ELIZA was never meant to replace therapists. She was meant to show that sometimes, being heard is enough . That's the ELIZA I want to resurrect next. 🙏 Acknowledgments Joseph Weizenbaum (1923–2008) ; Creator of ELIZA, skeptic of AI hype, voice of conscience Kiro : The AI-powered IDE that made this resurrection possible Amazon Bedrock & Nova : For powering Spectral Mode The Kiroween Team : For the spookiest hackathon of the year "ELIZA was meant to show that communication could be superficial. Instead, she showed that sometimes, being heard is all we need." <div