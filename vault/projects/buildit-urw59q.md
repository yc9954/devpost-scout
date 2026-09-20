---
slug: "buildit-urw59q"
url: "https://devpost.com/software/buildit-urw59q"
title: "BuildIt"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 1378
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/immigration_refugee"
  - "domain/retail_commerce"
  - "user/developer"
  - "user/educator_student"
  - "user/researcher"
  - "user/social_worker"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# BuildIt

> The majority of STEM resources are one-size-fits-all and English-only. BuildIt fixes that by generating personalized, hands-on projects for K-12 students based on time and budget — in any language.

[Devpost](https://devpost.com/software/buildit-urw59q) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[developer_tools]] [[education]] [[immigration_refugee]] [[retail_commerce]]
**user** [[developer]] [[educator_student]] [[researcher]] [[social_worker]]
**substrate** [[video_visual]] [[web_dom]]

**stack** css, express.js, github, groq, javascript, jsx, llama-3.3-70b-versatile, llama-4-scout-17b, localstorage, node.js, react-18, supabase, svg, tailwind-css

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for buildit

## Body

Inspiration Both me and my teammate have grown up in Cedar Park, Texas, a community that is one of the most linguistically diverse I have ever been a part of. Walking through my neighborhood, my school, my everyday life, you encounter families speaking Spanish, Hindi, Mandarin, Arabic, and more. For me (Joaquin Diaz de Leon) personally I was involved in the dual language education program from kindergarten through middle school. Being in a program that treated both English and Spanish as equally valid languages of learning did not just teach me basic things but it rather changed my perspective on the world around me. I was able to connect with more people, think through problems from different angles, and feel proud of something that too many students are made to feel like they need to hide. Dual language did not slow me down academically. It made me sharper. Then the program got cut. And I watched what happened to the students behind me — the ones who were just starting to build that foundation — when the rug got pulled out from under them. There was no replacement, no alternative, no safety net. The message it sent was that linguistic diversity was a budget line item, not an asset worth protecting. Around the same time, I started to notice something else about how I actually learn best. It was never sitting at a desk copying notes. It was building things, making things, figuring out why something did not work and trying again. Project-based learning gave me a reason to care about the science or the math behind what I was doing, because I could see it in front of me and hold it in my hands. BuildIt came out of both of those realizations at once. If students in communities like mine are losing the programs that make learning feel relevant and accessible, we need something that could meet them where they are — in their language, at their level, with their hands involved. That is what we set out to build. What it does BuildIt is an AI-powered STEM project generator built for K-12 students. You fill out a short form with your grade level, STEM interests, hobbies, budget, and how much time you have, and the app generates three fully personalized, hands-on maker projects you can actually build at home. Each project comes with a materials list, step-by-step instructions, and a shopping list for anything you need to buy. There is also a materials scanner that uses your camera to detect what you already have at home and generates projects around those specific items. Once you are building, the app has a guided build mode with an AI assistant you can ask questions, a concept explainer for the STEM ideas behind each project, and a reflection flow when you finish. A community section lets students share ideas for projects they want to build, which other students can then hit a Generate button on to get full AI-generated instructions tailored to their own grade level. Students can also share completed builds to a photo gallery where others can like them. The entire community is personalized to your grade band so younger students and older students each see content appropriate for their level. How we built it We built it as a React and Vite single-page app styled with Tailwind CSS using a custom Material Design 3 token system, and we used Claude as an AI coding assistant throughout the entire development process — from architecting the component structure to writing and debugging the AI prompt logic. All AI features run through the Groq API, using Llama 3.3 70B for text generation and Llama 4 Scout 17B for the vision-based materials scanner. To keep the API key off the client, we built a small Express proxy server that sits between the browser and Groq so all requests go through the backend. User data including saved projects, community posts, student profiles, and session state is stored in localStorage, with Supabase wired up as an optional upgrade path. The community gallery uses a storage key versioning system to handle seed data migrations without breaking existing sessions. Grade-level personalization was implemented by tagging all seed content with grade bands and passing the student profile through from the intake form all the way down to the AI generation prompts, which use the same tiered feasibility and complexity rules as the main project generator. Claude helped design and iterate on those prompts, write the component logic, debug edge cases, and build out features like the community section, the materials scanner, and the grade-aware generation system from scratch. Challenges we ran into One of the bigger challenges was making the AI-generated projects genuinely grade-appropriate and actually doable at home rather than just technically plausible. We had to write detailed feasibility rules, safety constraints, and tool-scaling rules directly into the prompts to stop the model from suggesting things like soldering, lab equipment, or disassembling devices, and to make sure a high schooler was never getting a project a second grader could finish in ten minutes. Another challenge was the community data model — separating a student's raw idea description from the AI-generated project title and instructions required restructuring the data layer mid-build, and we used storage key versioning to force clean re-seeds in the browser without wiping user data. Getting the materials scanner to work reliably with the vision model also took iteration around prompt structure and how detected items were passed into the generation flow. Building the two-server architecture locally so the API key stayed server-side while Vite handled hot reload on the frontend added some configuration overhead that had to be worked out carefully. Accomplishments that we're proud of We are proud that the app genuinely scales with the student. A kindergartner and a high schooler both get projects that feel right for their level — not because we built separate experiences, but because the same system adapts through grade-tier rules baked into the AI prompts. We are also proud of the bilingual experience being seamless rather than an afterthought — every piece of generated content, every instruction, and every UI element responds to the student's language preference in real time. Building a full community feature with idea sharing, AI-powered project generation from community ideas, a photo gallery, and grade-filtered content on top of a working core app within a hackathon timeline is something we are genuinely proud of. And doing it with a completely free and open-source stack accessible to any developer or school means the barrier to building on top of it is as low as possible. What we learned We learned how much prompt engineering actually matters for educational tools. Telling a model to generate a STEM project is easy — getting it to generate one that is safe, grade-appropriate, genuinely buildable at home, and teaches the concept naturally without labeling it "STEM explanation:" required layers of specific rules and iteration. We also learned how important the student profile is as context — once we started threading grade, budget, interests, and time constraints all the way through every AI call, the quality of every output improved significantly. On the technical side, building a proxy server to protect API keys while keeping a smooth local development experience with Vite taught us a lot about how to structure full-stack apps that are both secure and developer-friendly. What's next for BuildIt The next step is deploying BuildIt to a public URL so any student can access it without running it locally. From there, we want to add real user accounts so students can build a portfolio of completed projects over time and track their growth across grade levels. We want to expand the community features with moderation tools so teachers can manage a classroom-specific gallery and assign projects directly through the app. On the language side, we want to go beyond English and Spanish and support any language a student types in, making the tool viable for immigrant and heritage language communities across the board. Longer term, we want to partner with schools that have lost STEM or dual language programs to pilot BuildIt as a free supplemental resource and measure whether it actually moves the needle on student engagement with STEM. <div