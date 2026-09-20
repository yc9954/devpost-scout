---
slug: "a-farmer-s-life"
url: "https://devpost.com/software/a-farmer-s-life"
title: "A Farmer's Life"
hackathon: "Snap AR Lensathon"
organization: "Snap Inc."
winner: true
words: 993
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/agriculture_food"
  - "domain/supply_logistics"
  - "user/frontline_worker"
  - "substrate/video_visual"
---

# A Farmer's Life

> A persistent augmented farming simulator game right in Snapchat. Using time-based elements, weather API data and hand-tracking, users are able to experience a simulator game like never before.

[Devpost](https://devpost.com/software/a-farmer-s-life) · hackathon [[Snap AR Lensathon]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[agriculture_food]] [[supply_logistics]]
**user** [[frontline_worker]]
**substrate** [[video_visual]]

**stack** javascript, lensstudio, machine-learning, snap, snapchat, weatherapi

## How they structured the write-up

- foreword
- what is a farmer's life?
- development notes
- challenges
- accomplishments
- future plans for a farmer's life

## Body

Foreword Max and I have been building lenses for quite a while in the Snapchat community but we haven't really seen a lens that works over a longer period of time. It's a concept that's forgotten pretty easily as lenses are mostly fast and fun to use, but it's very interesting one to think about. Having a game that spans over multiple hours or even days, can be a fun and challenging alternative to the, now missing, Snap Games environment. Our lens has also been inspired by simulator games like Stardew Valley and Farming Simulator, which are very popular within every demographic. What is A Farmer's Life? For this hackathon we build a real-time farming simulator game right within Snap. The game uses persistent storage to save crops, money, and time-based elements. It’s a game you have to come back to during the day to farm and maintain your crops. All crops have three different growth cycles, custom models and VFX. The weather in Amsterdam (where we are based) influences crop cycles and weather elements in-game. When it rains, you don't have to water the crops and rain pours down on the farm. If there's sun (sadly there's never sun in Amsterdam) the crop timers will speed up and your crop will be growing faster! In the selfie cam there’s a reward shop where you can unlock several new looks with hard-earned cash. We've build these assets to be fun and easy to share to let users show off their achievements with friends. Development notes During development of the lens we explored a lot of different areas of Lens Studio. Getting the time-based elements right was tricky, as is the Hand Tracking that's required to work the crop fields. By building a highlighter system it made it much easier for the user to see what they are doing and to visually give them hints about the pointing/distance checking system. By collecting, creating and adjusting these assets to work within the low-poly environment of Lens Studio, we have enough to cover this experience and possibly continue development in the future There's many UI elements that work together to give the user the full experience, packaged in a few menus. By designing the icon to make them as recognizable as possible, we made the experience as inclusive as possible. It's a fairy complex game so this was one of the hardest part of the development experience. These are the newest Lens Studio features we used: Weather API Persistent Memory Hand Tracking Custom VFX Challenges As mentioned previously, we have to give the user the easiest experience as possible to navigate and use the lens. It can be hard to explain to a new user what to do and where to find the right tools to play the game. The hand tracking can be funky as well so we built a highlighting system that shows users what the game is seeing and where to go from there. Another challenge was using the right tracking to place the game in a good way. We resorted to a slightly hacked version of the world tracking to make the asset appear 160cm below the camera, which will fit most users. It's important that we leave space for the hand tracking to distinguish between the six different crop patches and that the user feels like they are really working the crop lands. This is why we had to resort this option. It includes sense of space, but leaves a little bit of quality in having actual surface tracking. In a future update we could have users place the crop fields as they please or move these around in the scene, but for now it's pretty good as it is. Accomplishments We built (possibly one of) the first time-based lenses that really empowers users to come back into the lens and achieve new unlockables over time. We hope this sparks a new wave of lenses that have consistent new content and will save the users hard work in a persistent way. We also hope this is a cool example of using hand tracking outside of Spectacles to really interact with a game. Future plans for A Farmer's Life Here's a roadmap and a monetization plan: Phase I : Give the user more selfie looks to unlock using Remote Assets to fit more in. Add more variety of crops and have crops perish if not watered. Give crops purpose. Ability to stack farmed ingredients in an inventory system. Phase II : Introduce a crafting mechanic by using farmed ingredients to create products. Give products purpose. Unlock more content in the game and use them to expand crop fields or boosting the farm. Give buildings a purpose and make them upgradable with materials bought from a shop. For example: Barn can be an inventory boost and a pig pen could unlock pig related items in the selfie shop. Phase III : Add farm animals that wander around and can be bought with cash. Use crafted products to feed animals and unlock new ones. Take care of animals, get back fertilizer and boost crop yield. Achievement system that stores data based on gameplay. Introduce even more selfie looks. Monetization plan Expand the farm. Speed up gameplay by placing more crop patches. Fix buildings or upgrade your farm to unlock new content. Fixing or upgrading would require materials bought from the selfie-shop or using in-lens purchases. Content expansion. Introduce farm animals to feed and grow, creation of farm products from ingredients, add new looks for the selfie camera. Work with brands to introduce their product in the game. Craft the promoted product and use the product to expand the farm. Could be tools or food products. Transport the farm to a sponsored location. By introducing a virtual environment, we could work with brands to transport the user into a different place. This would be toggleable. Thank you for reading! Max van Leeuwen Danny Marree <div