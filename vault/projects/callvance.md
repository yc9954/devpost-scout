---
slug: "callvance"
url: "https://devpost.com/software/callvance"
title: "CallVance"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 633
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# CallVance

> CallVance automates AI-powered voice calls to confirm appointments, update statuses in real time, and reduce no-shows. Complete with dashboard, CSV upload, and call tracking.

[Devpost](https://devpost.com/software/callvance) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]]
  <sub>weak: cross_origin_web</sub>
  <sub>weak: transportation</sub>
**substrate** [[structured_db]] [[transcript_audio]]
  <sub>weak: web_dom</sub>

**stack** autoprefixer, bolt.new, date-fns, digitalocean-app-platform, dotenv, elevenlabs, fastify, fastify/cors, fastify/formbody, fastify/websocket, heroku, lucide-react, netlify, node.js

## How they structured the write-up

- inspiration
- challenge compliance
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for callvance

## Body

Inspiration The inspiration for CallVance came from a real challenge in my own business: the overwhelming time spent making manual appointment confirmation calls. With a high volume of clients, this repetitive task consumed valuable time that could otherwise be spent delivering better service. I envisioned a tool that would not only automate this task but also empower front desk staff to focus on more meaningful interactions with clients. Challenge Compliance Voice AI Challenge (ElevenLabs) Integrated ElevenLabs Conversational AI to power both inbound and outbound appointment confirmation calls. Enabled real-time voice interactions through WebSockets bridging Twilio and ElevenLabs. Implemented dynamic conversation variables , such as client name and appointment details, to personalize agent speech. Post-call analysis and transcript handling are secured via HMAC-validated webhooks . Fully aligned with ElevenLabs best practices, including custom agent setup and live audio streaming. Deploy Challenge (Netlify) The application frontend is deployed on Netlify , providing public access to all users. Real-time appointment updates are streamed through WebSocket connections to ensure live feedback. Server is hosted and exposed with HTTPS support, making it compliant with Twilio and ElevenLabs requirements for secure media and webhook handling. Startup Challenge (Supabase) Integrated Supabase to manage authentication and appointment data storage. Enabled scalable infrastructure with real-time data updates and secure access control. Backend is configured to support multi-user expansion and production-level reliability, making it startup-ready. What it does CallVance is an AI-powered appointment confirmation platform that makes natural, human-like voice calls to clients. It automatically confirms, reschedules, or logs appointment outcomes using ElevenLabs Conversational AI and Twilio, with real-time status updates delivered via WebSocket. Users can input appointments manually or upload them in bulk using a CSV file, and monitor all results from a streamlined dashboard. How we built it The project is built with a Fastify Node.js server integrated with the ElevenLabs API for voice AI and Twilio for call handling. WebSocket is used to stream audio and deliver real-time status updates to the frontend. The frontend is built with React and Tailwind CSS, allowing users to manage appointments, view call logs, and track confirmations. A CSV parser was added for bulk uploads, and webhook handling was implemented to process call results and update the UI dynamically. Challenges we ran into Integrating real-time audio streaming between Twilio and ElevenLabs was technically complex and required low-latency WebSocket bridging. HMAC signature validation and secure webhook handling also presented some challenges, especially with ensuring message integrity. Designing the system to be business-agnostic for broader demo use also required refactoring logic to support dynamic appointment data. Accomplishments that we're proud of Fully automated call flow from appointment data to client interaction and real-time status updates Seamless integration of ElevenLabs AI for natural conversations A reusable, responsive dashboard with clear visual insights and CSV export Secure, scalable backend that supports live demos and production use What we learned This project deepened my understanding of WebSocket infrastructure, AI voice call orchestration, and real-time UI synchronization. I also learned how to design APIs and services that are scalable and secure enough for public deployment. Managing Twilio call states and parsing webhook data into actionable frontend updates was especially enlightening. What's next for CallVance Next steps include adding support for inbound calls, customizable agent personalities per business, and full CRM integration. I also plan to build a self-serve onboarding flow so that any appointment-based business can start using CallVance without custom setup. Additionally, we’ll introduce automated text messaging so clients can receive appointment information and interact with a chatbot via SMS. This system will support live agent transfer , allowing the chatbot to escalate conversations to a human when needed. We're also implementing call forwarding , enabling the ElevenLabs AI agent to seamlessly transfer active calls to a front desk staff member when the situation calls for personal assistance. <div