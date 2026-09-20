---
slug: "mediglot-ai"
url: "https://devpost.com/software/mediglot-ai"
title: "MediGlot.ai"
hackathon: "UC Berkeley AI Hackathon"
organization: "Cal Hacks"
winner: true
words: 493
team_size: 5
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "domain/immigration_refugee"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# MediGlot.ai

> Enabling medical care across the language barrier

[Devpost](https://devpost.com/software/mediglot-ai) · hackathon [[UC Berkeley AI Hackathon]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[health_clinical]] [[immigration_refugee]]
**user** [[clinician]] [[patient_family]]
**substrate** [[document_pdf]] [[web_dom]]

**stack** flask, google-translate, openai, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned

## Body

Inspiration The mom of one of our teammates inspired us. Our teammate’s mom grew up outside of the US with an ear infection. Because her native country did not have widely-accessible healthcare, this condition went untreated, leading to chronic pain and hearing loss later in her life. When she came to the US and was able to access specialized health professions, she was given the option between having a surgery and taking medications. In the appointment, the doctor explained the risks and benefits in English, with my teammate there to translate for his mom (who did not speak English). Despite this effort, his mom still struggled to understand her options; our teammate was juggling, unsuccessfully, the double task of translating this medical jargon into simple terms and then translating that into a different language. As a team we all felt a deep connection to this experience, which is all too common for children of immigrants. * We made our projects so that, moving forward, patients in countries where they don’t speak the native language can feel comfortable in the doctor’s office, enabled to make informed decisions about their health, their bodies, and their lives. What it does MediGlot.ai leverages GPT-3.5 to simplify and translate doctor instructions for patients whose first language may not be English to better understand and make informed decisions about their health. How we built it Our project, MediGlot.ai, is built with the following languages: Python, Flask, HTML, CSS, and Javascript . We also made use of partner resources including Pinecone, Featureform, and OpenAI . Lastly, we used Google text-to-speech software. Challenges we ran into As stated before, this hackathon was the first time working with artificial intelligence for most of us. I’m glad to say that we rose to the challenges that we encountered along the way. First of all, we came up against rate limit errors for most of the tools we sought to incorporate, owing to the fact that we had a limited amount of requests we could make to each API. In addition, we also faced translation limit errors, since many of these tools also had limits on the number of characters we could translate. We also faced issues collaborating and staying organized since many of us were meeting for the first time during this event, but thankfully our design document allowed us to overcome that challenge fairly early on. What we learned For some of us, this was our first hackathon, for others, this was our first time working with artificial intelligence. We learned a lot about how to ship code rapidly while learning along the way. Moving quickly in this way came down to playing to each team member’s strengths and keeping an organized design document to avoid a duplication of effort. Getting this color-coded design document together was invaluable in us being able to move forward together as a team, seeing as it allowed us to be (literally) on the same page. <div