---
slug: "mirror-l89356"
url: "https://devpost.com/software/mirror-l89356"
title: "MirrorPort"
hackathon: "Hack the North 2023"
organization: "Techyon"
winner: true
words: 680
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/elder_child_care"
  - "domain/housing_homeless"
  - "domain/immigration_refugee"
  - "user/clinician"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# MirrorPort

> The portal for your bright future: a decentralized app for those starting a new life to securely store records via encryption, translate documents and provide contact to essential services.

[Devpost](https://devpost.com/software/mirror-l89356) · hackathon [[Hack the North 2023]]

## Facets

  <sub>weak: cross_origin_web</sub>
**domain** [[elder_child_care]] [[housing_homeless]] [[immigration_refugee]]
**user** [[clinician]] [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]] [[video_visual]]

**stack** icp, react, react-native

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mirrorport

## Body

Login Page Landing Page Scanner Camera Upload Success! Inspiration According to Statistics Canada, nearly 48,000 children are living in foster care. In the United States, there are ten times as many. Teenagers aged 14-17 are the most at risk of aging out of the system without being adopted. Many choose to opt-out when they turn 18. At that age, most youths like our team are equipped with a lifeline back to a parent or relative. However, without the benefit of a stable and supportive home, fostered youths, after emancipation, lack the consistent security for their documents, tacit guidance for practical tasks, and moral aid in building meaningful relationships through life’s ups and downs. Despite the success possible during foster care, there is overwhelming evidence that shows how our conventional system alone inherently cannot guarantee the necessary support to bridge a foster youth’s path into adulthood once they exit the system. What it does A virtual, encrypted, and decentralized safe for essential records. There is a built-in scanner function and a resource of contacts who can mentor and aid the user. Alerts can prompt the user to tasks such as booking the annual doctors' appointments and tell them, for example, about openings for suitable housing and jobs. Youth in foster care can start using the app at age 14 and slowly build a foundation well before they plan for emancipation. How we built it The essential decentralized component of this application, which stores images on an encrypted blockchain, was built on the Internet Computer Protocol (ICP) using Node JS and Azle. Node JS and React were also used to build our user-facing component. Encryption and Decryption was done using CryptoJS. Challenges we ran into ICP turned out to be very difficult to work with - attempting to publish the app to a local but discoverable device was nearly impossible. Apart from that, working with such a novel technology through an unfamiliar library caused many small yet significant mistakes that we wouldn't be able to resolve without the help of ICP mentors. There were many features we worked on that were put aside to prioritize, first and foremost, the security of the users' sensitive documents. Accomplishments that we're proud of Since this was the first time any of us worked on blockchain, having a working application make use of such a technology was very satisfying. Some of us also worked with react and front-end for the first time, and others worked with package managers like npm for the first time as well. Apart from the hard skills developed throughout the hackathon, we're also proud of how we distributed the tasks amongst ourselves, allowing us to stay (mostly) busy without overworking anyone. What we learned As it turns out, making a blockchain application is easier than expected! The code was straightforward and ICP's tutorials were easy to follow. Instead, we spent most of our time wrangling with our coding environment, and this experience gave us a lot of insight into computer networks, blockchain organization, CORS, and methods of accessing blockchain applications through code run in standard web apps like React. What's next for MirrorPort Since the conception of MirrorPort, it has always been planned to become a safe place for marginalized youths. Often, they would also lose contact with adults who have mentored or housed them. This app will provide this information to the user, with the consent of the mentor. Additionally, alerts will be implemented to prompt the user to tasks such as booking the annual doctors' appointments and tell them, for example, about openings for suitable housing and jobs. It could also be a tool for tracking progress against their aspirations and providing tailored resources that map out a transition plan. We're looking to migrate the dApp to mobile for more accessibility and portability. 2FA would be implemented for login security. It could also be a tool for tracking progress against their aspirations and providing tailored resources that map out a transition plan. Adding a document translation feature would also make the dApp work well with immigrant documents across borders. <div