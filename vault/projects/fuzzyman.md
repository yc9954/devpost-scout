---
slug: "fuzzyman"
url: "https://devpost.com/software/fuzzyman"
title: "Fuzzyman - A Postman Fuzzer"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 376
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/web_dom"
---

# Fuzzyman - A Postman Fuzzer

> Fuzzyman takes your Openapi 2.0 spec and creates a fuzzed collection of your API to help discover bugs and vulnerabilities. The tests can be run with postman runners.

[Devpost](https://devpost.com/software/fuzzyman) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]] [[security_privacy]]
**user** [[developer]]
**substrate** [[web_dom]]

**stack** docker, flask, gcp, jquery

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that i'm proud of
- what we learned
- what's next for fuzzyman

## Body

Fuzzyman Inspiration Despite having worked for the inventor of fuzzing, I have never worked with fuzzers myself. Most applications have unit tests, but lots don't have easy to use fuzzers. After doing some research on fuzzing in the postman ecosystem, I did not see an existing solution, so I decided to make one. What it does Fuzzyman allows you to upload your OpenApi 2.0 Spec, and it will generate a new collection of fuzzed requests automatically. By default, Fuzzyman creates five requests per endpoint fuzzing query parameters, path parameters, and arbitrary application/json body payloads. The output of Fuzzyman is static; if you would like to regenerate the fuzz test, you must rerun Fuzzyman. This tool is designed to be self-hosted, where the backend will automatically create the collection for you. Fuzzyman accomplishes this by leveraging a user-generated Postman API key that, in the future, you will be able to set as an environment variable. To demonstrate Fuzzyman's functionality on the hosted website to put YOUR fuzzed collection in YOUR workspace, I have added the ability to paste your Postman API key to create the collection on the client-side. If you do not have an OpenApi 2.0 spec to test this out with, I used OAI's petstore example which you can download from here: https://github.com/OAI/OpenAPI-Specification/blob/master/examples/v2.0/yaml/petstore.yaml How I built it This project was built with Flask, Jinja2, Jquery, and docker. I leveraged Prancer, an openapi parsing tool, to read the openapi spec. I hosted the project on Google Cloud Platform using Cloud Run. Challenges we ran into Learning how to use docker/docker-compose was difficult, but rewarding. In an effort to make this a self-hostable tool, it was a must. Additionally, I am not a front end dev, so creating a decent UI that was functional and aesthetic proved difficult, but rewarding. Lastly, I consider myself an openapi novice, and I learned about lots of different features and functionalities for future versions of Fuzzyman! Accomplishments that I'm proud of Converting an idea to reality Creating a functional docker-compose based application Building a decent front end. What we learned How to create a docker-compose based application What the Postman Developer API can do What Postman runners are What's next for Fuzzyman Add support for the following Openapi 3.0 Authentication <div