---
slug: "twogether"
url: "https://devpost.com/software/twogether"
title: "omw"
hackathon: "Hack the North 2021"
organization: "Techyon"
winner: true
words: 667
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
---

# omw

> omw (on my way!) is a real-time navigation tool that harnesses the power of community to make commuting safer

[Devpost](https://devpost.com/software/twogether) · hackathon [[Hack the North 2021]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[geospatial]]

**stack** amazon-web-services, apollo, apollo-federation, figma, flask, google-maps, graphql, node.js, numpy, pandas, postgresql, prisma-orm, pulumi, pyspark

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for omw

## Body

Introducing 'omw' - A mobile application to help you commute safer. User Journey - Traveller User Journey - Companion Screens - Onboarding Screens - Adding Emergency Contacts Screens - Other Tech Stack Inspiration The recent events involving gender-based violence at Western University shed light on the issue of campus safety and the feeling of fear that many women face when travelling alone at night. 63% of university students in Ontario have experienced some type of sexual harassment on campus and 50% of women say they always or often feel unsafe walking alone at night. Although an issue of this gravity demands a cultural shift in mindset, we were inspired to explore ways in which technology can empower individuals to feel safer. What it does omw is a real-time navigation tool that enables users to safely commute to their destination with greater peace of mind. The app consists of 3 key features: 1. Route Optimization: The app identifies the safest route from point A to point B by avoiding areas in which a substantial amount of gender-based violence cases have occurred. The route is displayed in an easy to understand, visual format and users simply follow the step-by-step directions. 2. Heat Map Visualization: The app creates a heat map based on which areas are most dangerous. Users are able to browse this map to learn more about their surrounding environment and make informed decisions about their travel. 3. Peer Notification System: Users are able to input emergency contacts with whom their respective journeys will be shared. This contact will be able to view the user’s whereabouts, journey progress, and will be notified upon safe arrival. How we built it Frontend: React Native, Expo, Typescript Backend: GraphQL, Apollo Federation, PostgreSQL, Prisma ORM, Node.js, TypeScript Infrastructure: Pulumi IaC, Amazon Cognito (custom passwordless flow), Amazon RDS, AWS Fargate, Docker, Amazon SNS Machine Learning: Flask, PySpark MLlib, Pandas, NumPy, Google Maps API Design: Figma Challenges we ran into · Generating an impactful and technically feasible idea · Understanding the nuances of gender-based violence and the reasons that cause feelings of fear · Navigating the development of an application that could potentially prevent future incidents of sexual assaults, while knowing that the onus should not be on the victim. Accomplishments that we're proud of · Tackling an issue that hits close to home and developing anMVP that successfully implements the app’s core functionality · Designs and branding for the end-to-end product experience; We were able to conduct some primary user research as well as a few usability tests which helped inform our final solution What we learned · For some of us, it was our first hackathon and first time working with React Native. As well, learning to design for the various edge cases and in-between states of the user flow. · Monster drinks fuel technological breakthroughs though may induce headaches What's next for omw 1. Incident Reporting: The ability to report noteworthy observations when travelling (e.g. regions that are poorly-lit, areas where there are disruptive behaviour, etc.). The heat map and recommended paths will adjust accordingly to these first-hand, community-generated insights. 2. Integration with Police Services: The ability to call authorities within the app itself during a potentially dangerous encounter. 3. Walking Buddies: Pairing users with other friends nearby to travel together, if both parties are headed to the same destination/ in the same direction. 4. Anonymous Forums: The ability to post about your experiences, as it relates to gender-based violence, in a confidential manner. 5. Route Sharing Optionality: Beyond importing specific emergency contacts (with whom location sharing will be enabled), adding entire socials circles and creating emergency groups based on outings, living arrangements, etc. 6. Resources & Accessibility: We would like to incorporate a page in which users can contact hotlines, links, and other resources for support in the case of sexual harassment and assault. We would also love to make our app more inclusive with a settings page that allows user to customize various accessibility features to their needs. <div