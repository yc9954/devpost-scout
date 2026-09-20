---
slug: "hashouse"
url: "https://devpost.com/software/hashouse"
title: "Hashouse"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 372
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "user/developer"
---

# Hashouse

> A crypto based API to serve low computing powered devices

[Devpost](https://devpost.com/software/hashouse) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[developer_tools]]
**user** [[developer]]

**stack** api, cloud, flask, hash, heroku, python, requests

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hashouse

## Body

Postman documentation Inspiration I really loves to solve problems that are simple but would reflect very big value in the developers or techies needs. I was inspired to do something creative as it is my first exposure to flask framework and API frameworks and most importantly my first exposure to collections and postman. What it does Hashing have become a crucial part of cryptography and cyber security, Expanding our forefronts to IOT devices and multiple light weight devices the power of computing would be low. With advancements in wireless technology a low latency network is now available around the globe so when migrating the workloads of computing hashes and security related algorithms to cloud would make it more fast and secure with non tamperable request logs. And example for request would be as follows curl https://hashouse.herokuapp.com/hash/md5?query=Sup3rS3CR2TP@ssw0RD# would return { "algo": "md5", "result": "322d3b5dcd59d841c69819b348d739ee" } How we built it Python was my favourite language but for production I thought of using a framework and hence I found flask framework. Flask is very easy to build a prototype product. I got help with python hashlib library to compute out the calculations and a jsonify library to make it a standard JSON output Challenges we ran into I have wandered more than an hour to add another request into a collection. It was actually a simple save button. It was the community who helped me also for the code, Also I am not that good with front-end of the project so link in browser wont be that good but I`m working on it as I am writing this Accomplishments that we're proud of Learned API Learned a lot about Postman, Will contribute more to public library of postman Found a good framework to test, execute and work on API`s of a project Got more deep knowledge in JSON and API related stuff What we learned First of all I learned a lot about postman and APIs, I learned how to write APIs so next time when I do project I would know to write APIs and serializing APIs What's next for Hashouse Scale it up to an application which can handle millions of requests in parallel, Scaling it to kubernetes to handle concurrent requests <div