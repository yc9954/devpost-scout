---
slug: "tracectrl-your-data-your-rights"
url: "https://devpost.com/software/tracectrl-your-data-your-rights"
title: "TraceCtrl - Your Data, Your Rights"
hackathon: "Google Cloud Gemini Hackathon"
organization: "Google"
winner: true
words: 750
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# TraceCtrl - Your Data, Your Rights

> Uncover companies that hold your personal data and access, edit, or erase it with ease.

[Devpost](https://devpost.com/software/tracectrl-your-data-your-rights) · hackathon [[Google Cloud Gemini Hackathon]]

## Facets

**substrate** [[structured_db]] [[web_dom]]

**stack** gcp, gemini, gmail, langchain, python, streamlit, vertex

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tracectrl - your data, your rights

## Body

TraceCtrl architecture Without TraceCtrl - VertexAI Without TraceCtrl - AI Studio Inspiration Today, our personal data is collected by countless companies—often without us knowing exactly where or how it’s being used. For the average person, a staggering 83% of their digital footprint is held by companies they've interacted with just once. On top of that, the average user's data is held by around 350 companies. This creates significant privacy risks. Under GDPR, we have the right to access, erase, and modify our personal data. However, identifying companies that hold our data is very time-consuming and daunting, let alone reaching out to each company individually. With this problem in mind, I decided to build TraceCtrl. What it does TraceCtrl is a web app that scans the user's Gmail inbox and identifies companies that hold personal data with which the user did not interact. Users can then review these companies in a convenient table and choose which ones to send GDPR requests to. Our Gemini-powered bot will search through the privacy policies, find an email for GDPR requests, and send an appropriate request on your behalf, saving you hours of manual web searching and email writing! How we built it The app uses Google Authentication and the Gmail API to access the user's mailbox. The email content is then analyzed by the Gemini model to extract the company, email type, and company website. Next, this information is displayed to the user on the front end, accompanied by the company logos sourced from logo.dev. Once a user selects the companies and request types, the tool uses FireCrawl to return the company's page with the data privacy policy. The content of the policy is analyzed by the Gemini model to search for and return an email address for GDPR requests. This is possible thanks to the large context window and cost efficiency of the Gemini model. After extracting an email address, the tool sends a GDPR request selected by the user, whether to access, erase, or modify their personal data. The request is sent as an email on the user's behalf, fully automatically. The front end of the tool is built with the Streamlit library. Challenges we ran into One of the initial challenges I faced was the Vertex AI quota limit. Since the app scans the user's inbox, it needs to call a Vertex AI Gemini endpoint multiple times per minute. The quota initially assigned to my GCP account was 5 requests per minute (RPM), which was too low for the app to function efficiently. I raised this issue with both the Devpost team and GCP teams. Another challenge I had was enabling Google Authentication for the app deployed on Cloud Run. Due to limitations with Streamlit, this process proved to be more complex than anticipated. Accomplishments that we're proud of I'm proud to have built a user-friendly tool that gives people real control over their digital footprint with minimal effort. Integrating Google Authentication, Gmail API, and Gemini LLM in VertexAI environment allowed to create a solution that automates often tedious process of identifying companies holding user data and sending GDPR requests. One of the proudest achievements is the use of FireCrawl and Gemini to find GDPR contact based on just company website - saving users hours of manual work. What we learned I learned how to work with the Vertex AI Python library and Gemini models. I also explored testing prompts in Vertex AI Studio, which made it easy to fine-tune responses and improve model accuracy with structured output. Additionally, I deepened my understanding of GDPR and data privacy rights, as well as the practical challenges users face when trying to exercise those rights. What's next for TraceCtrl - Your Data, Your Rights Even though the app is currently in a working POC stage, I have ideas for the next set of features: • Expand Email Provider Support: Add compatibility with more email providers beyond Gmail to reach a wider audience and make the tool accessible to more users. • User Accounts and Personalized Analytics: Introduce user accounts with a personalized dashboard, offering tailored analytics to help users track and manage their digital footprint over time. • Broader Data Sources: Enable the app to identify companies holding users' personal data beyond just inbox data—such as web scraping for data brokers and integrating mailing list databases. • Enhanced Security Measures: Add an additional security layer to hash or encode user emails, enhancing privacy and building user trust in the app’s data handling. <div