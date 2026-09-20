---
slug: "druidchatbotintegration"
url: "https://devpost.com/software/druidchatbotintegration"
title: "Druid Chatbot Integration"
hackathon: "Power Up Automation"
organization: "UiPath"
winner: true
words: 1046
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# Druid Chatbot Integration

> It brings conversation capabilities to UI Path robots and adds cognitive services to the DRUID chat bots.

[Devpost](https://devpost.com/software/druidchatbotintegration) · hackathon [[Power Up Automation]]

## Facets

**domain** [[finance_payments]] [[labor_employment]]
**substrate** [[document_pdf]] [[web_dom]]

**stack** angular-5;, asp-.net-core, microsoft-azure-technology-stack;, microsoft-botframework;

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for druid chatbot integration

## Body

CRM web form UiPath execution queue Druid Connector - UiPath action config chat window making the request Druid FlowStep - UiPath action config Connector Action UiPath Task druid convesation flow designer chat window with response- queue item no UiPath Studio running RPA process Inspiration Chat bots are used to provide a conversational interface between systems users, enhancing the human workflows, and help streamline and simplify the completion of tasks. The RPA is responsible for task execution, connecting to the systems, mimic and replace the human-driven workflows. Implementing RPA processes, there are times when the robot needs human feedback. Either there is an approval required or there is a need to complete missing information in a document, the robot needs to pass the control to a person. If that person is on the go, or at the office, it will be nice the RPA robot start chatting with the person and ask what it needs. The joint functionality of chat bots and RPA combined, alleviates the burden experienced by the human workforce brought on by repetitive, mundane and low value admin driven tasks. It only seems natural for instant chat and Robotic Process Automation to come together in contributing towards the customer self-service and employee productivity revolution. What it does The DRUID chat bot platform provides native integration with UI Path. It brings conversation capabilities to UI Path robots and adds cognitive services to the DRUID chat bots. There are two use cases supported: **Use case 1: Start RPA process from chat bot.** **Use case 2: Ask for human feedback within an RPA process** Use case 1: Start RPA process from chat bot. The customer representative chat with his DRUID Virtual Assistant and ask him the profile of a particular client. DRUID chat bot connects to the CRM system, extracts the data and responds to the sales person. The data include also the suggestion for a new better product for the customer. The customer confirms the new offering. The sales person tells the DRUID chat bot to apply the changes in the customer record. The DRUID bot calls the UI Path robot to perform the changes (creates an item in the designed UI Path queue). The UI Path robot do the followings: Receives the new product details from the DRUID chat bot Connects to the CRM system Identify the customer record Configuring a new product requires filling various forms in CRM. UI Path robot do this a. Connects to the current contract and click inactivate b. Fill in required fields and click submit c. Click new contract d. Fill in required fields and click submit. e. Go to Notes tab, click Add note and fill in the time, robot name, user initiating the request Send an email to sales person and customer announcing the change Trigger back an conversation with the DRUID chat bot, telling the task is done. The Druid chat bot initiate the feedback conversation with the sales person announcing the provisioning is complete. In this scenario, the sales person received the help of the UI Pat robot, without connecting to the CRM system. Use case 2: Ask for human feedback within an RPA process The UIPath robot started the “New contract activation” for a customer. He identified that the customer already has an active contract and according with the process rules the approval of a sales person is required. Using the DRUID chat bot integration, the UIPath process uses the DRUID Integration, Trigger Conversation activity. Sets the parameters Target User (sales person), Conversation Flow (configured in the DRUID Chat Bot platform), Customer Name, Current Contract details (text), New contract Details (text), call back queue item id. The DRUID chat bot starts a conversation via skype for business with the sales person. The sales person immediately receives the notification, enters the conversation, sees the details and text “Approve”. DRUID chat bot submits the response as a new item in the designed queue, monitored by the UI Path process. Resolution is extracted and the RPA process continues. How we built it We started from a POC idea in which we wanted to start RPA processes from Druid conversations and viceversa. Besides this we needed to make sure that everything runs automated with no human intervention. Due to this requirement we started using the UiPath Orchestrator queues to push and consume conversation business related information. When developing our sample RPA processes to be triggered from a conversation we needed a way to send back to our Druid platform, the needed information for this trigger to happen. The idea of having a custom code activity emerged including we a REST client triggering an API call to the Druid Platform. The conversations are configured with the Conversation Designer in DRUID platform. No code required. Chatting with the bots is possible in Intranet web pages (land bot page, skype for business, skype, slack or even in Facebook). Challenges we ran into There were no actually big challenges since using the UiPath products is very simple and intuitive. The documentation offered on the internet is detailed and sufficient. The only challenge we had was with making our custom activity more appealing by having an icon and displaying it under the right category in the UiPath Studio. We had to start learning Windows Workflow Foundation. Accomplishments that we're proud of Happy to see how many processes can be now implemented by the chat bot consultants and UI Path consultants. The DRUID chat bots can complete much more tasks, connecting via RPA to systems where it was not possible before. With the Druid Trigger conversation activity available in UI Path Studio, you can now start conversation with no code. What we learned Applying the UI Path best practice is valuable. Talk with the UI Path experts what you want to do, ask for advice. Very valuable. Will save you time and give you confidence that the final product is good. What's next for Druid Chatbot Integration We are building pre-configured packages for common processes and industries. There are complete solutions, chat bots and RPA settings for Human Resources, Cost Control, Finance, Customer Support, Sales, Contract Management and Project Management. Pre build configurations are built with leader in their industry: Banking and Financial Services, Healthcare, Manufacturing, Real Estate, Construction, Oil and Gas, Retail. <div