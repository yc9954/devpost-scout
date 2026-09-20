---
slug: "pantrypuzzle"
url: "https://devpost.com/software/pantrypuzzle"
title: "PantryPuzzle"
hackathon: "HackMIT 2023"
organization: "HackMIT"
winner: true
words: 669
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# PantryPuzzle

> Feeding the future of food sustainability

[Devpost](https://devpost.com/software/pantrypuzzle) · hackathon [[HackMIT 2023]]

## Facets

**mechanism** [[sensor_fusion]] [[vision_ocr]]
**domain** [[agriculture_food]] [[supply_logistics]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** firebase, flask, google-cloud-vision, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pantrypuzzle

## Body

Enter food in your pantry through text or image Share with your community if you don't want the food! Inspiration It’'s pretty common that you will come back from a grocery trip, put away all the food you bought in your fridge and pantry, and forget about it. Even if you read the expiration date while buying a carton of milk, chances are that a decent portion of your food will expire. After that you’ll throw away food that used to be perfectly good. But, that’s only how much food you and I are wasting. What about everything that Walmart or Costco trashes on a day to day basis? Each year, 119 billion pounds of food is wasted in the United States alone. That equates to 130 billion meals and more than $408 billion in food thrown away each year. About 30 percent of food in American grocery stores is thrown away. US retail stores generate about 16 billion pounds of food waste every year. But, if there was a solution that could ensure that no food would be needlessly wasted, that would change the world. What it does PantryPuzzle will scan in images of food items as well as extract its expiration date, and add it to an inventory of items that users can manage. When food nears expiration, it will notify users to incentivize action to be taken. The app will take actions to take with any particular food item, like recipes that use the items in a user’s pantry according to their preference. Additionally, users can choose to donate food items, after which they can share their location to food pantries and delivery drivers. How we built it We built it with a React frontend and a Python flask backend. We stored food entries in a database using Firebase. For the food image recognition and expiration date extraction, we used a tuned version of Google Vision API’s object detection and optical character recognition (OCR) respectively. For the recipe recommendation feature, we used OpenAI’s GPT-3 DaVinci large language model. For tracking user location for the donation feature, we used Nominatim open street map. Challenges we ran into React to properly display Storing multiple values into database at once (food item, exp date) How to display all firebase elements (doing proof of concept with console.log) Donated food being displayed before even clicking the button (fixed by using function for onclick here) Getting location of the user to be accessed and stored, not just longtitude/latitude Needing to log day that a food was gotten Deleting an item when expired. Syncing my stash w/ donations. Don’t wanna list if not wanting to donate anymore) How to delete the food from the Firebase (but weird bc of weird doc ID) Predicting when non-labeled foods expire. (using OpenAI) Accomplishments that we're proud of We were able to get a good computer vision algorithm that is able to detect the type of food and a very accurate expiry date. Integrating the API that helps us figure out our location from the latitudes and longitudes. Used a scalable database like firebase, and completed all features that we originally wanted to achieve regarding generative AI, computer vision and efficient CRUD operations. What we learned We learnt how big of a problem the food waste disposal was, and were surprised to know that so much food was being thrown away. What's next for PantryPuzzle We want to add user authentication, so every user in every home and grocery has access to their personal pantry, and also maintains their access to the global donations list to search for food items others don't want. We integrate this app with the Internet of Things (IoT) so refrigerators can come built in with this product to detect food and their expiry date. We also want to add a feature where if the expiry date is not visible, the app can predict what the likely expiration date could be using computer vision (texture and color of food) and generative AI. <div