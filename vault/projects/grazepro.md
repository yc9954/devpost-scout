---
slug: "grazepro"
url: "https://devpost.com/software/grazepro"
title: "GrazePro"
hackathon: "TreeHacks 2023"
organization: "Stanford TreeHacks"
winner: true
words: 860
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/simulation_digital_twin"
  - "domain/agriculture_food"
  - "domain/climate_energy"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# GrazePro

> Enabling farmers to sustainably optimize resources.

[Devpost](https://devpost.com/software/grazepro) · hackathon [[TreeHacks 2023]]

## Facets

**mechanism** [[on_device_local]] [[simulation_digital_twin]]
**domain** [[agriculture_food]] [[climate_energy]]
**user** [[frontline_worker]]
**substrate** [[geospatial]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** convex, css, figma, html, netlogo, next.js, npm, react, tailwind, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for grazepro
- works cited

## Body

Cover Photo Simulation Dashboard History Page Inspiration When tackling the issue of sustainability, we looked first at the major sources of emissions. One thing that caught our eye was agriculture – Particularly, livestock production (especially cattle) which is the largest contributor for carbon emissions. Annually, each cow produces 220 pounds of methane and in totality accounts for 14.5% of global greenhouse gas emissions. Agriculture continues to be one of the most important industries that technology overlooks. As a team, we are driven to build in communities and industries that are underserved by existing technologies and from this, GrazePro was born . We decided to focus on rotational grazing, a popular farming technique that involves moving livestock between paddocks so that only one or some paddocks are grazed at any given time. On the contrary, continuous grazing involves only one paddock, and the forage is not allowed to fallow. We realized that there was an efficiency maximization problem related to when farmers should switch paddocks to maximize cattle health and ability for grass to regrow. We decided to model this using a simulation. What it does GrazePro is a virtual simulation intended to enable farmers to accurately predict and forecast the optimal approach to rotational grazing. This means that we can take real data points provided by farmers, input them into the algorithm that we’ve created and generate actionable suggestions to improve cattle health, sustainable practices and cost efficiency. Our algorithm can help answer questions such as: How many segments farmers should divide their paddock into? What is the optimal time that cattle should stay within one area to ensure that the grass has time to regrow? The prediction algorithm is built on a cellular automata model, which is a collection of cells on a grid that evolves over discrete time steps according to a set of preferences and rules. In this case, we modeled how fast grass grew back based on various factors, including number of cattle, amount of water used, fertilizers used, previous cover crops and more. Users have the ability to change certain inputs, such as number of paddocks, number of cows, growth rate of grass and rotation time. When the simulation is played, the dashboard also displays the health of the grass and the cattle and how they change over time according to the feeding patterns of the cattle. Farmers can then use this data to inform their farming practices. How we built it We used a combination of coding languages, including Typescript, React, Netlogo. A number of technologies, frameworks and packages were used, including Next.js, Convex, Vercel, Tailwind. We designed and built our wireframe in Figma. Challenges we ran into On our journey to TreeHacks this year, our car was broken into and our laptops, belongings and personal items were stolen. While this unfortunately has severely impacted our ability to hack, as we were unable to begin until 12 hours into the hackathon, there is nothing that builds stronger bonds than trauma . Thankfully, we were still able to build GrazePro with the limited resources we had, and were able to find some hacky solutions (i.e, figuring out a way to locally install Node.js on Stanford's admin protected computers). A huge shout-out to the TreeHacks organizers! Accomplishments that we're proud of This was our team's first major in-person hackathon since the pandemic began, and it presented a significant learning opportunity. While we encountered some initial challenges, we are proud of the progress we were able to achieve as a team without any laptops or personal devices (explained above) AND the additional time constraint of 24 hours instead of 36. What we learned We learned to never leave our suitcases unattended…kind of a hard thing to do at a hackathon. In all seriousness, as the first hackathon that we have participated in as a team, one of the most important lessons that we learned is how to work together. This was integral in dividing the workload of this huge project into manageable and sizable chunks that we could delegate effectively to maximize the use of our time. On a technical level, we were able to use, learn, and implement some really interesting frameworks and packages from the TreeHacks sponsors (shoutout to Convex and Vercel!). We also had the chance to participate in a mock interview with YC which really taught us how to navigate the business-side of a startup alongside a technically-refined product. What's next for GrazePro Where to even begin? Firstly, incorporating satellite and drone imaging technology into our platform and setting up a method to scan the uploaded image to determine the existing health of the grass would help streamline the onboarding of new users. Secondly, using more data to train our simulation would make it more realistic and improve scientific accuracy and predictability. Thirdly, we would introduce features that would complicate our simulation, such as changing the shape of each paddock, reproduction and death of cattle, incorporating weather patterns and forecasts into the model to determine crop growth, use of rivers and riparian buffers to prevent waste contamination from cattle feces, nitrogen fixation mechanisms and their effect on soil quality. Works Cited https://www.ucdavis.edu/food/news/making-cattle-more-sustainable <div