---
slug: "spothelp"
url: "https://devpost.com/software/spothelp"
title: "Spothelp"
hackathon: "Codegeist Unleashed"
organization: "Atlassian"
winner: true
words: 975
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/disaster_emergency"
  - "domain/mental_health"
  - "user/frontline_worker"
  - "substrate/document_pdf"
---

# Spothelp

> help on the spot!

[Devpost](https://devpost.com/software/spothelp) · hackathon [[Codegeist Unleashed]]

## Facets

**domain** [[disaster_emergency]] [[mental_health]]
**user** [[frontline_worker]]
**substrate** [[document_pdf]]

**stack** altaskit, chatgpt, forge, javascript, openai, react

## How they structured the write-up

- inspiration
- what it does
- category
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for spothelp

## Body

Inspiration The inspiration behind our project, Spothelp, stemmed from observing the challenges faced by our customer support team. These dedicated individuals were working tirelessly, round the clock, leading to burnout and decreased efficiency. Being a small-scale company, recruiting additional customer support executives was financially daunting. This dilemma prompted us to create an AI-powered innovative solution, Spothelp! What it does Spothelp serves as an AI-backed customer support executive , significantly improving the efficiency of our customer support operations. Here's what it does: Auto Assignment : The application can automatically assign customer issues from JSM to specific Jira boards based on the settings defined within the application. This eliminates the need for manual assignment, streamlining the process. First Responder : It acts as the initial point of contact for customers. Using AI-generated responses, it delivers polite and helpful messages to customers, ensuring they receive immediate attention. Team Availability Notification : In cases where the designated team is unavailable or enjoying their Holiday , the system can notify the customer, managing expectations and providing transparency. Multilingual Support : If a customer creates an issue in a language other than English, the application can respond in the customer's chosen language. This feature enhances the customer experience and eliminates language barriers. Category "AI Apps for Collaboration ✨" Enables AI-powered collaboration between the different departments that use Jira or JSM for their day-to-day work. ✅ Collaborates with Helpdesk teams to get customer tickets resolved in a shorter time. ✅ Integrates Jira, Jira Management Service, and Confluence in a smarter way to make the user experience smoother. ✅ How we built it We employed a combination of technologies to create Spothelp, ensuring it's both functional and visually appealing. Here's how we built it: Atlassian Custom UI and Forge : We used Atlassian's Custom UI and Forge to construct the application's framework. These tools allowed us to seamlessly integrate our solution within the Atlassian ecosystem. Forge API : Various in-built forge APIs were used to create the app such as Storage, Async, JIRA & Confluence rest APIs. Atlaskit Components : To enhance the visual appeal of our application and ensure it integrates seamlessly with Atlassian's environment, we incorporated components from Atlaskit. This not only makes the application aesthetically pleasing but also ensures it aligns with the user experience expectations of Atlassian users. OpenAI APIs : To power our AI capabilities, we leveraged OpenAI APIs. These APIs allowed us to generate AI responses, making it possible for our application to communicate effectively with customers. Challenges we ran into While developing Spothelp, we encountered several challenges that required innovative solutions. Here are some of the key challenges we faced: AI Model Selection : Selecting the right AI model was crucial for the success of our project. We experimented with various models, but some were too slow in execution, while others had limitations imposed by API usage restrictions. Response Format : Another hurdle was getting the correct format of responses from the OpenAI Chat API. Achieving the desired response format was essential to provide a seamless and natural interaction between our application and customers. Despite these challenges, we overcame them through creative problem-solving and dedication to creating a functional and cost-effective solution for our customer support needs. Accomplishments that we're proud of We take immense pride in the following achievements of our project, Spothelp: Replicating Customer Service Tasks : Our application successfully emulates the responsibilities of a customer service executive with minimal and one-time inputs. This achievement ensures that customer support operations can be enhanced without the need to hire additional employees. 24/7 Helpdesk : Companies can now benefit from our application by establishing a 24/7 helpdesk without the requirement to recruit additional staff. This cost-effective solution ensures continuous customer support availability. Robust UI and Backend : The robustness of both the user interface (UI) and the backend of our application is a significant accomplishment. We have meticulously addressed most fail points and loading views, resulting in a seamless and reliable user experience. What we learned Our journey in developing Spothelp was a valuable learning experience. Here's what we gained: In-Depth Understanding of OpenAI APIs : We delved into the intricacies of OpenAI APIs, gaining a comprehensive understanding of their capabilities. We also explored various other AI models, enabling us to make informed decisions about their usage. Forge Expertise : We acquired knowledge about Atlassian Forge, a critical component of our project. This knowledge empowered us to leverage event-based function calls, which we applied for the auto-assignment of customer issues. Design Excellence with Atlaskit Components : The application's elegant and minimal design was made possible by our exploration and application of beautiful Atlaskit components. This not only enhanced the visual appeal but also ensured a user-friendly experience. What's next for Spothelp As we move forward, here's what's on the horizon for Spothelp: Expanded Request Types : In the current MVP stage, our application is tailored to handle technical issue types such as "Report a bug" and "Technical support" within Jira Service Management (JSM). Our future updates will include the expansion of this feature to accommodate other issue types. This will broaden the application's usability across various use cases. Cost Integration for OpenAI Key : While testing the application in a real-world scenario, the OpenAI key is necessary. We plan to include this cost within the application's pricing structure, making it easier for users. Additionally, we aim to provide the option for users to add their own OpenAI account key. Enhanced Data Extraction : A comprehensive Confluence document is required in the pipeline. This document provides detailed insights into how a team works, the underlying tech stack, collaborative team aspects, and more. In the future, we envision improving extraction from this document by incorporating domain-based machine learning. This means tailoring the documentation to specific domains, such as healthcare, will meet the unique needs of healthcare industries. <div