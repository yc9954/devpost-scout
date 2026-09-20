---
slug: "sleep-fixer-b2p4xj"
url: "https://devpost.com/software/sleep-fixer-b2p4xj"
title: "Sleep Fixer"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 644
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/mental_health"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# Sleep Fixer

> Sleep Fixer doesn’t just track sleep, it helps you fix it. Get a personalized, day by day science-backed plan and smart AI nudges to shift your schedule and wake up refreshed.

[Devpost](https://devpost.com/software/sleep-fixer-b2p4xj) · hackathon [[Student HackPad 2025]]

## Facets

**domain** [[developer_tools]] [[education]] [[mental_health]]
  <sub>weak: civic_government</sub>
**substrate** [[code_repository]] [[web_dom]]
  <sub>weak: structured_db</sub>

**stack** dart, flutter, gemini, hive, http, material-design-3, nosql, sdk, url-launcher, vs-code

## Body

💤 Inspiration Sleep is broken for millions. Between school, work, and stress, we found ourselves — and many friends — falling into irregular sleep schedules. Fixing it isn't easy. Existing apps either focus on tracking or meditation, but not on the core problem: shifting sleep schedules gradually and intelligently. We wanted to build a solution that does what no other app does well — help users move from any current sleep time to their ideal schedule, without shocking the body or causing burnout. 💡 What it does Sleep Fixer is an AI-powered sleep schedule optimizer that: Takes your current and goal sleep/wake times Generates a daily, science backed, customized, gradual adjustment plan Includes a solidification phase to lock in your new schedule Supports users with customized AI notifications Adapts to fixed wake-up constraints (like school) Has gamifications with experience points, levels, and stats It’s not just a tracker, it’s a plan. 🛠 How we built it To build Sleep Fixer, we engineered a cross-platform mobile solution using Flutter (Dart), allowing us to maintain a single codebase for iOS, Android, and the web while ensuring performance and design consistency via Material Design 3 components. Frontend: The app UI is written in Flutter with a declarative widget structure, utilizing state management patterns (Provider/ValueNotifier) for reactivity and modularity. We followed atomic design principles to keep components reusable and maintainable. Local Storage: We used Hive, a fast, lightweight NoSQL database optimized for Flutter, to persist user sleep data (e.g. daily sleep logs, shift plans) offline. SharedPreferences was used to store app settings and preferences, enabling quick access without serialization overhead. API Integration: We integrated Google Gemini API through Dart’s http package to power natural language generation for sleep coaching. Prompts are dynamically constructed based on user behavior, tone preferences, and current sleep trends. Device Integration: Using Device Info Plus, we detect device platforms and OS versions to customize platform-specific experiences (e.g., dark mode handling, app permissions). URL Launcher allows seamless deep linking to system-level settings like blue light filters. Sleep Plan Engine: Our custom-built algorithm computes gradual sleep/wake shifts based on principles from chronotherapy and circadian rhythm biology. The logic factors in: current vs. target wake/sleep time max shift per day (15–30 minutes) phase response curves fixed wake-up constraints vs. flexible schedules The algorithm outputs a day-by-day schedule with annotations (e.g., “Delay bedtime 15 min, wake at same time”), which is then contextualized by AI for user-facing clarity. The AI coach leverages Google Gemini's LLM API to translate raw sleep plan data and behavior insights into supportive, friendly feedback. Prompts are engineered to mimic conversational, emotionally intelligent tone with adaptive language (e.g., emoji usage, tone softening for sensitive topics). Codebase managed via Git, hosted on GitHub, and developed using VS Code and Android Studio. CI/CD planned using GitHub Actions for automated testing and builds. ⚠️ Challenges we ran into Some users have strict school/army wake times but flexible sleep times. We had to design the algorithm to support both effectively. There were errors in the math for the time calculations, which we had to find workarounds for We wanted to add too many features but staying focused on one problem helped. 🏆 Accomplishments that we're proud of Creating a fully working app that outputs real, science-informed daily plans Solving a real, relevant problem for everyone Designing an aesthetic and pleasant UI 📚 What we learned Sleep is deeply personal and requires personalized plans Small consistent changes are more effective than aggressive resets Quality over quantity, focus over features 🚀 What's next for Sleep Fixer Launch on the Play Store and App Store Add dynamic plan adjustments (for inevitable days when you can't follow the plan) Build a Reddit-style sleep community within the app Integrate sleep tracking and sync with Google Fit / Apple Health Partner with schools, governments, or health orgs to combat sleep debt at scale <div