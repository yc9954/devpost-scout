---
slug: "universe-planner"
url: "https://devpost.com/software/universe-planner"
title: "Universe Planner"
hackathon: "Graph For All Million Dollar Challenge"
organization: "TigerGraph"
winner: true
words: 555
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "substrate/structured_db"
---

# Universe Planner

> Tackle any complex problem with the social planning app where you can tap into social knowledge exactly when you need it!

[Devpost](https://devpost.com/software/universe-planner) · hackathon [[Graph For All Million Dollar Challenge]]

## Facets

**mechanism** [[graph_reasoning]]
**substrate** [[structured_db]]

**stack** android, c#, gsql, ios, tgcloud, tigergraph, unity, xcode

## How they structured the write-up

- inspiration and what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for universe planner

## Body

Inspiration and What it Does Planning is at the core of solving any complex problem, and so the catch-all solution to solve everything, everywhere... would be the ultimate planning application platform. Universe Planner is a new multiverse-metaverse planning app that shows the bigger picture view and also socially connects you at every granularity level to others working on the same or similar mission, plan, or task - seamlessly crowd-sharing knowledge of approach. Sometimes what you need to get stuff done is to see tasks from the perspective of spacetime: Universe Planner analogizes Missions as stars, Plans as planets, and Tasks as cities. Let's try it out for planning out a mission that is fully within our control... such as Saving Food "The first thing I can think of is to store food properly. And then... "Maybe I'll consult the community for ideas! It looks like there are 4 others working on this mission. "Looks like most people have not opted into identifying themselves. Incidentally, Universe Planner features a automatic device UUID-based login system that is barrier-free and opt-in, to get people straight into their productivity mode without having to register or worry about a password. I'm going to finally update my Username so that I won't show as an Anon to others. I'll also add in my LinkedIn. "It looks like the only non-Anon who has identified herself also trying to solve the personal problem of Saving Food is just my dog corgi.cam. Let's tap to make sure this is the same corgi on LinkedIn. Let's see what she has to say. "Once selected, my dog's mission shows up as a new star that I can touch to warp to... to discover her plans in Saving Food. "Ah, very corgi insightful! Coming soon: To complete tasks, we travel an itinerary across cities in our Plan planet. We can also discover who else is working on similar tasks, plans, or missions! (And socially connect.) Universe Planner is designed to help foster local in-person community for working from home. Immediately, when you first open the app, you can discover others nearby who are also getting things done. You can find out the intersection of their mission, plans, and tasks with yours - and maybe even serendipitously discover local collaborations! By making the process of getting things done less lonely, Universe Planner hopes to connect the world through productivity and stardust. How we built it Using Queries as exposed endpoints, we developed a serverside solution that uses only tgcloud. Barebones no-dependency Unity wrappers (see github public) for Oath2 token into TGCloud and signed GET requests for processing the queries. Some hackish architecture insight after realizing the analogy of planets as plans, tasks as cities, and missions as stars in one's universe. Space Graphics Toolkit and Stardust magic in Unity Challenges we ran into Dependency issues in TG.net for Unity so just wrote my own barebones class Wrapping RDBS mindframe around graph concepts... traversals instead of joins Accomplishments that we're proud of Made a MVP from TigerGraph / TGCloud / GSQL / graph database crash course in a weekend! Entire serverside made in TGCloud! What we learned TigerGraph/TGCloud/gsql nodal traversal thinking as opposed to join's primary_id's are not immediately indexed for search in TG What's next for Universe Planner So much more! Everything, everywhere, all at once! !!! <div