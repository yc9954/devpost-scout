---
slug: "topdown-tank-online"
url: "https://devpost.com/software/topdown-tank-online"
title: "Vulkan Tank Online"
hackathon: "ConUHacks X"
organization: "HackConcordia"
winner: true
words: 259
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Vulkan Tank Online

> An online PvP game powered by Vulkan and GameNetworkingSockets using C++

[Devpost](https://devpost.com/software/topdown-tank-online) · hackathon [[ConUHacks X]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[geospatial]] [[video_visual]]

**stack** c, c++, gamenetworkingsockets, vulkan

## How they structured the write-up

- inspiration
- how we built it
- challenges we faced & what we learned
- accomplishments that we're proud of
- what we learned

## Body

Inspiration We were inspired by Call of Duty and Battefield. Also we didn't want to use a game engine, so we went for Vulkan instead, the successor of OpenGL. How We Built It We started with a C++ Vulkan code template from vkguide.dev and used Valve's GameNetworkingSockets for multiplayer functionality. It features: Tank animation Shadow mapping OBJ model loading via Assimp Phong shading Simple camera controls Cross-platform build with CMake Projectile shooting Multiplayer over LAN or internet Networking: Simple multiplayer system using host/join methods, NetPlayer state synchronization via unreliable messages, connection callbacks for player lifecycle management, and VulkanEngine integration that sends local camera data and updates remote player positions every few frames. Challenges We Faced & What We Learned This project taught us network programming and cross-platform development, along with graphics programming. Vulkan is notorious for its difficulty. Network Challenges: Moving from localhost to LAN revealed major connectivity issues. Windows Defender and macOS firewalls blocked connections, requiring custom firewall rules. The WiFi networks at the hackathon used AP/Client Isolation, so we used ZeroTier. Build Issues: Compiler variations and 32/64-bit compatibility created cross-platform headaches, highlighting the value of package managers like vcpkg. Accomplishments that we're proud of We're proud of achieving real-time multiplayer in a Vulkan graphics demo within a hackathon timeframe. We successfully integrated GameNetworkingSockets, built client/server architecture, and synchronized player control across Windows and macOS despite networking hurdles. What we learned Our hardest problems weren't code related but involved real-world networking: firewalls, AP Isolation, and subnet configuration. We learned that servers must explicitly listen and accept connections. <div