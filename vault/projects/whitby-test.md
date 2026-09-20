---
slug: "whitby-test"
url: "https://devpost.com/software/whitby-test"
title: "Rankings.lol"
hackathon: "Global Power Rankings Hackathon"
organization: "Amazon"
winner: true
words: 752
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "user/legal_professional"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Rankings.lol

> LoL power rankings + prediction of games website.

[Devpost](https://devpost.com/software/whitby-test) · hackathon [[Global Power Rankings Hackathon]]

## Facets

**user** [[legal_professional]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** amazon-web-services, javascript, machine-learning, next.js, pandas, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for rankings.lol

## Body

Feature Importances AWS Diagram Correlation Matrix (Shortened) Inspiration We wanted an app that would help us win pickems this year. Joking aside, we wanted to make a website from scratch that would be fun to use and we wanted to see what we could make in a short timespan. It's always fun to learn new things and get your work judged by representatives of two companies that you admire. We think we were able to deliver a fun experience and we hope you believe the same. What it does The website and the API both generate a list of all teams in the world, with additional filtering. It also has fun aspects like radar chart visualizations, predicting match outcome, predicting draft, and predicting the knockout stage. How we built it We first gathered all the game data using python, and then did analysis on it using pandas in a python notebook. To generate the rankings list we found the gathered a list of features of a league game at 5 minute intervals up until the 20th minute, and then we used a Random Forest Classifier to see which features were the most important to win a league game. After that we normalized each team's mean performance and then multiplied the score in each category/feature by the importance of that feature, and then we summed up those scores to come up with a total score for that team. We then created an elo calculation script to see what each team's elo would be. After we did that, we multiplied the scores by the elos to come up with a blended list to see who the best teams in the world are. For the tournament API, we used a linear regression model to find the time variant score of each team going into the tournament. This also blends with the feature importances along with our region multipliers to get a relative rating for each team. At runtime, we resolve a tournament ID to a unix time, and use that to solve the regression, which we use to sort the teams to get the rankings of the teams going into the tournament. All this info was put into a Flask backend application and a Next.js application to have the data readily available. All the additional information on how we built this application as well as images to support the description can be found on the website itself at https://rankings.lol/methodology . Challenges we ran into Some team names were missing from the set, and it was hard to identify who they were just by looking at the raw data, so to ensure that we had all the teams that we needed, we created a data set to look the results of the summer split for each region and filled in the names by using their summer split record. Creating the starting elos for each region also required a lot of looking at international tournaments and seeing how each region did against each other. We needed to do this we needed to stop the Istanbul Wildcats from being the best team in the world. It took a ton of iterations to find a starting elo that made sense. There were a ton of front-end issues that came up as well since this was our first time making a react website from scratch. Accomplishments that we're proud of Our list looks super realistic! It even has some interesting things like G2 possibly being better than T1, and Cloud9 being a top 10 team with a chance to make quarters. We think our website looks great, it's fun to use and easy to understand. What we learned We learned a lot. We had never made a publicly available website before, and we never really used Next.js or even React to make a website from scratch. We also learned a ton about the services that AWS provides, with the most exciting one being App Runner as it made deployment of our backend so easy. What's next for Rankings.lol So this can also be found on our methodology page, but the next steps are: Set up a staging environment (improved operational excellence) Infrastructure as code through CloudFormation (improved operational excellence) Migrate to AWS Fargate (cost savings) Embed UX analytics via Google Analytics (gather data to improve customer experience) Enable PWA (offline support and improved customer experience) Improved backend model (better accuracy and lower latency) Set up lazy loading + code splitting on the frontend (reduce time to First Meaningful Paint) <div