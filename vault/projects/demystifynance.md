---
slug: "demystifynance"
url: "https://devpost.com/software/demystifynance"
title: "DemystiFynance"
hackathon: "HackUTD X"
organization: "hackutd"
winner: true
words: 660
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/education"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# DemystiFynance

> A Google Chrome extension that utilizes generative AI to automatically explain intimidating financial concepts in order to demystify the world of finance and investments.

[Devpost](https://devpost.com/software/demystifynance) · hackathon [[HackUTD X]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[education]] [[supply_logistics]]
**user** [[educator_student]]
**substrate** [[video_visual]] [[web_dom]]

**stack** chrome, css3, extension, google, html5, javascript, react

## How they structured the write-up

- inspiration 💡
- what it does ⚙️
- how we built it 🔧
- challenges we ran into 💪
- accomplishments that we're proud of ⭐️
- what we learned 🧠
- what's next for demystifynance 📈

## Body

Our Chrome extension's icon logo. Image of iteration 1 for our extension layout. Image of iteration 2 for our extension layout. final implementation final implementation cont. Inspiration 💡 Financial literacy is a hard ask for many individuals, especially college students like ourselves or people that don't speak english as a first language. One of the biggest hurdles for these diverse groups of unique individuals to overcome is the daunting terminology related to investments and finance. Often times, the terrifying chain of oversized words and multi-letter acronyms act as the biggest deterrent for would be investors, but fear no more, DemystiFynance is here to clear up any confusion you might have :D. What it does ⚙️ DemystiFynance is a Google Chrome extension that utilizes generative AI to explain intimidating financial concepts, effectively demystifying the world of finance and investments so that it is more accessible to all. When the user highlights a section of text and clicks on the extension, it gives an AI generated explanation which can then be simplified into easier to understand English or translated into another language of the user's choice. The extension also gives text size and color scheme options to offer further customization and accessibility. How we built it 🔧 We used HTML, CSS, and Javascript with Google Chrome's extension documentation to build our product. We parsed through the user's current page with Google Chrome's built in content scripts and will use ChatGPT's API to generate intuitive definitions and translations for users. Challenges we ran into 💪 The lack of up to date documentation for the implementation of a chrome extension through a react app (especially for manifest 3.0 as of August 2023) proved to be our largest hurdle. In order to jump this hurdle we decided to scrap the idea of react altogether and utilize the significantly improved compatibility between chrome and pure css/html/js. In doing so we managed to get our extension up and running but the solution was far from perfect as it created new obstacles of a restricted set of development tools. Pop-up windows through chrome extensions are far more complicated than a single hackathon would allow for us, and thus, concessions had to be made where we sacrificed the pop-up window for feasibility albeit cluttering out extension. Accomplishments that we're proud of ⭐️ Despite all of us having no experience with making a Google Chrome extension and half of us never having used React, we're proud that we managed to figure it out and actually get to running our Google Chrome extension integrated with Reactjs in our very own browsers. We're also proud that we were able to stay flexible with our project. Throughout the course of 24 hours, we switched from Reactjs to HTML, redesigned our minimum viable product, and made new GitHub Repos multiple times after running into time-consuming roadblocks. Staying flexible with our expectations helped us deliver minimum viable product on time when it would have been impossible otherwise. What we learned 🧠 We learned how to make a Google Chrome extension and how to use EventListeners to sense exactly when a user has selected text and instantly relaying the data to the Google Chrome extension. How to integrate Reactjs with the built in tools that Google Chrome provides. We also reached a better understanding of how to use CLI to manage our version control with GitHub. How to handle chrome permissions in a way that would enable active reading scripts on any webpage. That there exist significant security risks to using extensions that are not verified by google (little effort is necessary to make a malicious extension) That code is like life. Both are unpredictable and flexibility along with an open mind is required every step of the way. What's next for DemystiFynance 📈 Fully incorporating AI generative text simplifications into our extension Using contextual clues to generate better simplifications Improve our translation feature to take input from various languages (currently restricted to english only) <div