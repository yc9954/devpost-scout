---
slug: "instayum"
url: "https://devpost.com/software/instayum"
title: "InstaYum!"
hackathon: "Atlas Madness"
organization: "Google"
winner: true
words: 638
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/developer"
  - "user/small_business"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# InstaYum!

> Rediscover the joy of cooking. InstaYum! is a revolutionary cooking assistant, that uses voice control to make cooking easy, and AI to get recipe recommendations.

[Devpost](https://devpost.com/software/instayum) · hackathon [[Atlas Madness]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[developer_tools]] [[supply_logistics]]
**user** [[developer]] [[small_business]]
**substrate** [[structured_db]] [[video_visual]]

**stack** google-app-engine, google-cloud, mongodb, mongodb-atlas, nestjs, vue

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for instayum

## Body

Landing Page on Desktop Figma Design InstaYum! Architecture Inspiration I was on a trip to Seattle, eating some clam chowder in Pike Place Market when I suddenly came up with an idea for a hands-free cooking app! The idea was to make an app like Siri but for cooking. What it does InstaYum allows you to query recipes according to the ingredients you have on hand. Just say something like "I have some beef, some lettuce and some bread", and InstaYum will query a database of over 140,000 recipes to bring you the best matches for your ingredients. After picking your recipe, you can browse it like a regular recipe site, or you can use Hands-free Mode to easily get instructions while you're in the kitchen! Also: It's mobile-first! You can use InstaYum from the palm of your hand. Very convenient! How we built it InstaYum leverages MongoDB complex aggregation queries to find the ideal recipes for your ingredients. The frontend and backend are independently deployed as services on Google App Engine. My original intent was to use Google's speech API directly in order to process speech for recognition, and to synthesize voices for Hands-free mode. Sadly, the project was getting out of scope and I was running out of time, so I decided to make a "naive" version that uses WebSpeech API instead. WebSpeech actually uses Google services under the hood (in Google Chrome), so it's not bad for a quick implementation. The backend was done in NestJS, and the frontend in Vue. Both are standalone projects, allowing seamless integration, easy collaboration and deployability. Both are deployed as separate services on Google Cloud. Finally, the backend uses MongoDB Atlas to store the data, and the data is managed from the backend service using mongoose. Challenges we ran into I ran into a few challenges with the WebSpeech API not behaving as expected. The voice features in the app are far from perfect, there are issues when loading voices, or distinguishing our voice versus background noise. It doesn't work properly with headphones, either. I also had a couple of issues deploying the frontend to GAE, mostly related to .yaml configs being tricky, and the backend secrets not loading correctly (I was in a hurry and couldn't integrate with Google Cloud secret management). Accomplishments that we're proud of I'm really proud of developing this project on my own, although I really wanted my friends to join me and make something even better! I found it hard to balance full-time work, college courses and this hackathon, but luckily I developed the MVP on time! What we learned I learned a lot about MongoDB aggregation as I came up with ways to wrangle the 145,000+ recipes in the database. Deploying things on Google Cloud has also been a great learning experience, as the process can be a bit complex when you're dealing with various services working in parallel. In general, making an app with a multi-tiered architecture that works properly was very educational! My developer experience with MongoDB Atlas and Google Cloud has been fantastic overall, and I'll be using their products for my personal projects and freelancing from now on. What's next for InstaYum The next step is to add some AI features! What if you could make a query by just taking a picture of what's in your fridge? That would be quite simple to do with some image recognition AI. Or use actual NLP to extract the ingredients from the query! I also want to add a fridge/pantry inventory management feature to take the InstaYum experience to a whole new level. Not only individuals, but restaurants and cafes would be very interested in using the app too! Disclaimer: InstaYum! doesn't use AI in the strict sense of the word yet. I said that for branding purposes. :) <div