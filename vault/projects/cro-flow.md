---
slug: "cro-flow"
url: "https://devpost.com/software/cro-flow"
title: "CRO Flow"
hackathon: "monday Apps Challenge: Dream it, build it"
organization: "Monday.com"
winner: true
words: 1009
team_size: 6
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/measured_ablation"
  - "domain/developer_tools"
  - "user/developer"
  - "user/general_public"
  - "user/researcher"
  - "substrate/video_visual"
---

# CRO Flow

> The Conversion Rate Optimization Process Management App for monday.com

[Devpost](https://devpost.com/software/cro-flow) · hackathon [[monday Apps Challenge- Dream it- build it]]

## Facets

**mechanism** [[measured_ablation]]
**domain** [[developer_tools]]
**user** [[developer]] [[general_public]] [[researcher]]
**substrate** [[video_visual]]
  <sub>weak: code_repository</sub>

**stack** git, netlify, nuxt, scss, vue

## How they structured the write-up

- our inspiration
- what it does
- how we built it
- repository information
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cro flow

## Body

CRO Flow: The Conversion Rate Optimization App for monday.com CRO Flow: Overview Diagram CRO Flow: What's included CRO Flow: The Research Tracker screenshots CRO Flow: The Hypothesis Builder screenshots CRO Flow: Extra Features included CRO Flow: The Idea Tracker screenshots CRO Flow: Idea Cards screenshots CRO Flow: The Experiment Tracker CRO Flow: Screenshots of Dark Mode and Multi-Language The Story Behind CRO Flow Our Inspiration We’re a small but mighty team of web developers, digital analysts and certified Conversion Rate Optimization consultants. Polished Geek is based out of NC, USA and our team has been working 100% remotely for over five years now (and using monday.com for almost the last two years). A lot of systems and tools exist to manage the final (and admittedly "sexier") stages of CRO programs, the technical experimentation phase. However, very few exist to support the earlier stages of an effective CRO process. The research and ideation phases are critical to making sure you are testing the right things in your A/B tests, things that have the most potential to improve your business and deliver ROI. Thus CRO Flow was inspired by three important things colliding: An ongoing business need in our own organization to better manage CRO projects A lack of affordable CRO tools in the market to manage the foundational stages of a CRO process. Together with our love of working with monday.com! CRO Flow will be released to the public via the monday marketplace as soon as Workspace Templates are available. What it does CRO Flow is a full end-to-end solution for managing your Conversion Rate Optimization process and projects: From Research to Ideation, through generating a solid Hypothesis and keeping track of your Experiments. CRO Flow leverages the ease, power and transparency of monday.com to help CRO teams better manage their projects and collaborate with external clients and internal stakeholders. It includes: 5 custom board templates Support for the user's choice of two leading prioritization frameworks in the CRO industry, PXL or PIE 3 custom board views A completely new way to visualize your CRO ideas with a mini-card board view 5 dashboards (native monday.com functionality) A CRO Flow Support center dashboard for easy access to documentation and help Dark mode support Multi-language ready How we built it We actively participated in the monday developer workshops and hackathon webinars to learn as much as we could about monday apps. Things certainly change fast around monday, so we ended up having to refactor multiple times. Even the last few days coming up to the contest, monday quietly released two-way item links between boards, so we rebuilt all of those in our board templates to use the latest features. Because Workspace Template apps (AKA Solution apps) are not yet available for developers, we were not able to completely package our solution for the contest. We discussed this with Dipro Bhowmik and were told we should submit with links to our board template views and video walkthroughs. Here are links to our board templates: Research Tracker Idea Tracker PXL method Idea Tracker PIE method Hypothesis Builder Experiment Tracker CRO Task minor supporting board Important Here is a link to our YouTube CRO Flow Playlist that will show each board and the Idea Cards in action since you cannot fully install it yet as a Workspace: YouTube playlist Repository information Our repo is not public, but if you send us a request for your Github username and email address you would like us to grant permission to for full access, please send that to getmonday@polishedgeek.com The repo address is: Repo Challenges we ran into The API rate limit per minute was a major challenge and remains one today. We wanted to use micro API calls in a modern fashion but with the rate limit, we had to utilize a mix of monolithic and micro API calls for now. We do still see a problem at times with hitting the rate limit, for example when an enthusiastic user starts rapidly playing with the Idea Cards board view settings. We often ran into undocumented features during development, and having direct access to monday.com developers through the Developer Workshops (thanks Dipro!) and Hackathon sessions were invaluable to help get us past any roadblocks. Accomplishments that we're proud of While we've been a development company for over a decade, this was our team's first project using Vue / Nuxt, so there were absolutely some growing pains! We're proud of building an app that enables powerful views in a custom board view, using client-side columns (like progress and formula columns) that provide key data for the Idea Cards view. (This does mean that users will need to be Pro level or higher to use all CRO Flow features.) We're proud that we were able to take a rough sketch of Idea Cards and turn them into a really unique and exciting way for monday users to visualize their data. Just like monday.com itself, our Idea Cards are a treat for the eye and help teams work together more effectively remotely. CRO Flow is a powerful SaaS-level solution built to take advantage of the best of monday.com, and we can't wait to release it to other Conversion Rate Optimization teams and see how it grows. What we learned Dark mode is not nearly as easy as we first thought! We originally assumed that dark mode would be a fairly quick change once the main light mode was done. But it took a lot of back and forth to get a dark mode version that's easy on the eye and beautiful. Be sure to take a look at the Idea cards in dark mode. What's next for CRO Flow We have multi-language features ready to go once the API supports letting us know the user profile language preferences. Future features planned include deeper connections between the boards once we can build custom column types and trigger actions that way, plus API integrations with popular CRO A/B testing tools like VWO, Convert.com and more. We have a public roadmap here: Roadmap <div