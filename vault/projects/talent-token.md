---
slug: "talent-token"
url: "https://devpost.com/software/talent-token"
title: "Talent Token"
hackathon: "Web5: Building the Decentralized Web"
organization: "TBD"
winner: true
words: 827
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/disaster_emergency"
  - "substrate/code_repository"
---

# Talent Token

> Empower your professional journey with Talent Token! Manage your profile, share and receive endorsements of your skills, languages and work experiences without compromising privacy.

[Devpost](https://devpost.com/software/talent-token) · hackathon [[Web5- Building the Decentralized Web]]

## Facets

**domain** [[disaster_emergency]]
**substrate** [[code_repository]]

**stack** bootstrap, primevue, tailwind, vite, vue.js, vue3, web5

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for talent token

## Body

User Profile Edit User Profile View, including endorsed skills User Profile View, including endorsed experiences and languages View of confirmed endorsements requests for one skill List of contacts view, including contact request form Modal with one of the confirmed contacts Skill Endorsement Request, with received and sent pending requests Experience Endorsement Request Confirmed given skills Confirmed received skills Splash screen on Web5 Agent loading Endorsement Protocol, confirm/success endorsement request Endorsement Protocol, request deletion Talent Token Inspiration About a month before this hackathon's submission period started, 500 million LinkedIn profiles were leaked and offered for sale on a well-known hacker forum . The domain of online professional networking is complex . On one hand, platforms like LinkedIn are great to show your professional skills and experiences while creating and extending your work network. On the other hand, this exposure comes with an inherent risk of getting your data shared with undesired users, entities or companies. I created Talent Token to leverage Web5 in the implementation of a platform that manages users' professional profiles and skills in a decentralized manner. What it does Talent Token is a decentralized professional networking platform built using Web5. Profile management Users can create and manage their profiles, including personal information, work experience, education, skills, certifications, and language proficiency. The profile also includes avatars, social networks, and other contact options. Users can share their profiles directly to the DWNs of other users by DID. Once shared, the user will also receive a contact request that, once accepted, will share their own profile. Endorsements The platform provides a way to exchange endorsements for skills, languages, and work experiences among users in a decentralized web node. Users can request endorsements for elements in their profile to contacts in their network. All confirmed endorsements are displayed in the user's profile, detailing the DID and provided name of the endorsers, as well as the endorsement date. The endorsements are stored in the DWNs of both the endorsed and endorser, and are signed by the respective author's DID to ensure data integrity. Users can also confirm or reject endorsement requests they receive. How we built it We built Talent Token using Vue3 for the front end and Web5 to leverage decentralized web nodes for storing user information. The decentralized approach ensures data security and user privacy. The platform also utilizes Bootstrap 5 and PrimeVue components for UI and enhanced functionality. Protocols Talent Token defines protocols for the User Profile, contact requests, and Endorsements. In the case of endorsement, the same protocol is used for endorsement requests, confirmations, and rejections. Endorsement Process Flow To limit who can endorse a skill, language, or work experience, Talent Token relies on an endorsement request protocol. The user needs to know the DID of the endorser (available by the DID Resolver that the agent is connected to). On creation, the endorsement request record is created in both nodes. The endorser can confirm or reject the request, and the result is stored in both DWNs and verifiable by the author's attributes. Additionally, the requester can mark the endorsement request as deleted in both nodes. The user's agents will retrieve this record later and perform the physical deletion to avoid flooding the node. A similar flow for physical deletion is performed when the request is confirmed or deleted. Challenges I ran into During the development process, I faced challenges in integrating Web5.js seamlessly and ensuring a smooth user experience. Since most of my experience is in backend development, troubleshooting both Vue3 and Web5 issues required deep diving into both source code, documentation, as well as the TBD discord channel 💜. The main challenges during the design and development of Talent Token were related to understanding the constraints of decentralized technologies to provide the best user experience possible. Accomplishments that I'm proud of I'm proud of the final result of integrating Web5 into Talent Token's user-friendly interface. The endorsement system adds a unique touch, fostering a sense of community and trust among users while skipping a centralized authority overall. I'm really happy that the whole protocol can be implemented without any stateful centralized service. What I learned Throughout the hackathon, I gained valuable insights into the complexities of working with decentralized technologies, the limitations it presents and the problem-solving involved in rethinking user flows. I also got onboarded in Vue3 and learned how to overcome challenges associated with integrating various technologies into a cohesive application. What's next for Talent Token Apart from refining the user interface, the next big step is to make the profile-sharing scalable. In the current implementation, while reusing protocols and UI components allowed to implement contacts and profile sharing, the real challenge would come with large networks of users that need to handle updates. Some additional design would be required to, for example, write a confirmation endorsement for an endorsed user and all the users in their network (since the record needs to be verifiable and the profile information up to date). <div