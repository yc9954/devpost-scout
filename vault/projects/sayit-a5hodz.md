---
slug: "sayit-a5hodz"
url: "https://devpost.com/software/sayit-a5hodz"
title: "SayIt"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 1327
team_size: 0
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/education"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# SayIt

> SayIt is an AI-powered communication app that helps people with speech or motor impairments express themselves.

[Devpost](https://devpost.com/software/sayit-a5hodz) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[accessibility]] [[education]] [[elder_child_care]] [[health_clinical]] [[mental_health]]
**user** [[patient_family]]
**substrate** [[code_repository]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** html, react, tailwindcss, typescript, ui, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sayit

## Body

Inspiration SayIt was inspired by real people, real limitations, and real moments where communication something most of us take for granted becomes a daily struggle. At a local market I visit often, there is a vendor who cannot speak. Every time I wanted to buy tomatoes, fruits, or drinks, there was no conversation. I had to type the quantity I wanted on his calculator. He would read it, then type the price back on the same calculator to show me how much it cost. That was how every interaction worked numbers replacing words, calculators replacing voices. It functioned, but it wasn’t communication. There was no emotion, no speed, no dignity. A simple exchange that should take seconds became a reminder of how inaccessible everyday life can be for people who cannot speak. This wasn’t a rare situation it was routine, normalized, and quietly accepted. Around the same time, I had a neighbor with autism. She struggles with verbal expression, but she can use a phone, press buttons, and play games. Despite this, communicating her needs, feelings, or thoughts to her family is still difficult. Watching her made something clear: the ability to interact with technology often exists but the ability to communicate meaningfully does not. In Nigeria, and in many similar environments, conditions such as autism, ALS, stroke-related disabilities, and other speech or motor impairments are widely misunderstood, underdiagnosed, or not formally recorded. Many families live with these realities silently. There are few accessible tools, little awareness, and almost no technology designed specifically for how people here actually live. For many individuals, the challenge is not just speech it is movement. Some people cannot use their hands reliably, if at all. Yet they can still move their head. They can nod. They can turn side to side. They can blink or open their mouth intentionally. Existing communication tools rarely consider this. That realization became the turning point. SayIt was inspired by a simple but powerful question: What if communication didn’t require speech or hands only the small movements people still have? What if someone could speak by moving their head? What if selecting a message didn’t require tapping a screen? What if communication adapted to people instead of forcing people to adapt to technology? SayIt was created to restore voice, dignity, and independence to people who are often unheard in markets, homes, schools, and communities. It is for the vendor who relies on a calculator. For the neighbor who wants to express herself more freely. For people with autism, ALS, and motor impairments. And for families who just want to understand their loved ones better. This project is not just inspired by technology it is inspired by humanity, empathy, and the belief that everyone deserves to be heard, in their own way. What it does SayIt is an AI-powered Augmentative and Alternative Communication (AAC) application that enables people with speech and motor impairments to communicate independently, expressively, and hands-free. It allows users to: 1-Communicate using pre-built phrases and custom expressions 2-Speak in multiple languages, including Nigerian and global languages 3-Customize voice type and tone (calm, polite, casual, expressive) 4-Navigate and interact using head movements and facial gestures 5-Select buttons by opening and closing the mouth, without touching the screen Most importantly, SayIt works for users who cannot rely on their hands. By tracking head movement (up, down, left, right) and facial actions, the app enables full navigation and selection without physical input. This transforms communication from a struggle into a natural, dignified experience. How we built it SayIt was built using modern, scalable web technologies with accessibility at its core. Core Technologies 1-React for the user interface 2-TypeScript for reliability and maintainability 3-Vite for fast development and performance 4-Tailwind CSS and shadcn/ui for clean, accessible design Key Technical Concepts 1-Gesture-based navigation logic 2-Camera-based head and facial movement detection 3-Text-to-speech output with voice and tone customization 4-Multilingual language handling 5-Phrase-based AAC communication structure Challenges we ran into Building SayIt came with real technical and design challenges: 1-Reliable Head & Facial Detection Human movement varies widely. Making head gestures responsive without being too sensitive or inaccurate required careful calibration. 2-Accessibility Without Overcomplexity Many AAC tools fail because they overwhelm users. Designing something powerful yet simple was a constant balance. 3-Mobile Limitations While the hands-free mode works well on desktop, mobile browsers have limitations with camera access and gesture precision something we’re actively addressing. 4-Inclusive Design in a Low-Resource Context Designing for users in environments where accessibility tools are rare meant avoiding assumptions about hardware, internet speed, or prior experience. Accomplishments that we're proud of 1-Building a hands-free AAC system that works through head and facial gestures 2-Supporting multilingual communication, including underserved languages 3-Allowing users to control voice, tone, and expression 4-Creating a solution inspired by real people, not abstract personas 5-Designing with accessibility as the starting point, not an afterthought What we learned Accessibility is not niche it affects families, communities, and societies Small design decisions can radically change someone’s independence Technology should adapt to people, not force people to adapt to technology Empathy is a technical skill, not just an emotional one Innovation doesn’t always mean new hardware sometimes it means rethinking interaction What's next for SayIt SayIt is already breaking barriers in communication — but this is just the beginning. Our next phase is focused on making SayIt more accessible, more powerful, and truly universal. We want everyone, everywhere — regardless of ability, language, age, or device — to be able to connect, speak, and be understood. 🧠 1. Expand Hands-Free Interaction 🟰 Improve head-movement sensitivity and accuracy allowing smoother navigation without false triggers 👁️ Add eye-blinking detection ; so users with very limited movement can still interact using intentional blinks 😮 Refine facial gesture recognition ; enabling richer control options (e.g., smiling to confirm, eyebrow raise for options) With better gesture detection, SayIt will empower users who have minimal motor control to communicate with confidence, without ever touching a screen. 📱 2. Bring Hands-Free Mode to Mobile Devices Right now, SayIt’s hands-free mode works on web browsers , but we must reach people where they actually live and move: 📲 Mobile optimization: Enable full gesture control on Android and iOS web browsers 🧪 Research device capabilities to improve camera tracking in mobile environments 📱 Make SayIt usable across all smartphones without installing extra software This step will dramatically increase accessibility, because many users rely on mobile devices as their primary or only technology. 📦 3. Launch on Lightweight Tablets A portable, touch-free communication tool can be life changing: 💡 Offer SayIt on lightweight tablets for families, caregivers, and clinics 🖐 Include simplified touch alternatives for users who have partial hand movement 🧑‍🦽 Design tablet interfaces with large, accessible buttons and optional hand-touch features This makes SayIt practical for daily use at home, school, clinics, and community centers giving people an always-available communication partner. 🌍 4. Broaden Global and Local Language Support Our vision is to make SayIt truly global, but also deeply local: 🔤 Add more Nigerian languages and dialects 🗣 Expand support for African and global languages 🎙 Increase voice and tone diversity so users can choose voices that reflect their identity Language is identity expanding this support brings dignity and inclusion to diverse communities. 🤝 5. Partnerships and Adoption We want SayIt to reach people who need it most: 💼 Collaborate with NGOs, caregivers, schools, and clinics 📣 Promote SayIt at conferences, health expos, and disability-rights events Our ultimate goal is for organizations in different countries to adopt SayIt as an inclusive communication tool. 📈 6. Continuous Technology and Community Growth We will stay committed to iterative improvement: 🧠 Collect user feedback from caregivers, therapists, and users 📊 Use data (with privacy-first design) to refine phrase suggestions and UX 🧪 Test new AI-assisted communication enhancements like predictive phrasing and emotion inference We envision a future where SayIt feels less like an app and more like an extension of the user’s voice and personality. <div