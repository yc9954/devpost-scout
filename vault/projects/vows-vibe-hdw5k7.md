---
slug: "vows-vibe-hdw5k7"
url: "https://devpost.com/software/vows-vibe-hdw5k7"
title: "VOWS&VIBE"
hackathon: "DevNetwork [API + Cloud + AI] Hackathon 2026"
organization: "DevNetwork"
winner: true
words: 384
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/retail_commerce"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# VOWS&VIBE

> Vows & Vibe is a collaborative bridal styling app with AI try-on, personal color guidance, shared feedback, and group previews so every look works beautifully together

[Devpost](https://devpost.com/software/vows-vibe-hdw5k7) · hackathon [[DevNetwork -API - Cloud - AI- Hackathon 2026]]

## Facets

**domain** [[retail_commerce]]
**substrate** [[code_repository]] [[video_visual]]

**stack** fabric.js, next.js, node.js, react-native, supabase, youcamapi

## How they structured the write-up

- inspiration
- what it does
- what's next for vows&vibe

## Body

Inspiration Bridal-party styling is often fragmented across group chats, screenshots, shopping links, and individual decisions. Bridesmaids may choose dresses that look good individually but clash with the wedding palette or with each other, while the bride has no easy way to visualize the full group before everyone commits. Traditional online shopping also focuses on one person at a time. It does not help the bridal party answer questions like: How will this dress look on me? Does this shade work with the wedding palette? How will the whole bridal party look together? Can we coordinate and give feedback without endless group chats? What it does Vows & Vibe brings the entire bridal-party styling process into one collaborative workspace. Virtual Try-On: Users upload a full-body photo for dress visualization using Perfect Corp's Clothes Virtual Try-On API. VTO attempts are stored through the vto_attempts model so users can revisit previous renders without losing progress. Personal Color Guidance: YouCam Skin Tone Analysis provides representative skin and available hair-color HEX values. These colors are converted into CIE Lab and compared with the selected dress using undertone relationship, skin-to-dress lightness contrast, and color intensity to produce an advisory compatibility score and explanation. Compose Studio: Dresses and participants are organized into Palette Match , Family Match , and Other using broad color-family logic and perceptual color comparison with CIEDE2000. Exact palette matches always take priority. Shared Bridal Lineup: Confirmed looks appear together in an interactive 2D studio, allowing the bride to arrange and evaluate the full bridal party visually. Collaborative Suggestions: Participants can give styling feedback directly within the shared experience instead of relying on separate group chats. AI Group Preview: The bride can generate a more natural group preview using the selected venue and confirmed looks. One Shared Source of Truth: Everyone can view the latest lineup saved by the bride, revisit their choices, update their look, and stay coordinated around the same event. What's next for VOWS&VIBE Mobile App: Bring the collaborative styling experience to iOS and Android with a mobile-first interface. Broader Wedding Styling: Expand beyond bridesmaids to couples, groomsmen, family, and other wedding-party members. More Occasion Types: Extend the same coordination workflow to prom, formal events, and other group occasions. Smarter Group Styling: Improve AI group previews, color coordination, and personalized recommendations using real-world feedback. <div