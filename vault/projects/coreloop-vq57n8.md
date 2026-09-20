---
slug: "coreloop-vq57n8"
url: "https://devpost.com/software/coreloop-vq57n8"
title: "CareLoop"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 455
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
---

# CareLoop

> Turning Proof of Work, into Proof of Good. Building a blockchain-based system that lets community volunteerism earn Moneta tokens.

[Devpost](https://devpost.com/software/coreloop-vq57n8) · hackathon [[Frostbyte Hackathon]]

## Facets

  <sub>weak: provenance_signing, realtime_stream</sub>
  <sub>weak: education, labor_employment</sub>
  <sub>weak: educator_student</sub>
**substrate** [[geospatial]]
  <sub>weak: structured_db, video_visual</sub>

**stack** flutter, flutter-map, openstreetmap, polygon, postgresql, supabase, web3dart

## Body

Inspiration The thought behind CareLoop came from something very common around us. Students regularly take part in activities like cleanliness drives, plantation events, or donation camps. After the event ends, the effort is usually recorded on paper or through a basic form, and later there’s no clear way to show where or how someone contributed. For a generation that tracks everything digitally, this felt disconnected. There was no transparency, no motivation, and no proper recognition. That’s when we started thinking about building a system where social work is recorded properly and participation actually feels rewarding, without changing the core purpose of helping people. What it does CareLoop connects volunteers, organizers, and proof of participation in one place. Event browsing: People can locate nearby social activities through a live map interface. Participation validation: To stop fake entries, we introduced a two-step check: Location-based presence to confirm physical attendance A secure QR scan for both entry and exit Recognition system: After confirmation, organizers issue Moneta (MON) tokens using the Polygon blockchain, creating a permanent and tamper-proof record of contribution. How I built it The development focused on practicality and scalability: User interface: Flutter was used to ensure smooth performance on Android and iOS. Server side: Supabase handled authentication and real-time data storage, while PostgreSQL Row Level Security ensured controlled access. Web3 layer: Smart contract interaction was implemented using Web3Dart on the Polygon network. Mapping system: OpenStreetMap with flutter_map replaced paid APIs, keeping the project lightweight and open-source friendly. Challenges I ran into Paid map limitations: Early versions relied on Google Maps, but billing restrictions forced a complete shift. Reworking the navigation system using OpenStreetMap during the hackathon was challenging but improved performance. Access control issues: A major issue prevented users from marking completion. The root cause was incorrect RLS rules — records could be created but not modified. Custom SQL policies solved this. Android build conflicts: Camera and QR libraries caused dependency clashes, which required manual Gradle configuration and enabling MultiDex. Accomplishments that I'm proud of Hidden blockchain complexity: Users interact with a simple reward screen without dealing with gas fees or wallet setups. Open-source mapping decision: Removing paid services reduced cost and improved long-term sustainability. Dual-use QR logic: A single scan handling both start and end states was implemented efficiently. What I learned Database logic is powerful: Moving critical rules to the backend increases reliability. Ease of use matters: Reducing user interaction with blockchain steps greatly improves adoption. Version control discipline: Proper handling of environment files and assets avoids team conflicts. What's next for CoreLoop Digital impact certificates: Converting rewards into soulbound credentials usable for resumes. Activity rankings: Public scoreboards to highlight consistent contributors. Sponsored participation: Allowing organisations to fund incentives and support community work. <div