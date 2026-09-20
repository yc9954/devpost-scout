---
slug: "working-conditions-improvement-check"
url: "https://devpost.com/software/working-conditions-improvement-check"
title: "Working Conditions Improvement Check"
hackathon: "The Worthy Web App Challenge"
organization: "Progress"
winner: true
words: 932
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/labor_employment"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# Working Conditions Improvement Check

> We measure the impact of a CSR project for worker rights in Pakistan and Vietnam. With Kendo, we easily created a survey as a chat and a dashboard to visualize the results and gather viable insights.

[Devpost](https://devpost.com/software/working-conditions-improvement-check) · hackathon [[The Worthy Web App Challenge]]

## Facets

**domain** [[labor_employment]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** heroku, intellij-idea, react

## How they structured the write-up

- our story
- our mission
- our customer's request as challenge for this hackathon
- how we built it
- kendoreact components
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for working conditions improvement check

## Body

Chat as mobile first with chiplets for easier communication Survey as chat completed positively Entrance view of the dashboard with data selection and NPS as measure of employer satisfaction Women are often affected strongly by poor working conditions. The dahsboard allows to compare data between the gender of the workers. The comparison between the first and the second survey is crucial to emasure the improvement. The donut chart is a great way to visualize! Data queries and filtering are important to gain insights. This can help before a factory audit to see, what to check for in particular. Our story The four of us came together in 2020 at a competition for digital talents. We loved working together so we just continued to collaborate after the competition. We decided that we want to use our digital skills to solve problems of ecological and social sustainability. After a research period, we started our journey on the topic of worker rights. At another hackathon, we developed our first prototype. We directly won the hackathon and afterwards got positive feedback at demos of our prototype from industry experts. Out of these talks, we started our impact start up called atlat. During our pilot project, we ran into the issue of showing our positive impact. The solution to this issue will be our task for the "Worthy WebApp Challenge''. Our mission Textile companies often produce their goods in low wage countries. Sometimes, the suppliers in these countries do not respect the basic rights of their workers, like paying for overtime or safe working environments. A key part to solve this problem can be a tool that enables the workers at suppliers to file complaints at the brands they produce for. The brands then use their power over the suppliers to solve the issues of the workers together. This approach is backed by a new law in Germany that will make complaint mechanisms mandatory for larger companies. Hence, our core product is a system that builds the bridge between workers and brands. We are proud to say that we have two german fashion brands as pilot customers. Together we do a project in Pakistan and in Vietnam. Our customer's request as challenge for this hackathon In a meeting with our pilot customer, the CSR manager said, “Your complaint mechanism is great, but we need to measure our impact.” If we can prove the positive impact on the workers' condition, we have a strong case to bring our tool to more companies, more suppliers and hence more workers. We took this challenge from our pilot partner to this hackathon: Let's measure our impact and make the results visible. How we built it Now, what can we do to measure our impact? We ask the people who know best: the workers. We conduct a survey before and after the pilot project. Additionally, we need to make the survey data accessible to the CSR manager. What we built has two sides: An automated messenger chat to run the survey for the workers on their mobile phones. A mobile solution, without the need to install an app, is crucial to reach as many workers as possible, since the majority does not own a laptop or desktop pc. A dashboard for the CSR manager to analyze the data and thereby gain insights on how and where to improve the workers rights situation. KendoReact components For the automated messenger chat, we used the Conversational UI component of the KendoReact library. It was easy to set-up and we were even able without prior knowledge of the library to use a slider as a custom element in the toolbar. As a disclaimer, we did not build the database connection and the language adaption to our core product yet, since we first need the feedback and approval from our pilot project partners. However, since the Conversational UI component is easily connectable to Google Dialogflow, this will be no hurdle for us as soon as we get the final approval. For the dashboard, we used several of the charts components to visualize the data. Additionally, we applied the data query components to make a live selection of subsets available. This allows deep-dives into the data, e.g. the comparison of factories or the difference in the answers between genders. All data results can also be exported to Excel or as a PDF via the export and generator components. Challenges we ran into We did not run into any bigger technical challenges. Everything is documented with many details. We only once confused ourselves with the different behaviour of a component in a development build compared to a production build. But after we found our misunderstanding, we were happy that we had learned something new. Accomplishments that we're proud of We're proud that we developed the messenger and the dashboard with KendoReact in such a short time. It all felt natural for us and was also well documented. Hence, besides achieving what we wanted to build, we even had the time to properly style it with our custom colors and fonts. What we learned We had no prior experience with KendoReact and hence learned how good the library is. What's next for Working Conditions Improvement Check We want to show the prototype we built here to our customers and hope they love it as much as we do. As we are user-driven, we are eager to get their feedback. Hopefully, this tool for the measurement and the visualization of our impact can help us to roll out our main product, the complaint management mechanism, to more factories and workers. <div