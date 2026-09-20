---
slug: "voxcastor"
url: "https://devpost.com/software/voxcastor"
title: "Voxcastor"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 828
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/web_dom"
---

# Voxcastor

> World is fast and we have almost limitless access to information. Fight the information overload by choosing your own sources and let the state-of-the-art algorithms and robots do the rest.

[Devpost](https://devpost.com/software/voxcastor) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**substrate** [[web_dom]]

**stack** amazon-web-services, api, azure, google-cloud, javascript, mailgun, postman, rest

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for voxcastor

## Body

Voxcastor's mascot Voxcastor has been created using Postman Inspiration We're living in a world, where we have almost limitless access to information. But too much information can cause information overload. There are too many sources, too many articles and our days don't change - they are still 24 hours long, for everyone, everywhere. You probably know this story all too well: "I just want to read the headlines and then back to work" 2 hours later... and you're still down the information rabbit hole, with 10 tabs still open to read. And that's why we came up with Voxcastor. With Voxcastor, you become your own podcast (or should we say voxcast?) creator. You choose the source of news, you put your articles in and the machine takes care of the rest. All you need to do now is put on your headphones, stream the audio to your car infotainment system and listen. What it does Voxcastor skips the step of opening the news sites and quickly becoming overwhelmed by articles and headlines left and right. There are currently two main scenarios how it can operate: Select the news source(s) and/or theme you are interested in. Voxcastor extracts the headlines, converts them to SSML format and creates the audio file for you. Input the direct article URL of your choice and let Voxcastor do the rest (pun intended). Being highly modular, it can also do some optional transformation steps: Creating just a summary of the text. Good if you want the get the gist of the information, but don't need to know the details. Translating the text from and to almost any language. Useful in cases you want to diversify your information sources but don't speak the language of the source or if you want to have first-hand information from a foreign country which language you don't speak. Sending the audio file anywhere - to your email, to the IM of your choice (Slack, Signal...) or just store it in your cloud storage. How we built it We knew right from the start that we didn't want to become dependent on a single provider. Not all APIs are built the same, all of them have some upsides and downsides - be it the ease of use, feature set or pricing. In some countries censorship is unfortunately also a thing. That's why we decided to implement the core functionality using the big three cloud providers - Google Cloud, AWS and Microsoft Azure. Next step was creating the main scenarios described above and splitting it into the smallest possible chunks of functionality. The rest of the time was spent reading documentation, signing up for the services, creating the API keys and putting it all together so that the idea of modularity and scalability is achieved. Challenges we ran into Since the main idea was to create the service using Postman, we were highly reliant on access to REST APIs. However, some services don't play nicely with REST and they are dependent on providers' proprietary SDKs and/or the use of the services with REST is not well documented. Also Postman's handling of binary files could be better for our use-case. Some of the audio files are returned as binary files, some of them as base64 encoded strings. While transformations between the two are indeed possible, the transferring itself (sending buffer streams/binary data) as well as working with filesystem is a bit cumbersome. It's definitely not impossible, but the solutions we found proved to be more on the complicated side and with this prototype of Voxcastor we aimed for as much simplicity as possible. Accomplishments we're proud of Simply and clearly, we're most proud of the achieved scalability and modularity. The structure of the current solution is clean, readable and robust. We can swap the providers in no time, we can add/remove steps along the way and we're not dependent on the single source of truth. And that's how it should be and that's what we aimed for. What we learned The main takeaways from this inspiring journey are: Nowadays you can build almost anything just by "connecting the correct wires". Sure, you need to know where they are and how to plug them in correct order but with all the resources available throughout the web, the internet quickly becomes your imagination's playground. Neural language synthesis is better than we expected. The clearly robotic voices are a thing of the past. Robots of today sound more and more like humans (which is also slightly terrifying) and that's just the start. What's next for Voxcastor Using Postman allowed us to test the underlying idea of synthetically created voxcasts rapidly and we were able to quickly create a fully functional prototype / MVP. After showing Voxcastor to a couple of friends it now seems, that the product is really worthwhile and it could benefit many people with different use-cases. Creating a public beta with more transformations and integrations seems like a logical next step. <div