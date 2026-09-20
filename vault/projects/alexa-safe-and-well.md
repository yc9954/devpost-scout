---
slug: "alexa-safe-and-well"
url: "https://devpost.com/software/alexa-safe-and-well"
title: "Safe and Well"
hackathon: "Alexa Skills Challenge: Tech for Good"
organization: "Amazon"
winner: true
words: 431
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/immigration_refugee"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# Safe and Well

> Have Alexa check on your loved ones in areas hit by natural disasters.

[Devpost](https://devpost.com/software/alexa-safe-and-well) · hackathon [[Alexa Skills Challenge- Tech for Good]]

## Facets

**domain** [[developer_tools]] [[disaster_emergency]] [[immigration_refugee]]
**user** [[developer]]
**substrate** [[document_pdf]] [[web_dom]]

**stack** amazon-alexa, amazon-web-services, moment.js, node.js, request-promise, underscorejs, voca

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- what's next for alexa safe and well

## Body

Welcome screen Most recent updates Initial help screen Help on setup Help on updates Main event loop display Showing all updates "Exit" screen Inspiration The instructions for the Alexa "Tech for Good" Skills Challenge mentioned "helping those in need after a natural disaster strikes." While it's not a natural disaster, my mind first turned to the separation of children from parents at the U.S. border and the incredible hurdles involved in maintaining connections and communication between people when life is thrown into chaos. My research into didn't reveal many accessible systems for establishing or maintaining contact through crises--apart from the American Red Cross "Safe and Well" system. Individuals affected by disasters can register on their system and leave messages about their current status and location. Friends and family can then search the registry based on name and phone number (or mailing address) and retrieve the status of their loved ones. What it does This Alexa skill provides two things: A way to create and store a list of people affected by a disaster. A voice-based frontend for easily retrieving updates from the Red Cross Safe and Well system. How I built it The skill was developed in NodeJS using version 2 of the Alexa ASK. After exploring several ways to make it easy for users to store and maintain a list of contacts, I decided to store this information in a specially-named Alexa list. Once this list has been created (by the skill) and populated with contact information (by the user), Alexa will search for updates from the American Red Cross Safe and Well registry and read them to the user. Challenges I ran into The American Red Cross Safe and Well system is an invaluable resource but it was not designed with ease of use or accessibility in mind. Anyone interested in using the system must manually enter a person's name and contact information each time in order to retrieve their status updates. Automating that process was difficult, though, because the only external access to the Safe and Well registry is through a post-submitted HTML form. Without a developer-accessible API, my skill emulates a form submission through an AJAX request and then parses the HTML response to find the update messages. What's next for Alexa Safe and Well Store the last date/time that updates were requested in order to let the user know if there are in fact new updates. Allow the user to request updates for specific individuals. Let users push their own updates to the Safe and Well registry from the skill (this may not be possible). <div