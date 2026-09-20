---
slug: "meshnet"
url: "https://devpost.com/software/meshnet"
title: "MeshMap"
hackathon: "UNIHACK 2026, funded by the European Union"
organization: "UNIHACK"
winner: true
words: 1136
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/security_privacy"
  - "user/frontline_worker"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# MeshMap

> network to relay messages and crisis alerting without wifi through BLE

[Devpost](https://devpost.com/software/meshnet) · hackathon [[UNIHACK 2026- funded by the European Union]]

## Facets

**mechanism** [[simulation_digital_twin]] [[voice_speech]]
  <sub>weak: on_device_local, vision_ocr</sub>
**domain** [[developer_tools]] [[disaster_emergency]] [[security_privacy]]
  <sub>weak: health_clinical</sub>
**user** [[frontline_worker]] [[patient_family]]
**substrate** [[code_repository]] [[geospatial]] [[video_visual]]

**stack** claude, corebluetooth, cryptography, gradle, junit, kotlin, next.js, supabase, swift, twilio

## How they structured the write-up

- mesh network group communication
- map-based event sharing
- news platform interoperability
- direct messaging and contacts
- language support and accessibility
- ios and android support
- emergency alert system
- offline distribution
- bluetooth low energy networking
- encrypted messaging
- image transfer
- alerts map
- web of trust
- news platform
- sos messaging
- ios
- android
- web server (news network + sos)

## Body

IOS Chat IOS Dark mode chat IOS Map Page with filtering IOS SOS Warning IOS Contacts IOS Account Page IOS Alert Details News Home Page News Platform Article Android Map Android event alert Android chat Alerting Police Inspiration The primary inspiration for our project comes from the Iran internet blackout crisis, where for nearly two weeks authorities blocked most civilian internet access, reducing connectivity to around 1% of normal levels. According to Human Rights Watch, the shutdown was intended to conceal massacres and human rights violations occurring during the unrest. In situations like these, the ability to contact medical help, locate family members, or avoid danger zones can mean the difference between life and death. Our application aims to serve as a communication bridge during infrastructure failures, allowing people to communicate locally through a mesh network even when traditional internet access is unavailable. Nodes within the network that still have internet connectivity can also relay SOS messages or share information externally, helping connect affected civilians with emergency services or the outside world. Centralized communication infrastructure is vulnerable to both intentional shutdowns and accidental outages. Our app provides a decentralized communication alternative designed for emergency resilience. At its core, the project supports the fundamental right to communicate, using technology to promote human rights, democratic access to information, and infrastructure resilience. What We Built We built a mobile application that enables local communication without internet access. Using Bluetooth Low Energy (BLE), devices form a peer-to-peer mesh network that supports messaging and map-based event sharing. BLE allows direct communication between nearby devices at distances of roughly 100 meters. By forwarding messages across multiple nodes (up to seven hops), the network can achieve a communication radius of approximately 700 meters. For context, Tehran, the capital of Iran, has a population density exceeding 12,000 people per square kilometer. This corresponds to an average spacing of roughly 8 meters between individuals. This density makes BLE-based peer-to-peer connectivity a viable communication method even when most devices lack internet access. Features Mesh Network Group Communication Users communicate through nearby nodes in a decentralized mesh network, participating in a shared public group chat without relying on a centralized server. Image sharing is also supported. Map-Based Event Sharing Users can post local events, updates, and photos through a map interface. These posts propagate through the mesh network to nearby devices, providing situational awareness during emergencies. News Platform Interoperability Devices with internet connectivity can share collected map data externally or upload it to a public news platform, allowing first responders and family members outside the affected area to gain visibility into local conditions. Direct Messaging and Contacts Users maintain contact lists and can send direct encrypted messages through intermediate mesh nodes. Direct messages are encrypted using: X25519 ECDH HKDF-SHA256 AES-GCM Language Support and Accessibility The application includes: Multiple language options Accessibility features such as large text and text-to-speech iOS and Android Support Complementary applications are available for both iOS and Android, with cross-platform communication compatibility. Emergency Alert System A built-in SOS feature allows users to quickly alert authorities or nearby nodes about emergency situations. The system broadcasts location coordinates and emergency status across the mesh. Offline Distribution Android users are able to distribute this app offline using Bluetooth file transfers. How We Built It + Tech Stack This project required working across the Network Layer, Transport Layer, and Application Layer of the internet stack. A more detailed technical whitepaper is available in our GitHub repository. Bluetooth Low Energy Networking The mesh network uses dual-role CoreBluetooth, where each device simultaneously advertises and scans for nearby peers. Key components: GATT Service: 6E400001-B5A3-F393-E0A9-E50E24DCCA9E Characteristic: 6E400002-B5A3-F393-E0A9-E50E24DCCA9E Peers connect, subscribe to notifications, and relay mesh envelopes using write and notify operations. Additional optimizations include: TTL-based message propagation Duplicate message filtering Cycled scanning windows to balance discovery and power consumption Message size capped at 512 bytes for BLE MTU limits Encrypted Messaging Each device generates a persistent identity using Ed25519-style keys stored in the Keychain. Encryption flow for direct messages: X25519 ECDH → HKDF-SHA256 → AES-GCM Additional authenticated data includes: sender ID recipient ID timestamp Image Transfer Images are optimized for mesh transmission: resized to a maximum of 320px compressed to ≤12 KB Images are split into fixed-size chunks to comply with the 512-byte envelope limit. Each chunk contains: transferId chunkIndex totalChunks data Receivers reassemble the chunks using transferId and display the reconstructed image. Alerts Map The map system supports geographic event markers such as: hazards help requests emergencies custom alerts Each label includes: latitude longitude category optional name, description, or icon Events are displayed on a MapKit interface within a 5 km radius. Web of Trust Alert reliability is evaluated using a trust scoring system based on: author credibility vouch confirmations or denials relationship status (friend / associate / stranger) physical proximity (GPS / RSSI) time decay (2-hour half-life) Events are clustered by: distance: 500 meters time: 15 minutes Users vote on alerts through VouchPayload messages propagated across the mesh. News Platform When connected to Wi-Fi, users can upload collected map data to the MeshNews platform. The web server aggregates events and generates structured news reports using an LLM with contextual information from the mesh network. SOS Messaging The SOS system allows users to broadcast emergency alerts. When triggered: A map label is created at the user's location. The SOS event is broadcast across the mesh network. The signal is rebroadcast after 0.3 seconds to improve propagation. Nearby devices receive a time-sensitive notification. Each user may maintain one active SOS at a time. Technology Stack iOS Swift GRDB CoreBluetooth Android Kotlin Gradle Android SDK JUnit (CI/CD) Web Server (News Network + SOS) Next.js Supabase Claude API Twilio Challenges We Faced Integrating a BLE-based mesh network for sharing events and map data was challenging because there were few existing examples implementing similar functionality. Key challenges included: maintaining synchronized state across devices without a central server handling packet loss and partial transmissions implementing reliable image transfer over BLE testing multi-device connectivity Initially, images frequently failed to fully transmit. Implementing compression and chunking improved reliability. Testing required manually installing the app on multiple devices and physically separating them to simulate real network conditions. Additionally, the scope of the project was extremely ambitious for a single weekend, and most team members were participating in their first hackathon. What We Learned Four out of five members of our team were participating in their first hackathon, yet we successfully collaborated to build a product we are proud of. We learned that clear task delegation and modular feature ownership were essential for managing a project of this scale. The experience also gave us a deeper appreciation for the potential of mesh networks as a decentralized communication tool. Continued development of this technology could significantly improve communication access and resilience during infrastructure disruptions for vulnerable populations around the world. <div