---
slug: "cumulus-lc45gy"
url: "https://devpost.com/software/cumulus-lc45gy"
title: "Cumulus"
hackathon: "Hack the Northeast: Beyond"
winner: true
words: 1033
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Cumulus

> We're a data-as-a-service platform using big data to help job seekers figure out the skills they need to be successful in the job market.

[Devpost](https://devpost.com/software/cumulus-lc45gy) · hackathon [[Hack the Northeast- Beyond]]

## Facets

**domain** [[finance_payments]] [[labor_employment]]
**user** [[developer]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[web_dom]]

**stack** css3, d3.js, express.js, fetch, heroku, html5, javascript, node-fetch, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cumulus

## Body

The landing page mocked up in Figma The search page mocked up in Figma The icon for Cumulus, licensed under Creative Commons Inspiration As development and programming have become more accessible, the requirements and knowledge necessary to land a job in tech has grown exponentially. Today, programmers need to know a plethora of languages, each with a variety of frameworks, each often having their own unique ecosystem and tooling. This is the problem that Cumulus aims to solve. We're a data-as-a-service platform intent on helping job-seekers figure out what they've got in the bag—and what they still need to know—by providing a snapshot of what the job market looks like right now . While we’re inspired by the demands of the tech industry, we envision our platform as being useful to any field or any job title. What it does Given a job title, the website searches in scraped job postings and displays several metrics about the job to help job hunters gain insights. These metrics include the most popular skill it demands, the most active company associated with the job title, the top majors, and job types. At the moment, data visualization is limited to featured jobs on the search page. How we built it Backend The backend for Cumulus is built using node.js and express.js . Our API is read-only, meaning the frontend can GET endpoints but not POST anything. At the moment, we’re using JavaScript object and array manipulation to transform our dataset into useful insights. In the future, we hope to migrate to a noSQL service to help optimize some of this work. Frontend The frontend was built using plain HTML, CSS, and JavaScript. Because of the limited scope of the proof of concept, we decided to forego any frameworks in favor of the speed and customization that going vanilla offered us. As a result, we’re able to deliver a smooth, fluid user experience, with custom onload and onunload hooks to make transitions feel in line with our design ethos. As our service scales up, we may consider migrating to react.js or a similar framework to make code more maintainable. Challenges we ran into We envisioned using an API to provide job postings, but most API’s do not have affordable pricing for a large amount of API calls. So we scraped job postings instead using Node.js fetch. We initially planned to use Amazon Comprehend to recognize keywords in any job postings, so that the application could get meaningful data from any job posting, such as the most in-demand skills for any job title. However, it turned out to be complicated to integrate Comprehend with our app, so we decided to only provide insights about tech jobs for now and use a pre-approved list of keywords to display top skills. Accomplishments that we're proud of We are proud of our concept Cumulus, which ties together the UI and the functionality of the application. Cumulus is the latin word for accumulation, and our app is an accumulation of data points to help users find their dream jobs. It is also a classification of clouds, inspiring for the theme of clouds in our airy and innovative UI design. As the job market can be stressful, the design of Cumulus is perfect for inspiring our users with the feeling of limitless possibilities. We are proud of our mission of helping our users to navigate the stressful job market and providing them with valuable insights. While there is a wealth of information on the Internet of how to learn any employable skills, there is no service like ours that tells users exactly what they in-demand skills they already have and what they need to catch up on. What we learned We learned to not rely on API's and do our own web scraping. We learned to effectively use RegEx to find keyword matches. What's next for Cumulus As our service scales up, we have many ideas (both technical and otherwise) to improve Cumulus . These are described below. Technical As described in our technical outline, our backend needs to be migrated to proper database hosting. We envision MongoDB or some other noSQL database as being the correct choice for this application; the high scalability and JSON syntax of using these services lend themselves to the data analysis we intend to perform. In addition, integrating this backend with proper APIs would help boost both the quality and quantity of visualizations available. As of right now, our dataset is limited to tech internships in New York. With a broader scope, job seekers could gain deeper insights into the current job market. For the frontend, we’re considering migrating to React. This won’t be difficult, but if our UI increases in complexity, it will be very much worth it. We’ll be able to quickly scale both the types of visualizations and the views that we present to the user. Non-technical Aside from the technical pursuits listed above, we also have several ideas for expanding what Cumulus can do. First, we plan to have a user authentication system. While we’re not sure how we plan to implement this, adding it will allow users to save searches and keep tabs on specific skills, companies, and other metrics. In addition, this should allow users to upload their resume, a key feature that we plan on monetizing. This resume upload feature would allow job seekers to be notified when their skills don’t quite match up with what the market needs. This feature could be locked behind tiers: a free tier, where some percentage of the resume is monitored every so often, and a premium tier, with more comprehensive monitoring and notifications. In addition, we could also expose these resumes to employers, another market that we’re interested in. While marketing to job seekers is at the core of our mission, the employer market can also benefit from the data we collect. While we’re not sure yet how we plan to integrate this side of the service, we know that we want to market to employers who want to get insights on their hiring and their talent. This could be a very lucrative aspect of the service, and is definitely worth exploring further. <div