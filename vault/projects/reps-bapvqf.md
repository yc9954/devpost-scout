---
slug: "reps-bapvqf"
url: "https://devpost.com/software/reps-bapvqf"
title: "REPS"
hackathon: "Build with MeDo Hackathon "
organization: "Baidu"
winner: true
words: 1473
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# REPS

> You paste in something and the app turns it into a convo where you explain the concept and an AI tutor pokes holes using the Feynman technique. Tracks which concepts you grasp vs. which you're faking.

[Devpost](https://devpost.com/software/reps-bapvqf) · hackathon [[Build with MeDo Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]] [[transcript_audio]] [[web_dom]]

**stack** medo

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for reps

## Body

Inspiration There's a specific kind of self-deception I've gotten really good at: reading something dense, nodding along, and walking away convinced I understood it. Then a week later, someone asks me to explain it and I realize I absorbed almost nothing. I'd just gotten good at recognizing the words. This is the gap most learning tools don't fix. Flashcard apps can drill you on definitions all day, but they can't tell whether you actually understand the thing or you've just memorized the shape of the answer. The only test that's ever worked for me is the one Richard Feynman talked about decades ago — try to explain it, in your own words, to someone who'll push back when you wave your hands. Reps came out of wanting that "someone" to exist on demand. Not a quiz. Not a chatbot that congratulates you. A tutor that catches you when you're pattern-matching instead of understanding. What it does Reps turns anything you're trying to learn into a Socratic conversation. You drop in source material — pasted text, an article URL, a YouTube link, or a PDF. Reps parses it, extracts 3–8 testable concepts, and lets you pick which ones to drill. Then it drops you into a chat where an AI tutor asks you to explain a concept like you're smart but unfamiliar with it. You type your explanation. The tutor doesn't lecture back. Instead, it picks the weakest part of what you said and probes it: "You said X causes Y — walk me through why." "What would break if [edge case]?" "You used the word [jargon] — define it without using the word itself." If you try to fake it by rephrasing the source material, the tutor catches you. That's the whole point. The loop continues until the tutor marks the concept solid, shaky, or faked it — then auto-advances to the next concept. At the end of each session, you get a per-concept verdict with two-line notes explaining why. It's the Feynman technique, but the friend who pokes holes in your explanations is always available. How we built it The entire app was built with MeDo. The pitch I gave myself going in was that the tutor's prompt — not the infrastructure around it — was the actual product, and I needed to spend my time on the prompt rather than on Next.js scaffolding and API plumbing. The stack ended up as Next.js with Tailwind on the frontend, the Anthropic Claude API for both concept extraction and the tutor conversation, and a handful of lightweight libraries for the input modes — readability extraction for URLs, youtube-transcript for video sources, pdf.js for documents. The build broke down into roughly four chunks. First, source ingestion — getting paste, URL, YouTube, and PDF inputs to all funnel into the same clean text representation. Second, the concept extraction pass — a single Claude call that takes the source and returns a structured list of testable concepts with a one-line "what mastery looks like" for each. Third, the drill loop — the Socratic tutor that does the real work. Fourth, the verdict and recap screen. MeDo handled the scaffolding, the chat UI wiring, the API routes, and the deployment. I described changes in plain language ("the tutor should auto-advance when it marks a concept mastered, not wait for me to click anything") and the app updated. The visual editor let me tweak the chat interface without dropping into code. That separation — me on the product brain, MeDo on the plumbing — was the whole reason this shipped in a weekend. Challenges we ran into The hardest problem was getting the tutor to actually detect faking, not just generic shallow answers. The first version of the tutor prompt was too generous. It would accept any answer that vaguely paralleled the source — if I copy-pasted a sentence from the article with two words swapped, it would congratulate me on a "solid explanation." Useless. The whole point of the product is that it catches the thing flashcards can't. The second version overcorrected. I added skepticism so aggressively that the tutor kept demanding more depth even when I'd genuinely nailed a concept. It felt like being interrogated by someone who'd already decided I didn't know what I was talking about. Real users would bounce in 90 seconds. The version that shipped lives in the middle. The tutor is explicitly instructed to bias toward "this answer could have been generated by surface-level pattern matching" rather than "this sounds reasonable" — but it also has clear conditions for marking a concept solid and moving on (two consecutive exchanges where the user demonstrates real reasoning, not just terminology). Getting that calibration right took maybe twenty iterations on the prompt, tested against my own deliberate attempts to fake my way through. The other real challenge was scope discipline. The original spec had a persistent weakness map across sessions, voice input, spaced repetition, and saved sessions. I cut all of it. V1 ships the loop, nothing else. Resisting the urge to build "just one more feature" before launch was harder than the actual engineering. Accomplishments that we're proud of The tutor catching a faked answer in a demo. There's a specific moment when you paste in a 500-word article, the tutor asks you to explain a concept, you answer by literally copy-pasting a sentence from the source with a couple of words changed — and the tutor calls you out specifically, not generically. That moment is the whole product condensed into ten seconds. Getting it to land reliably feels like the real accomplishment. Shipping a working, deployed app in a weekend that's actually useful to me personally. Not a demo. Not a prototype. I've used Reps three times this week on technical reading I was pretending to understand, and it's caught me each time. Keeping the design restrained. The cream-and-orange palette, the editorial typography, the minimalist landing page — Reps doesn't look like a generic AI app, and it doesn't look like a kids' learning toy. It looks like a focused study tool, and that visual identity was worth protecting through the build. What we learned The hardest part of building an AI-native product isn't the AI. It's knowing what to not build around it. The temptation to add dashboards, gamification, streaks, leaderboards, and "your weekly insights" reports was constant. None of it would have made the core loop better. Most of it would have made it worse by signaling "this is a productivity app" rather than "this is a thinking tool." Prompt iteration is the new product iteration. When the AI conversation is the product, every behavioral tweak that used to require a sprint of engineering becomes a 30-second prompt edit. That's a fundamental shift in how the work feels. You spend your time being precise about behavior instead of being precise about code — and that's a skill worth getting good at. Building with MeDo reframed what "shipping" means for me. The traditional bottleneck — the four hours of auth scaffolding, the half-day fighting deployment, the morning lost to Tailwind config — was just gone. What was left was the interesting work: the tutor's voice, the verdict logic, the moment-to-moment feel of the conversation. That's the part of building that I actually care about, and MeDo let me stay in it. What's next for REPS The immediate next step is putting it in front of real users and watching where the tutor breaks down. The current calibration is tuned to my own learning style and the kinds of technical sources I tend to read. I expect it to feel too aggressive for some users and too lenient for others, and the only way to find out is to ship and observe. After that, the roadmap shapes up roughly like this: A persistent weakness map across sessions — so a user drilling on transformer architecture over three weeks can see which concepts keep coming back as shaky and which ones have actually stuck. This is where Reps starts to differentiate from any one-off Q&A tool. Spaced repetition built around the verdict data — automatically resurface shaky concepts at the right interval, but drill them through new Socratic exchanges rather than re-asking the same questions. Voice mode, eventually. Explaining out loud is closer to real understanding than typing, and the tutor catching hesitation or "ums" as a signal of shaky knowledge is a direction worth exploring. And a longer-term ambition: shareable drill packs. A professor uploads a course reading, generates a set of concept drills, and shares the link with students. The tutor stays the same; the source material becomes social. That's where Reps could move from a personal tool to something more like a learning protocol. For now, though: ship the loop, watch it break, fix what matters. Everything else can wait. <div