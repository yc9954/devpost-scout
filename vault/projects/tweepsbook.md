---
slug: "tweepsbook"
url: "https://devpost.com/software/tweepsbook"
title: "TweepsBook"
hackathon: "Chirp Developer Challenge"
organization: "Twitter"
winner: true
words: 626
team_size: 7
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/transportation"
---

# TweepsBook

> A notebook for all your bookmarks. Sync your Twitter bookmarks, add custom tags, & organize. Search by content, authors, & labels. Take & share your thoughts on individual bookmarks.

[Devpost](https://devpost.com/software/tweepsbook) · hackathon [[Chirp Developer Challenge]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[transportation]]
  <sub>weak: developer_tools, media_journalism</sub>
  <sub>weak: code_repository</sub>

**stack** cloudflare, fastify, jwt, mongodb, nextjs, node.js, railway, vercel

## Body

Our brand banner GIF How to import your Twitter bookmarks GIF How to archive a particular Tweet GIF How you can add multiple tags to a Tweet TweepsBook was initially launched in April 2021 as a minor project built by three indie devs & was recently relaunched in July 2022 after building it from the ground up with the latest technologies & APIs. The primary motivation to build the project again was the domain cost. After keeping the project on autopilot, we decided that if we would spend another ₹1000 again just to keep the service running, why not build something great out of it? Besides that, Twitter launched its V2 API & we wanted to learn Fastify as a part of our development journey (TweepsBook was previously based on ExpressJS). All that was enough motivation to start the development of the product. The initial journey for the development of TweepsBook was very brisk. We would spend most of our days looking for front-end devs & designers who would help us build a better UI/UX for the product. DMing people on Twitter & exhausting our network worked for us & we eventually settled for a team of two designers, four devs, & one manager. Building a solid team was not an easy task. We had to shuffle through many folks who lost interest mid-project. Some people left because the project was out of their expertise. There were lots of ups & downs. We sometimes thought that TweepsBook wouldn’t see the light of the day. But everything’s well if it ends well. We have a dedicated blog about the entire team-building process & its intrinsic details, which you can read here . Let’s talk about tech for a moment. Tech at TweepsBook is very critical to the project. The journey has been full of differential learnings, from writing the first line of code to publishing the final commit just before the launch. From implementing the Twitter API to connecting the internal APIs & then hosting it on different platforms all connected via Cloudflare is something we are very proud of. Creating an individual user client whenever a user requests to import their bookmarks, fetching real-time data for the tweets, or authenticating the users with JWT tokens all took a lot of time & effort to learn & implement. CI/CD, for e.g., is based on multiple pipelines. Our front-end is hosted on Vercel, whereas our back-end is hosted on Railway. We have different environments for development & production purposes as well. The community has been very keen on the tech & hence we decided to write a dedicated blog explaining the entire tech, which you can read here . We would like to take a moment to share some stats since the launch of V2. In the 2-3 weeks that have elapsed, we have had more than 1000+ people using the app. People have imported more than 100,000 bookmarks on the platform. More than 500 tags have been created, & 50+ notes shared. Building this project was no small feat. The journey has been incredible, from iterating through multiple design changes, getting critical feedback from our early users & then making real-time changes to implementing various marketing strategies & conducting live Twitter Spaces to brainstorm features with our users. If you are further interested in the whole launch day BTS, we highly suggest you read this blog . For each of us, TweepsBook is very near & dear to our hearts. Building something on this scale is a first for all of us & experiencing what the users have to say about us at the end is delightful. Closing it in, we would like to call it, “We are not yet done when it’s still day one!” <div