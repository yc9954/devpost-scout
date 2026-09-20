---
slug: "find-the-snowflake"
url: "https://devpost.com/software/find-the-snowflake"
title: "Find the Snowflake"
hackathon: "Meta Horizon Creator Competition: Elevate Your Mobile World"
organization: "Meta"
winner: true
words: 722
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
---

# Find the Snowflake

> Find the Snowflake is a hidden object game where your observation skills are put to the test. Search for hidden items like a snowflake surrounded by stars or a duck shaped cloud in the sky.

[Devpost](https://devpost.com/software/find-the-snowflake) · hackathon [[Meta Horizon Creator Competition- Elevate Your Mobile World]]

## Facets


**stack** inkscape, metahorizondesktopeditor, typescript

## How they structured the write-up

- what it does
- inspiration
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for find the snowflake

## Body

Find the Snowflake ❄️ World select screen with world unlock progress bar Awards, Achievements and Statistics page Find the Snowflake Find the Duck shaped cloud What it does Players explore a series of colorful and uniquely themed worlds, each with 30 timed hidden object levels. As they find the whimsical target item (like a snowflake, green phone, or sad robot), they earn points based on speed with an added level bonus at the end. Completing worlds unlocks new ones, and a new Awards & Achievements system tracks and celebrates progress. Inspiration The update to "Find the Snowflake" was inspired by the desire to transform a simple concept into a progression-focused experience that keeps players engaged over time. I've found other games with short goals keep players motivated and playing. Before the update, the game featured 6 worlds, with 2 initially locked. Once players completed the first 4, the final 2 would unlock. Together with the basic "Congratulations" message at the bottom this wasn’t enough to keep players engaged long-term. After the update the game introduced a much more fun and rewarding progression system. Now, players begin with 4 unlocked and 8 locked worlds. Every time they complete 2 worlds, 2 new ones are unlocked. A bright colored progress bar helps visualize this loop, and unlocking new worlds is celebrated with a large message and a cheerful sound effect. Combined with the new Awards and Achievements screen, players are now more motivated to progress, return later, and complete everything. How we built it Find the Snowflake is built using the Meta Horizon Desktop editor and it mainly uses the Custom UI gizmo. Game logic was created in TypeScript. There are three main Custom UI gizmo's where each is being used as a page or screen in the game. A game manager script is created to hold the main logic and to switch between different screens. And an audio manager script receives events from other scripts and handles audio playback. All the artwork for the UI components, world backgrounds and objects, were designed and created by me using Inkscape, a powerful free vector based graphics editor. It was fun to create all the objects such as a duck shaped cloud or smiling sea stars. To add to the whimsical nature of the game, fun and unique sound effects are added for each object. For example you can hear the phone dialing when clicked, or the sound of someone eating when the player finds the pizza Hawaii. Persistent Player Variables are used to store the games progress in an object and in simple number variables. Testing was done using the Mobile Preview mode in the editor, and on two different smartphone brands to ensure the graphics looked correct and the game was playable on different devices. Challenges we ran into The biggest challenge was designing and implementing the new progression system, including the colorful progress bar and unlocking logic. New code had to be written and new worlds had to be designed to make the game last longer. Building a 2D casual mobile game using an advanced editor capable of building high-end VR experiences was also a unique challenge, but it proves how flexible the desktop editor is. Accomplishments that we're proud of I'm proud of creating a game that plays well on a mobile phone, players are able to quickly play a game without the need for a long onboarding or setup. It's also well-suited for short gaming sessions, which are common in mobile gaming. The newly built progression system makes it more fun and rewarding to complete worlds. Adding 6 new worlds designed from scratch took a lot of time but it was very fun to do and challenged me to be creative. What we learned This competition really helped me think about how to keep a player playing and engaged using an effective progression system. I've also gained experience working with Persistent Player Variables and the Custom UI gizmo. What's next for Find the Snowflake Here are some of the things I'd like to add in future updates: More Achievements to motivate players to keep playing even after they unlocked all worlds. New worlds based on Holidays and Seasons, for example adding 6 new Christmas themed worlds. Use the new World Persistent Variables feature, to create social features like custom leaderboards. <div