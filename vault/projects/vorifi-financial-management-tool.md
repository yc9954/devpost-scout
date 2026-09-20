---
slug: "vorifi-financial-management-tool"
url: "https://devpost.com/software/vorifi-financial-management-tool"
title: "Vorifi Financial Management Tool"
hackathon: "Hackonomics 2025"
organization: "hackonomics"
winner: true
words: 780
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "user/government_staff"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Vorifi Financial Management Tool

> A revolutionary finance management app with a powerful ai chatbot to add accounts and categories as well as know your income and expenses.

[Devpost](https://devpost.com/software/vorifi-financial-management-tool) · hackathon [[Hackonomics 2025]]

## Facets

**domain** [[education]] [[finance_payments]]
**user** [[educator_student]] [[government_staff]]
**substrate** [[document_pdf]] [[financial_record]] [[structured_db]]

**stack** azure, clerk, css, gemini, hono, neondb, next.js, plaid, react, ts

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for vorifi financial management tool

## Body

Inspiration My inspiration for this project came about when assessing the current generation's and high school's inability to manage personal finances. One of my close friends does not have any worth for finance and just spends as much as he wants without really knowing how much he has spent. I hope to benefit Monta Vista by providing students with the abilities to keep a better track of their finances and there are a lot of cases of people without significant finance education at Monta Vista. What it does This app tracks one's everyday income, expenses, and remaining amount. It allows the user to input their transactions, account name, and categories. From there, the app calculates these three fields based on the transactions the user has made. From there, it creates a comprehensive graph with information regarding the income and expenses of the month. In addition, the user can also upload a CSV document of their bank statement, and the app parses those into the transactions, accounts, and categories. The best feature is Plaid which allows users to connect their bank account and manage their finances that way as well. Additionally, the app also has an ai chatbot that can access the income and expenses of the user as well as add a new account or category. To hone in on the theme of economic growth, we wanted to create an application that ensure's individual economic vitality. This would ultimately help contribute to the community's economic growth as a whole. By targeting individuals, we can develop a sustainable microeconomic system that will greatly contribute to the macroeconomic system as well. How we built it This app was built using nextjs and react. I authenticated the sign in and sign up using clerk, configured the backend requests using hono, and I also used neon and drizzle-orm as my SQL databases. I also used the shadcn-ui to be able to easily and quickly download needed libraries for the frontend. In addition, the Plaid software was used to allow users to seamlessly connect their bank accounts to the app. We used Microsoft Azure for our receipt scanning system and used alpaca to retrieve the stocks information. Finally, we used gemini api to train our AI chatbot and make it more knowledgable and experienced in finances. Challenges we ran into Some of the challenges we ran into were being able to process the backend requests correctly and parse them into the databases and update it in the app, correctly configuring the clerkMiddleware and zodValidator. Another thing that was challenging for me was coding the schema.ts and drizzle.ts so they work correctly. The hardest thing though was being able to get the CSV document feature working as it took a lot of time to be able to figure out how to parse the values into the database. In addition, configuring the Plaid Link software took some time as I needed to figure out what how to configure the plaid.ts file correctly so it established a link. Additionally, adding the commands into the ai was a major challenge that took a lot of time to figure out how to correctly configure the token. Accomplishments that we're proud of I am really proud that I was able to add the CSV document feature into my app. In addition, this was my first time working with neon and drizzle-orm, so it was really great that I was able to get those working. I am most proud of being able to connect Plaid to the app. It took a significant amount of time, but was ultimately rewarding. For the ai chatbot, we tuned a model with gemini to get accurate and fast answers. What we learned I learned a lot about backend requests using Hono as well as using the Neon and DrizzleORM databases. I also learned a lot about using databases and how to parse values from client requests. This project further developed my understanding of Nextjs and its capabilities in making a comprehensive and resonating web application. I learned a lot about how to use and configure Plaid Link to allow users to connect their bank accounts to web applications. This also helped me to learn more about how to incorporate user context and commands into ai. What's next for Vorifi Financial Management Tool I also hope to make the UI better as well as add more features such as an AI to help make adding transactions easier. I hope to incorporate more commands into the ai and allow the user to have a better overall experience with the chatbot. We also hope to implement a course feature where users can learn about finance from expert professionals. <div