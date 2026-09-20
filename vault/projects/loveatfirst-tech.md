---
slug: "loveatfirst-tech"
url: "https://devpost.com/software/loveatfirst-tech"
title: "matchmadein.tech"
hackathon: "Hack the North 2023"
organization: "Techyon"
winner: true
words: 402
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "substrate/code_repository"
---

# matchmadein.tech

> Code Your Way to Connection: Where Shared Commits Lead to Committed Relationships.

[Devpost](https://devpost.com/software/loveatfirst-tech) · hackathon [[Hack the North 2023]]

## Facets

**substrate** [[code_repository]]
  <sub>weak: sensor_telemetry</sub>

**stack** flask, github, javascript, python, react, scikit-learn

## Body

Homepage After entering GitHub Username The user "favorited" Inspiration We’ve all been in a situation where collaborators’ strengths all lie in different areas, and finding “the perfect” team to work with is more difficult than expected. We wanted to make something that could help us find people with similar strengths without painstakingly scouring dozens of github accounts. What it does MatchMadeIn.Tech is a platform where users are automatically matched with other github users who share similar commit frequencies, language familiarity, and more! How we built it We used a modern stack that includes React for the front end and python Flask for the back end. Our model is a K-Means Cluster model, and we implemented it using scikit-learn, storing the trained model in a PickleDB. We leveraged GitHub's API to pull user contribution data and language preferences data for over 3 thousand users, optimizing our querying using GraphQL. Challenges we ran into A big issue we faced was how to query the Github API to get full representation of all the users on the platform. Because there are over 100 million registered users on Github, many of which are bots and accounts that have no contribution history, we needed a way to parse these users. Another obstacle we ran into was implementing the K-Means Cluster model. This was our first time using any machine learning algorithms other than Chat-GPT, so it was a very big learning curve. With multiple people working on the querying of data and training the model, our documentation regarding storing the data in code needed to be perfect, especially because the model required all the data to be in the same format. Accomplishments that we're proud of Getting the backend to actually work! We decided to step out of our comfort zone and train our own statistical inference model. There were definitely times we felt discouraged, but we’re all proud of each other for pushing through and bringing this idea to life! What we learned We learned that there's a real appetite for a more meaningful, niche-focused dating app in the tech community. We also learned that while the tech is essential, user privacy and experience are just as crucial for the success of a platform like this. What's next for MatchMadeIn.Tech We’d love to add more metrics to determine user compatibility such as coding style, similar organizations, and similar feature use (such as the project board!). <div