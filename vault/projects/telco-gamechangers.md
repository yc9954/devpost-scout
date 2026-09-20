---
slug: "telco-gamechangers"
url: "https://devpost.com/software/telco-gamechangers"
title: "Telco Gamechangers"
hackathon: "Agentforce Virtual Hackathon"
organization: "Salesforce"
winner: true
words: 947
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Telco Gamechangers

> Here is a go to market Agentic AI accelerator tailored for Telecom business to reap the benefits of enhanced efficiency, CX, intelligence driven insights and operations- all powered with Digital labor

[Devpost](https://devpost.com/software/telco-gamechangers) · hackathon [[Agentforce Virtual Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[finance_payments]] [[labor_employment]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** agentforce, amazon, datacloud, emailnotifications, experiencesite, llm, lwc, promptbuilder, s3, servicecloud, slack

## How they structured the write-up

- inspiration
- what it does
- how it works
- issues faced
- accomplishments that we're proud of
- what we learnt
- what's next for telco gamechangers

## Body

Logged in screen with Agentforce detailing the usage pattern Inspiration We all use telecom services day in day out- be it mobile, internet, broadband, TV or OTT services. We understand how frustrating it could be if the telco services don't work as expected. E.g. mobile data stops working suddenly, call drops, internet connectivity too slow, issues with billing, sim activation and what not. For telcos to be able to adapt to the evolving customer needs, be able to ensure reduction of churn, get customer loyalty- here is the GTM accelerator that we have created for the Telecom business with the power of Salesforce Agentforce to help their customers intelligently and efficiently. What it does We have come up with multiple ready to launch Telecom Agentic flows on the basis of our extensive experience in the domain that would ensure an immediate value gain for the business. When a customer logs in to the company portal, the first thing that happens is the suggested plans- these plans are suggested in real time on the basis of Customer's usage pattern for last 90 days Customer's location Customer's loyalty Customer can also enquire around their sim activation issue, billing, raise dispute, get the best suited plans and enquire about the data services not working, issues with connectivity, etc. via Agentforce Service Agent. There are queues created on the basis of skills to be able to assign the cases correctly to the agents. Additionally, we have embedded a customer sentiment calculator based on customer's tonality, issues and loyalty and such kind of cases would directly go to our special slack channel created for immediate attention to the loyal customers. Human Agents on the slack channel will be sent the relevant information about the case, and they would use Agentforce on slack to take actions like sending some proactive emails, special offers to take care of any negative sentiment and prevent churn. Also, they could assign the case to another agent accordingly for quicker/ relevant actions. We also have created a proactive monitor for customers with call drop issues (more than 3 call drops in a month) and Agentforce would send notifications and special offers to such customers to tell them that we care and are looking into such issues proactively. How it works This project is a complete amalgamation of the capabilities of Agentforce, Data Cloud, Prompt Builder, Slack, LWC, Apex, Flows, etc. Amazon S3 bucket ingestion has been used in Data cloud to mimic call data from external systems for various customers , capabilities of customer identification, unification and segmentation are being done in Data cloud. We have also used RAG capabilities to showcase the newly launched offers in the region of residence of the customer. We have used prompt builder to generate the best recommended plans for customer based on the usage patterns and loyalty. Additionally have also included capabilities of Agentforce for handling customer enquiries, case creation, identification (type, sub type, description), case assignment. Also have created a sentiment calculator on the basis on tonality and issues of the customer and created an integration with slack to route such issues to Slack agents. Also, enabled Slack Agentforce integration for sending notifications, emails and other actions. We have used experience site to host all this. Also, based on the login of the user, the recommended product list changes. We have put additional logic in the flows to also enable the data services plan and put a payment instruction, along with a new case creation if the person is complaining about their data service not working- in additional to showing the analysis around why the services are not working, what are the maximum usage days and trends and what plan they should be buying. We are also sending email notification to customers proactively with a good offer through Agentforce who are identified to have more call drops. Issues faced Data cloud issues for not being able to do the dynamic segmentation, RAG issues- the file and looks ups not reflecting per the change, lot of issues with recommending the best plans based on the criteria defined- also unpredictability of the outcome of the plan name, LWC issues to fetch the dynamic content being populated by AI, plans and cases to be reflected/ updated in run time, initial issues with slack integration, we wanted to showcase the Agentforce icon in a different way, that couldn't work, also the image detection capabilities if could be handled would have been great Accomplishments that we're proud of For all this ready to launch, real-time Agentic work to be developed within this short period of time with the kind of value that it will provide to the telecom providers is a game changer for sure and we are proud of this. What we learnt We have included all the latest capabilities of Data cloud, Prompt builder, Agentforce including pre chats, etc., LWCs, lot of HTML, CSS changes, Slack integration, etc. for this initiative. We do have a lot of new areas to be covered too like dynamic segmentation which didn't work as expected and we had to use another way of doing this by not using data graphs. We have learnt there are a lot of advancements coming on each of these areas and to be able to provide the best solution- we need to have a complete view of new features, upgrades coming in and be able to absorb those on the go for our initiatives What's next for Telco Gamechangers We also plan to publish our solution onto Agent Exchange and use this accelerator for our customers to be able to showcase quickly the power of Agentforce and Generative AI on Salesforce <div