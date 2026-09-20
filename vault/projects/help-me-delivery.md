---
slug: "help-me-delivery"
url: "https://devpost.com/software/help-me-delivery"
title: "Help Me Delivery"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 1149
team_size: 0
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/elder_child_care"
  - "domain/retail_commerce"
  - "domain/security_privacy"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Help Me Delivery

> Giving vulnerable populations an easy platform to identify local shops, build shareable shopping lists that they can easily share with friends, family or trusted connections on social media.

[Devpost](https://devpost.com/software/help-me-delivery) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**domain** [[elder_child_care]] [[retail_commerce]] [[security_privacy]]
**substrate** [[geospatial]] [[web_dom]]

**stack** aws-ec2, aws-lambda, awsec2, foursquare, google-maps, materials-ui, materialsui, mongodb, nginx, node.js, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for help me delivery

## Body

Shop Finder Screen Shopping List Creation Process Generated Shareable URL Display Unique Shopping List Display How It Works About HelpMeDelivery Inspiration During the current Global Crisis there is a significant percentage of the population that are considered to be vulnerable and unable to go out to complete essential shopping. This includes the elderly, currently sick or those with preexisting conditions that have been asked to completely isolate. The knowledge that there is a large percentage of people who are in this position has been widely publicized but many are left wondering how they can help or even how they can ask for help during this challenging time. Help Me Delivery tries to answer those questions through an easy to use website that allows for store selection, shopping list creation and easy sharing between trusted individuals. My hope is that anyone who needs help can turn to Help Me Delivery to create a shopping list of essentials that they then share on social media asking for assistance. Or, if you are someone who wants to help that they can share the link to the site on forums or social media saying that they are happy to make deliveries to anyone who needs it. What it does Help Me Delivery is a website that people can turn to when they need to ask someone for help to complete their shopping. When visiting the site it presents you with local grocery stores that are currently listed as open. A user can then select a shop and develop a shopping list using a simple pop-up dialog. When finished this information is then compiled and formatted into a shopping list and a unique link is generated that they can share with a trusted friend and/or relative to invite them to help. When visiting this unique link the shopping list and address of the shop are presented along with a friendly message of how to help out. How I built it The HelpMeDelivery.com website is built using React and Node.js with the visual components coming from Material-UI . The React solution is deployed on an Amazon EC2 Linux server and is being server using Nginx. This frontend interacts with two Python backend APIs, the first of which is an endpoint which takes your location data and returns all the relevant and nearby shops that are currently listed as open. This information is extracted from the Foursquare Places API and then formatted in such a way that only the relevant information is returned to the site. The second API is a wrapper for a MongoDB which is used to store newly created shopping lists, assign them an ID and then to return them when the generated link is accessed. These Python APIs are deployed on AWS Lambda serverless functions. Challenges I ran into A core challenge that I wanted to tackle throughout the development of Help Me Delivery was making the process as easy as possible while also protecting the person requesting the shopping trip. This lead to making important and challenging design decisions about how shopping lists could be shared and what data we would request and share on the shopping list URL. It also lead to the development of the unique URL system to ensure the shopping list can only be viewed by receiving the URL from the creator of the list. My experience in the past mainly revolved around creating functional backend applications but this mission required me to expand my knowledge further and take on a new technology and programming language. A result of taking on a new technology like this was the inexperience of deploying such an application into production. The Hackathon had a strict deadline of 4 days of development time which required a strict scope of what the application functionality would be and what it would look like at the end of this time. The strict time management together with the unfamiliarity of how to deploy a production React web application proved to be a challenge when development was completed. Accomplishments that I'm proud of I am proud that the final product turned out to be as polished as I had hoped and that the functionality is how I had envisioned and planned for. I am satisfied with the level of functionality achieved given the time we had to develop and deploy the application. I am however mostly proud of the fact that this application is now available free of charge to anyone who is currently struggling to get their shopping done. I hope that Help Me Delivery has the impact of being a tool that anyone can use with ease and makes people's lives a little bit easier during this tough time. What I learned I previously have not had much experience writing in React and Node.js outside of some mobile app development. So one of the big learning curves for me was designing and building and deploying an interactive and easy to use website. I spent a lot of time testing components to see if they were as easy to use as I had hoped and constantly tweaking flows to try and make the process as quick and simple as possible for anyone to use. The process of developing a full stack application in a small time frame was also something that I previously had not had much experience in and was steep learning curve for me when selecting technologies to interact with each other and developing interactions between different components of the solution. What's next for Help Me Delivery The core idea of Help Me Delivery is to make the process of creating and requesting shopping from a friend as quick and easy as possible. I think that there will always be elements that can be improved, revised and newly introduced to try and build towards that idea more and more. For me I think that integration into Social Media will play a major role in this. The aspect of sharing is something that is important to the project and would be something great that could be built upon through the use of Facebook Messenger integration or even Twilio for the mobile communication of shared shopping lists. As it stands now the sharing of the link needs to be done manually, but I think adding some automated messaging options will make the process even easier Full mobile support is also a key area of expansion and I think that the development choice of using React allows for easy entrance into cross platform mobile applications through React-Native. This would then also allow for a new way of sharing and accepting shopping lists with trusted friends through device to device communication. There are further points of development available that could be aided through mobile integration such as the inclusion of more of the shopping process such as order acceptance, reporting of unavailable products and delivery estimation times. <div