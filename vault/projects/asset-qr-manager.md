---
slug: "asset-qr-manager"
url: "https://devpost.com/software/asset-qr-manager"
title: "Asset QR Manager"
hackathon: "Codegeist 2025: Atlassian Williams Racing Edition"
organization: "Atlassian"
winner: true
words: 334
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/video_visual"
---

# Asset QR Manager

> Asset QR Manager bridges physical items & Jira Assets. Generate QR labels to auto-update metadata via Smart Modes. Eliminate manual entry & keep records accurate with a single scan! Scan & Sync.

[Devpost](https://devpost.com/software/asset-qr-manager) · hackathon [[Codegeist 2025- Atlassian Williams Racing Edition]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[video_visual]]

**stack** atlassiancloud, atlassianforge, forge, forgebridge, javascript, jira, jiraassets, materialui, react, react-qr-code, react-qr-reader, restapi, storageapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for asset qr manager

## Body

This image shows user filling the form to generate QR code and download the QR code. This image shows QR code download preview. This Image shows user scanning the QR code and the details reflecting in real time. This image shows the QR code scan history, where user can view updated logs. This image shows user adding attributes to the created mode. Inspiration Asset management workflows often rely on QR codes only for identification, while asset updates are still handled manually. This gap between physical asset interaction and digital data accuracy inspired us to build Asset QR Manager , where every scan meaningfully updates asset information. What it does Asset QR Manager allows users to generate, print, and scan QR codes for Jira Assets. On scanning, it automatically updates configured asset fields such as scan date or user information and maintains a complete scan history for traceability. How we built it We built the application using Atlassian Forge and Jira Assets APIs, with a React + Material UI frontend. QR generation and scanning were implemented using QR libraries, and a configurable Mode-based system was introduced to control which asset fields are updated during scans. Challenges we ran into Key challenges included validating asset field configurations, handling unsupported attribute types, preventing incorrect updates, and ensuring reliable camera access across browsers. Designing a flexible yet safe configuration model was also a major challenge. Accomplishments that we're proud of Introduced Mode-based configuration for controlled asset updates Ensured safe updates with strict field and type validation Enabled real-time asset updates through QR scanning Built a clean, user-friendly configuration and scanning experience What we learned We gained hands-on experience with Atlassian Forge, Jira Assets data modeling, and building configuration-driven automation. The project also strengthened our understanding of UX design for admin tools and data safety in enterprise applications. What's next for Asset QR Manager Future plans include supporting additional field types, role-based Mode access, enhanced audit reports, bulk scan analytics, and deeper integrations with Jira Service Management workflows. <div