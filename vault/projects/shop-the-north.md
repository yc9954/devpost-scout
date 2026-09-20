---
slug: "shop-the-north"
url: "https://devpost.com/software/shop-the-north"
title: "Shop The North"
hackathon: "Hack the North 2024"
organization: "Hack the North"
winner: true
words: 766
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Shop The North

> Sometimes online shopping can be dull, and most of all, turn away customers who are unsure about buying clothes online. VR will allow for customers to try on clothing in a virtual world.

[Devpost](https://devpost.com/software/shop-the-north) · hackathon [[Hack the North 2024]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[finance_payments]] [[retail_commerce]]
**substrate** [[financial_record]] [[video_visual]]

**stack** c#, github, json, oculus-gear-vr, shopify, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for shop the north

## Body

Using unity to make the environment Yellow shirt, black shirt, tropical shorts and black pants on the Shopify-hosted store The VR shop and the items available from the Shopify store for interaction (shirts and pants) Holding items Looking at mirror with the black shirt, red button can be pressed for purchase Trying on yellow shirt and tropical pants Inspiration Online shopping is hard because you can't try on clothing for yourself. We want to make a fun and immersive online shopping experience through VR that will one day hopefully become more realistic and suitable for everyday online shopping. We hope to make a fun twist that helps improve decisiveness while browsing online products. What it does This VR experience includes movement, grabbable clothes, dynamic real-time texturing of models using images from Shopify’s Web API, and a realistic mirror of yourself to truly see how these fits shall look on you before buying it! The user that enters the virtual clothing store may choose between a black/yellow shirt, and black/tropical pants which are products from an online Shopify store (see screenshots). The user can also press a button that would simulate a purchase :) How we built it Using the Shopify ProductListing API, we accessed the different clothing items from our sample online store with a C# script. We parsed the JSON that was fetched containing the product information to give us the image, price, and name of the products. We used this script to send this information to our VR game. Using the images of the products, we generated a texture for each item in virtual reality in the Unity game engine, which was then put onto interactable items in the game. Also, we designed some models, such as signs with text, to customize and accessorize the virtual store. We simulated the shopping experience in a store as well as interactable objects that can be tried on. Challenges we ran into Linking a general C# script which makes REST API calls to Unity was a blocker for us because of the structure of code Unity works with. We needed to do some digging and search for what adjustments needed to be made to a generic program to make it suitable for the VR application. For example, including libraries such as Newtonsoft. We also ran into conflicts when merging different branches of our project on GitHub. We needed to spend additional time rolling back changes and fixing bugs to take the next step in the project. One significant difficulty was modelling the motion of the virtual arms and elbows when visible in the mirror. This must be done with inverse kinematics which we were never quite able to smoothly implement, although we achieved something somewhat close. Getting the collision boundaries was difficult as well. The player and their surroundings constantly change in VR, and it was a challenge to set the boundaries of item interaction for the player when putting on items. Accomplishments that we're proud of Our project has set a strong foundation for future enhancements. We’re proud of the groundwork we’ve laid for a concept that can grow and evolve, potentially becoming a game-changing solution in VR shopping. What we learned We learned the importance of anticipating potential technical blockers, such as handling complex features like inverse kinematics and collision limits. Properly allocating time for troubleshooting unexpected challenges would have helped us manage our time more efficiently. Also, many technical challenges required a trial-and-error approach, especially when setting up collision boundaries and working with avatar motion. This taught us that sometimes it's better to start with a rough solution and iteratively refine it, rather than trying to perfect everything on the first go. Finally, working as a team, we realized the value of maintaining clear communication, especially when multiple people are contributing to the same project. Whether it was assigning tasks or resolving GitHub conflicts, being aligned on priorities and maintaining good communication channels kept us moving forward. What's next for Shop The North We want to add even more variety for future users. We hope to develop more types of clothing, such as shoes and hats, as well as character models that could suit any body type for an inclusive experience. Additionally, we would like to implement a full transaction system, where the user can add all the products they are interested into a cart and complete a full order (payment information, shipping details, and actually placing a real order). In general, the goal would be to have everything a mobile/web online shopping app has, and more fun features on top of it. <div