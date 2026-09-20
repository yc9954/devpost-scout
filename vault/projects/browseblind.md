---
slug: "browseblind"
url: "https://devpost.com/software/browseblind"
title: "BrowseBlind"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 915
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "domain/accessibility"
  - "domain/labor_employment"
  - "domain/legal_justice"
  - "domain/retail_commerce"
  - "user/legal_professional"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# BrowseBlind

> World's First AI Browser. Allowing blind people to interact for the first time with the internet. Also helping visually impaired. Also, automated processes help average people save time.

[Devpost](https://devpost.com/software/browseblind) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]] [[retrieval_grounding]]
**domain** [[accessibility]] [[labor_employment]] [[legal_justice]] [[retail_commerce]]
**user** [[legal_professional]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** agenticframework, browsers, deepgram, fetch, gemini, gemini-bounding-box, groq, pyqt5, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for browseblind

## Body

Inspiration I was doing an application last week when one of the questions about diversity prompted me into thinking about how we take things for more than just granted. It struck me that blind people aren't able to interact with the internet (shop on e-commerce websites, research to learn, play video games, social media - the list is quite endless). I then asked my dad, who works in the computer-science industry, about whether the visually impaired and blind are able to contribute to their likeness in the workforce when I realized how far off the scales were tipped. Assil Eye Institute If I were in their shoes, then I would immediately build such a software to be connected like and with everyone else, but in their case I would be blind so I wouldn't be able to, luckily I'm not so I know the right thing to do would be to build a software for them. Also, I realized that for people like me who are quite lazy or would like parts of their browser processes being automated (like telling it to reserve my tennis court from 5-6 PM rather than doing it myself), an AI browser might also sound quite valuable. Rather more of a business market "want" than a "need", I think regardless it's novelty in the market and it's usefulness for a customer segment (did a bit of customer discovery as well reaching out to centers and found out directly from people that they are very much look forward to it) makes this idea worth venturing about this hackathon in CalHacks. What it does It's the same as your regular web browser application (Chrome, Safari, Brave, etc) in the way you surf the web, but in addition, you can do so freely while being blind-folded. Well, how does that work? Also, controlled by text and/or speech input (pressing the space bar for over a second starts a recording and leaving it ends the recording), any user's instructions are followed by the browser. When a user lands on a page, a quick summary of the page is read including the nav bar components, etc so the user can navigate and explore the web just like any other person. A user can ask the browser to click on any element/part of the page and also fill in information on the page via true NLP. They can also open/close tabs, search using the search engine, ask questions (variant of RAG approach taken) over the current page, save the page locally/print the page, and so many other tasks that the current set of agents have to offer. Every time something new is displayed on the browser (ex. going to a different page) they are notified so they can take judgements. How we built it Using the PyQt5 Browser Development framework, I started my code by building a browser. I organized my prompt engineering agentic framework using Fetch AI's agentic system. For prompting questions with images/text I used Gemini's models. I also used Gemini's bounding box model for detecting where to proceed next on the page. This was not too accurate, so I coupled it with my algorithm I wrote where I take the html code of a website and parsed it down to the important segments (removing PII and unnecessary contents) in order to save tokens and decide based on html where to move next as a backup. After much testing, I settled on Groq for the decision-making segments of the LLM chain for its speed. I also used it for the STT part where the user has the option to speak in our application. The TTS part was handled by DeepGram and other voice agent integrations. Building requires testing and I tested this by imitating a blind person by being blind. One such successful testing included making accounts on websites I have never visited before. Challenges we ran into Parsing the HTML took one of the longest parts due to its implicit complexity. Event listeners attached to elements across the DOM tree. Event listeners on images like a hamburger icon which has no text so a mapping is needed. These multiple edge cases had to be considered before reaching the threshold where it was doing perfect on every website as it is doing now. Another challenge I ran into was fine-tuning. The accuracy of this model was at around 60% and it was a hard and enduring work to get it to around 95% where it is currently at right now. Accomplishments that we're proud of Controlling the browser by "having a 2-street conversation" with it simply blows my mind and really changes the way one surfs the web. It's really fun and really useful at the same time. What we learned How to build your own browser. How to fine tune the boundary box model with Gemini through prompt engineering to extract high accurate insights. Learned documentation for multiple voice agent companies that were integrated. What's next for BrowseBlind Perfecting the software model and finding ways to even further reduce token consumption in order to push this into the market as soon as possible. Also, building "background tabs" a feature I didn't have time to finish but essentially you can give a tab a task (ex. find the part on the wikipedia page that talks about fourier transform or find the contact page for X, Y, Z company) and the tab does the task in the background and comes back up when finished. <div