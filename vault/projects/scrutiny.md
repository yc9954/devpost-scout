---
slug: "scrutiny"
url: "https://devpost.com/software/scrutiny"
title: "Scrutiny"
hackathon: "Junction 2016"
winner: true
words: 367
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/disaster_emergency"
  - "domain/media_journalism"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Scrutiny

> Crowd sourced fact checking: stop the spread of misinformation!

[Devpost](https://devpost.com/software/scrutiny) · hackathon [[Junction 2016]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[disaster_emergency]] [[media_journalism]]
**substrate** [[financial_record]] [[web_dom]]

**stack** chrome, css, flask, html, ibm-watson, javascript, mongodb, natural-language-processing, nltk, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for scrutiny

## Body

Marking factual inaccuracy in article Video fact checking Inspiration These days, misinformation spreads like wildfire online. It has been used by politicians (there's this one guy in America...) and media to skew public opinion. There's gotta be a way to fight this! What it does Suppose you are on a news website/blog/whatever and see a false statement. You simply highlight it, explain why it is wrong and provide a reference for your claim. Other users and a moderation who read the article will be to approve/veto your annotation. Once approved as a genuine claim, it will be automatically shown to every user who has our extension and visits the same page (the misinformation is highlighted in red and you can hover it to see the explanation). Approved posts are fed to an AI engine which crawls common news sources and identifies equivalents snippets, automatically tagging them as incorrect -- this is crucial, since the same incorrect is usually posted by several media outlets. But of course, we can't ignore that a lot of information is consumed through Youtube videos. That's why we also incorporated video fact checking, which allows users to also annotate video segments! How we built it Tagging is done through a google chrome extension which communicates with a Python (flask) server. The AI engine was coded in Python and used nltk and IBM-Watson's Natural Language Classification Service. Challenges we ran into It was really to hard to come up with a good AI engine. Overlaying our own content in websites was also quite hard: at first, our chrome extension was distorting the websites' layout. We later realized that this was because we were injecting bootstrap into the page to show our menu, which of course generates conflicts. Therefore we had to load all of the interface into iframes and to inject bootstrap there. Controlling these iframes was another ordeal, but we managed to do it eventually! Accomplishments that we're proud of Having solved the challenges above and created a tool that we believe is truly relevant in today's information landscape. What we learned Chrome extensions are freaking hard. It w What's next for Scrutiny Improve support for video fact check and AI engine. <div