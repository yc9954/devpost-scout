---
slug: "therefore"
url: "https://devpost.com/software/therefore"
title: "Therefore"
hackathon: "Perplexity Hackathon"
organization: "Perplexity"
winner: true
words: 882
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/general_public"
  - "user/researcher"
  - "substrate/genomic_bio"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Therefore

> Move beyond health tracking into structured experimentation.

[Devpost](https://devpost.com/software/therefore) · hackathon [[Perplexity Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[health_clinical]] [[scientific_research]]
**user** [[general_public]] [[researcher]]
**substrate** [[genomic_bio]] [[sensor_telemetry]] [[structured_db]]

**stack** cloudflare, next.js, perplexity, react, tailwind, vercel

## How they structured the write-up

- overview
- features
- how it works
- usage
- why this matters
- roadmap
- get in touch

## Body

∴ Therefore Everyone tracks their health. Nobody experiments properly. Turn your health goals into scientific experiments through structured, AI-supported, N-of-1 protocols. Create your first protocol today: Therefore | From Health Tracking to Personal Science (therefore.bio) Overview My WHOOP shows my HRV dropped to 30 overnight. Google says this was because of X , possibly Y , and I should try Z . Therefore says: based on 4 studies, 3g glycine before bed increases HRV by 15%. A scientific experiment is defined as a process used to derive answers to questions from observations. This is through formulating a hypothesis, designing and conducting an experiment to test it, and drawing conclusions based on the results. Therefore bridges the gap between health tracking and evidence-based action. It helps you design and run structured N-of-1 experiments on yourself, powered by peer-reviewed research from PubMed, scientific journals, and academic databases. Health trackers tell you what happened. ∴ Therefore tells you what to try next. Features Feature Description Protocol Builder Utilize a 5-step guided flow to create a structured experiment Intervention Suggestions Choose from 6 AI-suggested interventions tailored to your goal and timeline Smart Metric Recommendations AI analyzes studies to suggest which metrics to track, with confidence levels based on scientific evidence for your specific intervention Projected Outcomes View evidence-based predictions for how your metrics will change Protocol Research Get a detailed analysis of intervention effectiveness, mechanisms of action, and optimal protocols with direct citations to summarized study details, including key findings How It Works AI Integration i.e. Usage of Perplexity Sonar API /src/lib/ai-config.ts ∴ Therefore makes use of engineered AI prompts that act like a research scientist: Multi-Stage Research Pipeline Goal Refinement: Perplexity structures vague health goals into testable hypotheses - not just "more energy" but "maintain consistent energy levels without significant daily dips" Intervention Matching: Perplexity analyzes how each intervention works in the body to match it with your specific goal (e.g., This stack supports muscle relaxation and reduces stress, making it easier to wake up feeling rested and energized.) Metric Selection: Perplexity evaluates which biomarkers actually demonstrate intervention efficacy based on studies Outcome Projections: Synthesizes effect sizes across studies to predict personalized outcomes with confidence intervals Protocol Optimization: Extracts optimal amount, timing, and duration across multiple study methodologies Prompt Architecture Cascading prompts that build context (goal → intervention → measurements → projections) Enforced JSON schemas ensure structured, parseable research output Domain-restricted search (PubMed, ScienceDirect, Nature, etc.) prevents hallucination Real-Time Research Synthesis Analyzes papers in seconds to find scientific evidence for a custom specific goal Not a static database - discovers latest research as it's published Cross-references multiple studies to gauge confidence in identifying consistent effects This positions the use of Perplexity as an enabler of personalized experimentation at scale. Usage Production You can get started immediately with creating your first protocol at Therefore | From Health Tracking to Personal Science . This project is built using: Category Technologies Application Next.js, Tailwind, Radix (Shadcn), Motion, Lucide AI Integration Perplexity Sonar Storage localStorage Infrastructure Vercel, Cloudflare Why This Matters Unmet needs Health trackers today are built to tell you what has already happened, but t has come to a point where this data needs to be actionable with the power of these wearables. Market research shows that the current size of health wearables are around $53bn, and growing at a rate of over 20% year over year. In 10 years time by 2034, this would be more than $400bn ^1 . Consumer willingness The premium health tracking ecosystem has already validated the consumer willingness to invest in the "quantified self" for health optimizations. Monthly subscriptions of around $25-30 have proved to be feasible business models. Therefore is able to capture value at this intersection as the intelligence layer above these devices, not competing with hardware but making their data actionable. Our users already own or have invested $350-500+ in tracking devices, possibly spending much more annually on supplements. They are already primed for a platform that creates a natural premium positioning, maximizing their hardware's ROI by connecting measurement to evidence-based intervention through scientific protocol design. Timing of opportunity Generic health advice in a post-pandemic world does not carry the same credibility as people realize catch-all solutions don't meet individual biological needs Therefore democratizes the gold standard of clinical trials through self-experimentation Personalized medicine, while emerging, continues to be behind expensive gentic testing and research institutions ^2 LLMs like Perplexity Sonar enables live research synthesis at scale Roadmap Direct wearable integrations with WHOOP, Oura, etc. Social proof and public protocol sharing Protocol templates library for common goals Increased individual control and refinement of protocols Automated outcome and real-time adjustment recommendations based on biomarker changes: "Your overnight HRV suggests delaying today's intervention." Aggreggated protocol effectiveness data to power matching: "Similar users saw XY% success with this intervention." Get In Touch Get Started : therefore.bio Portfolio : zsy.sh Disclaimer : ∴ Therefore is not a substitute for professional medical advice, diagnosis, or treatment. The information provided through our AI research synthesis are not medical advice, prescriptions, or treatment recommendations. Always consult with qualified healthcare providers before starting any new health protocol, especially if you have existing medical conditions or are taking medications. Results from personal experiments may vary, and what works for one individual may not work for another. <div