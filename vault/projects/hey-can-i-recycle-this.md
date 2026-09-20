---
slug: "hey-can-i-recycle-this"
url: "https://devpost.com/software/hey-can-i-recycle-this"
title: "Hey, Is This Recyclable?"
hackathon: "The PartyRock Generative AI Hackathon by AWS"
organization: "Amazon"
winner: true
words: 896
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Hey, Is This Recyclable?

> Ever wondered whether to throw something out or recycle it? Well this AI powered app can teach people to recycle items their local recycling centers can handle, reducing waste & increasing recycling.

[Devpost](https://devpost.com/software/hey-can-i-recycle-this) · hackathon [[The PartyRock Generative AI Hackathon by AWS]]

## Facets

**substrate** [[video_visual]] [[web_dom]]

**stack** amazon-web-services, bedrock, markdown, partyrock

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hey, is this recyclable?

## Body

Location Customized Recycling Tips! Provides answers for more than just curbside recyclables! Sample use of Hey, Is This Recyclable? Inspiration I want to see things that can be recycled actually recycled. I became extra concerned about recycling when I realized well meaning people (including me), put items not meant to be recycled in the recycling and these are considered "contaminants". Contaminants cause the recycling process to breakdown or worse cause legitimately recyclable material to be considered contaminated and treated like trash (causing it to end up in a landfill). What it does This app uses AWS PartyRock tooling to bring the power of AI to this problem. The user enters the item they wish to recycle and their location into the app and then AI uses it's vast resources to determine whether the item is truly recyclable or trash. The app uses rules to help find services that can deal with a wide variety of recyclable material, a much better solution than just going to your local trash hauler website. Recycling options change over time and we all like to travel, this app makes it easy to learn the latest recycling guidelines for wherever we happen to be. Also, just for the fun of it, the app uses a feature of PartyRock to display an AI generated image of the item being searched. How we built it The AWS PartyRock app creation process really couldn't be simpler. I watched part of one video and jumped in to create the first version of this app. I went to the PartyRock site and filled in a description of what I wanted AI to do for me. I started with something like "Determine whether the type of plastic entered by the user can be recycled in the location entered by the user." PartyRock presented me with three widgets one to enter the type of plastic, one to enter the city and state and one to see the results. The widgets are easy to customize for size, location, wording, etc. I soon realized the app would be more useful if it could search in the county the person was located in and I knew that the output of one widget could be passed in to another. So I updated my "Recyclability" widget by simply adding "and the County of the " followed by an @ and the name of my CityState widget...simple! I also wanted the user to be able to search for more than just plastic, and include more recycling services than just the city or county waste facility. So I changed the description of widget one from "Type of Plastic" to "Thing I Want to Recycle" and changed the Recyclability widget by adding: "If [The thing you want to recycle:] is metal, also consider facilities in the area that recycle scrap metal". This allowed users to search for other types of curbside recyclables and also learn about recycling of dishwashers, computer parts, snow blowers, etc...hopefully keeping them out of the landfill. Challenges we ran into Some surprises occurred in using the PartyRock app, for example I easily added a Static Text widget with plenty of text to describe the app and when I went back in to edit the widget to remove its title (to simplify the app page), it deleted the widget without warning! I also had some challenges getting the output to be concise. Once I added the "rule" that If the item is metal, also consider scrap metal facilities, the output would frequently include silly text like: "Since 'pizza box' is not metal there is no need to consider local scrap metal facilities." I reduced the chance of this happening by changing the rule to If (and only if) [The thing you want to recycle:] is metal Not challenging but frustrating AI results (hallucinations) at times. Incorrect answers for whether a particular item can be recycled. I requested "Include a link to the appropriate website for more details" be included in the output, the resulting URLs were invalid but close to correct. For example search for Plastic bags and the URL result is https://www.stpaul.gov/departments/public-works/recycling-hazardous-waste/recycling/plastic-bags-film but that page doesn't exist. It's close though, because page this does exist https://www.stpaul.gov/departments/public-works/ and a human can follow the prompts from there. Accomplishments that we're proud of It's neat to be able to use new technology to construct something, especially something useful. I'm proud of the fact that this app is a useful and fun tool that can educate folks and perhaps improve the recycling process, cause less waste and more recycling. What we learned Frankly this hackathon was the first I had heard of PartyRock and it brought it to my attention as well as AWS Bedrock. I learned PartyRock apps work well on a phone as well as a computer. I learned I have this handy tool I'm sure can be put to use for other problems I might run into. I also learned that only #1, #2 and #5 plastic types are recyclable in my town. What's Next for Hey, Is This Recyclable? I'm a member of a local computer/tech club that meets monthly and I plan to present PartyRock and Hey, Is This Recyclable? . I also have been using another PartyRock app for image generation and am thinking of adding it on to a previous art project some friends and I built during Covid. <div