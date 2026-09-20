---
slug: "smartcards-qxdusb"
url: "https://devpost.com/software/smartcards-qxdusb"
title: "SmartCards"
hackathon: "ShellHacks 2024"
organization: "init"
winner: true
words: 690
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "domain/finance_payments"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# SmartCards

> SmartCards is a user-friendly addon for your budgeting app to help you better categorize your transactions and find investing opportunities from each purchase.

[Devpost](https://devpost.com/software/smartcards-qxdusb) · hackathon [[ShellHacks 2024]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]] [[finance_payments]]
**substrate** [[code_repository]] [[financial_record]] [[structured_db]]

**stack** express.js, flask, kaggle, node.js, openai, react, tailwindcss, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for smartcards

## Body

Thumbnail and Branding Landing Page Upload Screen Example Transaction Breakdown Investment Insights & Opportunities Application Schematic SmartCards SmartCards is a user-friendly addon for your budgeting app to help you better categorize your transactions and find investing opportunities from each purchase. Simply upload a picture of any receipt and our GenAI technology will organize your purchases while providing insights to help your financial future. Inspiration SmartCards was inspired by real-world problems we've encountered with split transactions in popular budgeting and cash management applications like YNAB (You Need A Budget). We noticed that these apps typically don't integrate or inspire their users to invest in stable (or unstable) opportunities while using the app. While some may offer learning resources on their websites, this information isn't readily presented to users within the app interface. SmartCards was also conceptualized because of the growing need for financial literacy in our world. Many people are unsure about investing, and we want to help provide the tools to show them the many alternative places a dollar can be outside of the bank account. What it does SmartCards is a user-friendly addon for budgeting apps that helps users better categorize their transactions and discover investing opportunities from each purchase. Our key features include: Intelligent transaction categorization using GenAI technology Investment opportunity identification based on spending patterns and other user information Seamless integration with existing budgeting apps User-friendly interface for easy receipt scanning and financial management Users can simply upload a picture of any receipt, and our GenAI technology organizes purchases while providing insights from spending patterns and cashback opportunities to help their financial future. How we built it We built SmartCards using a combination of modern web technologies and AI: Frontend: React+Vite and Tailwind CSS for a responsive and intuitive user interface Backend: Node.js for serverside management & Flask to run our local classification model (trained on a Kaggle dataset of 42,000 different products, 83% accuracy) AI Integration: Leveraged OpenAI's API for intelligent transaction categorization and investment insights Version Control: Git and GitHub for collaborative development Development Workflow: npm for package management and running development servers Challenges we ran into First time using OAuth2, there were a few different ways of integrating it and so we needed to find what worked for us We decided to use a classification model to separate the products / services into categories, but this model needed to be run using Python libraries. Therefore we had to set up and create a parallel Flask server for the model. Huge mixup with the localhost v 127.0.0.1 involving incorrect redirects and other shenanigans. hour long setback Using context provider with react is a pain, since there is no simple way to transfer information from siblings for some horrible reason. Accomplishments that we're proud of Nice looking landing page and elegant branding / presentation (more for the readme and devpost Fully connected front and back end using 2 servers (This was insane!) Use of chartjs to give cool-looking visuals and a working MVP! WIP database to store user transactions and itemized purchases. What we learned Always remember to keep it simple, we want the MVP here, we're not trying to recreate the entire banking system Starting with some boilerplate is not cheating, know how to set that up easily so that you're ready to roll Don't try to learn a new framework in 24 hours it won't happen. Use your unfair advantages, but also recognize learning does come quite quick Be willing to change project ideas and incorporate company challenges into your project, they have the bigger perspective. Used new libraries like chartjs, and figured out context providers, and first time using a classification model in a full-stack project. What's next for SmartCards We have exciting plans for the future of SmartCards: Implement machine learning models for even more accurate transaction categorization Integrate with major financial institutions for real-time transaction updates Develop a mobile app for on-the-go receipt scanning and financial management Improve investment opportunity detection algorithms Introduce social features for comparing anonymized spending habits with peers We're committed to continuously improving SmartCards to help users make smarter financial decisions and discover new investment opportunities. <div