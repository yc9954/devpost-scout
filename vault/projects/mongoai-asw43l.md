---
slug: "mongoai-asw43l"
url: "https://devpost.com/software/mongoai-asw43l"
title: "MongoAI"
hackathon: "MongoDB World Hackathon"
organization: "MongoD"
winner: true
words: 770
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/transportation"
  - "user/developer"
  - "user/frontline_worker"
  - "user/general_public"
  - "substrate/structured_db"
---

# MongoAI

> Backend-as-a-Service tool for the Unity Engine to automatically evolve your AI by collecting data from every instance of your game and running a Genetic Algorithm

[Devpost](https://devpost.com/software/mongoai-asw43l) · hackathon [[MongoDB World Hackathon]]

## Facets

**domain** [[developer_tools]] [[transportation]]
**user** [[developer]] [[frontline_worker]] [[general_public]]
**substrate** [[structured_db]]

**stack** c#, mongodb, unity

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for mongoai

## Body

Using MongoAI in Unity Engine Easy Visual Editor allows you to define and pick what genetic properties are stored How MongoAI works Import the package Easy to import the package Inspiration As a Unity Developer, I always strive to create useful tools for myself and other developers. One issue that I have been having with a game I've been working on is developing challenging and engaging AI for players. This project solves that issue. Genetic Algorithms are a good solution to optimize and evolve parameters in game development. However, they require a very large dataset to be effective. MongoAI solves that issue by providing a Backend-as-a-Service solution that aggregates all AI data on every single instance of your game. A user (a game developer) can program their game to "save" the data. Under the hood, this tool will send their data to Stitch, which will store it in a MongoDB Atlas instance. When you want to Instantiate a new object with optimized AI parameters, you just tell the tool you want a new child, and MongoAI will look through the Atlas Database, pick the fittest "genes", and apply a Genetic Algorithm which gives you back your parameters. Tests I conducted have showed how well this data aggregation feature works. I first tried multiple tests with an Example project to see how long evolution would take. In this example, there is a Box with RGB values, and these RGB values would evolve over time to achieve a desired color. When running 1 instance, it took on average 53 generations--a long time for evolution for a game. When running 2 instances concurrently, it took about 16 generations per instance. When running 4 instances, it took less than 10 generations per instance. By collecting more data from every single instance, MongoAI enables faster evolution for your parameters. In a world where gamers are smart and always getting better, you need to quickly evolve, or your AI will no longer remain exciting and engaging to play against. The speed at which MongoAI enables evolution will present a challenge to your players and keep them involved with your game. What it does MongoAI abstracts all the hard stuff--data collection, data storage, running the algorithm, caching data, and so on--allowing you to focus on the fun part: Watching your AI evolve over time. All you need to do is download MongoAI, Import it into your Unity game, and call MongoAI whenever you want to store or load AI parameters! Check out https://github.com/jgbakke/MongoAI-Documentation for the Documentation on how to get started! How I built it I used Mongo Atlas to store data, Stitch to execute functions, and the Unity Engine and C# for the MongoAI Driver. Challenges I ran into The MongoAI Driver connects to a Mongo Atlas Cluster, so I needed the MongoDB C# driver to work with my project. Unfortunately, Unity is still using an older version of C#. (4.x) So I was unable to use the newest version of the .NET Driver to work in Unity. It took a ton of work before I was able to get an older version to work with Unity, but once it started working and I was calling Stitch functions from within Unity, it was super cool! Accomplishments that I'm proud of I found very, very few links online for getting Mongo Atlas and Stitch to work with Unity. Nothing on StackOverflow, Medium, or any of my other usual sources when I run into a problem. I had to figure it out on my own and I'm really excited that I got it to work. Furthermore, from my research online, it looks as if not many people have used Stitch with Unity before. I can truly say I was among the first people to use Stitch with Unity. It feels great knowing I came up with an innovative use-case with 2 great technologies, and was able to pull it off! What I learned I have used Mongo before, but I had never used Atlas or Stitch so I had a ton of fun with that and plan to use them at my future hackathons I go to. I think that Stitch is really cool and hope to continue learning more. What's next for MongoAI I am looking into offering this as a Backend-as-a-Service. After the hackathon, I plan to release a Beta version to a subset of the public, so if you are interested in being part of the beta let me know. After that, I plan to sell this as a product to the public to help other game developers create rapidly-evolving AI for their games! <div