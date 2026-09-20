---
slug: "hub-yvcpzw"
url: "https://devpost.com/software/hub-yvcpzw"
title: "Hub"
hackathon: "hack:now"
winner: true
words: 400
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
---

# Hub

> Rekindle team culture, learn about colleagues, and cultivate connections.

[Devpost](https://devpost.com/software/hub-yvcpzw) · hackathon [[hack-now]]

## Facets

**domain** [[developer_tools]]

**stack** python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hub

## Body

Inspiration As more and more teams go remote due to the COVID-19 crisis, we realized that building company culture and learning about your coworkers is more difficult than ever. We wanted to build a product to directly address this growing culture problem, with an emphasis on giving individuals a space to express themselves and share who they are. What it does With direct integration with Slack and (planned integration with) other workplace tools, we allow users to build and share profiles. Users can also search for profiles by team or by name, and can easily access the profiles of new hires, employees with birthdays, and employees with work anniversaries. They are also given suggestions to message users based on their own interests. How we built it We built the backend with Flask and deployed on Google App Engine, and built the frontend with React + Typescript. The entire application was created from scratch. Challenges we ran into We had never used Google App Engine in the past, and ran into issues with old versions persisting even after we opened new ones. It was also difficult to debug some of our React errors, and bootstrap networking in a short amount of time. Lastly, while debugging a few hours ago, our Slack API application was rate-limited and is currently prevented from making more requests. We hardcoded some data to account for this, but all of the code is present in the repo. We weren't able to get OAuth working, so all of the interactions are through the perspective of a single user. Out all of the data is pulled from an actual Slack repo that we populated with dummy users and information. We also tested all of our code on Chrome, and didn't test with other browsers. Accomplishments that we're proud of Although we initially believed that our idea was too ambitious and we wouldn't be able to get everything we wanted, we were able to focus on our MVP and have the product working end-to-end. What we learned As we weren't all together for this hackathon, we learned about working remotely and being able to communicate effectively. What's next for Hub We plan on adding integration with other platforms for easily importing employee data, and continuing to flesh out other features to build culture that we weren't able to get to during the hackathon: Coffee Chats Company Polls Profile Posts <div