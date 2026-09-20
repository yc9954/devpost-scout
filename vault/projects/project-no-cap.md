---
slug: "project-no-cap"
url: "https://devpost.com/software/project-no-cap"
title: "Project No Cap"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 1101
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/finance_payments"
  - "domain/media_journalism"
  - "user/developer"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Project No Cap

> Project NoCap: Bringing clarity to the chaos of misinformation through real-time AI verification.

[Devpost](https://devpost.com/software/project-no-cap) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[finance_payments]] [[media_journalism]]
**user** [[developer]] [[general_public]]
**substrate** [[financial_record]] [[web_dom]]

**stack** brightdata, chroma, claude, creao, fetch.ai, fishaudio, gemini, groq, janitorai, lava, vapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for project no cap

## Body

Inspiration Our team sees a significant issue in the increasing polarization of the United States populace and common media consumption. In hopes of tackling this problem, our team decided to explore the impacts of misinformation on these growing dynamics and find a means to mitigate any potential spread of false information. Throughout our research and personal experiences, we uncovered that misinformation is often being spread through biased/false publications and mismanaged word of mouth. From here, we determined that it would be far too difficult to ensure perfect accuracy on the publishing end so we settled for the next best thing which was a consumer centric implementation. Employing an AI-centered approach to information assurance, we were able to develop a convenient product that provides an additional layer of verification to any online readings or conversations. By creating an application that is multi-faceted and easy to apply, we’ve provided a new avenue by which individuals can access material on the internet without fear of misinformation or bias. What it does This innovative project uses a three part solution to combat misinformation by checking for written bias, ensuring verbal accuracy, and providing a medium for productive debates. When the application is active on any website or article, any declarative statements are cross referenced with any other similar publications and any potential biases/incorrect information are listed to provide the reader more context on any content. Another use case of our project is when the user needs to verify information of a call/meeting in which case our tool will transform any speech into text to be analyzed and cross checked by various AI agents to determine how factual any declarative statements are. Finally, the application provides a medium by which individuals can engage in an AI moderated debate which can help people communicate their ideas effectively and without misleading or confusing others through false statements. In our unique combination of various future-forward technologies, users can be more confident of any information they receive regardless of the medium. How we built it Our project required a diverse blend of different AI agents and tools to completely cover the complete breadth of different cases that we wanted to include. Our first task was to dissect the various technologies available and ensure that we could effectively fit together each piece of the puzzle without sacrificing efficiency or complexity of the solution. In order to organize our large tech stack, we spent a lot of time diagraming the interactions between different technologies and procuring necessary API credits or subscriptions. With the background work complete, we were able to begin leveraging Creao to put together a working back end and front end shell which were used to house all of our additional APIs and AI Agents. At this point we configured a speech to text then text to AI search agent pipeline which handled our entire fact checking work flow. At this point we spent some time maximizing efficiency with speech sensitivity and statement identification. Working with a large number of different implementation, we also had to split our program into a web app and phone application piece in order to create a fully comprehensive application from both mediums. Challenges we ran into Our project was initially extremely ambitious and technically challenging which meant that we were plagued with various difficulties throughout the entire process. Since our project relied on the combined implementation of various different AI agents, we had to precisely navigate many different unique API’s and documentation which took a large amount of time. We originally found many of the technologies that we intended to implement were difficult to utilize in combination with other key technologies which led to many significant changes early on. Another difficulty that we had was ensuring a positive user experience while still maintaining reasonable computational complexity and effectively building out an MVP that still stayed true to our original expectations. With so many different moving parts in this project, we were working right up to the deadline and had to strategically cut some features in order to ensure that our product was reliable and consistent which led to various technical compromises. By making these decisions to cut back on certain technical aspects, we slightly decreased our project’s initial scope in exchange for time to further polishing our current application and ensure that all key features were sound. Another key component that we found difficult was our importance on underutilized and irregular applications of the various APIs and AI Agents which added further complexity to the final product. Regardless of all these hardships, we were able to persevere and achieve a satisfactory result. Accomplishments that we're proud of We are proud that throughout the competition we stayed well organized and maintained a solid work flow in spite of unexpected circumstances. Our team came into the competition with very ambitious expectations and we were able to adapt to new technologies while working under a severe time crunch. Throughout the entire event, our team communicated effectively and was able to make use of each member’s unique skills. At the end of the day, we stayed upbeat and effectively managed our time and energy to complete a technically complex product that upheld our original intentions. What we learned Thanks to the incredible variety of innovative sponsors and the prominence of various emerging AI frameworks, our team gained hands-on experience with cutting-edge technologies and AI workflows. Due to strict time constraints, we needed to organize our thinking and leverage various generative AI agents while efficiently cutting unnecessary components in order to complete a fully integrated product. Additionally, we explored the various benefits of simultaneous use of different AI products to increase redundancy and accuracy through cross-examination. In the future we intend to expand upon these newfound skills that we acquired at Cal Hacks 12.0, growing into more complete engineers. What's next for Project No Cap In the future we would like to begin expanding our product to synthesize multiple different sources that the user is hoping to compare and allow for summarizing capabilities. Another feature that we believe could be practical is something along the lines of measuring confidence in a certain assurance and to potentially provide context for any situations with lower confidence. There are additionally many interesting avenues with regards to providing a backlog of alternate options of articles to expand the user’s perspective or background knowledge on a topic. In terms of technical refinements, we hope to expand to as many different platforms as possible to align with that goal of easy accessibility and to hopefully decrease the latency on some of the voice features. <div