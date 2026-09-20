---
slug: "rss-to-discord"
url: "https://devpost.com/software/rss-to-discord"
title: "Postman Sherlock"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 496
team_size: 3
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/runtime_tool_creation"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Postman Sherlock

> 🔍❤️🚀 Hunt down social media accounts by username across social networks, from inside Postman!

[Devpost](https://devpost.com/software/rss-to-discord) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[graph_reasoning]] [[runtime_tool_creation]]
**substrate** [[code_repository]] [[structured_db]] [[web_dom]]

**stack** postman, sherlock

## How they structured the write-up

- inspiration
- what it does
- how it works
- what we learnt
- challenges we ran into
- what's next

## Body

A port of Sherlock to Postman Workspaces. Try it out here Inspiration Using Sherlock to solve open-source intelligence challenges in capture-the-flag competitions. Then later wondering how they managed to make such a tool and how it operates under the hood. What it does Sherlock is a command line utility written in python. You supply it some username and it generates a list of social media services and other websites where that username has been registered. This is useful for things like capture-the-flag competitions, finding out how common a username is or stalking people on the internet 🤔. Postman-Sherlock loads data from Sherlock source code and provisions a new Postman Collection on the fly that mimics the Sherlock tool, allowing you to do account enumeration of 270 social media services from inside of Postman. All of this is done within a single Postman Workspace using test scripts. That's a lot of requests How it works This workspace comprises two main collections, the generator and the enumerator. On running all of the first generator collection, it: Fetches the webservice database and specification file off the Sherlock Repository , which instructs the original tool how to detect if an account with some username exists on various services. Uses Postman Test scripts to convert each service listed in the specification file into a single Postman Request item inside a new collection. Generates javascript tests on the fly for each service to emulate the account detection logic within the Postman Tests; and Uploads the new collection to the workspace via the Postman API, creating the enumerator collection. Using this collection, we can dynamically generate the second enumerator collection any time there is an update to the Sherlock webservice database. On running all of the second enumerator collection and supplying it with a username environment variable, it: Makes a request to each endpoint specified. Uses Postman Test scripts to determine if the username has or has not been registered. Each passed test in the summary then indicates that an account has been registered with that username. With this workspace, not only can you effectively run the Sherlock tool from within your web browser using Postman Web, but you can also better understand the detection logic of Sherlock by looking at the generated tests. 61 accounts tied to username watson were found! What we learnt Not every API needs a pretty JSON output to he meaningful. Sometimes scraping HTML or access codes gives you all the information you need. Challenges we ran into We put javascript in our javascript and thats hard to debug 😅. Yo dawg I heard you liked javascript What's next Connecting the generator collection to Google's knowledge graph to generate brief descriptions on what each webservice is. Implementing the Sherlock unit tests inside a collection and hook that collection onto a Postman monitor - to periodically check that the webservice database is up to date. Also please ignore the devpost permalink, we updated our project midway through haha <div