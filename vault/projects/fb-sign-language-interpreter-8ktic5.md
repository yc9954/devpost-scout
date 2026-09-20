---
slug: "fb-sign-language-interpreter-8ktic5"
url: "https://devpost.com/software/fb-sign-language-interpreter-8ktic5"
title: "Somi Sign Language"
hackathon: "2018 Developer Circles Community Challenge"
organization: "Facebook"
winner: true
words: 794
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/accessibility"
  - "domain/education"
  - "domain/finance_payments"
---

# Somi Sign Language

> AI-Based Avatar Interpreters for social media, integrated with Facebook pages to interpret posts in Sign Language.

[Devpost](https://devpost.com/software/fb-sign-language-interpreter-8ktic5) · hackathon [[2018 Developer Circles Community Challenge]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[accessibility]] [[education]] [[finance_payments]]

**stack** asp.net, facebook, facebook-graph, javascript, sl-web-interpreter-api

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for somi sign language interpreter
- how to try it out:

## Body

This is SOMI in action :) Find all FB pages currently integrating SOMI Inspiration I developed the technology at 16 years old, for a high school competition, “INTEL ISEF Awards 2008”. Knowing I’ve been coding since 6th grade, my school encouraged me to participate and come up with a solution to the problem of high marginalization of the Deaf community due to lack of services/content offered in Sign Language. What it does I came up with the idea of avatars that can be integrated in any platform to translate the content (text/speech) to Sign Language. The project ended up winning the Intel ISEF 2008 Behavior and Social Science Third Award. How I built it Using Facebook page tab application. New tab is added to FB page. -Using Facebook Graph api, Javascript Page feeds is retrieved. -Deaf-Friendly Page, designed to have posts interpreted to Sign-Language. -Using MindRockets Sign Language Web Interpreter API’s, the feeds are interpreted in sign language using 3D avatars. -If the feeds are in language other than the avatar language, third-party automated translation service is used. -In case of mobile (as page tab apps are not supported on mobile) a new tool called QRWidget is provided, it's added to the project which uses Facebook open graph meta tags. So, QR code for the page link is being created with a link to the post. -Using Social platform plugins, when opening the app outside the Facebook it shows social plugins to keep the experience of exploring a page such as embed post, page widget, share post, share QRWidget. Challenges I ran into When the page has less than 2000 likes, it cannot be added automatically , so currently we are adding them by making the page admin tester and installing the tab for them. Accomplishments that I'm proud of After the competition, I kept the project as a hobby, and developed it in the form of mobile apps which I kept on the Google and iOS App stores. The apps started getting thousands and thousands of downloads from the US (it was in American Sign Language that I first developed it) as well as comments from individuals expressing gratitude for the impact it was having on their lives. [some comments from Google Store & iOS App Store: "Love it... I absolutely love this app. I can now talk to my grandson and he understands me. Keep it up!" "This is going to be a great help! My daughter is so lost when I'm not there to interpret, and this app will give her so much independence and control over her own life. Thank you so much and God bless you!" "Helpful! This app is very helpful. My landlord is deaf and it will help me communicate with him." Seeing this impact, I quit my full-time job in 2016 and started Mind Rockets Inc (Assistive Technologies for the Deaf), as startup dedicated to expanding and scaling this technology to the next level. Now, almost 2 years later since we started, we are a team of 10 people. My cofounder, Mohammad Kilany, has almost 20 years of experience in IT multinationals; we have 2 Deaf people on the team so we’re connected with the Deaf community in every step we take. Furthermore, we’ve been winning global startup competitions around the world: (K-Startup Grand Challenge (South Korea), Seedstars World (Switzerland), MIT EF Pan Arab (Bahrain), GITEX Future Stars & AIM Startup (Dubai), Get In The Ring (Portugal), Arab Mobile Challenge, Imagine Cup.) Now, we have more than 20 websites integrating our avatars to make the content accessible in Sign Language for the Deaf. These are institutions like ministries and govt. entities in the UAE, telecom companies (ZAIN Jordan), Universities, and other private institutions. Only recently did we develop the avatar for Facebook integration, and now we have more than 40 FB pages already integrating our avatars, making their content accessible for the Deaf. What I learned I Learned that sign language is not one language, and most deaf people cannot read or write. I also learned that via Facebook tools, we can connect deaf people with organization and providing better service for them via a Facebook Page. What's next for SOMI Sign Language Interpreter Provide a version of Contact US service on the Facebook Page Sign language Interpreter as plug in, making service available on multiple sign languages, Possibly, with the help of FB, a future integration with Facebook Status feature. How to try it out: 1) Use the following link http://mindrocketsinc.com/api/installpage.aspx 2) Select your page 3) Enter your email 4) On the payment method, select free (for non-commercial pages) 5) Click "next" and enjoy Sign Language! Please note that Somi works only with published pages who are not restricted to countries and age groups. <div