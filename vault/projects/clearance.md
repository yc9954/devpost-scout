---
slug: "clearance"
url: "https://devpost.com/software/clearance"
title: "Clearance"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 955
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/disaster_emergency"
  - "user/general_public"
  - "user/government_staff"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Clearance

> AI-powered body camera intelligence that sees threats in real-time, calls for backup hands-free, stores evidence on-chain, and writes the report—so officers protect communities, not paperwork.

[Devpost](https://devpost.com/software/clearance) · hackathon [[NexHacks]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]]
**domain** [[disaster_emergency]]
**user** [[general_public]] [[government_staff]] [[researcher]]
**substrate** [[document_pdf]] [[financial_record]] [[transcript_audio]] [[video_visual]]

**stack** arize-phoenix, deepgram, fastapi, gemini-2.0-flash, ipfs, javascript, livekit, next.js, overshoot-api, python, solana, supabase, tailwind-css, typescript

## How they structured the write-up

- ✧ about the project
- ✧ inspiration
- ✧ what we built
- ✧ system architecture
- ✧ real-time streaming infrastructure
- ✧ live event streaming interface
- ✧ automated ems and backup dispatch
- ✧ ai-generated documentation
- ✧ evidence integrity and verification
- ✧ lessons learned
- ✧ challenges
- ✧ why it matters

## Body

✧ Clearance ✧ A Tamper-Evident, Real-Time Body Camera Intelligence System ✧ About the Project Clearance is a real-time body camera intelligence and verification system designed to increase transparency in policing while actively supporting officers in the field . The system combines live video and audio analysis, automated emergency response, AI-assisted documentation, and cryptographic evidence integrity into a single, continuous workflow. Rather than analyzing footage only after an incident, Clearance is built to: understand events as they happen respond when seconds matter generate records that can be independently verified ✧ Inspiration Modern policing relies heavily on body cameras, yet much of their potential remains unrealized. Officers are often required to review hours of footage after the fact, complete reports long after incidents occur, and depend on systems that provide limited guarantees against tampering. Meanwhile, critical events such as gunfire or medical emergencies demand immediate action. We were driven by a simple question: What if body camera footage could document itself, summon help automatically, and prove its own authenticity? Clearance was designed to serve both sides of accountability: the public’s need for transparency officers’ need for speed, accuracy, and operational support ✧ What We Built Clearance consists of four tightly integrated capabilities: Real-time video labeling and action recognition AI-based gunshot and taser detection with automatic EMS dispatch Automated generation of structured police reports Tamper-evident evidence verification using cryptographic receipts Together, these components form a single end-to-end workflow from live incident to verified record. ✧ System Architecture ✧ Real-Time Video Understanding Body camera footage is processed continuously as it streams. Video frames are sampled at fixed intervals and analyzed by a constrained vision model that reports only critical policing events , such as: weapons visible physical altercations individuals on the ground All outputs are intentionally constrained to be: concise and factual written in third person timestamped and limited in length This ensures results resemble incident logs rather than narrative summaries. ✧ Parallel Audio Intelligence Audio is analyzed simultaneously using a real-time gunshot and taser detection pipeline. This layer is essential because critical events often occur off-camera or during rapid motion. Detection uses a hybrid approach: machine-learned classification signal-level constraints on amplitude, frequency, and timing A sound must satisfy multiple conditions before being classified as a gunshot, significantly reducing false positives while remaining fast enough for real-time response. ✧ Real-Time Streaming Infrastructure Clearance uses LiveKit as its real-time media backbone. LiveKit provides low-latency, encrypted transport for live video and audio streams while allowing multiple AI systems and dashboards to consume the same media in parallel. This separation between media transport and intelligence enables real-time analysis without compromising reliability or security. ✧ Role of LiveKit in Clearance LiveKit is responsible for: streaming live body camera video and audio fan-out of media streams to multiple AI pipelines synchronization of video, audio, and detected events secure isolation of sessions per incident maintaining stream continuity even when AI services fail ✧ High-Level Flow Body Camera or Mobile Device Publishes video and audio tracks via WebRTC Adaptive bitrate ensures stable streaming LiveKit SFU Receives encrypted media Distributes streams to multiple subscribers AI Subscribers Vision pipeline samples frames for event detection Audio pipeline analyzes short windows for gunshots or tasers UI pipeline renders live footage Event Layer AI detections are timestamped using media timing Events stream back to the interface in sync with playback ✧ Security Model Each incident runs in its own isolated room Officers publish using short-lived, scoped access tokens Supervisors and analysts join as read-only subscribers All media transport is encrypted No peer-to-peer exposure exists between clients. ✧ Live Event Streaming Interface Detected events appear in real time and align precisely with video playback. Events are grouped into clearly defined tiers: Critical : shots fired, person down Warning : weapon drawn or visible Audio : gunshot or taser detection Scene : environmental context Transcript : speech recognition This creates a synchronized timeline where video, audio, and AI interpretation remain aligned. ✧ Automated EMS and Backup Dispatch When gunshots are detected with sufficient confidence, Clearance can automatically initiate phone calls to EMS or backup units. This removes the need for officers to manually place emergency calls during high-stress situations and ensures medical response begins as early as possible. Safeguards such as confidence thresholds and cooldown periods prevent duplicate or unnecessary calls. ✧ AI-Generated Documentation Clearance generates a structured police report draft using detected events, timestamps, and scene context. The workflow ensures that: all content is clearly labeled as AI-generated officers review and approve all reports no report is finalized without human confirmation This reduces administrative burden while preserving accountability. ✧ Evidence Integrity and Verification For each recording, Clearance generates a cryptographic evidence receipt: The video is hashed using SHA-256 The file is stored using content-addressed storage Hashes and metadata are anchored immutably A verification receipt is generated Any alteration to the footage changes the hash and invalidates the receipt. Evidence integrity becomes mathematically provable. ✧ Lessons Learned Real-time insight often matters more than delayed perfection Strict output constraints improve reliability Audio analysis is essential for off-camera events Trust must be technical, not purely institutional ✧ Challenges Real-Time Performance Balancing inference speed, cost, and accuracy required careful optimization. False Positives Environmental noise made gunshot detection challenging, requiring hybrid logic. Streaming Reliability Unstable real-time AI services necessitated a modular, fault-tolerant design. Ethical Design Privacy, minimal data retention, and officer control were treated as first-class constraints. ✧ Why It Matters Clearance is not designed to replace officers or automate judgment. It exists to: reduce administrative burden improve emergency response times increase public trust produce evidence that can be independently verified By combining real-time intelligence, automated response, structured documentation, and cryptographic proof, Clearance demonstrates how technology can strengthen accountability while preserving human decision-making. ✧ ✧ ✧ <div