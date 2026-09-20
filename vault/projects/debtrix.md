---
slug: "debtrix"
url: "https://devpost.com/software/debtrix"
title: "Debtrix"
hackathon: "Hackonomics 2025"
organization: "hackonomics"
winner: true
words: 626
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/structured_db"
---

# Debtrix

> Debtrix combines AI with a psychological assessment to create your unique path to debt freedom. It's not just math, it's a mindset.

[Devpost](https://devpost.com/software/debtrix) · hackathon [[Hackonomics 2025]]

## Facets

  <sub>weak: provenance_signing, realtime_stream</sub>
  <sub>weak: education</sub>
**substrate** [[structured_db]]

**stack** api, css, figma, framer, framer-motion, nextjs, perplexity-sonar-api, react, shadcn/ui, supabase, tailwind, typescript, vercel

## Body

Landing Page Dashboard Financial Assessment AI Financial Coach Featured Articles Financial Education Center Inspiration The inspiration for Debtrix came from a simple observation: for most people, especially the younger generation, debt isn't just a number on a spreadsheet—it's a source of immense stress and confusion. Traditional financial tools are cold and impersonal; they offer calculators but ignore the crucial psychological component of debt management. I saw a gap between the logical solutions offered and the emotional reality people face. This led to the core idea: what if we could build a tool that first understands the user's mindset? What if we could make the daunting journey of debt elimination feel empowering, strategic, and even a bit rebellious? The "Escape the Debt Matrix" theme was born from this desire to transform a negative experience into a game-like challenge. By framing debt as a system to be understood and "beaten," Debtrix aims to make financial literacy engaging and accessible for everyone, especially those 13 and older, as per the hackathon's mission. How I Built It Building Debtrix was an exercise in leveraging a modern, integrated tech stack for rapid, high-quality development. The goal was to create a production-ready application that was both technically proficient and visually appealing. First, I designed the user experience, focusing on a Matrix-inspired dark theme to create a cohesive and immersive feel. The UI was built with a mobile-first approach to ensure accessibility for all users. Next, I set up the backend and database using Supabase , which provided robust user authentication, real-time data capabilities, and a powerful PostgreSQL database. This was crucial for securely managing user financial data with Row Level Security . The core logic of the platform—the debt assessment and strategy recommendation engine—was built to analyze user input and apply proven financial models like the Snowball and Avalanche methods. Finally, the AI Financial Coach was brought to life by integrating the Perplexity Sonar Pro API , which was fine-tuned to provide safe, context-aware financial advice. // A simplified look at the tech stack integration const App = { frontend: "Next.js & TypeScript", styling: "Tailwind CSS & Shadcn/ui", backend_database: "Supabase (PostgreSQL)", ai_integration: "Perplexity Sonar Pro API", deployment: "Vercel" }; Challenges I Ran Into One of the biggest challenges was balancing the "Matrix" theme with the need for financial trust . It was essential that the design felt cool and modern without seeming gimmicky or insecure. I solved this by using the theme for accents—like the signature green ( #00FF41 ) for success states and subtle animations—while keeping the core data presentation clean, professional, and aligned with established fintech design patterns. Another technical challenge was managing the context for the AI coach . To give personalized advice, the AI needs to understand the user's financial situation, but I also had to ensure user privacy. I engineered a solution where a lightweight, anonymized "context object" summarizing the user's debt profile is sent with each query, allowing the AI to provide relevant advice without exposing sensitive details. What I Learned This project was a profound learning experience. On a technical level, I learned how incredibly powerful a modern, integrated stack like Next.js, Supabase, and Vercel can be for building and deploying complex, full-stack applications at high speed. Integrating the Perplexity API also taught me a great deal about prompt engineering and the importance of providing clear context to get safe and useful responses from a large language model. Most importantly, building Debtrix reinforced my belief that the best technology is human-centric. By focusing on the user's psychological state first, we can build financial tools that are not only smarter but also more compassionate and effective. This project solidified my passion for using technology to create solutions that empower people and provide real, long-term value. <div