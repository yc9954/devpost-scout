---
slug: "risk-navigator"
url: "https://devpost.com/software/risk-navigator"
title: "Asset Angel"
hackathon: "HackUTD X"
organization: "hackutd"
winner: true
words: 809
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/finance_payments"
  - "user/small_business"
---

# Asset Angel

> Assets Angel quantifies risk for small business owners and provides them actionable steps to optimize operations and minimize insurance premiums.

[Devpost](https://devpost.com/software/risk-navigator) · hackathon [[HackUTD X]]

## Facets

**domain** [[agriculture_food]] [[finance_payments]]
**user** [[small_business]]

**stack** golang, google-cloud, openai, vue-js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for assets angel

## Body

Logo assets Inspiration Small business owners confront a multitude of challenges, with financial uncertainties that can significantly impact their bottom line being one of the most daunting. Frequently, they lack the resources and means to identify these issues and proactively address them before they escalate. This initiative was conceived on the premise that by equipping small business owners with the right tools and insights, they can effectively navigate the intricate landscape of insurance and fortify their financial future. The goal is to provide them with the knowledge and resources necessary to identify and mitigate risks, ultimately ensuring a more secure and prosperous path forward for their enterprises. What it does The primary objective of Asset Angel is to assist small business owners in identifying effective strategies to reduce their risk and mitigate their insurance premiums. This is achieved through a user-friendly interface where various financial factors are inputted, generating a quantified assessment of their business's risk. Furthermore, the application provides actionable recommendations to diminish risk factors, ultimately leading to reduced insurance premiums. How we built it To develop Asset Angel, we employed a robust tech stack that seamlessly integrates Vue.js for the front-end and Golang with the Echo framework for the backend. The Vue.js front-end provides a user-friendly interface for small business owners to input their financial data and interact with the application. On the backend, Golang with the Echo framework ensures high-performance, scalability, and efficient data processing, making the app responsive and reliable. One of the standout features of our app is the quantified risk factor which is calculated through a heavily researched regression model. The integration of a ChatGPT plugin, which serves as a chatbot that offers personalized recommendations on mitigating risks based off of the user inputted data. Leveraging ChatGPT's natural language processing capabilities, we enable users to engage in meaningful conversations and receive actionable suggestions to reduce their insurance risk factors personalized to the user's business. This powerful combination of technologies enhances the user experience, making it easier for small business owners to understand and manage their insurance needs, helping bridge the gap between them and insurance assistance. Challenges we ran into Multiple Front-End Interfaces: One of the primary challenges we faced involved the development of two distinct frontends. The first frontend is designed for the user-facing app, prioritizing a seamless and intuitive user experience. The second frontend, in contrast, is intended to manage and control the demo, focusing on behind-the-scenes functionality and control. Balancing the design and functionality of these two frontends while ensuring they work harmoniously presents a significant development challenge. LLM Responses: The LLM has been presented a challenge by delivering inconsistent responses, resulting in prolonged load times for various system operations. To address this issue, we've incorporated concurrency measures to alleviate the problem, although it has only provided a partial solution. The goal is to attain more consistent and efficient responses to enhance overall system performance and user experience. Data Availability: We encountered a significant hurdle due to the limited availability of data related to the financial information of small businesses that we could utilize to inform our app's development. The scarcity of relevant data makes it challenging to build a robust and data-driven model for our application, potentially impacting its accuracy and effectiveness. Accomplishments that we're proud of Value Proposition to Small Businesses: Our value proposition to small businesses is centered around delivering a tailored and cost-effective solution that directly addresses their unique needs and challenges. Teamwork: We are proud of the entire team for uniting and collaborating effectively. Our collective effort and great synergy during the hackathon played a pivotal role in our success. It was inspiring to witness the team's dedication, creativity, and the way we seamlessly worked together to achieve our goals. Custom Risk Formula: We take immense pride in the development of our custom risk score formula, which integrates several critical components. This formula combines baseline risk assessments, risks associated with specific tasks and recommendations, and the incorporation of fundamental financial risk indicators, such as the Altman Z Score. This comprehensive approach allows us to provide a well-rounded and highly accurate risk assessment tool that offers invaluable insights for informed decision-making and risk management. What's next for Assets Angel Our vision for Assets Angel is to expand its capabilities to seamlessly integrate with State Farm's small business insurance services. This expansion would empower business owners to not only access insurance information but also apply for insurance coverage and file claims entirely through the Assets Angel mobile app. By doing so, we aim to provide a comprehensive and user-friendly platform that simplifies the insurance process for small business owners, streamlining their interactions with State Farm and enhancing their overall insurance experience. This integration would not only save time for both business owners and insurance providers but also improve accessibility and convenience in managing their insurance needs. <div