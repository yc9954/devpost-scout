---
slug: "tweetsmash"
url: "https://devpost.com/software/tweetsmash"
title: "Tweetsmash"
hackathon: "Chirp Developer Challenge"
organization: "Twitter"
winner: true
words: 698
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "domain/scientific_research"
  - "substrate/code_repository"
---

# Tweetsmash

> Streamline information that matters from Twitter bookmarks

[Devpost](https://devpost.com/software/tweetsmash) · hackathon [[Chirp Developer Challenge]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]] [[scientific_research]]
**substrate** [[code_repository]]

**stack** amazon-web-services, nextjs, react, supabase, vercel

## How they structured the write-up

- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what’s next for tweetsmash

## Body

Create workflow automations for your Twitter bookmarks Organise how you want to read your bookmarks Receive personalised short digest right into your inbox Automatically get your research papers, journals to Zotero Organise your content research by setting up a sync to Notion Inspiration We started to use bookmarks to save anything we found informational on Twitter. Over time we had hundreds of tweets which includes resources, valuable threads, and countless learnings from the community. Even though we knew this, we couldn't resist bookmarking tweets every time. After desperately searching for a solution, we started to work on this idea in the hackathon. While we worked on it, we were firm about two facts, Our solution should be able to self organize And other it should be a system that ensures we consume what we curate into it. What it does Tweetsmash allows the creation of workflows that help to consume curated information easier. The time most we bookmark is when we are overwhelmed with the information and we didn’t want to miss it out. Keeping this our prime feature, we combine curated tweets by similar categories and preferred reading length. With Tweetsmash, now users can able to see 5 mins of content on Business tweets or even 20 mins of a week’s curated tweets to read on weekends. With 3rd party integrations, it can sync research papers to Zotero and also content research to Notion. How we built it Tweetsmash primarily uses Twitter's Bookmark API to import all the user's curated tweets. We also support curating low signal content via Likes and slightly higher signals by DM's. Additionally, we use Twitter List data to analyze user's preferences to better categorize their curated tweets based on interests. Tweetsmash maintains cluster relationships of the curated tweets for the user. Then when the user gives his preferred reading length, it uses Bin packing algorithm to create the mash in each category. Users can then connect their email to receive it as a digest. Challenges we ran into When we started Tweetsmash, it was a browser extension which uses a content script to retrieve Twitter's bookmarks. After we launched our earlier version, Twitter releases their support for Bookmarks API. Later we moved most of our endpoint to v2 and our initial transition is a little bit difficult and took a few days to rewrite our codebase. Another issue we face now is some of the v2 features were still not ready completely. For instance, the Twitter OAuth v2 in mobile doesn't work much great with the app installed. Accomplishments that we’re proud of As users starts to use our product we were quite surprised by the use cases we potentially can address. For example, we were surprised when one of our users use the curated content as an inspiration for his content and the tweet he posted from the Tweetsmash inspiration went viral, eventually he became our customer. With 3rd party integrations, we began to make the curated tweets into action. For us, we bookmark the testimonials, curate user problem descriptions, and competitive products and have it sync to a Notion base. Also now it is possible to curate content research and make the content creation process better. What we learned We learned there were countless use cases in that people were trying to put their curated content to use but without a proper system, it is difficult now. But by properly aligning these curated content that resonates with the user, it is possible now to promote content creation. What’s next for Tweetsmash At Tweetsmash we are focusing on how to make the curated tweets actionable by connecting to their creative workflow. These were the top 2 features we are planning to work next. Making a shareable collection that would help content creators to share their best works with public We were planning to organise the best content for categories and make it easily available for even outsiders to discover the information available on Twitter. We plan to start with Indie hacking where tweets are categorised for each key section from different authors. Since we provide a way to consume information, users can subscribe and receive it just like a newsletter. <div