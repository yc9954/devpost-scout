---
slug: "perkify"
url: "https://devpost.com/software/perkify"
title: "Perkify"
hackathon: "Formula 0001: Rapyd Fintech Grand Prix"
organization: "Rapyd"
winner: true
words: 996
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/educator_student"
  - "user/small_business"
  - "substrate/web_dom"
---

# Perkify

> Use Perkify to offer subscription services to your employees.

[Devpost](https://devpost.com/software/perkify) · hackathon [[Formula 0001- Rapyd Fintech Grand Prix]]

## Facets

**domain** [[education]] [[finance_payments]] [[labor_employment]]
**user** [[educator_student]] [[small_business]]
**substrate** [[web_dom]]

**stack** collect, express.js, firebase, issue, javascript, materialui, rapyd, react, wallet, webflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for perkify

## Body

Log In Home FAQ View Card Footer Features How it Works Use Case Sign Up Pricing Dashboard, Create Group Dashboard, Groups Dashboard, Manage People Inspiration When I got to college, I found out that as a benefit of my enrollment, I could subscribe to the New York Times, the Economist, and the Wall Street Journal, all paid for by the university. I was excited at the time, but two years later and despite numerous attempts to access these subscriptions, I’ve only been able to reliably use one. All required me to delete my existing accounts, sign up with my @yale.edu email address, and use a VPN. If I want to continue accessing these newspapers after I graduate, I have to create a new account. I was reflecting on this recently during a conversation with my parents. They’re small business owners, and are experiencing serious difficulties both recruiting and retaining workers. I suggested that they might like to offer free Netflix to new hires, or buy Spotify Premium for their existing employees. We discussed it further and got excited by the idea. Many people are disproportionately bothered by the costs of subscription services, and accordingly would be highly appreciative if their employer covered them. And relative to employee salaries, subscriptions are a remarkably cheap way to increase employee satisfaction. When I looked into how a business could offer subscriptions to its employees, I was reminded of the difficulties I experienced trying to access content purchased for me by my university. Only a small number of content providers (pretty much only national newspapers) have established programs for businesses to offer group subscriptions to their employees; all of these take a long time to set up, and must be managed separately. Manual alternatives would be highly inconvenient to both employees and managers, requiring the latter to maintain lists of credentials for different employees’ accounts on any number of different servers, each of which they would have to sign up for one at a time. What it does Perkify solves these problems. It allows businesses to create an account, link a payment method, paste a list of employee email addresses, and choose the subscriptions they’d like to offer from a list of over 50 options, all in under five minutes. Instead of requiring special sign-in methods, Perkify issues each employee a virtual credit card that can be used only for their approved services. There’s no need for employees to create a new account with a given service, or to delete it if they change jobs. Employers pre-pay for each month's total subscription costs, which is transferred to a Wallet maintained by Perkify. The employee cards are linked to this wallet. Employers can select perks for each employee individually from our intuitive dashboard, or create “groups” with set lists of perks and add members to them. We also integrate with ADP and Quickbooks to make it even easier for businesses that use these companies’ software to get set up. Once perks have been selected, Perkify will automatically email each employee a list of their permissions and a secure link where they can view their credit card information. If an employer changes permissions during the month, Perkify automatically updates the cards. No oversight required. If any employees don’t use their perks, we return that money to the business at the end of the month. How we built it After discussing the idea, my collaborators and I began searching for fintech platforms and BaaS providers that could support our use case. While in the middle of reviewing docs and testing out different providers in their sandboxes, we discovered the Rapyd hackathon. After reviewing the API docs for Wallet, Collect, and Issue, we decided to build with Rapyd. Our backend is built with Firebase and Express, connected to a ReactJS front-end. We used Webflow to build a simple homepage and Material UI to design the front-end. We use the Rapyd Wallet API to create a money storage account for each business that signs up. Though we’ve not yet built this feature, we will also use Rapyd Collect to collect funds from businesses that will be deposited into their Wallets. We use Rapyd Issuing to create the cards employees use to pay for their subscriptions. Challenges we ran into We wanted to make the easiest employee sign up possible, so we weren’t sure how much information we actually had to collect. We spent time interviewing potential users—both employers and employees—to investigate what would be the smoothest user experience. One issue raised by employees was a concern that they might forget or fail to save their card information, and wanted a way to view it on demand. We resolved this by creating a form on the website that could re-generate the viewing link by simply submitting their email address. Accomplishments that we're proud of We’ve managed to sell the product before it exists! Three small and midsize businesses, for a total of about 100 employees, have told us that they’d like to use the platform once we’re live. What we learned We’ve all been really impressed and surprised by all of the infrastructure available for developing fintech applications. When we started the project, we were skeptical that it would be possible for 3 college students to be able to create a service that could collect and store funds, and issue cards. And yet we created a working demo in just 10 days! What's next for Perkify Hopefully we’ll be able to activate our account with Rapyd as soon as possible. Having built the product around the Rapyd APIs, we’d be able to onboard our first three customers as soon as that is completed. If we aren’t able to activate our account with Rapyd, we’ll rebuild our-back end with another Fintech provider, most likely Stripe or Unit. Either way, we’re incredibly excited by the traction we’ve achieved in just the past 2 weeks of working on Perkify, and we can’t wait to begin supporting our customers. <div