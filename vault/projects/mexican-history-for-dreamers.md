---
slug: "mexican-history-for-dreamers"
url: "https://devpost.com/software/mexican-history-for-dreamers"
title: "Wine Expert Plus"
hackathon: "Alexa Skills Challenge: Alexa Conversations"
organization: "Amazon"
winner: true
words: 612
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/retail_commerce"
  - "user/small_business"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# Wine Expert Plus

> First impressions count. And wine pairing really is a thing – get it wrong and you’ll be put off wine. That’s where Wine Expert Plus comes to help: get tailored recommendations tailored to your meal.

[Devpost](https://devpost.com/software/mexican-history-for-dreamers) · hackathon [[Alexa Skills Challenge- Alexa Conversations]]

## Facets

**domain** [[agriculture_food]] [[retail_commerce]]
**user** [[small_business]]
**substrate** [[code_repository]] [[document_pdf]] [[structured_db]]

**stack** axc, javascript, lambda, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for wine expert plus
- skill id, skill name

## Body

Wolfie the Sommelier, Wine Expert Plus Ambassador, is here to help! Inspiration I come from a wine culture. My grandparents used to grow grapes and prepare wine at home. It was not the refined experience we have today, but food wasn’t as varied either, and people were more focused on nutrition than enjoyment. The first time I walked a supermarket aisle chock-full of wine bottles, I almost got dizzy with so much choice. I only knew white and red. Where to begin? Little by little, through many years of joyous trial and error, and some wine tasting courses, I learnt to pair food and wine. But my case is special, I would not be put off wine due to a bad experience – wine runs through the veins of my ancestors and, on some evenings, through mine as well! I have many friends, however, who said they hated wine … until I introduced them to the stuff gradually. It’s time to share this knowledge to the world, and Alexa is here to help. What it does Wine Expert Plus is a simple skill that recommends you what wine to have based on what you will have to eat. It takes broad categories (red meat, fish, vegetables…) as well as more precise descriptions of your meal. The recommendation is twofold: it will suggest a wine category (red wine, white wine, sparkling wine,…) as well as a geographical denomination (Champagne, Cava) or a grape type (Cabernet Sauvignon, Merlot…) that will be recognized by any wine merchant, even supermarket staff, making wine shopping an undaunting experience. How I built it I built it fast! Thanks to Alexa Conversations, the creation and curation of likely dialogs covering the possible scenarios in a natural language conversation is a breeze. The bulk of the work is in the creation of content. I created a relational database (Microsoft Access) to create the list of wines and foodstuffs, and to document the wine and food matches. Then I used SQL queries to generate the JSON files that serve as data repository to the skill’s back end. As this content is static and not too large, I decided against using a database (Dynamo, Aurora): this would have been overkill. Challenges I ran into I had created Alexa skills before and that was both a blessing and a curse. I had a good sense of what I wanted to do and how to design the interaction model, but the shift of core concepts took me a little while to get used to. The UX of a beta service is of course evolving and it could be unstable. Most changes were for the better and I experienced just a couple of issues. Accomplishments that I'm proud of Well, certifying this skill in less than 48 hours would be a tremendous achievement! Also check out the logo. Wolfie the Sommelier deserves his minute of fame! What I learned Witnessing how Amazon has brought AI/ML to the creation of the interaction model is pretty rad. Especially if I consider how it was just two years ago. I remember having to write code to automatically generate the possible string combinations for the sample utterances, intent by intent. Now AXC takes care of that. What's next for Wine Expert Plus More synonyms for the food categories so that more dishes are understood by the skill. Eventually, being able to purchase wine directly from the Skill is an obvious evolution, but we shall see. I would also like to add visual responses with pictures of the regions where the recommended wine comes from, or snapshots of the grape types. Skill Id, Skill Name amzn1.ask.skill.cc83f55a-7486-45a5-a2cc-90969d1b7e9c Wine Expert Plus <div