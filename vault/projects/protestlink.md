---
slug: "protestlink"
url: "https://devpost.com/software/protestlink"
title: "ProtestLink"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 1198
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/security_privacy"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
---

# ProtestLink

> Secure, real-time protest coordination via encrypted mesh and AI insights

[Devpost](https://devpost.com/software/protestlink) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[privacy_tech]] [[provenance_signing]] [[realtime_stream]] [[voice_speech]]
**domain** [[civic_government]] [[developer_tools]] [[disaster_emergency]] [[security_privacy]]
**substrate** [[code_repository]] [[geospatial]] [[transcript_audio]]

**stack** axios, bluetooth, esp32, flask, leaflet.js, numpy, openai, openstreetmap, python, react, sentence-transformers, sqlite, stadia, tailwindcss

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for protestlink

## Body

Inspiration In times of social unrest, the ability to communicate is as vital as the cause itself. Protesters across the world face increasing challenges when it comes to coordination, safety, and information sharing. Governments have been known to shut down cellular networks, limit internet access, or monitor online communication, making it difficult for protesters to organize effectively. Even when networks remain online, they often become overloaded, rendering them useless at critical moments. Protesters struggle with locating medical aid, distributing supplies, and avoiding high-risk areas where clashes may occur. Beyond digital suppression, protesters also struggle with navigating volatile environments, distributing supplies efficiently, and requesting medical assistance when situations escalate. How can protesters stay connected and informed when traditional communication systems fail? That was the problem we set out to solve. We asked ourselves: How can we create a communication system that is secure, decentralized, and resilient enough to function even under extreme restrictions? With this goal in mind, we built ProtestLink, a Wi-Fi mesh-based protest coordination tool that provides secure messaging, real-time resource allocation, and risk assessment without relying on internet access or centralized servers. ProtestLink ensures that protesters stay connected, protected, and prepared, even when traditional communication methods fail. What it does ProtestLink is a decentralized communication and coordination platform designed to keep protesters connected, informed, and protected even in the face of network disruptions, internet blackouts, and active surveillance. By leveraging Wi-Fi networking, live location sharing, and AI-driven speech analysis, ProtestLink provides an autonomous protest network that helps protesters navigate safely, request critical resources, and broadcast urgent alerts without relying on traditional service providers. With ProtestLink, protesters can: Share real-time location data with organizers and trusted participants to create an interactive protester map for coordination and safety tracking. Identify and avoid high-risk areas through real-time protest heatmaps that visualize areas of tension and clashes. Indicate an emergency alert status to notify others if they are in danger, being arrested, in need of medical aid, or require supplies. Broadcast emergency alerts to organizers and trusted participants. Automatically transcribe and analyze protest audio using Whisper AI, detecting keywords, sentiment, and potential escalation zones in real-time. Ensure trust-based access with a zero-trust authentication model, where protesters join securely via QR code, eliminating the need for personal data like phone numbers. How we built it At the core of ProtestLink is a self-hosted web server that facilitates location sharing, encrypted communication, and live protest heatmaps. We built a custom Wi-Fi network to allow devices to connect and interact without relying on traditional cellular infrastructure. Protesters can open the web app, share their live location, and send alerts—all without requiring a constant internet connection. To enhance real-time protest intelligence, we integrated Whisper AI, an edge-based transcription and NLP system capable of converting live protest audio into actionable data. This means that if a protester yells for help, reports police movement, or requests medical assistance, the system can analyze and categorize the request, ensuring it reaches organizers or other protest members in real time. We also used sentiment analysis to detect potential conflict zones, allowing ProtestLink to generate a live map of risk areas. The protester map is powered by WebSockets and real-time geolocation tracking, ensuring fluid updates without relying on centralized data sources. Protesters can pin their locations on the map, mark areas as safe or dangerous, and request water, medical aid, or evacuation support—creating a distributed protest intelligence network that operates independently of government-controlled systems. Security was a critical concern throughout development. We implemented end-to-end encryption to ensure that messages, locations, and alerts remain private and tamper-proof. The zero-trust authentication model allows protesters to join the network anonymously via QR codes, eliminating the need for phone numbers, email, or personal data. This ensures that no centralized entity can track or compromise protesters through ProtestLink. By combining Wi-Fi-based communication, AI-powered speech processing, and encrypted location sharing, we created a robust and decentralized coordination system that empowers protesters to act swiftly, securely, and strategically. Challenges we ran into One of the biggest technical challenges we faced was working with Bluetooth on iOS. Initially, we planned to leverage Bluetooth mesh networking for decentralized communication, but Apple's restrictive CoreBluetooth API made this extremely difficult to implement. Unlike Android, which offers flexible background BLE (Bluetooth Low Energy) support, iOS heavily limits background Bluetooth communication, making it nearly impossible to maintain persistent message relays between devices. After multiple failed optimizations, we ultimately pivoted to Wi-Fi-based networking, which provided greater reliability, better message throughput, and cross-platform compatibility. Navigating Apple’s strict development ecosystem also posed a challenge. Integrating Swift-based networking protocols with React Native required bridging complex native APIs while ensuring that location tracking and WebSockets functioned reliably across both iOS and Android. Debugging Bluetooth issues in Apple’s sandboxed environment further complicated development, as maintaining persistent connections in the background was heavily restricted. Despite these challenges, we successfully transitioned to a more scalable Wi-Fi-based approach, built a real-time protest tracking map, and integrated speech recognition AI into an autonomous protest coordination system. These obstacles forced us to rethink our architecture, leading to a more powerful and adaptable solution. Accomplishments that we're proud of Building ProtestLink required pushing beyond conventional networking and security models, and we are incredibly proud of what we accomplished. One of our biggest milestones was successfully implementing a live protester map that provides real-time protest intelligence without relying on external services. The ability to share live locations, report threats, and visualize protest dynamics makes ProtestLink a game-changer for secure protest coordination. We are also proud of integrating Whisper AI’s real-time transcription engine, which allows ProtestLink to analyze protest audio, detect emergency phrases, and generate dynamic risk assessments. Protesters can now transmit critical alerts without needing to type, ensuring faster responses in high-risk situations. Additionally, we successfully implemented a zero-trust authentication system, ensuring that protesters can join securely and anonymously without exposing personal information or metadata. By making ProtestLink fully decentralized and resistant to surveillance, we created a communication tool that protesters can truly rely on. What we learned This project reinforced just how fragile centralized communication systems can be in times of crisis. Governments actively shut down networks, throttle internet speeds, and exploit surveillance laws to suppress protests. ProtestLink has shown us that truly decentralized, peer-to-peer communication is not just a convenience—it’s a necessity. We also gained extensive experience in Wi-Fi networking, encrypted communication protocols, and real-time AI processing on edge devices. Working with Whisper AI and NLP-driven event detection expanded our knowledge of how machine learning can be used to enhance real-world safety. Most importantly, we learned that technology has the power to protect human rights. ProtestLink is more than just an app—it’s a lifeline for those who need a secure way to communicate, mobilize, and protect themselves in uncertain times. What's next for ProtestLink ProtestLink has the potential to redefine protest communication, and we’re excited to take it even further: Enhancing AI-driven risk detection to provide smarter, more responsive alerts. Expanding to more languages for global accessibility. Exploring LoRa-based long-range communication to expand mesh connectivity even further. ProtestLink isn’t just a project—it’s a movement. We’re committed to building censorship-resistant, decentralized technology that empowers people to speak, organize, and protect their rights—no matter what. <div