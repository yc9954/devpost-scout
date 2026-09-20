---
slug: "amputatorbot"
url: "https://devpost.com/software/amputatorbot"
title: "AmputatorBot"
hackathon: "Reddit Mod Tools and Migrated Apps Hackathon"
organization: "reddit"
winner: true
words: 667
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/transportation"
  - "user/developer"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# AmputatorBot

> Since 2019, AmputatorBot has fought back against AMP's threat to the open web, replacing privacy-invasive, publisher-harming links with the clean, canonical URL. Now a native Devvit app!

[Devpost](https://devpost.com/software/amputatorbot) · hackathon [[Reddit Mod Tools and Migrated Apps Hackathon]]

## Facets

**domain** [[developer_tools]] [[transportation]]
**user** [[developer]] [[general_public]]
**substrate** [[code_repository]] [[web_dom]]
  <sub>weak: video_visual</sub>

**stack** devvit, postgresql, reddit, rust, scaleway, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for amputatorbot

## Body

Screenshot of AmputatorBot in action Logo of AmputatorBot Inspiration Reddit is full of links, and a surprising number of them are AMP links. They're annoying for users, hide the publisher's real URL behind Google's infrastructure, and often get reposted across communities without anyone realizing it. While moderators spend time fighting spam, scams, reposts, and low-quality content, AMP links quietly make the browsing experience worse for everyone. AmputatorBot has been solving that problem for years. With Reddit's shift toward Devvit, this hackathon was the perfect excuse to modernize the bot, clean up years of accumulated technical debt, and bring a proven moderation utility directly into Reddit's developer ecosystem. What it does AmputatorBot automatically detects AMP URLs in posts and comments and replies with the clean canonical version. For users, that means a better browsing experience. For moderators, it means one less repetitive problem to think about. Communities get cleaner links automatically without requiring manual intervention or custom moderation workflows. The bot recognizes AMP links from Google, Bing, and numerous publisher-specific implementations through fourteen detection patterns. Once detected, it resolves the true canonical URL using a multi-stage resolution engine. What sounds simple is surprisingly difficult, trust me on that one. AMP URLs come in many formats, and blindly removing /amp often produces broken links or incorrect destinations. To reliably recover the original article, AmputatorBot combines multiple techniques including: HTML canonical tag extraction, OpenGraph metadata, Google AMP cache decoding, Bing cache markers, Schema.org JSON-LD parsing, Meta refresh detection, Redirect analysis and even guessing the canonical link and checking for article similarly. The result is over 98% accuracy across more than 200,000 test cases. How I built it The original AmputatorBot was built with Python, PRAW, and Flask. For this Devvit migration, I rewrote the core service in Rust and rebuilt the Reddit integration on top of Devvit. The Devvit app handles: Monitoring posts and comments Detecting AMP URLs Preventing duplicate processing Posting canonical replacements Managing Reddit-side integration and execution The Rust backend handles URL resolution and canonical discovery through the public Amputator API. The project is fully open source and hosted in the EU. Challenges I ran into Porting a mature project is very different from building a new one. The original bot had years of bug fixes, edge cases, workarounds and bugs buried throughout the codebase. Reproducing that behavior while moving to a completely different architecture required careful validation. Rather than perform a direct translation, I used the migration as an opportunity to simplify the design, remove technical debt, and improve reliability. Maybe detecting amp links by the substring amp/ wasn't great, based on all /lamp links AmputatorBot tried to convert (oops). I also had to learn Rust for the API rewrite. I can say now that I get the hype, but also the critics. But ultimately the codebase is now significantly easier to reason about and test. Accomplishments that I'm proud of Successfully migrated a long-running Reddit utility to Devvit Used MCPs, AI and other tools to help ease the migration Achieved feature parity with the original implementation Built a test suite with more than 130 automated tests Maintained 98%+ canonical URL resolution accuracy Processed over 1.7 million AMP links since launch What I learned This project reinforced how valuable migrations can be when they're treated as redesign opportunities rather than straight ports. Devvit significantly simplifies Reddit integration, while Rust provided stronger guarantees around correctness and reliability than the original implementation. I also learned that rebuilding something familiar is an excellent way to learn a new language, because you have a reference for correctness. What's next for AmputatorBot The Devvit migration brings the project onto a more sustainable foundation. The core logic is now covered by extensive automated testing and parity checks against the original implementation. The next step is validating performance under real Reddit traffic and continuing to improve detection coverage as publishers introduce new AMP variants. The internet always finds creative ways to generate terrible URLs. AmputatorBot will continue finding creative ways to remove them. <div