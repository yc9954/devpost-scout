---
slug: "diaper"
url: "https://devpost.com/software/diaper"
title: "Moolah"
hackathon: "Formula 0001: Rapyd Fintech Grand Prix"
organization: "Rapyd"
winner: true
words: 975
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/educator_student"
  - "substrate/financial_record"
---

# Moolah

> Moolah is an all-in-one personal finance app that gives kids and teens their first debit card and guides them to develop sustainable money management habits through gamified lessons.

[Devpost](https://devpost.com/software/diaper) · hackathon [[Formula 0001- Rapyd Fintech Grand Prix]]

## Facets

**domain** [[education]] [[finance_payments]] [[retail_commerce]]
**user** [[educator_student]]
**substrate** [[financial_record]]

**stack** heroku, mongodb, node.js, rapyd, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for moolah
- demo credentials
- thanks for reading!

## Body

Welcome Sign Up Wallet Pay or Request Non-user Receive Payment Non-user Payment Email Non-user Payment Page Stats Learning Profile Inspiration As a team, we spent two full weeks brainstorming and noticed that many of the fintech trends we found and ideas we generated pointed to a gap in the market for a kids’ payments solution. For years, children have been getting smartphones at younger and younger ages, so it’s no surprise that their online shopping rates have also been on the rise. Not only are these children and teens an emerging demographic in the realm of online shopping, but they are also a less-informed group who might lack experience managing their money. We saw this as an opportunity to create an app that would both help expose children to and teach them about tech-based payment methods like digital debit cards. We consulted with some advisors in the fintech industry and they validated this gap in solutions that would both empower kids to make their own payments, establish their own goals, and learn how to develop great spending habits from a young age. That’s why we made Moolah. What it does Moolah is an all-in-one personal finance app that integrates spending and learning. The app has 4 main sections with the following features: Wallet Debit Card : Spend the wallet balance with this card in person or online. The card can also be added to external mobile payment providers like Apple Pay, Google Pay, etc., and can be activated or deactivated in the settings panel. Manual Entry : An option to manually enter any spending or earnings. This is especially good for any cash transactions that wouldn’t be automatically logged. Pay/Request : A feature that makes transferring funds between friends and family super easy. It can work for both people who have and don’t have Moolah. If the recipient doesn’t have Moolah, they will receive either a payout page email or a checkout page email depending on whether they receive a payment or a request, respectively. Transaction History : Any transactions using the debit card or the pay/request feature will automatically be logged here. Manual entries will also appear here but won’t impact the wallet balance. Stats Stats Summary : A summary of spending and learning for the time period selected. Graphs : A variety of graphs will be generated weekly to better show the user how their spending and learning habits are changing. Learning Lessons : Curated sets of videos and learning checks to teach the user about various fintech and money management topics. Short videos break up even the most complex of subjects and make learning feel quick and easy. Learning checks make sure that the user understood the main ideas of the lesson. Profile Goals : An option to set goals that the user wants to save up for. As time passes, the user will receive reminders and be given checkpoints for the goals they are trying to manage. Badges : Badges are earned as the user spends and learns. They add some gamification to the spending experience and provide an incentive to complete the lessons. How we built it We used Figma and Adobe Illustrator to design plenty of UI/UX mockups and narrowed them down to the final screens after discussing which would result in the best user experience. We built the web app with a MERN stack (MongoDB + Express + React + Node.js) and TypeScript, serving it on GitHub Pages and Heroku. We were excited to be able to implement all 4 Rapyd Payment APIs into Moolah. Rapyd Wallet transfers funds between Moolah wallets. Rapyd Disburse sends an email with a payout page so that Moolah users can send money to non-users. Rapyd Collect helps Moolah users request money from non-users by sending an email with a checkout page. And finally, Rapyd Issuing issues the debit cards within Moolah. Challenges we ran into The biggest challenge was to come up with an idea that we found both interesting and meaningful. We barely had any working experience in the fintech industry, so this involved a lot of reading, research, and interviewing people who did know more about fintech and payments. One of the technical challenges we ran into was in using Rapyd API. Here are the blockers and workarounds for them that we came up with: https://github.com/64json/moolah/search?q=blocker Accomplishments that we're proud of By looking at payments from a kid’s point of view, we think we found a unique perspective on the proposed circuit challenges. We are also proud of how the app turned out visually and how the idea came together nicely to integrate all 4 of the Rapyd Payment APIs. We also think the name we chose for the app is amazing. :) What we learned We learned to not underestimate the amount of time required for brainstorming. Similarly, we learned the importance of building buffer time into our project timeline because the mini-deadlines we set for ourselves are bound to get pushed back as we encounter new challenges. We also learned that collaboration and communication between design and development are very important for creating both a technically feasible and user-friendly product. Two heads are for sure better than one! What's next for Moolah We’d love to take this project further and already have some ideas for possible next steps: Building for business collaboration with schools and teachers. Using receipt scanning to streamline manual entry. Adding the ability to split expenses We also hope to expand our audience by adding features to help older teens transition to adulthood and manage credit cards, loans, and credit scores by partnering with financial institutions. These partnerships would open up plenty of monetization opportunities along with sponsored content or ads. Demo Credentials To see Jasmine's account, go to https://jasonpark.me/moolah and sign in with the below credentials: email: jasmine@rapyd.net password: password Thanks for reading! <div