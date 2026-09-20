---
slug: "monet-we062k"
url: "https://devpost.com/software/monet-we062k"
title: "monet"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 566
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "substrate/web_dom"
---

# monet

> Monet embeds an invisible cryptographic fingerprint into creative files. If your work is stolen online, our Gemini-powered forensic engine proves authorship instantly, in plain language.

[Devpost](https://devpost.com/software/monet-we062k) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[provenance_signing]] [[retrieval_grounding]]
**domain** [[developer_tools]]
**substrate** [[web_dom]]

**stack** fastapi, firebase-authentication, gemini, geminiapi, google, react, tailwindcss, typescript

## How they structured the write-up

- inspiration
- chosen theme:
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for monet

## Body

Inspiration The creator economy is built on trust — trust that original work is recognized, attributed, and protected. Yet the infrastructure for proving digital authorship has remained largely inaccessible to independent creators. Enterprise-grade solutions like Digimarc exist, but they are priced for institutions, not individuals. We built Monet to close that gap: a provenance layer that any creator can use before they hit publish. Chosen Theme: Cybersecurity & Privacy – Build tools to protect data, secure applications, or prevent digital threats. Artificial Intelligence & Machine Learning – Build AI-driven solutions, predictive models, or intelligent automation tools. Data Analytics & Big Data – Analyze datasets to generate insights, improve decision-making, or visualize information creatively. What it does Monet protects creative files by embedding an invisible cryptographic fingerprint into their binary data before they are shared online. If a protected work is later found elsewhere — cropped, re-encoded, or redistributed without permission — Monet can verify its origin. Upload the file, and a Gemini-powered forensic engine returns a plain-language report detailing authorship certainty and content integrity, scored independently so that even subtle modifications are surfaced. How we built it The watermarking pipeline runs entirely client-side using the Web Crypto API. A SHA-256 hash of the raw media bytes is computed at protection time and embedded alongside a lightweight signature into the file's binary tail. At verification, the payload is extracted, the hash is recomputed against the isolated media content, and both values are compared to produce two independent scores: signature validity and integrity match. Gemini 2.0 Flash, called via the @google/genai SDK, then translates the numeric results into a concise forensic summary. The frontend is React + TypeScript built with Vite, and authentication is handled through Firebase. Challenges we ran into Designing a byte-level watermark that survives common file operations without corrupting the media required careful boundary parsing. Searching for payload markers from the end of the file — rather than the beginning — was critical to avoid collisions with media-specific headers. Prompt engineering for the Gemini report also proved non-trivial: the model needed to reliably distinguish between scenarios such as a valid signature paired with low integrity (derivative work) versus an invalid signature (forgery), and communicate those distinctions without technical jargon. Accomplishments that we're proud of The core protection and verification pipeline works end-to-end in the browser with zero server dependency. The forensic report produced by Gemini is consistently readable by non-technical users while remaining accurate to the underlying cryptographic evidence. The scoring system — two independent axes of signature and integrity — provides more expressive provenance data than a simple pass/fail verdict. What we learned Meaningful AI integration is not about volume of model calls — it is about placement. Gemini earns its role in Monet not by performing the forensics, but by interpreting them for the people who matter most: creators who should not need a computer science degree to understand whether their work has been stolen. What's next for Monet The immediate roadmap centers on active monitoring. Rather than requiring creators to manually upload suspected copies, a Gemini Vision-powered URL scanner will allow Monet to analyze any webpage and flag visual matches against a creator's protected portfolio — even after compression, cropping, or color grading. A Cloud Run backend will move the watermarking pipeline server-side, enabling a forensic API, automated DMCA filing workflows, and a Studio tier for teams managing large asset libraries. <div