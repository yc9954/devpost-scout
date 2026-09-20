---
slug: "cardiolensv2"
url: "https://devpost.com/software/cardiolensv2"
title: "Cabinet Clear"
hackathon: "USAII® Global AI Hackathon 2026"
organization: "USAII"
winner: true
words: 1211
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/vision_ocr"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/clinician"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Cabinet Clear

> Cabinet Clear turns a confusing hospital discharge letter and a messy medicine cabinet into a clear, AI-verified plan of what to keep, take, or throw away.

[Devpost](https://devpost.com/software/cardiolensv2) · hackathon [[USAII- Global AI Hackathon 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[vision_ocr]]
  <sub>weak: cross_origin_web</sub>
**domain** [[health_clinical]] [[scientific_research]]
**user** [[clinician]]
**substrate** [[document_pdf]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** anthropic, bcrypt, claude-api, css3, fastapi, fpdf2, grad-cam, html5, javascript, openfda-api, pwa, python, pytorch, sqlite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for cabinet clear

## Body

overview sign-in page upload the letter a screenshot of the letter summary screen scanning medicines Results: Keep/Dispose/Unclear/Pharmacy Results: Keep/Dispose/Unclear/Pharmacy page2 warning signs and pdf generation confusion matrix Grad-CAM results Inspiration A few months ago, a routine blood test showed my blood sugar was higher than it should be. My doctor said it might just be because I'd eaten breakfast that morning, so I didn't think much of it. Then it happened again. He told me to come back the next day fasting, for a real test this time. That night was one of the worst nights of my life. I remember genuinely thinking that if I just willed my body to behave, the next test would come back normal — like discipline could undo biology overnight. I barely slept. The next morning I went through a full round of tests, and the result came back: prediabetes. Then I was handed medication, and a whole new kind of confusion started. Nobody sat down and explained what the medication actually did to my body, why this specific dose, what I was supposed to watch for, or what would happen if I missed a day. I was a stressed teenager holding a pharmacy bag, trying to piece together what I was now supposed to do for the rest of my life from a label that assumed I already knew. I remember just feeling scared and alone with it, doing my own research at midnight because nobody had translated any of it into something I could actually understand. I'm someone who can read medical terminology, who has access to research papers, who can ask an AI to explain a drug interaction. And it was still overwhelming. That made me think about my own house. I have three younger siblings, and our cabinet is genuinely full of bottles — old antibiotics from someone's ear infection two years ago, fever medicine, things prescribed for one sibling that might or might not still be relevant for another. My parents are busy and, frankly, just as confused as I was. Nobody in my family has ever sat down and sorted that cabinet properly, because nobody has the time or the medical background to do it with confidence. So this isn't a hypothetical parent I imagined for a hackathon brief. It's the cabinet in my own kitchen. That gap between what medical documentation assumes you understand and what an exhausted family actually understands in the moment is what Cabinet Clear is built to close. What it does Cabinet Clear reads a hospital discharge letter — pasted as text, uploaded as a PDF, or photographed — and turns it into a plain-language summary: diagnosis, medications, follow-up appointments, and warning signs. Then it scans photos of the user's actual medicine cabinet — the front label and the expiration date can be two separate photos that get merged into a single reading, since those details are often printed on different panels of the box — checks expiration dates, and cross-references everything against the letter. The output is a simple, actionable plan, sorted into four buckets: Keep & take as directed Dispose (expired) Unclear — ask your pharmacist Missing — pick up from the pharmacy Users can also export the whole plan as a PDF to hand to a pharmacist, and the app installs directly to a phone home screen as a PWA. Signing in (with bcrypt-hashed passwords, never stored in plain text) saves a history of past discharge letters and cabinet checks, so a family can look back on previous visits over time. How we built it The system has three layers, each with a clearly scoped job: A custom-trained CNN clarity gate. Before any medicine label is read, a ResNet18 model (trained from scratch via transfer learning on 1,748 images, with Grad-CAM explainability) checks whether the photo is actually clear enough to trust. If it isn't, the photo is rejected immediately and the user is shown exactly which part of the image was the problem. AI extraction. The Claude API reads the discharge letter and the medicine labels, turning messy real-world documents and photos into structured data, with a self-reported confidence rating attached to every extraction. A deterministic cross-reference engine. This is the part we want to highlight: the AI does not make the final Keep/Dispose decision. Once structured data exists, a transparent, auditable Python rules engine — using real OpenFDA brand-to-generic drug data and fuzzy matching for OCR typos — decides which bucket a medication falls into. We made this split on purpose. A hallucinated "this is safe to keep" from a language model is a much worse failure mode than a rules engine making a traceable, explainable decision based on fields it was given. Stack: FastAPI (Python) backend, PyTorch/torchvision for the CNN, Grad-CAM for explainability, thefuzz for fuzzy string matching, fpdf2 for PDF export, SQLite with bcrypt-hashed passwords for accounts and history, and a vanilla HTML/CSS/JS frontend built as an installable PWA. Challenges we ran into Deciding where the "decision" lives. Our first instinct was to let the AI read both documents and just tell us what to do. We changed course once we realized that put a safety-critical decision inside a system that can hallucinate. Splitting "read messy input" (the AI's job) from "decide Keep or Dispose" (deterministic code's job) was the single most important design decision in this project, and it took real iteration to get right. OCR reliability on real photos. Expiration dates are often on a different panel than the drug name, in low-contrast print exactly why the CNN clarity gate exists in the first place. Being honest about our model's evaluation. Our CNN clarity classifier scores 100% on its validation set. We want to be upfront that this reflects testing on augmented variants of the same source photos, not a fully independent real-world test set. We chose to disclose this directly in our Responsible AI section rather than presenting the number without context. PDF generation with Unicode. Our exported summary originally used checkmark and warning symbols that crashed FPDF's core font encoding, fixed by sanitizing all dynamic text before it reaches the PDF layer. Accomplishments we're proud of A working three-layer pipeline where each layer's role is intentional, not accidental. A trained, explainable computer vision model with Grad-CAM verification, not just an API call wrapped in a UI. Real FDA drug data integration instead of a small hardcoded list. A full account system with bcrypt-hashed password storage and a working history page, so families can look back on past discharge letters and cabinet checks. And a clinical-safety-first architecture, where the part of the system most likely to be wrong (the AI) is never the part making the final call. What we learned How to separate language understanding from decision-making in an AI system, and why that separation matters more in a health-adjacent context than almost anywhere else. We also learned that a model's validation accuracy is only meaningful in the context of how the validation set was built — which is why we report our CNN's limitations explicitly rather than leading with the headline number. What's next for Cabinet Clear Expanding the FDA drug database beyond our initial pull, and broader real-world testing of the clarity classifier against independently collected (not augmented) blurry photos. <div