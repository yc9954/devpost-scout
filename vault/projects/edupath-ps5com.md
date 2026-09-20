---
slug: "edupath-ps5com"
url: "https://devpost.com/software/edupath-ps5com"
title: "EduPath: AI University Matcher"
hackathon: "TiDB AgentX Hackathon 2025"
organization: "TiDB"
winner: true
words: 770
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# EduPath: AI University Matcher

> Skip months of grad school research. Our AI extracts your profile from natural conversation and delivers categorized university recommendations instantly.

[Devpost](https://devpost.com/software/edupath-ps5com) · hackathon [[TiDB AgentX Hackathon 2025]]

## Facets

**mechanism** [[retrieval_grounding]]
  <sub>weak: realtime_stream, vision_ocr</sub>
**domain** [[education]]
  <sub>weak: labor_employment</sub>
**user** [[educator_student]]
**substrate** [[document_pdf]] [[structured_db]] [[web_dom]]
  <sub>weak: transcript_audio</sub>

**stack** cloudvercel, gpt-4o-mini, openai, tidb

## Body

home page of EduPath analyzing user's background and matching with school analyze result:possible schools analyze result:safe schools analyze result:dream schools Project Story Inspiration As a law student transitioning to computer science, applying to grad school was absolutely overwhelming. Every night, I'd open dozens of university websites trying to compare different programs. Some schools wanted GRE scores, others didn't. Deadlines were scattered from December to March. Some required work experience, others welcomed fresh graduates... There was no standard format, so I had to create massive spreadsheets to track everything. The breaking point was when I paid thousands of dollars for application consultants, only to get a school list that felt half wrong for my profile. That's when I thought: why can't there be someone who knows everything about every school and is available to chat anytime? That's how EduPath was born. What it does EduPath is like having that super knowledgeable friend who understands every graduate program. You just chat naturally: "I have a 3.5 GPA, want to study CS, prefer Canada..." The AI understands your needs and recommends schools It categorizes schools into three buckets: 🎯 Target Schools - Perfect match for your profile 🏆 Reach Schools - Challenging but worth applying 🛡️ Safe Choices - High acceptance probability It also generates a personalized application timeline showing when to prepare materials and estimated costs. Best part? You can ask the AI anything, anytime. No more late-night university website hunting. How I built it I built the frontend with React to make conversations feel natural. The backend uses Vercel serverless functions for quick deployment. For AI, we chose OpenAI's GPT-4o-mini - cost-effective and powerful. The most interesting part was the database. I collected information from 100 top universities and used TiDB's vector search capabilities to match schools intelligently. This way, the AI understands the connection between "I want to study machine learning" and "CMU's MSCS program." Challenges we ran into Data inconsistency : Every university website has different formats, missing information, or vague descriptions. Standardizing this into a coherent database required significant preprocessing. Natural conversation flow : How do you make AI naturally extract GPA, test scores, and preferences through casual chat? It can't feel like filling out a form, but we need enough structured information. This took many prompt engineering iterations. Feature scope : We had so many ideas - document upload, scholarship matching, interview prep - but had to stay focused on the core user journey to build something truly polished. AI response balance : Users expect instant chat responses, but comprehensive school analysis requires complex calculations. Finding the right balance was tricky. Accomplishments that we're proud of Seeing it actually work was incredibly exciting! ✅ Real conversations : The AI naturally extracts your profile and recommends relevant schools ✅ Intelligent matching : Vector search delivers surprisingly accurate recommendations ✅ Complete user journey : From chat to school list to application timeline ✅ Production deployment : Fully functional web app that anyone can use ✅ Solving real problems : This could genuinely help students like me who felt lost in the process Most importantly, we built something that could have saved me months of stress and thousands in consulting fees. What I learned Technical skills : Advanced prompt engineering for structured data extraction from natural language Vector embeddings and semantic search implementation Real-time conversation state management Full-stack deployment with modern tools Product insights : Solving problems you've personally experienced creates the most authentic solutions User experience trumps feature complexity Natural conversation interfaces require careful design AI can truly democratize expensive consultation services Personal growth : The power of focused execution on a clear vision How much you can accomplish with the right tools and determination The importance of user-centered design thinking This project taught me that the best solutions often come from the simplest ideas executed well. What's next for EduPath: AI University Matcher Immediate roadmap : Document analysis : Upload transcripts and resumes for automatic profile extraction Multi-language support : Serve international students in their native languages Scholarship integration : Match students with relevant funding opportunities Long-term vision : Success story matching : Connect applicants with similar backgrounds who successfully got into target programs Advanced analytics : Detailed acceptance probability calculations based on historical data Mobile application : iOS and Android apps for on-the-go application management University partnerships : Direct integration with application portals Ultimate mission : Make personalized graduate school guidance accessible to every student, regardless of their financial situation. Education should be more equitable, and information should be more transparent. That's exactly what we're building toward. Built by someone who knows the struggle firsthand 🎓 <div