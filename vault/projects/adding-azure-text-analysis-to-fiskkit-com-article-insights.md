---
slug: "adding-azure-text-analysis-to-fiskkit-com-article-insights"
url: "https://devpost.com/software/adding-azure-text-analysis-to-fiskkit-com-article-insights"
title: "Adding Azure Text Analysis to Fiskkit.com Article Insights"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 473
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/structured_db"
---

# Adding Azure Text Analysis to Fiskkit.com Article Insights

> Add sentiment analysis to each sentence of articles submitted to the Fiskkit.com online discussion system, as well as Named Entity awareness/highlighting/aggregate sentiment

[Devpost](https://devpost.com/software/adding-azure-text-analysis-to-fiskkit-com-article-insights) · hackathon [[Azure AI Hackathon]]

## Facets

**substrate** [[structured_db]]

**stack** amazon-web-services, lambda, mysql, python, rds, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for adding azure text analysis to fiskkit.com article insights

## Body

Inspiration Our inspiration is the terrible state of our public discourse, both in terms of how accurate information is that people put online, and also how people treat each other. We want to use analytics and design to build a better public discourse. What it does This demo is an extension of Fiskkit.com, and public discussion tool. This demo (rates the sentiment of each sentence in the article / rates the aggregate sentiment of all of the comments on each sentence in an article). It also identifies Named Entities in an article submitted by users, shows the aggregate sentiment of all the sentences the entity is named in, and allows the user to click on the Entity to toggle highlighting the sentences in the article where that entity appears. How we built it First we looked through the available APIs and selected Text Analysis as something that would be really helpful to the Fiskkit project. We did an initial design in Figma and refined it in a team check-in. We sent each sentence in the article and created a list of Named Entities of Type Person, Location and Organization. In the first version, we fed the sentiment results to the frontend to display in-line of the article on the Fiskkit Insight Page. Then we averaged the sentiment scores of each sentence containing a Named Entity and showed that at the bottom of the page. Then we got all of the immediate child-comments of each sentence in the article from Fiskkit’s comments, and sent those for sentiment ratings, and displayed those in-line in the article. Lastly, we set the Named Entities list at the bottom of the article to be clickable so they will toggle highlighting of the sentences that contain that entity. Challenges we ran into Because we were sending every sentence of an article for sentiment rating, as well as all the aggregate text that contained each named entity, and all the comments in Fiskkit for each sentence… we ran short on API calls and had to switch to just a couple sentences towards the end. Accomplishments that we're proud of We scoped our goals pretty well and achieved all of them in one weekend (plus a little more). We also think this is an actually very useful piece of functionality to add to a public discussion for social good! What we learned We learned that it is really quick and easy to use such off-the-shelf 3rd Party APIs as long as they are well-documented, and this will inform our thinking going forward. What's next for Adding Azure Text Analysis to Fiskkit.com Article Insights We want to test the accuracy of the sentiment ratings of the API on a larger data set, and also iterate the UI design to see what is the best way to present this information to users. <div