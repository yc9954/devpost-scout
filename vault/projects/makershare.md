---
slug: "makershare"
url: "https://devpost.com/software/makershare"
title: "MakerShare"
hackathon: "hack:now"
winner: true
words: 691
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/labor_employment"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# MakerShare

> A platform to request and provide physical resources to COVID-19 essential workers by uniting community members.

[Devpost](https://devpost.com/software/makershare) · hackathon [[hack-now]]

## Facets

**domain** [[labor_employment]]
**user** [[general_public]] [[patient_family]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** api, bootstrap, css, firebase, google-auth, google-cloud, google-cloud-hosting, google-maps, html, html5, javascript, jquery, twitter

## How they structured the write-up

- inspiration
- how it works
- how we built it
- challenges
- accomplishments that we are proud of
- what's next for makershare

## Body

Inspiration Our team has family members and friends who are working as essential workers. Many of them do not have proper safety equipment like masks and cleaning supplies. As many community members are making their own DIY masks and have surplus cleaning/medical supplies, we wanted to create a way where we can connect essential workers lacking supplies to generous community members who can make or already have these supplies. How it works A user can log in as either an essential worker or a community member. After logging in, they can access an integrated Google Map, where they view nearby posts of individuals who either need supplies, or can donate supplies. An essential worker will have the option to request supplies through a post or accept available supplies through replying to a post from a community member. A community member will have the option to accept an essential worker's post, and provide the services essential workers need or create their own post with services they can provide. Each listing will include a title of the supplies that can be given, or that is needed, description of the supplies, and contact information. After a listing is accepted, each party is informed and pick up details are left to both parties to decide. It is up to the community member and essential worker to decide who wants to pick up or drop off the supplies. How we built it We used Google's Firebase and Maps APIs for the backend construction. Namely, we used Firebase's hosting, authentication and database services. With the services we are able to put out the website, sign in users, and create listings for the community to interact with. We used the database's unique JSON formatting with Javascript to allow population of a listings page and the creation of new listings. For the front end development, we utilized HTML, CSS, and JavaScript to build the web app. Challenges Some members had very little prior front-end development experience before this hackathon. Though overcoming this challenge by improving our HTML, CSS, and JavaScript abilities was time-consuming, our well-designed, finished product is indicative of improvement in the front-end development related technical skills of our team. Some other challenges were incorporating the functionality of the Google Maps API effectively and in conjunction with the listings. Currently, it does not connect the addresses on the listings with markers on the Google Map because we did not have the resources or time to implement. Additionally, we were not able to fully incorporate a framework for accepting listings as of yet. However, we hope to accomplish these two tasks after the hackathon. Accomplishments that we are proud of Our team is proud of the front-end development knowledge gained throughout this hackathon; gaining a solid understanding of front end development has opened the array of projects we can create for the future. Additionally, we are very proud of the idea we ended up creating to attack the difficulties COVID-19 has presented our society. We feel it is a novel solution with a lot of potential to genuinely aid essential workers by providing them with the materials that they need most. Some of our team members did not have backend experience, and we are proud that we were able to learn how to incorporate Firebase with the hackathon's time constraint. We are now confident in our abilities to use Firebase on future projects. Following this hackathon, we plan to continue developing and improving upon the website, with hopes of launching it for the public to use as this pandemic continues. What's next for MakerShare In an attempt to improve upon our current design, we plan to do the following: 1) We created the best design given the time constraints, but there is always room to improve. We would revamp our design, making it more intuitive, organized, and visually appealing for users. One example of this is incoporating images in the listings: including sample images like medical masks, gloves, disinfectant wipes, etc. 2) Incorporate Facebook and Twitter API's for seamless sharing of MakerShare to social media platforms that will only increase the usage of MakerShare to benefit essential workers. <div