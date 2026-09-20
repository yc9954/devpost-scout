---
slug: "pronoobs"
url: "https://devpost.com/software/pronoobs"
title: "DotCloud"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 511
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# DotCloud

> A safe and smart way to save the .env

[Devpost](https://devpost.com/software/pronoobs) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[structured_db]]

**stack** azure, node.js, npm, postgresql, postman, typescript

## How they structured the write-up

- inspiration
- the reason
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dotcloud

## Body

Logo Working Principles Inspiration 10 minutes into every git init , we create a .env file to store all our confidential variables and worry every time that we did not push it to the codebase. DotCloud is a simple cloud hosted .env management solution that would help you reduce the risk of manually handling sensitive keys. The Reason Have you faced issues in managing your .env variables? Are you risking exposing sensitive keys to other contributors or interns at your organisation? Do you need to temporarily provide access to certain key to someone? Do you need a solution where you don't need to migrate your .env variables as you jump across hosting? Would you like a place where you can manage all your .env varibles of all projects in one place? DotCloud is a simple solution to all the aforementioned problems. What it does DotCloud is an API that holds all your project's environment variables securely so that they can be accessed any time by an authorized user or a server with a valid API token. You can create organizations and work in a team, allow your developers to access a specific key only for the duration you give them access to. A single API call is all you need to fetch all your keys for your project. All the hassle has been handled by DotCloud, so sit back, open Postman, and enjoy the API. All you need to do is use our API directly or our npm package that we've published and you're good to go. You can explore and run our collection directly on Postman. How we built it We used Typescript along with NodeJS and Express. For the database, we've used a Postgres database. We have also built an npm package so that it is even easier for the developers to use our API and collection. We used Postman for collections, monitoring of the API and even Mock API feature to debug and test throughout development of the API and the collections. Challenges we ran into We came across a lot of corner cases for our API which set us back with a lot of time Postman Visualiser does not support its Dark Mode efficiently like it does not invert the colors automatically thus we had to make some changes to our visualizer template. Accomplishments that we're proud of We have handled and built a very robust API that can handle many corner situations. We created and published an npm package which helps to bind DotCloud in a very simple way. We learned about so many Postman features we had no clue about before this. What we learned We got to explore various Postman technologies such as Monitoring System and Automated Runners. This also helped us collaborate very easily from remote locations. What's next for DotCloud We plan to devise a frontend for our API so that everybody can access it easily and quickly. We have published an npm package for DotCloud, we plan to add more features and expand it to other famous web frameworks too. <div