---
slug: "cardtank"
url: "https://devpost.com/software/cardtank"
title: "CardTank"
hackathon: "Devs Unleashed"
organization: "Atlassian"
winner: true
words: 589
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# CardTank

> CardTank allows you to visualize and interact with Jira boards by rendering them as fish tanks. Each task is a procedural fish you can filter, sort and assign. Explore your cards in a different way!

[Devpost](https://devpost.com/software/cardtank) · hackathon [[Devs Unleashed]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** dreambooth, forge, gcloud, golang, jira, phaser.js, stabledifussion

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that i'm proud of
- what's next for cardtank

## Body

Inspiration I tried to find a way to make the process of checking our Jira board a bit more exciting. Giving cards some character might make some parts of the development cycle a bit more entertaining, enabling developers to "collect fishes" while completing cards sprint after sprint. What it does Forge App The Forge App allows CardTank to embed a single-fish tank in a Jira description. Once installed, the component will display a procedural image of the fish representing the card. This sprite depends on the attributes of the card, and it is updated regularely based on its status. Additionally, the Web Application is able to render and display the status of all the cards in a given sprint, retrieved directly from Jira REST API. The main features included in the Web Application are: Rendering all the cards in a sprint as fishes Displaying fish details Fish sorting Fish filtering Evasion game Custom board loading Fish lab Assignation mode How I built it I started by looking for open-source game sprites of fishes that feet the customization level I was looking for. I finally opted to use Stable Diffusion (Dreambooth) to generate the base sprites of the fishes and implement a short algorithm that used the "body" and "fins" sprites separately to apply color, animate (by applying a sine wave function to the fins and changing the sprite's hue). With the sprite generator in place, the rest was straightforward. Both frontends use Phaser to display these procedural images, and provide a set of client-side functions (sorting, filtering, etc) on top. Challenges we ran into Image generation : The main challenge was to identify and map Jira card properties to fish attributes in a way that the card stayed identifiable across it's life cycle while showing variable state (such as "the time without any updates") Phaser integration : While consuming the procedural images in simple (as they have the Content Type image/png ), integrating them with Phaser presented some new challenges. This was mainly because the game engine needs to know the image size to correctly represent the animation before actually loading the image in memory. Accomplishments that I'm proud of I have very little frontend experience, and being able to build a dynamic representation of the fish tank was fulfilling. In the same note, learning React to integrate with Forge was rewarding, even when the Forge App itself is super simple. What's next for CardTank Now that I have the basic integration, there are a lot of features and improvements that can be added: Write operations : Allow users to handle some operations from the tank directly (such as assigning cards or updating the status) Procedural backgrounds : The background is currently a baked image. But we have all the tools in place in order to make a custom background for each sprint (depending on the amount of cards, sprint goal, swimlanes, etc) More fishes and AI generation : The current images are generated from a fixed amount of fish templates. If we can hook DreamBooth directly to the backend with consistent results, then every fish can be unique Stateful backend : For simplicity of development and setup (and since users can link their own credentials), I decided not to include any sort of repository layer. But with a database, CardTank will be able to generate and store new data for every card! Do you want to feed a fish, showing how hyped you are for a task? Do you need to show concern about your fish's health? <div