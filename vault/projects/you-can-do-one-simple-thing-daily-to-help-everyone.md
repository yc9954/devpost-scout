---
slug: "you-can-do-one-simple-thing-daily-to-help-everyone"
url: "https://devpost.com/software/you-can-do-one-simple-thing-daily-to-help-everyone"
title: "You Can Do One Simple Thing Daily to Help... Everyone"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 1093
team_size: 15
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/code_repository"
---

# You Can Do One Simple Thing Daily to Help... Everyone

> Everyone should track their health and symptoms daily (even when asymptomatic to help your community manage risk, inform policy, and win the war on COVID-19

[Devpost](https://devpost.com/software/you-can-do-one-simple-thing-daily-to-help-everyone) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**domain** [[health_clinical]]
**user** [[patient_family]]
**substrate** [[code_repository]]

**stack** azure, azure-data-explorer, fhir, hippa, react-native, sql

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of:
- what we learned
- what's next for you can do one simple thing daily to help... everyone

## Body

Calendar of personal symptoms Personal profile Health officials can see upticks before resources are needed Health officials can see upticks at scale before resources are needed Inspiration What if we knew more about the onset of symptoms? What if we knew whether that tickle in your throat meant something before it became a problem? Minor cases are not directed to the hospital, so we're missing tons of data and assuming spread based on models rather than data. So, we're all at risk. What if we were able to track everyone (or at least a statistically significant part of the population), including healthy people before they came down with COVID-19? What if we could help people identify their own risk before we have testing kits available everywhere? We believe there's potential to help the WHO and national health organizations (CDC, NHS, etc.) to understand more about the virus and its spread. We also see potential to help communities identify risk, by asking people to do one simple thing: take a short survey every day. What it does Everyone who opts in commits to taking the survey on an ongoing basis (e.g. 1x per day) People describe what they experience today in the survey, "describe your experience with these symptoms on a scale." The app will prompt the user every day to take the survey on their mobile device. The user can then opt into sharing their mobile location for a limited time, to generate even richer data for professional analysis, as well as their own information. We also want to be able to join this data with those who are tested for COVID-19, and their test results. This can also be joined after this is all over with data over time from those who had shown antibodies for COVID-19, even though they never became symptomatic or had the benefit of testing during the pandemic. On the back end, here's what the user gets: Understanding of the infection rate for their community The feeling that they're doing something to help A diary of their own symptoms over time (Optional) Places you've been that can be used to trace others to whom you've been exposed - alerting you to potential risk Public health organizations would get: A better statistical analysis of EARLY ONSET of symptoms, since most people are asymptomatic (or MOSTLY asymptomatic) for at least the first several days A clearer understanding of hotspots and spread, and possibly contain new hotspots to determine public policy recommendations A clearer understanding of minor cases that are not tested by understanding the change in rate of symptoms across a community without the need to test absolutely everyone by: Having a clear symptom "baseline" across a community Seeing when a community is statistically outside the normal variance Seeing when a community is now back below the threshold for concern beyond just measuring ER visits A way to show the math that the risk has receded Important details: The way you rate a symptom and I rate a symptom will always be different. Like they do in the ER, the important thing to note here is the AMOUNT OF CHANGE in symptoms to build and effective understanding of patient's relative experience. The assumption here is that we can survey both healthy and unhealthy - avoid biasing the data - assume everyone may become symptomatic at some point We need the ability to scale up to ingesting up to 20 - 100 million records daily in order to have a statistically significant sample set across the country (this can easily be extended to other countries) We will need some way of ensuring consistent identity from session to session At a minimum the user should share their location at the time of taking the survey We could use addresses to help collate the data, but it may be more important to get the samples are where people ARE (working, etc.) rather than where their home is or how many people live in the house. Risk comes from interaction. Unfortunately in this case, children pose a risk as carriers, but are excluded by the lack of availability of phones (which ethically, makes sense) How We built it React-native front end. Azure FIHR Compliant backend (in progress) Starting with Azure Data Explorer for data analytics PowerBi visualization Leveraged FIHR Libraries and protocols for governance and integration. Details on using the FHIR API for compliance YouTube 3min version of submission Challenges We ran into HIPAA Privacy Consent decrees Data Sovereignty (who owns the stuff) Geographic sovereignty In the US, the application cannot be used for self diagnosis, nor to recommend testing, based on limited resources for testing by region. We therefore had to create an application that will be able to be implemented in different countries/regions and meet their specific regulatory compliance requirements and rules. As this is a POC for the World Health Organization we brought all the elements together to align a simple, compliant and expandable application. Accomplishments that we're proud of: Variant on the use of Likert / Wong-Baker FACES scale for symptom tracking Notification for re-submission of the survey to track over time Learned to work with new Open Source technologies Fostering new connections and relationships among multidisciplinary team, distributed across 3 continents What We Learned The most valuable take-away for us has been a sense of empowerment and self-efficacy in the face of these complex and confusing current events. Working on this hackathon together, we felt a positive emotional lift from being able to do something to something to help...and we hope that users of our app will feel the same way, by doing one simple thing daily to help, too! We also grew and learned through: -The importance of collaboration, communication, mentoring, and keeping an open perspective Application of our professional skills outside of our day-to-day job duties, including new tools and technical environments Deeper knowledge of Coronavirus symptoms and conditions over the course of onset and progression Enhanced awareness of the needs of medical, clinical, and epidemiological professionals Empathy for everyone struggling to deal with the complexities of COVID-19, from patients, to care providers, to every person. What's next for You Can Do One Simple Thing Daily to Help... Everyone We need to find a health institution to back this project so that they can start collecting and analyzing data. We still need to improve the user sign in, identification, user charts, and app flow. We also want to decouple the front and backend so that the survey can be updated without needing to redeploy the application. <div