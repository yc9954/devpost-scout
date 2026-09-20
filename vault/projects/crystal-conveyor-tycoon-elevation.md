---
slug: "crystal-conveyor-tycoon-elevation"
url: "https://devpost.com/software/crystal-conveyor-tycoon-elevation"
title: "Crystal Conveyor Tycoon Elevation"
hackathon: "Meta Horizon Creator Competition: Elevate Your Mobile World"
organization: "Meta"
winner: true
words: 653
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "substrate/video_visual"
---

# Crystal Conveyor Tycoon Elevation

> Crystal Conveyor Tycoon reaches new heights with the additions of a second floor, quests, rebirths, and a PvE battle area.

[Devpost](https://devpost.com/software/crystal-conveyor-tycoon-elevation) · hackathon [[Meta Horizon Creator Competition- Elevate Your Mobile World]]

## Facets

**mechanism** [[benchmark_measured]]
**substrate** [[video_visual]]

**stack** blender, gimp, horizon, typescript

## How they structured the write-up

- inspiration
- primary updates for progression
- secondary updates for player experience
- how i built it
- challanges
- accomplishments
- next steps

## Body

Main Game Logo Floor 2 Completed Tycoon Area Quests Rebirth Station PvE Battle Area Inspiration While I had already planned to add a second floor to the tycoon in July, the hackathon announcement motivated me to expand my plans further. The competition gave me the push to implement several other new progression-based features within the competition timeframe. Primary Updates for Progression Floor 2 Expansion : Added additional droppers, upgraders, weapons, and walls that provide players with even more tycoon building fun. Quest System : Implemented quests to guide player progression. Some quests were designed to teach players about experience enhancing mechanics like using the manual dropper button or enabling the auto collector after completing floor 1. Rebirth System : Added player rebirths which increases income generation in future builds. Reaching 5 rebirths unlocks a reward enabling the auto collector option at the start of the players tycoon build. PvE Battle Area : Added a new PvE battle area with difficulty-increasing rounds and its own quest line. This gives players expanded content and also something they can enjoy while their tycoons generate income. Secondary Updates for Player Experience In World Signs : Signs with limited amounts of text help players understand how to play and provide area information. Floor 1 Enhancements : Auto collector unlocks once floor 1 is complete, added a front door which can be closed to prevent other players entry if the tycoon walls are also built, added trophy areas which display total quest progress as a possible sharable item and a reminder of remaining challenges. UI Improvements : Added a visual queue when taking damage on web and mobile platforms, rebirth availability information is displayed when a tycoon has been completed, quest completion notifications are displayed. Visual Improvements : Added grass, added additional mountain variety, improved the PvP area with updated flooring and fencing. General Performance Improvements for Moving Crystals : Reduced bridge .get calls by caching positions, replaced expensive math operations with alternatives like .magnitudeSquared . How I Built It Many hours with: Core Tools : Horizon Worlds Desktop Editor and Visual Studio Code. Additional Tools : Blender, GIMP, Meta and other AI Tools, Mesh Baker (Unity Asset Store) for combining meshes to reduce draw calls. 3D Assets are primarily from BitGem https://shop.bitgem3d.com/ , some other assets were generated via Meta’s in-editor AI. Challanges The largest challenge with this update was running into world capacity limits , which I found during the addition of floor 2. Key optimizations to decrease animated entities included: Crystal and Rune Entities Optimization : Originally, each crystal and rune asset included 9 mesh entities where a random mesh was enabled on each use to have a variety of crystals shown. With around 30 crystals and 16 runes per tycoon, this quickly consumed a large amount of world capacity. The solution involved having each crystal/rune only have one mesh entity using Blender to orientate things consistently, and updating server/local pooling to maintain variety using extra pooled crystals. Template Optimization : An entity-heavy template object was used that player tycoon object spawning and configuration was based on. Some world capacity was saved by replacing the template object with a static data file. The template asset can be added back into the world to make any updates needed and removed after scripting logs the data for the static data file. Accomplishments Through this update, I significantly improved my skills in the Horizon Worlds Desktop Editor and I am proud of the entire update. Circular references in TypeScript is an area I used to struggle with but now have a solution where that is no longer a problem by incorporating interfaces. Next Steps Possible future update ideas: Enhancing the player UI with images. Balancing and expanding the PvE area with power-ups and health drops. Revamping the PvP system to include structured rounds and buffs/de-buffs. Exploring how the world can be enhanced with the new World Variables system. <div