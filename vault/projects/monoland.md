---
slug: "monoland"
url: "https://devpost.com/software/monoland"
title: "Monoland"
hackathon: "Devs Unleashed"
organization: "Atlassian"
winner: true
words: 1483
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "domain/disaster_emergency"
  - "domain/labor_employment"
  - "user/frontline_worker"
  - "substrate/code_repository"
  - "substrate/geospatial"
---

# Monoland

> A tropical island adventure RPG featuring character customization where Jira Issues become farms to tend to and Jira Bugs become fierce slimes to battle. Be truly immersed in your work!

[Devpost](https://devpost.com/software/monoland) · hackathon [[Devs Unleashed]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[agriculture_food]] [[disaster_emergency]] [[labor_employment]]
**user** [[frontline_worker]]
**substrate** [[code_repository]] [[geospatial]]

**stack** bitbucket, confluence, forge, jira, phaser.js, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what does the name mean?
- what's next for monoland

## Body

The title screen of Monoland Select your project A farm showing 4 Jira Tasks at different stages. The tooltip can be clicked to change the status of them A group of people discussing the next sprint around a bonfire Other people workin on their own issues Two people fighting bugs (slimes) near a forest Inspiration We think that a good game built on top of Atlassian APIs needs to be one which people keep coming back to. It should not just be an existing game with random inputs taken from Jira data. It needs to add to the experience of using these products and not be a forgotten easter egg in the wide world of such apps. It would be great to make it fun and useful at the same time. This is how we arrived at the idea of building an RPG with a customizable character and the world’s elements not only representing the data from the APIs but also allowing them to be modified through the game. As you explore the world, you can see where your Jira Issues stand, who’s tending to them, what bugs they are fighting, what Confluence pages they are updating, which projects are being built, how large they are, what builds are broken, are there any alerts and a lot more. All of this data is aggregated to award achievements as people open/close more issues, write more commits and update more pages. This recognizes people’s work without it being implicit and without creating bad incentives. The only game you “play” is your actual work! Except that it’s now seen through a fun lens. What it does 🏝️ Monoland is a virtual island where you can interact with your Jira issues using your very own customizable Avatar. 🧑 Our character customization allows you to choose from over 3,700,000+ combinations, which means you can be your own unique self. 🌱 Jira Issues are farm crops which are tended to and grown by the person working on it. If the issue is in a To Do state, it is represented by a sapling, In Progress, a small plant, and Done, a fully grown crop. You can click on a farm crop (issue) to know more about the issue, transition it, or open up the jira page for it. You can see others working on their own crops too. 🐛 Jira Bugs are represented as slithery slimes ! As you make progress on the bug, you fight the slime and it’s finally vanquished once the bug is closed. 🌟 Earn Achievements which are awarded as stars in your profile. They are awarded when you reach specific goals, such as 20 issues closed or 100 commits written. 🪙 As you “play” through the game, you earn Coins for your work. These are completely virtual and allow you to upgrade your character by buying the merch and character customization you have always wanted. How we built it Since this was our first time building a 2D RPG, especially one that integrates external APIs and needs to be deployed to a JS environment, we went looking for a game engine or a framework. We explored CT.js, Godot, Unity, PixiJS, RPG Maker, Spline, etc. and we went ahead with Phaser 3 as it was proven to work with Atlassian APIs as shown in the starter app that was provided. We settled on making a 2D 3/4th RPG projection (a.k.a. the top-down oblique perspective) game since it allows the ease of making top-down games with the aesthetics of a side view. After we found some assets to start with, we were confused as to how these spritesheets are loaded into the game and the correct animations tagged or selected from them. While we came across tools such as Leshy SpriteSheet tool and TexturePacker, we decided against using them as it involved a large amount of manual repetitive manual work that would need to be done for each asset. Instead, we built a code generator that automatically picks up assets and generates code to load them. Then we programmatically extract the animations and tag them. Then we built the grid physics systems through several iterations and re-writes. It works on top of an Island Map that we built using the Tiled Map Editor and a few existing tilesets. We started the integrations with Jira. First, we had to generate interfaces from the Open API spec given by the Jira API. This helped us keep the code type safe even when using externals APIs without a library made for it. We added a menu screen that lists all the Jira Projects available to the signed in user. We make use of the “Get Projects Paginated” API for this. Since these APIs take a while to return responses, we cache the responses for 2 hours to make the game load faster. Once the user clicks on a project, we get the list of all issues in the project using the “Search for issues using JQL (POST)” API and display them in the farms. We then implemented a custom tooltip in Phaser based on an existing tooltip plugin. A tooltip is shown when you click on a crop (Jira Issue) that lets you: See the Issue ID See the status of the issue - To Do, In Progress, Done - as both text and as the crop’s growth stage Transition the status of the issue, from within the game All Jira APIs that the MVP of the app is making use of: Get projects paginated Get project Search for issues using JQL (POST) Get current user Get Jira instance info Transition issue Get all users default The resolvers we implemented for these APIs can be found here . We have also integrated Confluence APIs (such as Search content by CQL ) into the game but they could not be enabled as it required a separate Confluence page app to be installed instead of the existing Jira Global Page, which would break the workflow. The app is finally deployed as a Jira Global Pages app using Forge . Challenges we ran into This was our first time developing a 2D RPG . The journey involved a lot of exploring, trying, failing and then being overjoyed once something shows up on the screen. The Phaser 3 framework is really nice and provides great flexibility, but their documentation is lacking. While the library of examples is really helpful, it’s hard to find the right example we need to look at for what we are trying to do. Jira and Confluence APIs cannot be used in the same Jira Global Pages app. This held us back from making a game that integrated all of the user’s Jira issues and Confluence pages in the same app. It could have been a truly integrated experience. Accomplishments that we're proud of We built an MVP of the vision we had. The game looks and feels really nice. Integrated Jira APIs into the game, from both directions. That is, the game is not only centered around using data from Atlassian products, the player can also modify things in them. For example, they can change the status of an issue from inside the game. What we learned Building a 2D 3/4th RPG projection (a.k.a. the top-down oblique perspective) game: from the very basics like perspectives, tilemaps, spritesheets, grid-based navigation to using Tiled mapeditor, animations and finally integrating Atlassian APIs into them. Atlassian products: while all of us have used them before or use them daily, this experience of building on top of APIs for Jira, etc. gave a new insight into how they are architected, structured and what happens behind the scenes. What does the name mean? Did you know that the name “Jira” comes from Gojira? It’s the Japanese word for Godzilla, which was chosen because its closest competitor was named Bugzilla. Inspired by this, Monoland gets its name from the Japanese word for story (as in Jira stories) or epic - “monogatari”. Because the game is set in an island, the name “Monoland” was given. What's next for Monoland We would like to make Monoland a complete RPG and a fun and useful tool to use at work. To that end, we want to integrate all of the features that Jira provides into the game mechanics. It could even be an alternate user interface for all of Jira, Confluence and BitBucket. Real-time map : players would be able to interact with others on the same live map. Think of the Sims but it’s your office and the sims are you and your co-workers. Currently, other users are shown as working on what they were doing last. In the future, we want to see everyone’s movements being reflected on the map live. Integrate OpsGenie : new alerts will appear as the big bell being rung and people responding to alerts as first responders fighting a fire. <div