---
slug: "bach-turing"
url: "https://devpost.com/software/bach-turing"
title: "BACH Turing"
hackathon: "Hack for Humanity | 2025"
organization: "Kuba Apps"
winner: true
words: 382
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# BACH Turing

> BACH Turing is a privacy focused CAPTCHA integration

[Devpost](https://devpost.com/software/bach-turing) · hackathon [[Hack for Humanity - 2025]]

## Facets

**substrate** [[financial_record]] [[web_dom]]

**stack** css3, html5, javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what's next for bach turing
- problem statement

## Body

Inspiration In these days, privacy has become quite a major security concern in the lives of netizens, modern captcha solutions such as ReCAPTCHA are using user data such as "Search History", "Behavior on websites", "Advertiser data"; moreover, these companies are selling these data to advertisers to earn them more money. A privacy centered CAPTCHA solution is required, this is what mainly inspired me to create this as my project. BACH Turing, makes use of user mouse activity and social trends that allow people to easily prove their human identity What it does It makes use of mouse detection algorithms and minecraft crafting recipes to allow people to prove their identity How we built it I was able to create an integratable script by using javascript, the styling for the box is made by css, both of which are integratable. Challenges we ran into I had a problem with overlaying the captcha on top of all the website content, but the trusty stack overflow came to my help. What's next for BACH Turing I will probably add more CAPTCHAS based on trends such as the dalgona game from squid game. BACH BACH stands for: B attle A gainst C omputerised H umans Problem Statement We understand that privacy and bot prevention is really a big problem today, projects like "ReCAPTCHA" use your browsing history provided by google and other data that is used to identify you is currently being used. CAPTCHAs are even being to train AI projects these days. Thats why, we bring to you.. BACH . BACH makes use of current trends to build CAPTCHAs. For example, We can use crafting recipes from "Minecraft" to build a CAPTCHA, this style of captchas can really be used to physically identify humans. Computerised Humans tend observe trends and identify them, but this trend identification paired up with other human characteristics would prove to be really demanding and difficult for any robot. Setup Import the CSS file in your head tag html <link rel="stylesheet" href="https://eshangonemad.github.io/BACH-Turing-Test/BACH-TURING-TEST.css"> Import the Javascript file before the end of the body tag html <script src="https://eshangonemad.github.io/BACH-Turing-Test/BACH-TURING-TEST.js"></script> Add the following code for the BACH CAPTCHA BOX html <div class="BACH-Turing-Box"> <div class="custom-checkbox" onclick="BACHTURINGTEST()"> <input type="checkbox" id="CheckBOX-BACH"> <label for="CheckBOX-BACH"></label> </div> <p id="BACHHUMANTEXT">I am actually human</p> <div class="BACHTURINGLOGO"><img src="BACH.png" width="40px"><p>BACH Turing</p><a id="BACH-TURING-PRIVACY" href="https://github.com/eshangonemad/BACH-Turing?tab=readme-ov-file#privacy-statement">Privacy</a></div> </div> <div