---
slug: "handsurvivor"
url: "https://devpost.com/software/handsurvivor"
title: "Hand Survivor"
hackathon: "Meta Horizon Start Developer Competition"
organization: "Meta"
winner: true
words: 663
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "user/educator_student"
  - "user/patient_family"
  - "substrate/geospatial"
---

# Hand Survivor

> Use your hands and select your skills to protect your Nexus from enemies! Fire lasers, summon meteors, and many more. Find your optimal builld to live through 10 waves! Pure hand tracking.

[Devpost](https://devpost.com/software/handsurvivor) · hackathon [[Meta Horizon Start Developer Competition]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[developer_tools]]
**user** [[educator_student]] [[patient_family]]
**substrate** [[geospatial]]

**stack** c#, handtracking, meta, rider, unity, v81

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for handsurvivor

## Body

Title & Mars map background Laser example on Mars map Snow map preview Boss weapon trebuchet on Snow map Boss weapon Slingshot on Desert map Main menu Achievements menu Active Skill selection example with wave UI Passive Upgrade selection example Hand Survivor Inspiration We got inspired by SoulStone Survivor, Megabonk, Vampire survivor and the survivor genre in general. We wanted to make the player live a similar experience with the added fun of hand-tracking, which also brings a new twist to the genre. What it does HandSurvivor is a VR wave survival game where you : Earn experience by killing enemies You have a Spirit hand (can collect experience and cast spells) and a Physical Hand (allows you to squish some types fo enemies) At the start of a level, before acquiring any Active Skill, you will have to use your Physical Hand to get through the first enemies Cast spells using hand gestures (Laser, Heal, Shield), grabs (Meteor) or pick an automatic spell (UFO & LightningHand) Your first 3 level ups allow you to pick 3 Active Skills -> This will determine your build! After all your Active Skill slots have been filled, new levels will allow you to upgrade passives. Enemies have specific requirements to be killed (Immune to Magic or Physical) How we built it We began by spending a lot of time discussing the vision of the game: what makes the Survivor genre engaging, and how we could reinterpret those mechanics through hand tracking. A lot of the early ideas came from open brainstorming sessions where we played with different spell concepts, enemy behaviors, and ways the player might naturally use their hands. Many features emerged simply from experimenting, testing small prototypes, and keeping the ideas that felt the most fun and intuitive. Once the direction became clearer (this involved dropping some prototypes), we divided the tasks between us and organized the work by theme so we could focus fully on a specific area (Enemies & Animation, Navmesh logic, Special Weapons & Hand Interactions, UI, Data systems, Scene Management, etc.). The project is built in Unity 6000.2.10f1 with Meta XR SDK v81 for Quest 3 hand tracking. We implemented custom gesture recognition using ShapeRecognizer and TransformRecognizer (combined with custom scripts for distance between hands or to check if the hand is facing away from your face for example), and persistent data is saved on-device to track codex entries, tutorials, and player preferences. We used GitHub Desktop for version control, Rider as the development environment and Blender for mesh optimization. Challenges we ran into Performance optimization: Performance for Standalone VR . Implemented object pooling, event-driven updates instead of polling, and careful GC management to maintain steady FPS. Reducing triangle counts as much as possible in Blender. Navmesh challenges due to a tiny area for the enemies to move on. Accomplishments that we're proud of Intuitive gesture system that feels good to use Funny enemy interactions and animations Achievements & codex Managed to bring our idea to life with almost everything we wanted. What we learned We have to adapt to the limits and possibilities that Hand tracking offer, especially when trying to fit in a very specific genre that is Survivor games. Gestures need to be distinct enough or have more filters to avoid conflicts and unwanted triggers. What's next for HandSurvivor Art Global art / theme direction : we would like to create more "Lore" in this way : you are a child in your bedroom and getting bored. You play with your toys and create your world with your imagination. Only using his hands and toys. Having our own 3D and 2D assets (we used Synty assets). More diversity in spells and interactions Add more gesture-based spells (Giant-Hand spell that allows you to squish large groups of small enemies at once) Boss variety with unique mechanics requiring more specific weapon Meta progression : More achievements Extra life / More damage / Critical strike chances (classic stat improvements) <div