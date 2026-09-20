---
slug: "spilt-coffee-gwzinv"
url: "https://devpost.com/software/spilt-coffee-gwzinv"
title: "spilt coffee"
hackathon: "Facebook Hackathon: AI"
organization: "Facebook"
winner: true
words: 569
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "user/small_business"
  - "substrate/structured_db"
---

# spilt coffee

> Media monitoring and brand reputation trends powered by AI.

[Devpost](https://devpost.com/software/spilt-coffee-gwzinv) · hackathon [[Facebook Hackathon- AI]]

## Facets

**user** [[small_business]]
**substrate** [[structured_db]]

**stack** django, firebase, heroku, postgresql, react, square, twitter, wit.ai, yelp

## How they structured the write-up

- ✨ mission
- 📈 features
- 🧱 architecture
- 🔮 nlp model
- 💻 tech stack
- ✔️ to do
- 👻 fun facts

## Body

spilt coffee screens (search history, results, competitive analysis) spilt coffee logo GIF spilt coffee animation ☕️ spilt coffee Media monitoring and brand reputation trends powered by AI. We help small businesses use wit.ai to take control of their brand by giving them instant access to and sentiment analysis on mentions across social, reviews, news and more. ✨ Mission We believe everyone has room to grow and thrive. We commoditize big data for small businesses, reviews are better when they’re heard. No one should be left out because the cost is too great or the technology too complex. So we build easy tools to empower businesses to take control of their brand. Tools that make media monitoring, competitive analysis and reputation tracking effortless—spill the coffee. 📈 Features SEARCH We scrape data from Yelp, Twitter and News about your brand (and any brand), bucket reviews by sentiment and display results on user-friendly charts. MONITOR We automate searches to easily monitor brand sentiments over time, and display historical trends on this data. SENTIMENT ANALYSIS We utilize advanced sentiment detection tools like VADER and wit.ai to segment positive, negative and neutral mentions, and assign overall sentiment to each mention. COMPETITIVE ANALYSIS We allow businesses to compare and overlay competitor data with their own, keeping up to date with what the people are saying. 🧱 Architecture A brief overview of our application, with some key features (green) on the left and how we handle them on the backend on the right. 🔮 NLP Model MODEL Sentiment analysis was conducted based on an ensemble model aggregating both the VADER model and Facebook’s wit.ai NLP model. Train and test data was primarily formed from Yelp’s open data set (>8,000,000 user reviews) and the Sentiment140 Twitter dataset. IMPLEMENTATION We utilized wit.ai's sentiment analysis to rate and categorize reviews. We trained entity recognition to pull out and rank the most common entities in "very negative" and "very positive" reviews. We can then see what users tend to have issues with, and provide actionable recommendations to improve these businesses. ACCURACY Running our ensemble model on a subset (test) dataset, we achieved an accuracy 73.35% on a set of 2000 test Yelp points as well as a 74.25% for the Sentiment140 set on their given test set of 497 tweets. NEXT STEPS We hope to add more robust entity tagging as well as bi- and tri-gram recognition in order to better provide value for businesses. We also hope to extend the pre-trained wit.ai sentiment model to a five category model (very negative, negative, neutral, positive, very positive) for better bucketing. 💻 Tech Stack UI frameworks: ElasticUI Recharts Frontend: React.js Backend: Django DB: PostgreSQL Authentication: Auth0 Model: VADER wit.ai ✔️ To Do ☐ Provide helpful feedback and insights for businesses (actionable recommendations!). ☐ Perform more in depth competitor sentiment analysis, and ability to recognize competitors. ☐ Allow users to mark wrong sentiments (and correct them). Our models aren't perfect, we have room to grow too! ☐ We already provide a set of content marked as "extremely negative" or "extremely positive". Now, it's time to extrapolate reasons and analyze severity. ☐ Scrape more platforms (Facebook, Instagram, more news sources, etc.) 👻 Fun Facts In our first (virtual) meeting where we were struggling to decide on our product name, one member spilled coffee on himself—with that, "spilt coffee" was born. "8 million rows [of yelp review data] is a lot of rows." <div