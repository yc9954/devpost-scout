---
slug: "ratesheet"
url: "https://devpost.com/software/ratesheet"
title: "RateSheet"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 1011
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "user/government_staff"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# RateSheet

> All-in-one, open-source production tracking and piece-rate payroll built for garment manufacturing. Faster logging, accurate pay, and insights your team can trust.

[Devpost](https://devpost.com/software/ratesheet) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]] [[housing_homeless]] [[labor_employment]] [[supply_logistics]]
**user** [[government_staff]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[structured_db]]

**stack** clerk, convex, javascript, nextjs, react, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ratesheet

## Body

White Landing Page Dark Landing Dashboard Workers Sections Styles And Rates Payroll Production Logs Bonuses Reports Inspiration The garment manufacturing industry, a cornerstone of global commerce, often relies on outdated, manual processes. We were inspired by the daily reality on the factory floor: managers juggling stacks of paper ledgers, workers unsure of their earnings, and payroll departments spending days manually calculating wages. This system is prone to human error, lacks transparency, and creates massive inefficiencies. The most complex part is handling "piece-rates" that change over time, making accurate historical payroll a nightmare. We saw a clear need for a modern, digital solution that was accessible, powerful, and built specifically for the industry's unique challenges. We wanted to build a tool that brings clarity, accuracy, and efficiency to every stitch. What it does RateSheet is a comprehensive, open-source production management and payroll system designed to revolutionize garment manufacturing. It replaces manual paperwork with a seamless, real-time digital workflow. ✅ Real-time Production Tracking: Managers can log daily worker output by style and section, instantly creating a digital record of all work performed. 💰 Automated Dynamic Payroll: Our core feature is an intelligent payroll engine that automatically calculates wages based on dynamic, time-sensitive piece rates. If a rate changes, RateSheet uses the correct historical rate for the date the work was done, ensuring 100% accuracy. 👥 Workforce & Team Management: Admins can create organizations, set up production sections (like "Cutting" or "Stitching"), add workers, and invite managers with role-based permissions. 📊 Data & Insights: All production data is centralized, providing a clear overview of operational efficiency, worker performance, and payroll expenses. 🌐 Multi-Tenant & Secure: The platform is built with a secure, multi-tenant architecture, ensuring that each organization's data is completely isolated and protected. How we built it We chose a modern, real-time technology stack to deliver a fast, responsive, and reliable user experience. Frontend: Next.js 15 with React 19 and TypeScript for a robust, type-safe, and performant web application. Backend & Database: Convex serves as our all-in-one backend, providing a real-time database and serverless functions. This allowed us to build live-updating features with incredible speed, as data syncs automatically across all connected clients. Authentication: Clerk handles all user management, authentication, and organization control. Integrating Clerk saved us immense development time and provided enterprise-grade security out of the box. UI/UX: We used Tailwind CSS v4 and the beautiful, accessible components from shadcn/ui to build a clean, professional, and fully responsive interface with both light and dark modes. Package Manager: We used Bun for its blazing-fast performance in dependency installation and script execution. Data model highlights: Organizations, Sections, Workers Styles and Rates: each style has a schedule of rates with effective dates ProductionLogs: one worker + one style + one date (+ quantity) Payroll is computed by matching each log to the rate effective on that date Example: selecting the correct historical rate type Rate = { amount: number; effectiveFrom: string }; // ISO date function effectiveRate(rates: Rate[], onDate: Date): Rate | undefined { return rates .filter(r => new Date(r.effectiveFrom) <= onDate) .sort((a, b) => new Date(b.effectiveFrom).getTime() - new Date(a.effectiveFrom).getTime())[0]; } Challenges we ran into Our biggest challenge was architecting the dynamic payroll engine . Modeling a database schema that could accurately store and query time-sensitive pricing where a single style could have different rates in August, September, and October was complex. We had to ensure that every single production log was correctly cross-referenced with the rate that was active on that specific day . We solved this by creating a dedicated rate history table linked to each style and implementing robust Convex query functions that perform this date-based lookup automatically and efficiently. Another challenge was ensuring true real-time data synchronization across different user roles (admins and managers) without compromising security. This required carefully defining our data access rules and functions within Convex to guarantee data isolation and proper permissions. Accomplishments that we're proud of Solving the Core Payroll Problem: We are incredibly proud of successfully building the dynamic, time-sensitive payroll calculation system. It's the heart of RateSheet and directly solves a major pain point for manufacturers. A Fully Real-time Experience: From logging production to viewing dashboard updates, the entire application feels alive. Thanks to Convex, any data change made by one user is instantly reflected for all other members of the organization. Delivering a Polished, Production-Ready UI: We didn't just build a functional prototype. We created a polished, responsive, and aesthetically pleasing application with features like dark mode and smooth loading states, making it ready for real-world use. Open-Source Commitment: We successfully built and structured the project to be fully open-source, providing a powerful, free tool for private use and empowering the community to contribute and customize it. What we learned Throughout this hackathon, we gained significant experience with modern full-stack development. We learned how incredibly powerful a Backend-as-a-Service platform like Convex can be for rapid development of real-time applications, abstracting away complex WebSocket and server management. We also deepened our understanding of Clerk for handling multi-tenancy and role-based access control efficiently. Most importantly, we learned to dive deep into a specific industry's problem domain to build a solution that is not just technically impressive, but genuinely useful and impactful for its target users. What's next for RateSheet The journey for RateSheet is just beginning. We have a clear roadmap to expand its capabilities and provide even more value to the manufacturing industry. Advanced Analytics & Visualizations: Introduce dashboards with charts and graphs to visualize production trends, identify top-performing workers, and spot bottlenecks. Reporting & Data Exports: Allow managers to generate and export detailed payroll and production reports in PDF and CSV formats for their accounting needs. Public API: Develop a REST or GraphQL API to allow factories to integrate RateSheet with their existing HR or ERP systems. Worker Portal: Create a dedicated, view-only portal for workers to log in and track their own production records and estimated earnings, promoting transparency and motivation. Material & Inventory Tracking: Expand the scope beyond labor to include tracking of raw materials and inventory used in production. <div