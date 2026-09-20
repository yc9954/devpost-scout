---
slug: "luther-chips"
url: "https://devpost.com/software/luther-chips"
title: "Luther Chips"
hackathon: "Alexa Skills for Students – Powered by AWS Educate"
organization: "Amazon"
winner: true
words: 506
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "substrate/web_dom"
---

# Luther Chips

> A new and exciting way for students at Luther College to stay up-to-date

[Devpost](https://devpost.com/software/luther-chips) · hackathon [[Alexa Skills for Students - Powered by AWS Educate]]

## Facets

**domain** [[developer_tools]] [[education]] [[finance_payments]]
**user** [[educator_student]]
**substrate** [[web_dom]]

**stack** alexa-sdk, aws-lambda, javascript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for luther chips

## Body

Inspiration For my senior project in Computer Science, I am working on a project to recreate our student newspaper's website, which has never experienced much engagement. This Alexa Skill is a bit of a side-project to further enhance students' experience with the service. What it does This skill lets users listen to or read Luther Chips' most recent articles in any given section they ask for. How I built it I build this skill using the ASK SDK for Node.js. I originally started to build the skill in the first version of the SDK, but later switched to the second version in order to stay fully updated and with-the-times. Fortunately, good documentation exists for v2, and a great community has already been built up around it. Challenges I ran into My initial version of the skill was not very challenging to implement. I connected to an existing API that our Chips website uses internally, and just had Alexa read the content. When I updated to v2, I decided to use the render template Alexa directives, which turned out to be slightly more finicky than I expected. In addition to the challenge of figuring out the intricacies of the 'new' display format, I decided to process my API call a bit differently than I had before. While I had previously just called functions from inside of the API GET request, I recently decided that a more modern and potentially proper way to implement this functionality would be to use Javascript's async/await syntax. This led to some rethinking and rearranging, and then more rethinking and rearranging. In the end, I believe the result was worth the extra effort! Accomplishments that I'm proud of While this was simple to implement, I was overjoyed to use an additional SSML voice. Having a separate voice read the article title just adds so much to a skill like this without detracting from its purpose. So I suppose I could say I am proud that I discovered this feature and put it to good use. What I learned I learned a bit about the render template directive, and also about async/await syntax in Javascript. While the former is functional and serves its purpose, I am more of a fan of the async/await syntax, since it of course is a more widely-applicable and beneficial thing to learn. I also started using the ASK CLI with this project! In the past, I had always coded my skills directly in the lambda console, but it is so nice to work on the code on my machine and in my editor of choice. What's next for Luther Chips I have already began work on the next stages: giving the user access to more stories than just the most recent in each section and more advanced querying capabilities (top readership, most liked, etc). A feature that nearly made it into this release is displaying / reading a list of x recent articles, and letting the user select from that list. I'm excited to fully implement that feature! <div