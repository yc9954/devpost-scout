---
slug: "posteddb"
url: "https://devpost.com/software/posteddb"
title: "PostedDB"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 315
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# PostedDB

> Standalone indexedDB database reachable from Postman requests and scripts.

[Devpost](https://devpost.com/software/posteddb) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[structured_db]]

**stack** amazon-web-services, indexeddb, javascript, node.js, postman

## How they structured the write-up

- inspiration
- what it does
- challenges we ran into
- accomplishments that we're proud of
- getting started
- hosting posteddb sever (optional)
- what's next for posteddb

## Body

Inspiration All API development platform like Postman is intended for traditional client-server apps, however most of them as far as offline apps implements client-side database feature, as it happens: indexedDB. Browsing and browsing the web..I still haven't found any collaboration platform that simplifies building an API for this kind of service. So the challenge is launched... What it does PostedDB is a tool pair of API and chrome extension as standalone indexedDB database reachable from postman requests and scripts. Thereby, Postman leverages the full power of indexedDB data structure to write and execute more complex scripts. Embded code snippet generated in Postman visualize allows developers to build a complete application with indexedDB in few minutes. NB: Go to extensions management and click background page to view your indexedDB database Challenges we ran into Break client-side database scope barrier and overcome postman environnement isolation property. Accomplishments that we're proud of Deeply improvement skills in building and testing API requests in Postman. Getting started 1 - Download postedDB chrome extension here or get it in the "Try it out" links below. 2 - Open the Extension Management page by navigating to chrome://extensions . The Extension Management page can also be opened by clicking on the Chrome menu, hovering over More Tools then selecting Extensions. 3 - Enable Developer Mode by clicking the toggle switch next to Developer mode . 4 - Click the LOAD UNPACKED button and select the extension directory downloaded earlier. 5 - Fork PostedBD workspace and start coding. Hosting PostedDB Sever (optional) if you want host remotely or locally PostedDB server for your own purpose, download the source code here , and go to PostedDB_chrome_extension > background.js then change this config to suit your need: var socket = socketClusterClient.create({ hostname: '127.0.0.1', port: 8000 }); What's next for PostedDB Community feedback for more variety of common and particular configuration to build great API workflows. <div