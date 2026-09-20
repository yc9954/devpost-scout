---
slug: "safesteps-9x4o7i"
url: "https://devpost.com/software/safesteps-9x4o7i"
title: "SafeStep"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 562
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# SafeStep

> SafeStep is an AI-powered care companion designed to restore dignity and joy to the caregiver-recipient relationship.

[Devpost](https://devpost.com/software/safesteps-9x4o7i) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[elder_child_care]] [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[code_repository]] [[document_pdf]] [[geospatial]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** css, express.js, figma, firebase, gemini, google, google-maps, html, javascript, leaflet.js, lucide-react, mediapipe, node.js, opencv

## How they structured the write-up

- univabio fit
- prior work disclosure
- health impact
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- submission artifacts
- what's next

## Body

SafeStep tracking a patient taking their daily meals SafeStep tracking a patient taking medication Caregiver POV logging the patient's activity location Patient navigating through simplified AI UnivaBio fit SafeStep is an AI-powered care companion for older adults and the people who support them. It combines fall detection, daily-activity verification, navigation, reminders, and caregiver summaries in one demonstrable healthcare prototype. The product is designed to preserve independence while helping caregivers understand when support may actually be needed. SafeStep addresses a human-health problem that is both clinical and emotional. Families need earlier signals around falls, missed meals or medication, disorientation, and changes in routine, but constant manual checking can strain the relationship between a caregiver and the person receiving care. SafeStep uses AI as decision support so the technology can reduce that friction rather than add to it. Prior work disclosure SafeStep is pre-existing authorized team work created in 2026. It has eighteen indexed prior Devpost submissions and two observed awards. This UnivaBio entry reuses the existing concept, code, interface, repository, video, screenshots, and documentation. We are not claiming that these materials were created during UnivaBio. Health impact SafeStep focuses on four practical outcomes: Detect a possible fall or safety event sooner. Recognize selected daily activities such as meals and medication routines. Help an older adult navigate and receive accessible voice reminders. Give caregivers concise context without requiring constant calls or surveillance. The prototype does not replace a clinician or guarantee that every event will be detected. Its role is to organize signals, make routine care easier to understand, and support a faster human response when something looks wrong. What it does Uses computer vision for fall and activity-detection experiments. Provides simplified navigation and reminders for older adults. Lets caregivers log and review relevant activities and locations. Produces summaries that can support care conversations. Uses communications tooling for time-sensitive alerts. How we built it The interface is built with React, TypeScript, Vite, Tailwind CSS, and Lucide React. Node.js, Express, MongoDB, Firebase, and Google services support the application and data flows. Computer-vision experiments use YOLOv8, MediaPipe, OpenCV, Tesseract OCR, and Python. Twilio supports communications, while Leaflet and Google Maps support location and navigation features. Gemini is included in the project's AI tooling. Challenges we ran into Separating useful care signals from noisy or ambiguous observations. Designing safeguards without making the older adult feel constantly watched. Presenting information clearly to users with different needs and technical confidence. Connecting vision, location, reminder, and communications flows in one coherent prototype. Accomplishments that we're proud of Built a demonstrable care journey rather than an isolated AI model. Connected detection outputs to understandable caregiver actions. Designed separate caregiver and older-adult experiences around a shared care plan. Kept familiar routine moments, including meals, medication, navigation, and falls, at the center of the product. What we learned Good healthcare technology needs more than model accuracy. It needs respectful defaults, clear escalation, accessible interactions, and honest language about uncertainty. We learned to present AI observations as evidence for a human decision rather than as a diagnosis or guarantee. Submission artifacts Public repository: https://github.com/Ducksss/hack4good One-page SafeStep overview: https://raw.githubusercontent.com/Ducksss/hack4good/2fcabac2e3fb653b1ed1b061fea1ecfff82bd078/docs/hackathons/univabio/SAFESTEP-ONE-PAGER.pdf What's next Test the core care flows with more representative users and environments. Improve confidence handling and reduce false alerts. Add clearer consent, privacy, and caregiver-access controls. Make summaries easier to share with trusted family members or care professionals. Expand accessibility and multilingual voice support. <div