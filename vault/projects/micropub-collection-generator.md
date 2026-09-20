---
slug: "micropub-collection-generator"
url: "https://devpost.com/software/micropub-collection-generator"
title: "Micropub Collection Generator"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 312
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "substrate/web_dom"
---

# Micropub Collection Generator

> The Micropub protocol is used to create, update and delete posts on a website. To simplify manual testing for different configurations, we'll autogenerate a Postman collection for your Micropub server

[Devpost](https://devpost.com/software/micropub-collection-generator) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[on_device_local]]
**substrate** [[web_dom]]

**stack** ruby

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of

## Body

Inspiration Micropub is an awesome standard, and makes it straightforward to have a standard API for interacting with content (on your website). I've been really enjoying it over the last year of working with it, and am really glad there's been some good progress to making a standard API for updating content. As part of the initial local development for my Micropub server, and before I had built my own client, whenever I was testing against my Micropub server, I used curl . Although this worked, it didn't help all the time, because I'd need to keep re-fetching access tokens, or I would accidentally use a production token locally. Another tool that is better targeted for this manual testing is Postman, especially - as I found out while working on this hack - that it has some great OAuth2 support, which integrates nicely with the OAuth2 extension, IndieAuth , that Micropub utilises. When I spotted the Postman API Hackathon , I realised that maybe I could look at making it easier to use Postman to test Micropub servers, and hopefully help other folks with sending requests to their servers in the future. What it does Given a profile URL, i.e. https://www.jvt.me , generate a Postman collection that can be used with the Micropub server for that user. How I built it A pretty hacky Ruby script! Challenges I ran into I'd hoped that this originally could've been a service that folks could simply point a URL to and generate the configuration required. Unfortunately this doesn't quite work, as most folks protect their configuration endpoint. However, I've managed to create a web app that performs an IndieAuth flow and allows generation of collections behind protected Micropub servers. Accomplishments that I'm proud of Got to play around with the OAuth2 support in Postman (and therefore better understand Postman's Authentication/Authorization support) and generating Postman! <div