---
slug: "the-knowledge-pool"
url: "https://devpost.com/software/the-knowledge-pool"
title: "The Knowledge Pool"
hackathon: "Snap AR Lensathon 2022"
organization: "Snap Inc."
winner: true
words: 717
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# The Knowledge Pool

> A fountain at the Los Angeles Central Library becomes a magical platform for an augmented reality educational experience. Learn about space, the ocean, and more through interactive exploration.

[Devpost](https://devpost.com/software/the-knowledge-pool) · hackathon [[Snap AR Lensathon 2022]]

## Facets

**substrate** [[video_visual]]

**stack** lens-studio, lensstudio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the knowledge pool

## Body

Inspiration The Knowledge Pool was conceived and developed for Snap's 2022 Lensathon, as an entry in the Education category. One of my favorite places in Los Angeles is the Central Library in downtown. Its history, its mission, the resources it offers, the building itself, and the gardens outside of it are all truly inspiring and are treasures for the city. I wanted to create an educational Lens with the library at its center, and Snap's recently-released Custom Landmarker feature allowed the perfect opportunity to do that. There are fountains outside of the library that are part of a beautiful monument to the history of human learning, writing, and language. The fountains currently contain no water because of severe drought conditions in Southern California, but they are still an important part of the Library's physical presence and message. When I saw the empty fountains, I immediately knew I wanted to augment them somehow, and honor their history and symbolism by giving them a new life, while incorporating their connection to the Los Angeles Public Library and all that it provides. What it does The Knowledge Pool is activated in Snapchat while at a specific fountain outside of the LA Central Library. When users first view the empty fountain, they are asked to "unlock" it by holding up their library card. Library cards are free to everyone, and this seemed like a fun way to tie library patronage to the AR experience itself. After unlocking, The Knowledge Pool materializes—accompanied by music and particle effects—and offers the user a selection of bite-sized educational activities to try. When users complete any activity, they are awarded a star badge. These achievements are automatically saved using Lens Studio's persistent data store, so that even when users are at home, they can look at their library card with the Lens, and see their completion awards in AR. Current activities are centered around the general themes of space and the ocean, with more activities planned for release through coming updates (including a series on the world of atoms). The Lens also offers suggestions for library book titles that relate to the activities, so that interested users can then pop into the library to follow up on what they saw in the Knowledge Pool. How we built it The Knowledge Pool was created in Lens Studio, with assets created and modified in Cinema 4D, Adobe Illustrator, and Adobe Photoshop. Original music and sound effects were created in Logic Pro. Challenges we ran into This was an ambitious project to execute in a handful of weeks, and the level of finish I try to achieve in any given project meant a pretty intense sprint to get it all put together. Additionally, since the Lens relies on a specific physical location, I needed to spend a lot of time at the library, testing and iterating and retesting, away from my normal work environment. Finally, the number of technical features I was attempting to put into a single lens (custom landmarkers, image markers, physics collisions, persistent data storage, an achievement system, etc.) offered no shortage of coding challenges. Accomplishments that we're proud of I’m admittedly proud of the concept itself; its interactive and visual qualities, its nods to the library (and novel use of the library card) to me represent a nice concretization of ideas that I’ve been wanting to explore. On the practical side, I was happy to find ways to pack all of these technical features, art assets, animations and audio files into a Lens under 8 megabytes. What we learned In researching for the project, I learned a ton about the library, its history, and the monument to the evolution of knowledge that is its garden. Technically, I learned more about creating modular systems—as opposed to one-off AR experiences—so that I can more easily integrate new content and updated modules in the future. What's next for The Knowledge Pool Now that the fundamentals of the experience are in place, and the platform is ready for interaction, I have a bunch of additional educational modules and activities to design and add. I'm hoping to take it out of "hackathon" mode and develop it into a more robust experience. And if anyone at the library is is ever interested, I'd love to get their input or feedback. <div