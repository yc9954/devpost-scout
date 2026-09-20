---
slug: "obby-core-lab-remixable"
url: "https://devpost.com/software/obby-core-lab-remixable"
title: "Obby Core Lab: Remixable"
hackathon: "Meta Horizon Creator Competition: Open Source Champions"
organization: "Meta"
winner: true
words: 638
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/government_staff"
  - "substrate/video_visual"
---

# Obby Core Lab: Remixable

> Play it. Remix it. Build your own obby.

[Devpost](https://devpost.com/software/obby-core-lab-remixable) · hackathon [[Meta Horizon Creator Competition- Open Source Champions]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[government_staff]]
**substrate** [[video_visual]]

**stack** horizon, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for obby core lab: remixable

## Body

Logo Remixer Info Marker Top of Elevator looking down Player Menu Shop Bridge Inspiration I drew a lot of inspiration from classic Obby games, incorporating many of the features that make them fun and challenging. I also wanted to build something that looks great while using only the standard assets included in the Horizon Worlds desktop editor. Classic obbies were the perfect fit—they rely on simple shapes, clever mechanics, and creativity. What it does Obby Core Lab: Remixable is both a playable obby and a flexible foundation for remixers to expand on. The world includes classic mechanics like checkpoints , kill bricks , disappearing platforms , and moving platforms . On top of that, it includes per-player features such as a stage skip ability , a double jump ability , and a speed boost ability . The per-player abilities provide an opportunity for remixers to potentially monetize them, offer them as rewards, or enable/disable them by default. An example shop is included where players can “purchase” these abilities (which are always free in the example shop) and then enable or disable them—or use stage skips—through their menus. To help remixers, the project also includes: Templates for all the main mechanics Example stages showcasing most hazards and features in action How I built it I built the world in the Horizon Worlds desktop editor and scripted it with Visual Studio Code using TypeScript. All models and sounds in this world are from Horizon Worlds’ primitive shapes or other assets from Meta. I also used GIMP for quick image work and some AI tools during development. Challenges I ran into Collision detection was one of the biggest challenges. My first thought was to use trigger gizmos for everything, but I was concerned about the performance impact of having too many triggers in a world with many stages. I experimented with standard collision events, but they weren’t reliable enough, especially when players moved quickly. They also required confusing setup steps in the Properties Inspector, which I didn’t want remixers to struggle with. I also tried attaching a trigger to the player, which partially worked but would sway with animations if attached to the head/torso, not trigger if a shoe hit something while jumping, and were inflexible. Moving triggers with the player's position had similar downsides and may not have worked well at scale. In the end, I circled back to triggers, which were the most flexible per object, reliable, and understandable for remixers without having to change weird settings. Using triggers, however, still had the potential performance problems of too many triggers in the world. I came up with what I think is a great solution with triggers, which is in the next section! Accomplishments that I'm proud of To solve the “too many triggers” potential performance issue, I created a Trigger Toggle System . Here’s how it works: Developers place a large area trigger tagged TriggerToggleArea in the world. Any triggers inside that area with the tag TriggerToggle are automatically enabled or disabled based on player presence. Main areas without players in them will have the tagged triggers inside them disabled, potentially cutting down on active triggers substantially. It’s simple, flexible, and doesn’t require managing lists or special folders. You just drop tagged triggers inside the tagged area, and the system will enable or disable the triggers dynamically. The world already has several of these areas built in, so remixers can see it in action. What I learned I learned a ton about collision systems in Horizon Worlds, and I’ve become even more confident working with the desktop editor and TypeScript. I also learned (again!) that I’m not great at limiting scope. What's next for Obby Core Lab: Remixable Feedback will guide the future of the project, but there’s always room for more: New mechanics New abilities More stages <div