---
slug: "get-dummy-data-6getqf"
url: "https://devpost.com/software/get-dummy-data-6getqf"
title: "Show me the dummy data"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 873
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/general_public"
  - "substrate/structured_db"
---

# Show me the dummy data

> Generate dummy data that matches all the attributes in your API schema.

[Devpost](https://devpost.com/software/get-dummy-data-6getqf) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[general_public]]
**substrate** [[structured_db]]

**stack** express.js, kubernetes, mongodb, node.js, postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next

## Body

Inspiration When a new feature is being added, sometimes I need to start the front-end work while the API is not yet available. My only choice then is to hard code some dummy data to populate and test the front end code. The task itself is straightforward enough, but when I need quickly come up with a list of boilerplate users, each with names, addresses, heights, eye colors, and 8 other attributes, I wish there is some way to just quickly get some random dummy API responses. I also wish the data will be in the exact response format with all the object attribute keys, this way, I can write FE response parsing code right away, without waiting for the actual API to be available. What it does Quickly generate dummy data that will have all the attributes the user-defined. No more need for hard coding or using your friends' names for dummy boilerplate data. Get a list of objects like users with both standard attributes such as string , boolean , int , or with some pre-build custom data types such as address , city , postal/zip code , color and more. The public workspace included two collections. All the APIs for the custom dummy data generator is included in the workspace collection called Build your own , I've also included a list of 3rd party public available dummy data APIs under collection Off the shelf . How we built it Initially, I set out to collect different existing public APIs that offer dummy data, but soon I realized the options are rather limited. Some sites offer dummy data only via their web site UI, moreover, also the user can't define or change response keys and data types. Moreover, there are some public domain datasets that can be useful in creative ways for application testing or use as boilerplate but they exist in large CSV files or other formats and could be difficult to just quickly get a few random samples. The solution I come up with is an API service, where the user can define their own data attributes in the response. For example, an API to get a list of users with names, favorite sports team, running speed, etc. With this service, front end developer can write all their response parsing logic and even test how application response with real async server call, all while the actual API is still under development by coworkers. Back-end developers and testers can also use this service to get some random dummy data to populate the development database or write some test cases with the data generated. Challenges we ran into Setting up HTTPS in Kubernetes for the first time is a real pain. I probably worked through 6, 7 different error messages to get it finally working. Searching and adding custom data type lists could be time-consuming. It would be nice users can build their own list, say "superhero powers" and share it with others. Accomplishments that we're proud of Built something I can use for myself and hopefully also make other follow developer's work just a little bit easier. Very happy to have a working MVP from idea to a running public server in about a week and a half or so all on weekends and evenings, with all the essential elements such as persistent data store, request validation, CORS, HTTPS, unit testing, CI/CD, documentation, postman API monitoring with test validation. The app is also set up in a micro-service enabled architecture with Kubernetes which makes it easy for adding features, scaling capabilities in the future. What we learned Creating documentation with Postman collection is a breeze, I wished I discovered this earlier! Collection API monitoring is very helpful, really put my mind at ease with deployments. Working with a time window that I cannot change really helped me to think critically about what features to prioritize and what unknowns to avoid to get a minimum viable product up and running as quickly as possible. What's next The main focus of the app is to make generate dummy data as effortless as possible, and encourage public collaboration. The most important feature to add next would be to allow people to create their own data type lists and share them with the public. For example, some user can create a list of liquor names, if another user wants to build a cocktail generator app, they can search for existing public data types collections, and simply specify a field with type liquor_name , then he/she will be able to quickly generate lists of random liquor names in their dummy API response. Some other technical Improvements: - Add the ability to create a response with nested objects, for example, a purchase order object response with a list of product IDs in it. Add min and max parameters for numeric data types to give the user more control over the API response. Add some mechanism to parse API schema in a standard format such as OPEN API, this will make it even easier to get dummy data based on the existing schema. Add user module, so people can create a user account and track a list of dummy data schema they created in the past <div