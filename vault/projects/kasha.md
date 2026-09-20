---
slug: "kasha"
url: "https://devpost.com/software/kasha"
title: "Kasha"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 981
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "domain/retail_commerce"
  - "user/developer"
  - "user/educator_student"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Kasha

> Tired of doing mental math and nudging someone who owes you money? Kasha is an AI chat bot that tracks real time spending, auto-split charges with friends, and sends personalized reminders

[Devpost](https://devpost.com/software/kasha) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[developer_tools]] [[education]] [[finance_payments]] [[immigration_refugee]] [[retail_commerce]]
**user** [[developer]] [[educator_student]] [[small_business]]
**substrate** [[financial_record]] [[geospatial]]
  <sub>weak: web_dom</sub>

**stack** anthropic, claude-ai, express.js, fintech, janitorai, leaflet.js, node.js, postgresql, react, socket-io, supabase, typescript, visa-developer-apis

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for kasha

## Body

landing page of website offers for students to take advantage of mark certain expenses on the app using 'split requested', kasha will send a reminder based on a certain mood view budget, real time spending, visa offers, and spending categories gain personalized advice based on various AI assistant moods view nearby merchants and ATMs that are nearby on and off campus Inspiration Life in college is unpredictable; lectures, coffee runs, and midnight food deliveries often nudge budgeting down the priority list. Most financial apps have a rigid system or feel isolating, as though budgeting is solely a personal issue, rather than a shared experience. We wanted to design something collaborative, conversational, and made for real student life. That idea became Kasha, a multi-person chat app that helps students manage their finances together by engaging in real-time budgeting, AI-based financial guidance, and merchant integration with Visa. What it does Kasha improves personal finance by transforming it into a collective experience through AI and live financial data. Kasha features a dashboard displaying the chat assistant, Penny, as well as real time spending. Users can indicate which of their expenses is a split expense and which friends they share the expense with. Penny will then prompt the group chat with a notification that they owe the user money. If a friend forgets to pay the user back, Penny will send timely notifications until the amount is paid. This ensures that the user doesn't have to worry about nudging their friends constantly, preventing awkward conversations. Penny also adapts its persona and tone to different users’ own communication style. Integration of APIs via Visa for Merchant Search, Visa Offers, Transaction Controls, Foreign Exchange Rates, and ATM Locater bring transparency and reality about finances and savings opportunities to students. Kasha’s smart budgeting dashboard automatically categorizes expenses, sends alerts when you are near your spending limit, and visualizes progress over time. An interactive campus map outlines student-friendly merchants and deals nearby, while group finance tools allow friends to seamlessly split bills, track IOUs, and settle. How we built it Kasha was created using a variety of technologies, real-time communications, and external financial APIs. The frontend consists of React, TypeScript, and Vite for a fast, responsive experience and user-friendly experience. We made a clean and modern design for Kasha using Tailwind CSS and Lucide Icons. Real-time communication between users is done through Socket.io, giving chat messages updates across all devices in real-time and coordinating the budget updates. The backend was implemented using Node.js, Express, and TypeScript to help manage users, budgets, and interactions with AI. In order to facilitate communication with Visa's API, we created a dedicated Python FastAPI microservice and managed the asynchronous communication with the Visa API using aiohttp. We made use of Pydantic for strict data validation. We also integrated JanitorAI as Kasha's conversational intelligence, which can accommodate large context windows with up to 25,000 tokens to hold meaningful and coherent conversations over time. Challenges we ran into Building a real-time AI financial advisor that integrates multiple APIs in a short timeframe presented several challenges. One of the biggest issues was managing cross-origin resource sharing and proxy configurations between the Vite, Express, and FastAPI servers. We also had to navigate Visa API rate limits, which we overcame through caching and batch request strategies. Handling large AI context sizes efficiently required developing dynamic memory trimming systems, and synchronizing real-time financial and chat data across users tested our event architecture. Time was another major constraint, as integrating five Visa APIs and a conversational AI system under hackathon conditions demanded precise coordination and rapid iteration. Accomplishments that we're proud of Despite these challenges, we are proud to have built a fully functional and engaging experience for students that combines finance with social interaction. We implemented a real-time multiplayer chat system where students can discuss budgets while receiving AI-driven financial insights. We successfully integrated five Visa APIs into a unified experience and created eight distinct AI personalities that offer different tones of financial advice. We also designed a smart transaction synchronization system that prevents duplicate imports, keeping budgets accurate and up to date. Above all, we built a product that makes financial management feel approachable, supportive, and collaborative. What we learned As we made Kasha, we learned how to use multiple technical domains and disciplines. We learned how to connect Node.js and Python for backend messaging, use Visa's developer platform to incorporate real transactions and merchant data, and create AI personalities that respond to different emotional tones. We learned how to create event-driven architecture with Socket.io, and how to mix technical complexity with user empathy in financial design. Most importantly, we learned that students are more engaged with financial tools that feel personal and conversational. What's next for Kasha We want Kasha to develop into something bigger than a hackathon project; the next steps we would like to take are accessibility, education & scale. We hope to launch campus pilot programs in partnership with universities to allow students to track their spending and build financial literacy. The long-term vision for Kasha is to incorporate educational content regarding saving, investing, and responsible spending right within the platform, which will be a possibility if Kasha ever becomes a popular target for student engagement on campus. Scaling Kasha's API support to include even more banks and payment providers could open access to thousands of colleges and universities. We also want Kasha to innovate upon even gamified ways to help students budget, possibly looking at savings challenges or peer competitions that add interactivity and fun to the budgeting process. Finally, to reach even more students, we are launching a mobile version of Kasha specifically for students who are always on the go, plus a direct phone-based Kasha Agent that can join group chats directly (or without), allowing students real-time financial insights and support via text (or calls) when they are looking for help. <div