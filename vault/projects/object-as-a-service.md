---
slug: "object-as-a-service"
url: "https://devpost.com/software/object-as-a-service"
title: "Object as a service"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 394
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "domain/civic_government"
  - "user/general_public"
  - "substrate/web_dom"
---

# Object as a service

> A object creation service per domain, where you can merge objects together. It should be a standard convention. You can create your own simple or detailed object, easily.

[Devpost](https://devpost.com/software/object-as-a-service) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[civic_government]]
**user** [[general_public]]
**substrate** [[web_dom]]

**stack** amazon-web-services, angular.js, api, cognito, dynamodb, serverless, stripe

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for object as a service

## Body

Inspiration Hard to define scalable / reusable objects, you often redesign the object. What it does It is a service, which use standard convention per domain and metadata. You can create your own object easily, by selecting sub-domains, merging / linking domains, and include / exclude variables. How we built it Start with defining data types for standard convention, like date, time, weight, currency, country, city formatting. This should be consistent across the whole service. Each domain expert can create objects, that has related keys (variables). It can be restructured in nested objects (sub-objects) as well. For example: Car: { brand, model, ... } You can easily select or deselect variables that you want to use or not. Challenges we ran into Building a prototype, just started at the last day. Accomplishments that we're proud of I have thinking about this concept for quite a time. If all companies use the same kind of standard convention, it will be more easy to integrate 3th party apis. You will understand the object, without having to guess or read the documentation about the keys (variables). Also, it is easy to scale, because objects can easily be merged or added. You don't have to reinvent the wheel each time when you create an object. Just go to the object as a service provider, select the 1 or multiple domains you are in, find which variables are usually stored and why (documentation). For example... For a car, the key or object license plate (is interesting for government, to connect a citizen to a car license plate, for a car market place, to verify if it is a valid car). What we learned It will be a big graph network of objects at the end. Which is pretty cool. What's next for Object as a service Make a prototype, test if it works. Think about the future, should we host it, so objects can be created easily using an api? When you create an object from the website, it returns a unique Object ID, this object ID can be called through an api, so the more it is used, the popular it will be. And recommended for others to use. You can integrate it with postman in the future to test your own or other API, including the object ID, and maybe add even test data to it. <div