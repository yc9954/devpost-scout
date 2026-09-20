---
slug: "humans-ai"
url: "https://devpost.com/software/humans-ai"
title: "Humans.AI"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 1290
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "domain/transportation"
  - "user/developer"
  - "user/frontline_worker"
  - "user/researcher"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Humans.AI

> Providing income using mobile based Data Labelling game in India

[Devpost](https://devpost.com/software/humans-ai) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[climate_energy]] [[developer_tools]] [[education]] [[finance_payments]] [[labor_employment]] [[transportation]]
**user** [[developer]] [[frontline_worker]] [[researcher]]
**substrate** [[financial_record]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** android-studio, firebase, gcp-suite, mongodb

## How they structured the write-up

- inspiration
- who we are
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for humans.ai

## Body

Screenshot of the app. Client wanted us to label gender in 20,000 images How we stack up with competition Our team. Anand and Ishaan Our labeler using our app, and the impact it has had Inspiration One of the largest fall-outs from COVID-19 is the loss of jobs, especially for those who are the worst hit. Ishaan and I first hand saw the numbers of jobs being cut in the US and India and the rest of the world. The economical impact and lack of support to the lowest economic members of society are stark and to that end, we wanted to build a platform that will provide these labourers with a substantial means of revenue to sustain their families through hard times. Inspired by Uber and Lyft, the gig economy was the perfect elastic band for job losses. Speaking with various Uber drivers in the Bay Area, they started on Uber when they were laid off or were in between jobs. Unfortunately, due to COVID-19 there has seen a stark a drop in Uber rides as well and relying on ride-hailing apps as a means of income seems impossible in this climate. Ishaan and I were inspired by the gig economy to build a platform where anyone with a smart-phone can complete micro-tasks in the form of a game and gain income through the process. Amazon Mechanical Turk, unfortunately, is out of reach for a large number of Indians who either do not have a laptop or do not know how to navigate the tedious registration and job procedure on M-Turk. Both Ishaan and I have spent countless hours either as workers on M-Turk or job posters and can relate to the pain faced by both parties. Looking at the shortcomings on M-Turk and the strong demand for low-cost data labelling, we set about building a platform that does just that - mobile-first and facing towards the Indian labelling ecosystem. Who we are Anand Lalwani: Anand is a PhD candidate at Stanford University in Electrical Engineering with past experience in Product Management for Target, building low-cost satellites for NASA and his research focuses on developing sensors for the environment. He has two patents pending inventions and a strong background in Human-Computer Interaction research focusing on developing countries. Having grown up in India, he has close contact with the ecosystem and understands the needs of the labourers. Ishaan Agarwal: Ishaan is a Product Manager at Microsoft with strong experience in development, AI and published research in HCI. Ishaan did his undergraduate and masters degrees from Brown University. Prior to Microsoft, Ishaan interned at Facebook and first hand dealt with the problem of spam and flagged posts. Ishaan has strong design skills having spent 2+ years at Rhode Island School of Design and growing up in India, understands the local context. Ishaan and Anand have been working together for the past 3 years on various projects: from ballroom dancing to learning Mandarin to building apps. What it does Our app allows anyone, regardless of their literacy abilities, to 'play' and are compensated with real money for their services. The app shows the data needed to be labelled in the form of images for classification, annotation and bounding-boxes in an intuitive mobile-based UI/UX and the labelled is paid for every correct label. We maintain accuracy of over 98% (based on STL-10 dataset) by leveraging statistical averaging. By showing the same image to multiple labellers simultaneously, we can correlate the labels placed by different labourers and using their modal answer above a set threshold, we obtain the final label. Using the low-cost gig-economy labourers, we can keep our costs to less than 50% current market rates (as compared to Hive, Figure8 and Scale-AI) while simultaneously providing a secure income higher per hour than our labellers would make working for Uber or as a rickshaw driver. We securely and cost-effectively label data for startups, fortune 50 companies and AI researchers and provide a meaningful income to the worst-hit classes of India without requiring them to leave their homes or purchase a laptop. How we built it The app was built using Android's React Native and the backend is hosted on Google Cloud Consoles, Firebase and MongoDB. Ishaan, a developer and engineer, lead the engineering efforts. Anand's role was customer development and user-centred design. We designed the app specifically for low literacy wage earners in India's population as the labellers and the accuracy algorithms were built in conjunction with labs at Stanford and based on the needs of the AI companies who wanted to label their data. Challenges we ran into Customer development: Surprisingly, it was not hard to get our first set of paying customers from the Bay Area. Reaching out to various startups and research communities, it was clear that there existed a need that filled the gap between Amazon MTurk and traditional data-labelling companies. App development: As a two-man team, it has been challenging at times when our app has failed and debugging has taken longer than expected. We have had issues, though minor, with FireBase authentication and currently struggling to build out the payment integration platform for our labellers. Labellers training: We have been able to get 11 labellers so far to have actively 'played' on the app. However, the initial accuracy of the labellers remained an issue. Through conversations and design changes, we were able to improve the accuracy. Accomplishments that we're proud of Providing income to labellers: So far, we have been able to provide income to 11 labellers. Our labellers are small shop salesman, cooks and watchman (private security guard). Chandu, one of the security guards, earned over Rs. 5000 (68$) in 12 days - more than he would have been able to on his daily salary. All from the comforts of his own home. Stories such as his keep us going. Improve accuracy in labelling: By being able to cross-reference and use crowd-think to label, we have tested our accuracy on the STL-10 industry dataset and obtained accuracy of over 99% with over 1000 labelled images. It proves the model works and is accurate. What we learned Building is easy. Building for humans is hard. Engineering away on our own, without understanding the needs of the client or the labeller would have been easy. However, from day one, we spent more time understanding the needs and the jobs to be done on both ends of the market. We had to create an experience for the labellers that was smooth and more game-like, and at the same time provide timely and accurate results at low costs to our clients. Customer development can be slow. B2B is not known for its speed and it took is longer than expected to go from initial 'yes' from the CTO of the startup to being given our first dataset to build on. Balancing two sides of the market. Like Uber, we too need to balance both sides of the market: demand and supply. Keeping a steady stream of clients with data to be labelled and expanding on our labellers in sync is critical and we are still figuring that part out. What's next for Humans.AI We are actively looking for partners and companies who would use our platform to get their images/data labelled! We can help fight COVID-19 by providing a reliable source of income to India's worst-hit labourers while also aiding in the development of ML/AI algorithms. In the near future, we are piloting with a medical AI company to label CT scans, an online education learning company to correct homework and grocery delivery company to label receipts. As we grow with clients, we are onboarding new labourers and providing them with the training and help to survive these times. <div