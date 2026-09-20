---
slug: "clearpolicy-cp"
url: "https://devpost.com/software/clearpolicy-cp"
title: "ClearPolicy (CP)"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 606
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/education"
  - "domain/legal_justice"
  - "user/educator_student"
  - "user/general_public"
  - "substrate/document_pdf"
---

# ClearPolicy (CP)

> CP translates policy & ballot measures into plain language with adjustable reading levels- empowering every student to make confident, informed choices in civic and everyday life, on any device, free.

[Devpost](https://devpost.com/software/clearpolicy-cp) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]] [[education]] [[legal_justice]]
**user** [[educator_student]] [[general_public]]
**substrate** [[document_pdf]]

**stack** congress.gov, next.js, openstates, playwright, prisma, react, tailwind, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for clearpolicy (cp)

## Body

Inspiration ClearPolicy was inspired by my childhood spent in Cupertino CA, after my elementary school shut down from a misunderstood education funding law. I can still remember sitting at my kitchen table, struggling to make sense of a dense government PDF—frustrated along with my parents and teachers. Later, I spent hours trying to research a ballot measure for class, piecing together conflicting sources and still ending up confused. These moments made me realize most people aren’t disengaged by choice—they’re overwhelmed by inaccessible information. Years later, in my AP US History Class right now, I've noticed how creators on Youtube such as Heimler's History and OverSimplified are inspirational to me in the way that they are able to condense 30 pages of history textbook reading into an engaging 8 minute video. That’s when I realized that building this web app that distills complex policy into clear summaries would be the perfect problem to tackle in this focused hackathon sprint! What it does ClearPolicy (CP) empowers users to understand laws and ballot measures with clarity. Search for any issue or enter your ZIP code for instant, structured summaries in three clear sections: “What It Does,” “Who It Affects,” and “Arguments For/Against.” Each summary links back to nonpartisan sources for transparency. The web app features frosted overlays, info cards, crisp color contrast, and one-click large-text toggles for seniors and users with vision needs, making civic information approachable for all. The early access page has been built and is currently live (clearpolicy.org)! How we built it We built CP with Node.js and JavaScript in the Cursor IDE, using prompt-engineered OpenAI API calls to summarize content from sources like CA.gov and Ballotpedia. We designed normalization functions to handle different web formats and source structures, ensuring consistent summary generation. The responsive frontend enables accessibility toggles, clean navigation, and fast info retrieval. The waitlist page ( clearpolicy.org ) was built with the assistance of Lovable. We iterated summaries and layouts based on hands-on feedback from friends and family, as well as our own rapid testing. Challenges we ran into One challenge was handling varying government data formats—importing from nested web tables and structured text required custom normalization functions, especially when parsing source pages from Ballotpedia. Ensuring summaries remained neutral demanded continuous manual spot-checks and prompt tuning, since even small changes could affect tone. Building accessibility features for seniors required special attention to color contrast and text scaling. All of this was accomplished under the tight timeline of a 48-hour hackathon. Accomplishments that we're proud of We shipped a working prototype where California users can type their ZIP and instantly see structured, three-section policy summaries, with one-click access to the full legal text where data is available. Our use of a liquid glass-inspired UI and robust accessibility features helps make civic information truly inviting. Delivering clarity and neutrality for real users, especially while being under hackathon pressure, is something we’re proud of. What we learned Building CP taught us important lessons about prompt engineering, error-handling, and accessibility. For example, some users misread “Who It Affects” as listing only beneficiaries, not also those who might be impacted negatively—so we adjusted the section title and content for clarity. The project reinforced how empathy and fast feedback cycles can make tech more useful to everyone. What's next for ClearPolicy (CP) The next step is to extend our coverage to another state and add Spanish-language summaries to reach more users. We’re planning richer policy visuals, real-time updates for legal changes, and enhanced accessibility. Long-term, our vision is nationwide coverage, partnerships with schools, and community-driven feature expansion to empower every citizen to understand what’s truly on the ballot. <div