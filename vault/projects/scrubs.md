---
slug: "scrubs"
url: "https://devpost.com/software/scrubs"
title: "Scrubs"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 267
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/structural_withholding"
  - "mechanism/vision_ocr"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/video_visual"
---

# Scrubs

> Scrubs is an iPhone app that auto-redacts PHI — names, MRNs, faces — from healthcare photos before sharing. Fully on-device, so patient data never leaves the phone. One tap instead of one minute.

[Devpost](https://devpost.com/software/scrubs) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[on_device_local]] [[structural_withholding]] [[vision_ocr]]
**domain** [[health_clinical]]
  <sub>weak: labor_employment</sub>
**user** [[patient_family]]
  <sub>weak: clinician</sub>
**substrate** [[video_visual]]

**stack** coreml, swift, swiftui, vision

## How they structured the write-up

- features
- tech stack

## Body

Results Summary Main Screen Pre-Blurred Image After Photo Selection Post-Blurred Image About Scrubs Healthcare workers share photos constantly — a wound to consult a colleague, a chart to coordinate care, a med list to confirm a dose. Most of those photos contain protected health information that shouldn't leave the device unredacted: names on wristbands, MRNs on charts, faces in the frame. Redacting by hand is tedious and easy to skip, and the tools that do it well are stuck on desktops or behind enterprise licenses. Scrubs is an iPhone app that detects and redacts PHI in healthcare photos before they're shared. Capture or import an image, and on-device Face detection + OCR combined with a PHI classifier identifies the sensitive regions automatically — patient identifiers, dates of birth, identifiable faces — and masks them out. You get a clean, shareable version in seconds. Everything runs on the device. No patient data is uploaded, stored, or sent to a third party, which keeps Scrubs aligned with how clinicians actually need to work: fast, private, and on the phone they're already holding. Features On-device OCR to read text from healthcare photos without a network round-trip PHI detection for names, MRNs, dates of birth, addresses, and other identifiers Face redaction for incidental bystanders and identifiable patients One-tap export of the redacted image, ready to share Private by design — no uploads, no analytics on image content, no cloud storage Tech Stack SwiftUI for the iOS interface Zetic for face detection Vision for on-device OCR Zetic for PHI classification Filesystem-synced Xcode groups to keep .pbxproj conflicts low across the team <div