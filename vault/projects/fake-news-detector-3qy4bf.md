---
slug: "fake-news-detector-3qy4bf"
url: "https://devpost.com/software/fake-news-detector-3qy4bf"
title: "Fake News Detector"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 956
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/education"
  - "user/educator_student"
  - "substrate/structured_db"
---

# Fake News Detector

> Make your Social Platform Clean

[Devpost](https://devpost.com/software/fake-news-detector-3qy4bf) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[structured_db]]

**stack** mongodb, node.js, postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fake news detector

## Body

Fake News Detector Inspiration Nowadays, social media platforms like Facebook, Twitter, etc. are becoming more and more popular for not only recreation but also getting news about the surroundings. Many people prefer social platforms for getting current news rather than watching TV or reading newspapers as they spend a lot of time on these platforms. Though there are many authentic news portals available in social media, a large number of fake portals are spreading much quickly as getting popularity is not that hard here. These fake portals are publishing rumors and fake news regularly which mislead people from the truth. Sometimes, these rumors create so much chaos in the society that can cause the death of many people. We want to make a system that can detect these fake news and alert the users so that they don’t believe them easily. This can be a web browser extension which will immediately detect a news if it is fake or authentic that just appeared on the screen and alert the user how many negative votes and comments it got from the other users. This extension will also show if there exists any related news in the popular authentic news portals so that people can get a clear idea about the authenticity. What it does Our plan is to make web browser extension that will do the following things: When a news appears on the user’s screen while browning the social platforms, the extension will show a statistics how much negative votes and comments have been given for that news. It’ll also search for related news that has already been voted so that users can know all types of rumors related to a specific topic. Suppose a user reads a news article floating on social media and he knows that this is definitely a rumor, he can vote that news as negative and submit a comment. As a result, other users who will see that news also can check the negative votes and comments. So they can’t be manipulated easily. Users can also check the authenticity of specific news by using this extension. If a user sees a news and he wants to be sure about the authenticity, he can check if there exists any related news in the popular authentic news portal, such as BBC News, The Daily Prothom Alo, etc. How we built it As this hackathon is about to make Postman public Workspace, we have developed 3 APIs that do the following tasks we have mentioned. The first API, (/vote) takes News Heading, News Subheading, News Link, Publish Date, Up / Down Vote, User Comment as input and Stores these votes in the database so that these can be used to show statistics for the related news. The Second API, (/checkAuthenticate) takes News Heading, News Subheading, and News Link and searches in the database if there are related news that already exists or not. It not only grabs the exact news heading but also grabs all related news that matches with the searched News Heading as the same news can be shared with slightly different heading in different portals. It shows users the related news with total votes, comments, News link and publishes date. The third API (/searchFromAuthentic) takes News Heading and Subheading and searches in the popular News portal and grabs the related news so that users can get an idea about the authenticity. We have used Node JS, MongoDB and Postman collection for developing this project. Challenges we ran into We have faced a lot of challenges during development. As we are students, we had to give much time to make the Node JS and MongoDB concepts clear. We have faced some difficulties making the second API (/checkAuthenticate) as we need to make an elastic search so that users can get all related news, not just specific news heading. We had to build keywords from the news header and match them from the database. If we get above 70% similarity, we have shown them in the search result. We have taken help from a third party API for developing our third API(/searchFromAuthentic). We have to add more news portals so that users can get the best results from authentic sources. As we have also focused on our regional users (Bangladesh), our APIs can search Bengali News from the database. We’ll develop the third API so that authentic Bengali news search becomes more flexible in our next sprint as it’s a great challenge to get the open APIs from the regional authentic news portals. Accomplishments that we're proud of We are always passionate about our goals. We’ll try our best to make this plan successful and publish this system for public use. The thing that makes us proud is thinking about society. We want to remove the rumors from social media and stop making the people manipulate easily. What we learned We have learned a lot from this project. The teamwork always teaches some good things. We have faced a lot of difficulties building this project and we overcame on our own. As we have used Node JS and MongoDB for this project and as we’re still studying, our concepts became more clear after solving the problems we have faced. What's next for Fake News Detector We just developed the APIs. We have many things to do. As our plan is to make a web browser extension, we’ll focus on developing it first. We’ll try our best to make it user friendly with simple and clean UI/UX so that users can welcome it quickly. Our next target is to make this default web extension so that this can be integrated with the popular web browsers and users don’t need to install it separately. <div