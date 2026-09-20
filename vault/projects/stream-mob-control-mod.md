---
slug: "stream-mob-control-mod"
url: "https://devpost.com/software/stream-mob-control-mod"
title: "Spectators Control Minecraft Mobs"
hackathon: "Twitch Streamer Tools Hackathon"
organization: "Twitch"
winner: true
words: 769
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
---

# Spectators Control Minecraft Mobs

> This is a Minecraft mod that allows viewers in a Twitch stream to donate to the streamer either bits or subs (configurable) to control mobs in the streamers survival world for a limited/unlimited time

[Devpost](https://devpost.com/software/stream-mob-control-mod) · hackathon [[Twitch Streamer Tools Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]

**stack** fabric, java, minecraft, oauth2.0, twitch

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for stream-mob-control-mod

## Body

Inspiration Interactive Minecraft Streams! (e.g. Viewers donate to spawn mobs, etc.) Dream - Minecraft, But The Mobs Are Controlled By A Player Garry's Mod Prop Hunt What it does This Minecraft mod allows Twitch streamers to let viewers control mobs/monsters in their game through donations and/or subs (configurable), giving them mob-control for a limited time to interact with the streamer in real-time. The mod integrates with Twitch to handle viewer donations. (Warning: Extremely fun!) How we built it I created a Minecraft mod which uses the Identity mod as a dependency (a mod which allows players to morph into Minecraft mobs). Next, I modified the Identity mod's abilities and constraints to be applicable to this mod’s goal, and disabled client-to-server morphing request packets. Then, I created an interactive, configurable game environment where spectators can inhabit the existing mobs/monsters in a streamers Minecraft world via right clicking them, and adjusted morphed player damage and drop tables dependent on their inhabited mob so their loot and abilities are fully consistent with the original mobs. Finally, I integrated the Twitch oauth2.0 API's to allow viewers to securely link their Twitch account to their Minecraft account using this mod, and also to allow the streamers to link their stream donations to their Minecraft Server, so that player donations or subs can be converted into mob-time or mob morphing accessibility, configurable by the streamer. Note: Donations accrued prior to viewers authenticating their Minecraft account will still be counted towards their Minecraft player's mob-time so long as the Minecraft Server is active and authenticated during the donation. Challenges we ran into -I had to create a Minecraft mod from scratch, identify necessary dependencies, and fully playtest it with my friends (shoutout Juan Abrego and Jackson Prowell!) to identify bugs and balance issues. Thankfully, I am experienced in this area as a professional Java dev who's always up for a challenge, and previously/recently made my first Minecraft mod last (Building Mining Mobs: https://www.curseforge.com/minecraft/mc-mods/building-mining-mobs -- An A* algorithm powered mod that allows monsters to break/place blocks efficiently to reach the player), which I'm also very proud of! -I had to figure out the best method/grant flow for allowing the streamer to authenticate their Twitch stream with the Minecraft Server, as well as for allowing users to authenticate and link their Minecraft accounts to Twitch while being secure and minimally invasive. -As a bonus, I wanted to make this mod primarily server only so that client Minecraft mods are technically optional for a viewer, just in case viewers lack the technical expertise or are in a hurry. (I like making vanilla compatible Minecraft Server mods!) Accomplishments that we're proud of No one has made a mod like this before, and it is extremely fun to play! As a mod developer, that achievement in itself is the best thing I could ever ask for. I hope that a lot of others can find fun in it as well, and streamers can use it to better connect with their fanbase. Just bringing a cool idea of mine into reality is enough for me to be seriously proud of. What we learned This is my first time integrating a Minecraft mod with the Twitch API's offerings, or using the Twitch API at all in a project for that matter. Going into the future, if I have another idea for an interactive stream mod, I'll have some technical expertise to make it work smoothly. Most importantly, I also learned about one area where the Twitch oauth2 grant flow can be improved for interactive mods like mine: I would like if there was a more basic oauth2 service similar to the current device authorization flow where instead of requiring a user to authorize a Twitch app (which they may be potentially averse to for a strangers twitch app, regardless of it asking for zero scopes), it simply had the user login to Twitch to verify their account, then returned the users twitch id on approval instead of an auth token so that the user can simply verify which Twitch account is theirs. That way, donations can be allocated efficiently with minimal use and minimal invasiveness. Ideally, basic twitch id verifier can have more than an 800/requests per minute or 20/users authenticating concurrently max limitation to factor for streams with larger audiences. If I have the privilege of speaking to the Twitch dev team following this project, this is top on the list of what I will bring up with them. What's next for stream-mob-control-mod I am looking for a Twitch Partner / Affiliate to test this mod out with a large audience! <div