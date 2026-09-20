---
slug: "a-piraite-s-life-for-me"
url: "https://devpost.com/software/a-piraite-s-life-for-me"
title: "A PirAIte's Life for Me"
hackathon: "AWS Game Builder Challenge "
organization: "Amazon"
winner: true
words: 710
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# A PirAIte's Life for Me

> A pirate RPG where alll terrain can be manipulated using your trusty shovel, and NPCs are powered by an LLM that lets you interact with them on a much deeper level.

[Devpost](https://devpost.com/software/a-piraite-s-life-for-me) · hackathon [[AWS Game Builder Challenge]]

## Facets

  <sub>weak: runtime_tool_creation</sub>
**domain** [[developer_tools]]
  <sub>weak: disaster_emergency, transportation</sub>
**user** [[developer]]

**stack** unreal-engine

## Body

Avast, ye landlubbers! We've crafted a swashbucklin' adventure, a digital yarn spun from the threads of the Wild West and the high seas, all bundled into a rollickin' game built in Unreal Engine and powered by the mighty engines of Amazon Web Services. Our goal? To create a world bristlin' with life, where every encounter feels fresh as a sea breeze and every conversation is as unpredictable as a hurricane. The key to this? Dynamic NPC dialogue, far beyond the usual parrot-like repetition. When a player dares to parley with one of our salty sea dogs or grizzled gunslingers, the game sends a message through the magical pipes of API Gateway, which rouses a trusty Lambda function. This function, quick as a cannonball, gathers all the necessary intel: the state of the world (where the player be, what time o' day 'tis, what quests be afoot), the player's own words, and all we know 'bout the NPC from the depths of our DynamoDB treasure chest – their personality, backstory, and even what's been said before. This be the stuff we feed to the mighty kraken of Amazon Bedrock, a beast of language that weaves words like a seasoned storyteller. Bedrock spits back a response, which our Lambda function then deciphers, lookin' for any changes to the world – new quests discovered, old ones finished, and all manner of other surprises. The words themselves are then seasoned with a proper pirate twang, so ye know ye're talkin' to a true son of the sea. And what helped us chart this course? Why, Amazon Developer Q, o' course! That trusty first mate helped us rig our AWS infrastructure faster than ye can say "Jack Robinson," writin' code for all manner o' things – talkin' to Bedrock, managin' the API Gateway, keepin' records in DynamoDB, and all the rest. It even lent a hand in the Unreal Engine shipyard, speedin' up our work on the game itself, helpin' with everythin' from character animations to handlin' player input. In short, we used Unreal Engine for the game itself and a whole fleet of AWS services – Amazon Bedrock, Lambda, API Gateway, and DynamoDB – to make the dialogue as lively as a tavern brawl. And Amazon Developer Q was the wind in our sails, helpin' us bring this pirate western world to life faster than ye can plunder a galleon! What be on the Horizon? But our voyage ain't over yet! We've got plenty more treasures to uncover and features to add. Here's what we be plannin' for the future: Side Quests Galore: We aim to expand the world with a multitude of side quests, each with its own unique story and challenges. These quests will be dynamically woven into the world, offerin' players even more opportunities for adventure and reward. Dynamic Game Generation: We plan to further unleash the power of the LLMs to dynamically alter not just dialogue, but the very fabric of the game itself! Imagine a world where the starting conditions, available quests, and even the overarching narrative change with each playthrough, creating truly unique and replayable experiences. This could involve dynamically generating: Starting Scenarios: Each game could begin with a different set of circumstances, forcing players to adapt and make different choices. Quest Objectives and Rewards: The LLM could generate unique quest objectives and rewards based on player actions and the current game state. World Events: Random events, such as storms, raids, or discoveries, could occur dynamically, adding unexpected twists to the gameplay. Procedural Content Generation (PCG): While our focus has been on dynamic dialogue and quest generation with LLMs, exploring PCG for environments and other game assets could drastically expand the world and create even more variety. This would work in tandem with the LLM generated quests to populate the generated world with relevant content. Improved Character AI: We want to enhance the AI of our NPCs beyond dialogue. This could include more complex behaviors, such as reacting to player actions in more meaningful ways, forming alliances or rivalries, and engaging in more dynamic combat. With these future additions, we aim to create a truly living, breathing world where every playthrough is a new and exciting adventure, a true testament to the power of AI-driven game development. <div