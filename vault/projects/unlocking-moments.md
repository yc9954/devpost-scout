---
slug: "unlocking-moments"
url: "https://devpost.com/software/unlocking-moments"
title: "The Human Project"
hackathon: "The European Commission's EUvsVirus Hackathon"
organization: "European Commission"
winner: true
words: 1710
team_size: 6
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/mental_health"
  - "domain/security_privacy"
  - "domain/transportation"
  - "user/clinician"
  - "user/developer"
  - "user/frontline_worker"
  - "user/general_public"
  - "substrate/geospatial"
---

# The Human Project

> A platform for people that want to see and contribute to the human story of the essential worker community during this pandemic and beyond.

[Devpost](https://devpost.com/software/unlocking-moments) · hackathon [[The European Commission-s EUvsVirus Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[structural_withholding]]
**domain** [[civic_government]] [[developer_tools]] [[health_clinical]] [[labor_employment]] [[mental_health]] [[security_privacy]] [[transportation]]
**user** [[clinician]] [[developer]] [[frontline_worker]] [[general_public]]
**substrate** [[geospatial]]

**stack** amazon-web-services, docker, elasticsearch, google-maps, javascript, koa, next.js, react

## How they structured the write-up

- inspiration
- what is it
- the problem
- the solution
- what it does
- the value
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what’s next for the human project?

## Body

Onboarding Welcome Add Your Story Interactive Map View Stories Create an Account Changes in emotion over time Inspiration As seen through history, during moments of global crisis innovation sprouts at a massive rate. And we’re seeing it again as a result of Covid-19. A number of aggregators of information regarding the status of this pandemic have been created. And as a result, the global population can get real-time information about its status and impact. As we write this, 4,000 more cases of Covid-19 have been discovered in Spain. And another 378 new deaths have been reported in the same area. We see these numbers growing every day, and as a result, people are getting number fatigue. What started as a mission to provide information to the world has begun to be resented by that same population. People are scared, angry, and generally don’t understand why this hasn’t slowed down yet. They are ready for a new news cycle. Why is that? We believe it’s because we’ve taken the human element out of this pandemic, and we want to put it back in. How do our communities feel at any given point in time? And how can we use that data in a way that gives the world a more humanized picture during a global crisis? Those are the questions our team posed to ourselves when coming up with our solution. The Human Project. What is it The Human Project is a platform for people that want to see and contribute to the human story of the essential worker community during this pandemic and beyond. It aims to reveal the sentiment of the essential worker population across Europe in order to celebrate and promote positivity while simultaneously connecting help and support where it's needed. The Problem During times of global crisis and particularly with this pandemic, families, friends, and colleagues are torn from each other with little time to adjust. Isolation, fear, anxiety quickly set in with limited knowledge of what's happening from day-to-day. Portions of the population, essential workers, are thrust into the spotlight and must assume their daily duties with disregard for their own mental and physical health. How might we help the essential worker population share their feelings and stories with the rest of the world, and provide them the support they need? The Solution A platform that collects essential worker sentiment along with their stories. Mapped in a way that it highlights where this community needs the most support during this time of crisis. What it does The Human Project is first an aggregator to understand the general well-being of essential worker populations during a global crisis. Essential workers input their feelings from a set of keywords based on an emotion classification spectrum. That information populates a map, giving a global view of the emotions this population has at any given point in time. It uses this insight to identify trends and to understand how well-being has changed over time in areas of the world. The Human Project also provides the essential worker community a chance to share their stories. Giving the world visibility into their lives, to understand what they are going through at this moment, and to provide them support and celebrate their courage during this time of crisis. The Value The sweet spot for innovation lies at the intersection of a solution being viable, feasible, and desirable. We believe The Human Project does just that. Viability As a global community, we’re struggling to truly understand the impact this crisis has on the well-being of our essential workers across Europe and the world. The Human Project can identify trends in sentiment. If we can see where general well-being is dropping, then governments and organizations will be better equipped to protect those communities early. The human project is also important for our general population to understand what our essential workers are going through. By bridging the gap between quantitative numbers and storytelling, we’re humanizing the analysis. People won’t only know what others are feeling across the globe, but why they are feeling that way. And showing the ‘why’ is our psychological driver for our global communities to give support to those that need it. Feasibility The Human Project is a simple aggregator of anonymous information, reliant on crowdsourcing. With the help of partnerships with governments and organizations to share this product with essential workers in their communities, we strongly believe that being able to tell their stories will start a grassroots movement across Europe and beyond. Once that data begins to populate the experience, it will take on a life of its own. The team will be able to turn our learnings into actionable next steps to continue to grow the product. Desirability Research has given us the insights that the essential worker community is vulnerable, but they don’t have a place to make that known. By delivering this solution to them, we’re giving them their own place. An outlet that isn’t filled with other news, hashtags, and posts that drowns out their stories. This solution is for them. Because for this community, doing the hard work and being able to share their story is the reward. How we built it The ideation of this challenge came out of proven lean methodologies that promote structured processes so we could arrive at clear actionable outcomes. Problem Identification and Solution We set up 3 ideation sessions to help us arrive at our solution: Research interviews to gain a deeper understanding of the problems in the space of protecting isolated and risk groups. Expert Interview 1 - Holly Penalver (Founder Indigo Volunteers and NHS Nurse) Expert Interview 2 - Philippa Mander (Health Co-ordinator at Phunzira and NHS Nurse) Research Notes In summary, Holly and Philippa talked passionately about essential workers and volunteers feeling the most supported and connected when they were able to exchange real stories with each other in their community. This positive connection is what drives you to continue to support one another on a project or in times of crisis. Finalizing the problem to solve Individual solution sketch of ideas with a final vote on the direction to move forward with. Design The design team used the collaborative design software tool, Figma, to work through the user flow and design together. Development Build Fully in the cloud, this application is running software ready for the high load that it's expected from it. The frontend application is running in a ECS cluster in AWS ready to be scaled as needed. Connected to an Elastic cache the information both highly scalable and lightning fast. This app has been built from the ground up with some of the latest technologies used by most tech companies. React, NextJS, NodeJS, Styled-Components are just a few of the core components of this application. The map is powered by Google Maps API with a custom theme tailored for our look and feel. Final Expert User Test Holly Penalver (Founder Indigo Volunteers and NHS Nurse) In summary, Holly showed a real positivity towards this experience and understood quite quickly the value that an experience like this could bring to this community. Additionally, Holly provided some really clear consideration to move forward with as we iterate. Specifically areas around global accessibility and moderation of content. Challenges we ran into The two biggest challenges our team faced were: Understanding the problem space - Having no previous experience in this space, we were reliant on desk research and interviews with experts to take us down the right path. Deciding which problem to solve - The only real hiccup we had was deciding which path to go down. But we got there! Accomplishments that we’re proud of We’re not experts in this field by any means, but we are a passionate group strategists, designers, and developers that want to make a positive difference in the world. In the end, we’re all really proud of the outcome and would love to see this experience have a positive impact. What we learned First, we learned a lot about what our frontline workers are going through. And if this hackathon has given us anything, it’s greater respect and admiration for these strong and courageous people putting their lives on the line for us. They are no longer just a number. Secondly, make a decision and stick to it. While we are really happy with the outcome, it took the team some time to get there. What’s next for The Human Project? Iterate, release, and eventually scale. Iterate We’d love to release this experience to the public as soon as possible. There is still some work to get us there. Some essential insights from early testing have given us some immediate next actions. How might we make it safe to use? Creating and verifying an account Forcing login to be able to post content Is the system self-moderated eg: reporting content, or do we implement automated keyword flagging and blocking? How might we make it accessible for all languages? Inline translation plugins to translate in real-time eg: Google Translate Release Once some key iteration takes place, we’d look to release an MVP of this experience in the near future. For it to be a successful product, it’s important that we get it out in the public soon so we can learn and continue to iterate. Scale While our focus for this hackathon was essential workers on the frontline during Covid-19, we see many great benefits to understanding sentiment and hearing stories from other groups across the world. We understand many crises are happening around the world daily that could use this platform; war, famine, poverty, environmental. Our goal is for this product to be available for all. So the world can move away from treating people as numbers. We want to bring the story of each of those numbers forward. Future iterations we would consider: How might we represent changes in emotion over time for different regions Scrub through a timeline to see the local emotion change View specific time periods or ‘labeled events’ eg: Coronavirus See the changes on a global scale vs local scale How might we allow you to contribute from outside the platform Text/WhatsApp in your story Send in your story via a video or voice message <div