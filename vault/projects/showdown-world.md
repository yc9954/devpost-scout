---
slug: "showdown-world"
url: "https://devpost.com/software/showdown-world"
title: "Cardboard Farm"
hackathon: "Meta Horizon Creator Competition: Mobile Genre Showdown"
organization: "Meta"
winner: true
words: 1029
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/finance_payments"
  - "user/educator_student"
  - "user/general_public"
  - "substrate/video_visual"
---

# Cardboard Farm

> A relaxing farm-sim, where you farm crops, purchase decorations, and find hidden gnomes.

[Devpost](https://devpost.com/software/showdown-world) · hackathon [[Meta Horizon Creator Competition- Mobile Genre Showdown]]

## Facets

**domain** [[agriculture_food]] [[finance_payments]]
**user** [[educator_student]] [[general_public]]
**substrate** [[video_visual]]

**stack** typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cardboard farm

## Body

Optional flower watering for stress relief Digging up carrots, they help you see in the dark The bee wants a pumpkin, apparently... The robot has left some traps lying around, be careful! Inspiration Cardboard Farm aims to implement a simple familiar farming loop with a Horizon Worlds twist. There is a small amount of customisation based progression that a player can make by purchasing cats and balloons around their farm to improve the area cosmetically. There are also a number of hidden gnomes around the farm. Finding all of these will unlock a gnome trophy in the plaza, hopefully leading to some nice social interaction if people choose to help each other out. What it does Players can repeatedly visit the scarecrow in the plaza to pick up a new task. The player must then water the correct crop, wait for it to grow, before picking it up and bringing it to one of the animal residents. As players drop off crops and complete tasks, they earn a mixture of currencies, which can be spent upgrading their farm visually. At present, the farms contain two "batches" of decorations which can be bought: Balloons can be purchased with $, which is an infinitely farmable soft currency. Cats can be purchased for daily diamonds, a time gated currency. Going forward, the intention is that these decoration will rotate over time, meaning players are incentivised to complete a collection of decorations (and thus earn a matching statue for their plaza) before the set goes away and is replaced by something new. How we built it I started off building a world much like the ones I had previously been playing in horizon worlds: third person with a lot of grabbable interactions and physics. While this felt fun in VR especially, I found it more cumbersome on mobile, so instead changed to a fixed angle camera to more closely match mobile games I have played previously. However I opted to keep the physical carrying of crops as felt this felt like a good balance to still feeling natural to Horizon Worlds and worked well for both mobile AND VR. Challenges we ran into As this was my first experience with building for Horizon Worlds there were a few concepts that I had to dig around to find out how best to approach them. The first big hurdle I hit was wanting to run "client-only logic on non-owned entities". In some cases, I went with just going for server-side logic, as cases such as growing crops being a shared state felt more social and meta-verse'y anyway. However my other use case of allowing users to customise and improve their own farm, in a non-shared way, was solved by heavy use of setVisibilityForPlayers. I ended up using this for both the decorations that players can purchase as the progress, and also things like the statues that can be unlocked by completing certain quests or achievements. Another challenge I found, was when I first implemented the purchasable upgrades using a "selectable" trigger zone, that the lack of confirmation step felt underwhelming and prone to misunderstanding. I therefore wanted a dialog box, but the only references I found used a server-owned CUI in world space. After some trial and error, I ended up adding an additional screen-space blocking CUI to my "HUD Bundle" (Which is granted ownership to the player on connection) and drove visibility of this via a network event when doing the initial selectable trigger interaction. I was then subsequently able to hide the CUI again, and send a network event back to the server in the event that the player wanted to confirm a purchase. Accomplishments that we're proud of Overall I am happy where I landed with the controls, feeling I hit the right balance of a mobile friendly camera angle with a good amount of information available via the HUD, without straying too far away from the tactile and avatar-centric nature of Horizon Worlds. Knowing how important making a mobile game accessible is, and not having the time to invest in iterating on a bespoke tutorial, I went with a "Crazy Taxi" style arrow over the player, hoping that between this arrow, and the highlighting of interactive items, that players should find it relatively intuitive to work out what they always need to do next. What we learned Having now gained a much better understanding of best practices for personal data and world-state within a world, I feel if I were to start again I would feel much more confident in making the progression of the world much more "functional" rather than just cosmetic. As cute as the balloons and cats are, I do not doubt that if players were to instead unlock new fields and areas over time, that this would be much more compelling, and likely to result in better world retention. What's next for Cardboard Farm Progression: My first task would be to start splitting up and expanding the farm, to make the progression through different crops and residents more granular. By giving each resident a number of requirements or goals to complete their area, and "advance", I could make the gameplay feel more structured and directed. Onboarding: While the core loop of: Scarecrow->Water->Harvest->Dropoff can be explained relatively capably by the Crazy-Arrow, the decoration-purchasing or secret-finding elements of gameplay are left to my welcome screen to explain. It would therefore be worthwhile adding elements to the HUD / game world that can help introduce / onboard / explain these systems, potentially in parallel to the existing loop/tasks, allowing players agency in what they do next. Social Interaction: So far I have relied on asynchronous competition through leaderboards for my social element, I would be interested in expanding the game loops to also include features which are enhanced by playing with others. This could include: Chests that are locked away, requiring players to e.g. pull a lever allowing others to gain access. "Large plot" areas, where multiple players must water the crops at the same time, and maybe must work together to slowly drag the crops, which then resulting in a noticeably larger pay-out when they are dropped off. <div