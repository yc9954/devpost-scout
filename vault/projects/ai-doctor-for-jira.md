---
slug: "ai-doctor-for-jira"
url: "https://devpost.com/software/ai-doctor-for-jira"
title: "AI Doctor for Jira"
hackathon: "Codegeist 2022"
organization: "Atlassian"
winner: true
words: 1269
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/clinician"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# AI Doctor for Jira

> Health check for your Jira Cloud instance has never been easier. With just few clicks, you can see how healthy is your configuration. The system is checked using machine learning, data mining and AI.

[Devpost](https://devpost.com/software/ai-doctor-for-jira) · hackathon [[Codegeist 2022]]

## Facets

**domain** [[developer_tools]]
**user** [[clinician]] [[developer]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** forge, numpy, pandas, python, rest, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ai doctor for jira

## Body

Inspiration I have been doing Atlassian Assessment already for 10+ years. I spent days, if not months, reviewing configurations, removing obsolete objects, and querying my clients databases. I know exactly that nobody has time and will to do clean up on the regular basis unless Jira doesn't work properly. Currently, with “Cloud first” approach and hundreds of migration from server or datacenter to Cloud, clean up has become of the most important part of any transition. Why not to automate it or make it simpler? With the new technologies and trends of automating as much as possible, I came up with the idea to simplify this process. With the latest services and libraries, it is possible to use machine learning and AI to give recommendations to Atlassian users just in a few clicks on how to improve the performance of the instance and keep their Jira configuration clean. To make this dream come true, I have contacted the University of Science and Technology in Wroclaw to see if they can help me with research in this landscape. I am pleased that now with the Faculty of Information and Communication Technology we are working on this solution. What it does AI doctor for JIRA analyzes all Jira objects such as custom fields, issue types, workflow schemes, etc. and provides a report of usability. The report is presented in a lightweight form using a percentage scale. Each group of objects have its own sub-report with JAD (Jira AI Doctor) recommendations and score. Users can easily identify what can be improved. It's a great way to review your configuration, for example after a migration to the cloud. How we built it The application has been created in the forge environment and the AI part was programmed in Python language. We create all reports in connected confluence instance as separate pages. We analyze usage of all Jira objects based on the information fetched from Jira Rest Api and provide a health check report stating if the considered object is in use or redundant and can be safely removed. We also calculate the number count of usage of objects. For deeper analysis with usage of AI, we have created our own service in Python. Primarily, our service was analyzing data using only NLP cloud service. It is a service that is dedicated to Natural Language Processes. Using NLPCloud we can estimate object similarities described in the percent probability stating how much two objects have the same meaning. In our current development we are developing our own similarity detection code and have provided our own way to detect language. The pairs of objects are compared using Python libraries and models available openly in the Internet. Further development will include developing models optimized for Jira software-specific environment. Communication between the forge application and our AI code is done using REST API calls. Once two objects are compared, we are able to find objects that have the same meaning but are described in different languages, for example, 'work in progress' and 'in work'. Why to have both of them rather than just use built-in translation, modify workflow, and delete unnecessary object? We can find objects that are duplicates in the same language, for example, a custom field named 'Impact and notes' and 'Wirkung und Anmerkungen' in German. Finally we can fix typos, for example in “progress”, “in progres” and “in prrogres”. In my professional work as a Jira consultant, I find instances that have plenty of duplicated custom fields names. Challenges we ran into At this stage of development, getting to know the forge environment and overcoming technical difficulties is challenging. The main problem we have encountered and not yet fully solved is the long execution time that is required to generate the report. The preliminary approach to use NLP cloud service directly has failed as this service appeared to have 1 sec limited rate, so for a big Jira instance it takes up to a few days to find object similarities and detect languages. To overcome this, we have developed our own API that works as middleware between NLP cloud and Forge and is able to cache requests. The next step became natural, as we had our own AI API working (caching only), we have created our own code to analyze similarities and detect languages and dropped usage of the NLP cloud service. To our surprise, local models appeared to work faster than commercial solutions. We are still discovering the field of artificial intelligence and how to use it to fulfill our goals. We are learning how to overcome limitations induced by the Forge Environment – to do it Forge way, which are still purely technical problems. We believe that winning this grant will allow us to deal with the UI problems that are technical in nature and then move on and focus on the essential part of this application, which is Jira instance analysis. Lack of real data to be analyzed is another problem to overcome. It is well known that every machine learning code needs a lot of samples to learn from. We will develop business model that will encourage people to provide anonymously data from their own instances, that we can use to train AI model. Finally, when we overcome challenges, this application will combine expert knowledge and machine learning techniques. Accomplishments that we're proud of The full health check report has been generated with the final score. All sub-reports are in a few clicks available to be reviewed. We are especially proud of generation of custom field report and statuses. Both of them are fully utilizing machine learning to detect languages, translate texts to English, and cross-check similarities of all the objects in those sections. What we learned We are a group of consultants and developers diverging from completely different field of specialization, that became enthusiastic about The Atlassian Ecosystem. Therefore, every step we do in the field of the Forge environment is something completely new to us. The amount of knowledge we have had to digest in recent months is amazing. Forge, Python libraries for AI, AI services available on the market. However, the most important is collaboration with other enthusiasts of the newest technologies. I now understand that working in a garage can be fun and that all great things have been started there. Teamwork and collaboration are key factors for success. Focus on deliveries, find workarounds, ask the team for help if you have encountered blockers. Our motto is: "United we stand, divided we fall". What's next for AI Doctor for Jira It is just a beginning, first version which is still not released to the market. The ultimate goal for our app is to completely replace expensive consultants for doing instance assessments with AI Doctor for Jira. Support all migration from Server or Datacenter to Cloud, or Cloud to Cloud. It is a long way to go, but it is a marathon not a sprint. Next steps in a short brief: Release the first app to the market. Processing more customer data for testing and improving our application. Training of AI to be an expert in Jira matter. Using existing libraries and improving them by feeding more data. Provide an automated way to do some cleanup actions for the users, not only a recommendation. Create a version of our application that can be independent from Confluence. The report will be either directly available in Jira or being downloaded as a PDF file (for customers who do not have Confluence) Creating AI doctor which can support cleanup after moving to cloud from server or datacenter versions of Jira. <div