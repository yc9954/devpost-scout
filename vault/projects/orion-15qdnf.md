---
slug: "orion-15qdnf"
url: "https://devpost.com/software/orion-15qdnf"
title: "ToiletGO"
hackathon: "UNIHACK 2026, funded by the European Union"
organization: "UNIHACK"
winner: true
words: 963
team_size: 6
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/education"
  - "user/educator_student"
  - "user/general_public"
  - "user/legal_professional"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# ToiletGO

> When nature calls, 4.2 stars isn't enough. Give yourself the relief you deserve - ToiletGO

[Devpost](https://devpost.com/software/orion-15qdnf) · hackathon [[UNIHACK 2026- funded by the European Union]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[civic_government]] [[education]]
**user** [[educator_student]] [[general_public]] [[legal_professional]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** gemini, google-maps, python, toiletmap, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for orion

## Body

The Team Sign in Screen Toilet List Sample Review Write Review Screen Toilet Game Inspiration Throughout our years at school, we had far too many encounters with terrible toilets. You know the kind: the ones where you brace yourself, hold your breath, and try to get in and out as quickly as possible. After reliving one too many of those experiences, we decided to do something about it. That was the beginning of ToiletGO, an app designed to help people find, review, and share useful information about public toilets. What it does ToiletGO is a public toilet discovery and review platform designed to make one of life’s most inconvenient problems easier to deal with. At its core, the app helps users quickly find toilets near them, view useful information about those toilets, and decide which one is actually worth using. Users can browse nearby toilets through location-based search and view important details such as where the toilet is, what facilities it offers, and how other users have rated their experience. Rather than leaving people to rely on luck, the app creates a more transparent, community-driven way to judge toilet quality before walking in. A major part of the app is the review system. Users can leave ratings, write comments, and share their experiences so that others can benefit from real feedback. This means people are not just seeing a toilet pinned on a map, but are actually getting insight into cleanliness, usability, and overall quality from those who have been there before. To build on that, ToiletGO also includes an image-based rating feature. If a toilet has not yet been reviewed, users can upload an image and Google’s image analysis tools are used to assess visible cleanliness and condition, helping generate an estimated rating. This gives users a starting point for understanding toilet quality even when there is little or no review history available. The app also works as more than just a directory. It brings together location data, user reviews, facility information, and image-based assessment into one place, making it easier to compare options and choose the best nearby toilet instead of simply settling for the closest one. Finally, because the whole idea has a playful side, we added a built-in toilet-themed game inspired by Subway Surfers. While waiting, passing the time, or just having a laugh, users can open the game directly from the app for a bit of entertainment. It gave the project more personality and made the experience feel more memorable than a standard utility app. How we built it We built ToiletGO as a web application using React for the interface, with Vite to run and bundle the project, and Express on the backend for features such as the game leaderboard. The app scrapes nearby toilet data from the public toilet map context, and analyses uploaded toilet images through Google image recognition. We used browser geolocation to detect the user’s position and show nearby toilets, then stored user reviews and saved toilet data using local storage so feedback could persist within the app. The interface also includes filtering, review submission, dark mode, and a separate built-in toilet game. To make the app feel polished and interactive, we used modern UI libraries and animation tools for icons, transitions, and smoother user interaction. Challenges we ran into One of our biggest challenges was that most of us had little to no experience with TypeScript, so a lot of the development process involved learning on the fly, reading documentation, and experimenting with unfamiliar tools. We also had to make quick design decisions under time pressure, which meant improvising features and simplifying parts of the original vision. On top of that, this was our first hackathon, so team coordination, time management, and deciding who should work on what were all new challenges for us. Accomplishments that we're proud of This project did not begin smoothly. Our original idea, a tennis analysis app, ran into technical issues and had to be abandoned, which was a major hit to morale early on. What we are most proud of is the way we recovered. We regrouped, brainstormed quickly, and came up with ToiletGO as a new concept that was both humorous and genuinely useful. From there, we played to each other’s strengths, supported one another through technical roadblocks, and ended up building a project that felt far beyond what we thought we could achieve at the start. As first-year students and first-time hackathon participants, finishing a working product together is something we are genuinely proud of. What we learned We learned a huge amount in a very short time. Technically, we gained hands-on experience with TypeScript, React, API integration, image-based analysis, and GitHub collaboration. Beyond the code, we also learned how important teamwork, communication, and task delegation are in a fast-paced environment. More than anything, this hackathon taught us how to adapt quickly when things go wrong and still turn an idea into a finished product. What's next for Orion The next step for Orion is to turn ToiletGO into something more scalable and practical beyond the hackathon. One major priority is rethinking the toilet data source, since if we want to commercialise the app we would need a dataset we are fully permitted to use for commercial use (currently, we can only use our source, https://toiletmap.gov.au/ , for personal use only), whether that means obtaining permission, finding an alternative source, or building our own independent database over time. We would also want to improve the speed and accuracy of toilet discovery, expand the review system, and further refine the image-based cleanliness assessment. Finally, since the current version is a desktop web application, a natural next step would be to bring ToiletGO to mobile so it can be used more conveniently in real-world situations. <div