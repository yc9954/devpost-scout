---
slug: "team-insights-ai"
url: "https://devpost.com/software/team-insights-ai"
title: "Scrum Masterika"
hackathon: "Codegeist Unleashed"
organization: "Atlassian"
winner: true
words: 1183
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/structured_db"
---

# Scrum Masterika

> AI-Driven Agile Scrum Master

[Devpost](https://devpost.com/software/team-insights-ai) · hackathon [[Codegeist Unleashed]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[structured_db]]

**stack** gcp, google-bigquery, mongodb, node.js, sql, vertex

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for scrum masterika

## Body

Inspiration Most software projects fail or do not launch on time because the team started trashing very later-on in the project phase instead of doing it earlier on, this has has affected our own software development process at our start-up , we are inspired by the new AI tools now available to help monitor the progress of each task and story in real-time, providing automated updates to the team and stakeholders. We thought, "If only we have a solution to identify bottlenecks and suggest actions to overcome them, it would be really nice", so we build scrumasterika What it does Automated Sprint Planning: The app uses natural language processing to analyze user stories and automatically suggests sprint planning, including story points and assignment of tasks to team members. Sprint Progress Monitoring: The virtual Scrum Master monitors the progress of each task and story in real-time, providing automated updates to the team and stakeholders. It can identify bottlenecks and suggest actions to overcome them. Predictive Analytics: The AI engine uses historical data to predict sprint completion dates and helps in identifying potential delays in advance. It can also provide insights into which user stories are most likely to be completed in the sprint. Automated Retrospectives: After the sprint, the app conducts automated retrospectives based on team member input and historical data. It identifies areas of improvement and suggests action items for the next sprint. Smart Notifications: The virtual Scrum Master sends notifications and reminders to team members for stand-up meetings, sprint planning, and other Agile ceremonies. How AI is Used: The AI model, powered by a custom-trained machine learning algorithm, understands user story descriptions, analyzes historical project data, and uses predictive analytics to assist with sprint planning and monitoring. It also uses natural language processing to communicate with team members effectively. Responsible AI We have ensured that harmful and abusive content is not served up to our users and customers, the data governance is also very critical from our perspective in that, customer's data is customer's data and our AI/ML pipeline we have buit can only be trained on ether that customer's data, open source data or public data. We also ensured responsible AI practices by implementing data privacy and security measures in line with GCP's security and privacy guidelines and implemented transparency in AI decision-making, like in our video demo, we showed how the models used are trained and what data they are trained on i.e own data, open source data or public data. Atlassian Forge Integration: The app integrates seamlessly with Atlassian's Jira using the Forge platform to access and update user data, sprint details, and project information. Potential Impact: The AI-Driven Agile Scrum Master aims to significantly improve the developer experience by reducing manual effort, improving sprint planning, and enhancing collaboration. It helps teams deliver high-quality software more efficiently and consistently. How we built it Project Setup: We created a new GCP project and set up billing. The App was built using The Forge CLI that made it very easy to hit the ground running, we set up our Linux development environment which required setting up docker , nvm and the latest verssion of Node.Js, we then set up the env variables required by Forge and used react to help us accelerate the work . Data Ingestion: Data from Atlassian's Jira was ingested into GCP using the Jira REST API , since we leverage Generative AI with MongoDB Atlas and BigQuery, we were moving subsets of operational MongoDB Atlas data into BigQuery, creating machine learning models in BigQuery ML and using Generative AI models to perform natural language tasks. Data Storage: We stored the ingested data in Google Cloud Platform on a Mongo DB Atlas cluster then we set up a CDC Job that subscribes to change stream in MongoDB that track changes in our database in one collection, basically events that happen in our database We subscribe to these events in DataFlow CDC job, so that when we reaceive a change we can ETL it , transform in a meaninful way, like flatten fileds, remove some arrays, remove fileds we don't care about and store the data in a BiqQuerry table. Machine Learning Model Development: Develop a custom machine learning model using BigQuery ML, We then trained the model on historical data to understand relationships between user stories, team dynamics, and sprint outcomes followed by deploying our model in Vertex AI for a REST endpoint. Natural Language Processing (NLP): Implemented NLP components for understanding and analyzing user stories. Vertex AI model garden came in handy, using PaLM2 for text a foundation model .The table with the predicted results from the Data to ML step is the input for this, BigQuery GENERATE_TEXT construct was used to invoke the PaLM API remotely from Vertex AI .External Connection then created to establish the access between BigQuery ML and Vertex services. Predictive Analytics: We developed a predictive analytics module that takes into account historical data and sprint progress to predict sprint outcomes and detect potential delays. Integration with Jira: Utilized GCP's secure authentication methods to integrate with Jira. This involved creating a custom connector and utilizing Jira's REST API. Real-time Monitoring: We implemented real-time monitoring by periodically querying Jira for sprint status updates. We used Cloud Pub/Sub to trigger updates to the AI model and issue notifications to team members. Smart Notifications: We created a notification system that sends alerts and reminders to team members. We used Google Cloud Functions to send notifications via email and chat Security and Privacy: Ensured that the application adheres to security best practices. Used Google Cloud Identity and Access Management (IAM) to control access to resources and data. Responsible AI Practices: We implemented data anonymization and followed ethical AI practices to ensure responsible AI implementation. Documented these practices for the Codegeist Unleashed hackathon in a story telling blog on medium. Documentation and Storytelling: Created comprehensive documentation explaining how your application uses AI and GCP. This was important for the storytelling prize. Challenges we ran into Time was a factor , My team-mate Christine and I are both professionals and working full-time and in different location .I live in the city while she is currently in the country side, so finding time to Google meet for daily stand-was really hard. Accomplishments that we're proud of We formed a tight bond while working and managed to build an awesome app and write a compelling story to the community on how we built it. What we learned We learnt to call a Jira API and how to make API calls to the Jira REST API, this was intutive especially using tunnels on the CLI tool. What's next for Scrum Masterika Deployment and Scalability: Deploy our application on Google Kubernetes Engine (GKE) for scalability. This will allow our application to handle a growing number of users and projects. Monitoring and Logging: Set up monitoring and logging using Google Cloud Monitoring and Logging. This will help us track the performance of your application and troubleshoot issues. Testing and Validation: Thoroughly test our application with real-world data and scenarios to validate its performance. <div