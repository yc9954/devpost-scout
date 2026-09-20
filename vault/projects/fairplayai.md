---
slug: "fairplayai"
url: "https://devpost.com/software/fairplayai"
title: "FairPlayAI"
hackathon: "Google's Women Techmakers presents She Builds AI"
organization: "Google"
winner: true
words: 503
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "substrate/document_pdf"
---

# FairPlayAI

> In the United States, women make up 51% of the population, but on average only 30% of state legislators are women. FairPlayAI evens the playing field by analyzing complex policy for gender equality.

[Devpost](https://devpost.com/software/fairplayai) · hackathon [[Google-s Women Techmakers presents She Builds AI]]

## Facets

**domain** [[civic_government]]
**substrate** [[document_pdf]]
  <sub>weak: web_dom</sub>

**stack** css, datawrapper, flask, google-civic, google-gemini, html, javascript, legiscan, python, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fairplayai

## Body

FairPlayAI Search Policy Policy Analysis Conclusion Policy Analysis UN SDG Goal 5 Alignment Read Policy Contact Reps Inspiration I was inspired by this election season in the United States. It can be extremely difficult to understand all the complex policies if you go beyond the sound bites and try to dive into what the real, in-depth legislative actions include. I thought it would be great to provide a way to review those policies for gender equity issues and provide a report that would allow people to provide feedback to their representatives and participate equally in the legislative process. What it does FairPlayAI lets users select a US State or Federal location, then search for and view legislative policies by areas that affect women the most in the US - Reproductive Rights, Economic Equality, and Safety and Security. On the backend, the code uses a complex query to search Legiscan for each of these issues and return the full PDF document, allowing for downloading or full reading. Users may also upload documents for review. From here, users can request a policy analysis that directs Google Gemini Pro to analyze the policy in light of the UN SDG Goal 5 elements. The analysis includes a score for each of the Goal 5 element targets, as well as an analysis of each that details how the policy addresses (or doesn't) that element. Gemini Pro also analyzes the policy for explicit and implicit biases, cost effectiveness, and improvement recommendations, then provides an overall assessment taken from the main points of each section. The Gemini Pro analysis is processed via the code into a PDF file that is formatted cleanly with clear section divisions and a chart of how the policy meets each UN SDG Goal 5 element. This PDF can be downloaded and sent to the user's representatives to demonstrate the policy improvements that could be made. It also includes Google Civic, allowing users to search for their representatives by their location and get a quick link to their contact information. How we built it This was built using a combination of prompting techniques along with user design focused elements to ensure high quality output in a format that users would understand and feel comfortable with. Challenges we ran into Getting the PDF report to process correctly took a lot of experimentation, but in the end I'm very satisfied with the final output. Accomplishments that we're proud of I'm very proud of how well I was able to work with the Google Gemini API to get high quality, useful outputs without an extreme amount of prompting and after-response parsing. What we learned I learned that so much about US legislative policy and how little it takes into account the perspective and life experiences of women - but also how easily that could be changed. What's next for FairPlayAI I'm hoping to get this online and live so that more people can participate in the political process without undue burden because of complex legalese in legislative documents. <div