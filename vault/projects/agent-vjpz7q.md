---
slug: "agent-vjpz7q"
url: "https://devpost.com/software/agent-vjpz7q"
title: "FamCare - Healthcare management RAG"
hackathon: "TiDB AgentX Hackathon 2025"
organization: "TiDB"
winner: true
words: 1260
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/developer"
  - "user/frontline_worker"
  - "user/legal_professional"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/medical_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# FamCare - Healthcare management RAG

> FamCare helps you organise your health documents, ai chat to better understand records, create medicine scheduling using ai, keeping track of medicines, schedules, diet, exercise and create a calendar

[Devpost](https://devpost.com/software/agent-vjpz7q) · hackathon [[TiDB AgentX Hackathon 2025]]

## Facets

**mechanism** [[retrieval_grounding]] [[sensor_fusion]]
**domain** [[developer_tools]] [[elder_child_care]] [[health_clinical]]
**user** [[developer]] [[frontline_worker]] [[legal_professional]] [[patient_family]]
**substrate** [[document_pdf]] [[geospatial]] [[medical_record]] [[structured_db]] [[video_visual]]
  <sub>weak: code_repository</sub>

**stack** aisdk, jina, kimiai, moonshotai, react, tanstack, tidb

## How they structured the write-up

- ⚙️ installation
- 🗄️ database schema setup with tidb & drizzle
- 🚀 deployment

## Body

Rag System Diagram Problem With the Aging population, we are seeing more and more decline in fertility rate, increase in chronic diseases, and increase in healthcare costs. More Importantly, we are seeing a decline in the quality of life, which is leading to more and more people being dependent on others for their daily needs. Now we have a situation where younger ones responsible to look after older family members. Older family members are facing Chronic diseases like diabetes, hypertension, heart diseases, etc. This requires keep track of complex drugs, schedules, and a healthy lifestyle. The need to have better diet plans, exercises, medicine schedules, keeping track of health records, track sleep patterns, and organizing family activities to avoid loneliness is becoming more and more important. Introducing FamCare The Main objective of famcare is to help you organise your health documents, ai chat to better understand records, create medicine scheduling using ai, keeping track of medicines, schedules, diet, exercise and create a calendar, that can be shared with family members. You can download/ add events to your own ics supported calendars like apple, google, notion. 🔗 Open Source & Demo Source Code (Open Source) : https://github.com/biomathcode/famcare Live Demo : https://famcare-one.vercel.app Story behind building this app i moved back my parents house, and i have become responsible for managing family health, medicines, diet and exercise plans. I wanted to build an app which can help me manage all these things in one place. I also wanted to use AI to help me with the same. AI can be a great organizing tool as well as a research tool to find information about medicines, side effects, interactions etc. Also to save medical history, records and their medicine Schedules. Features: Add Family Members Add Medicines Add Health Records/ docs/ pdf Add Medicine Schedule, Add Diet, Add Exercise Goals, Add Sleep Goals. Chat Features. Create a Medicine Schedule Calendar. Tech Stack Frontend: React, shadcn, tanstack-router, tailwind Backend: trpc, drizzle, zod, Database: tidb AI: moonshot ai kimi k2 Vector DB: tidb, embeddings : jina ai, parser : jina ai How the RAG System work? This is a health management system that uses RAG to answer questions about health. We upload the file then create chunk, embedding, and this become the knowledge base of our rag. We create and save vectors in tidb of length 768. I created a custom type for vector in drizzle export const vector = customType<{ data: number[]; config: { length: number }; configRequired: true; driverData: string; }>({ dataType(config) { return `VECTOR(${config.length})`; }, toDriver(value: number[]) { return `[${value.join(",")}]`; }, fromDriver(value: string) { try { return JSON.parse(value) as number[]; } catch { return value .replace(/^\[|\]$/g, "") .split(",") .map(Number); } }, }); Here is a Diagram of the rag system powered by jina ai, moonshot ai and tibd As you can see we have different ways of parsing image and pdf/docs. We use the moonshot-v1-8k-vision-preview for getting the readable text from the image and we use jina reader api to get the text from pdf Documents. Then We use the segment from jina ai to create chunks and the jina-embeddings-v3 to create embeddings. Retrieving Doc Chunks using the vector search by tidb 🔍 Search Flow User submits a question Generate query embedding (Jina AI) Perform Vector Search in TiDB: SELECT id, media_id, chunk, `order`, vec_cosine_distance(embedding, ?) AS distance FROM mediaChunks ORDER BY distance LIMIT 5 Retrieved chunks passed to Kimi AI for final response generation. Tools in AI Chat You can use the following tools to help the user: getMembers : Use this tool to get all members from the database createExerciseGoalTool : Use this tool to create an exercise goal for a member createDietTool : Use this tool to create a diet plan for a member createMedicine : Use this tool to log a medicine entry for a member getDrugLabel : view drug labeling info getAdverseEvents : lookup reported side effects getDrugRecalls : check recall or enforcement reports findRelevantContent : Use this tool to find relevant content from the database createBulkEventsTool : Use this tool to create events in bulk or than one event Integration with Medical APIs Medicine search using RxTerms API Condition search via Clinical Tables API Real-world adverse event data via OpenFDA We are use open fda api for getting conditions and list of medicines. We also use the tool getAdverseEvents to get the real recorded side effects of medicines. For getting getting the list of medicines we are using the rxterms api async function fetchMedicines(query: string) { if (!query) return []; const res = await fetch( `https://clinicaltables.nlm.nih.gov/api/rxterms/v3/search?terms=${encodeURIComponent( query )}&maxList=20` ); const data = await res.json(); // data[1] = array of names return data[1] as string[]; } Similarly for getting the Conditions async function fetchConditions(query: string) { if (!query) return []; const res = await fetch( `https://clinicaltables.nlm.nih.gov/api/conditions/v3/search?terms=${encodeURIComponent( query )}&maxList=20` ); const data = await res.json(); return (data[3] || []).map((item: string[]) => item[0]); } Here is the updated and polished section to add at the end of your write-up, with proper formatting and clarity: ⚙️ Installation git clone https://github.com/biomathcode/famcare.git cd famcare/apps/client pnpm install Add a .env file inside apps/client/ based on the provided sample.env . Here is a clear and structured documentation section for setting up the database schema on TiDB using Drizzle ORM in your project: 🗄️ Database Schema Setup with TiDB & Drizzle FamCare uses Drizzle ORM to manage the database schema on TiDB . Step 1 – Configure Drizzle In your project, the database schema is defined using Drizzle's schema DSL (e.g., inside src/lib/db/schema/ ). A typical schema file looks like this: import { mysqlTable, varchar, int, timestamp, json, customType } from 'drizzle-orm/mysql-core'; export const member = mysqlTable('member', { id: varchar('id', { length: 36 }).primaryKey(), name: varchar('name', { length: 255 }).notNull(), dob: timestamp('dob').notNull(), conditions: json('conditions').notNull(), // ... other fields }); Step 2 – Drizzle Kit CLI Your package.json includes a script to manage the database schema: "scripts": { "db": "drizzle-kit" } This uses drizzle-kit for migrations. Step 3 – Running Migrations Make sure your .env file contains the correct database connection details: DATABASE_URL=mysql://user:password@host:port/database Generate a migration based on your schema files: pnpm run db generate Apply the migration to your TiDB database: pnpm run db push Step 4 – Inspect & Manage Migrations You can inspect generated migration files in the drizzle/migrations directory. To reset the database or apply migrations from scratch: pnpm run db reset Example Workflow # Install dependencies pnpm install # Generate migration from schema pnpm run db generate # Push schema changes to TiDB pnpm run db push The migrations are designed to be idempotent, so you can run db push safely during development. 🚀 Deployment You can deploy the app on Vercel, Netlify, Cloudflare, or any Node server since the app uses Tanstack Start. Vercel Set target: "vercel" in vite.config.ts . Deploy with: npx vercel deploy --prod Cloudflare Set target: "cloudflare-module" in vite.config.ts . Deploy with: npx wrangler deploy .output/server/index.mjs --assets .output/public Netlify Set target: "netlify" in vite.config.ts . Deploy with: netlify deploy This makes your submission complete, easy to follow, and ready for any judge or developer to try. Would you like me to generate a formatted PDF version with this included? 🚀 Impact FamCare empowers families to manage complex healthcare needs with ease, improving the quality of life for older adults while easing the caregiver's burden. It brings medical records, scheduling, and health advice into one place, supported by powerful AI tools. 💭 Future Roadmap Integration with wearable devices (Fitbit, Apple Watch) Advanced analytics for health patterns Multi-language support Push notifications for schedules and reminders TiDB Cloud account Email: sharma.pratik2016@gmail.com <div