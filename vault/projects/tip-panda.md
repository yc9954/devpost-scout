---
slug: "tip-panda"
url: "https://devpost.com/software/tip-panda"
title: "Tip Panda"
hackathon: "Garuda Hacks 2020"
winner: true
words: 960
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Tip Panda

> A digitized equitable system for tipping

[Devpost](https://devpost.com/software/tip-panda) · hackathon [[Garuda Hacks 2020]]

## Facets

**domain** [[civic_government]] [[finance_payments]] [[health_clinical]]
**substrate** [[financial_record]] [[structured_db]]
  <sub>weak: document_pdf</sub>

**stack** azure, figma, flask, mongodb, python, react-native

## How they structured the write-up

- inspiration
- what it does
- business aspect
- how we built it
- challenges we ran into
- accomplishments we are proud of
- extended video
- what we learned
- what’s next for tip panda:

## Body

Business Plan - https://docs.google.com/document/d/1I4wBwRRYEmvL6qafLt9Ih93cR5fbHhTYCgpsdbV2WfI/edit?usp=sharing Pitch Deck Slides - https://docs.google.com/presentation/d/12-arqmuH6cdw9Qoxk9UpYxFOtCD2MJeuBWyScLlWdhs/edit?usp=sharing Inspiration After a meal at a restaurant, we tend to write a tip to the waiter/waitress who served us, but have you ever wondered where that money is going and how exactly is it being distributed? In reality, the current tipping system does not credit each employee fairly for their share of the work. We were inspired by the opening keynote speakers who mentioned that there is a large plurality of the population who remain unbanked or underbanked, and a large number of this population earn their livelihood through the food service industry. There are 3 current options for distributing tips in restaurants, all of which can negatively impact certain employees: The restaurant distributes all tips equally among all employees, in which case employees who work harder don’t get their fair share of the tip The restaurant allows employees to keep their individual tips, in which case employees such as chefs and cleaning staff don’t get their fair share of the tip The restaurant holds on to tips and often does not fairly or transparently distribute the tips amongst employees Tip Panda is our solution to ensure equitable tipping in restaurants, and helps strike a balance between equal and unequal tipping. This system ensures that all employees, whether it be chefs, waiters or cleaning staff, get tipped fairly, thereby incentivizing quality service. Tip Pooling as a concept is currently available only as localized and relatively feature-scarce solutions; so we decided to come up with an approach that closes the loop on fair and equitable payments as we integrate with our microloan service. What it does Tip panda provides a digital platform for tip sharing, and forms a direct link between the customer and the employees to increase equity and incentivize quality work. We use a novel rating system and algorithm to give extra credits and incentives to harder working employees. This system works in the following way: Tipping System After a meal, the waiter/waitress opens up Tip Panda, and selects the names of all the employees involved in preparing the meal (such as the chefs, cleaners etc.) Next, our app automatically generates a QR code that links all this data to our database. The customer now opens Tip Panda and scans this QR code. Then, they enter the tip amount, and also optionally rate their experience such as the food, service, hygiene etc. Now, the customers can pay the tip with the click of a button, and the money is transferred to a pooled tip jar for the restaurant, where it is split equitably among the employees based on ratings. If no ratings are given, the money is split based on an employee-specific average of previous customer’s ratings. To make this system fair, the bias is reset every month. We also make all the tip data available to all the employees to view to ensure integrity. Loan System There is also a microloan system where employees can request loans from a common restaurant tip jar. These loans are either accepted or rejected based on voting by the other employees. For the employees who vote yes, their share of the loan will be transferred to the employee in need. The employee in need will be required to pay back the loan on a deadline of their choosing. The employees who vote in favor of the loan have the interest repaid with the loan divided amongst them in a manner proportional to the funds provided for the loan. Restaurant and Employees Each restaurant is owned by a manager account, who can add or delete employees from the restaurant, as well as assign roles to the employees (either chef, server, or cleaning staff). Business Aspect Cost-benefit Analysis Customer Assurance of tip reaching the intended recipient Assurance of equitable distribution based on customer experience Employee Guaranteed receipt of tips Equitable tips that rewards hard work Ability to loan money Manager Employees driven to work harder Increased customer satisfaction Reduced work for restaurant Business Model 0.5% commission on all tip transactions above a threshold 1% service fee on all internal microloans 2% service fee on all external transactions Advertisements (in app) Market Size The global outdoor dining market was 3.2 trillion USD in 2016 Of this, the Asia Pacific Region had a share of 1.13 trillion USD Averaging tips to 10% globally, gives us a figure of 320 Billion USD Optimistically, a 10% share of this market will mean 3.2 Billion USD of cash will flow through our system annually This does not account for other non-food verticals in the service industry such as hospitality, tourism etc. How We built it In order to build Tip Panda, we used: Figma to design the front-end React native to code the front-end mobile application Flask python for the backend server for the system MongoDB for storing user data, restaurant data, orders and loans. Microsoft Azure functions for back-end endpoints Challenges We Ran Into Our first challenge we ran into was designing and creating the over 20 user interface screens, for the customer, employee, and manager interface. Furthermore, being some of our first times, it was challenging to transition to using Microsoft Azure functions for our back-end endpoints. Validating the business model and use case also required considerable amounts of research. Accomplishments We are proud of We are extremely proud to have created a coherent working mobile application, and integrating it correctly with our backend server. Extended Video https://www.youtube.com/watch?v=TxRpEnLP0Ag What We learned We learned how to use and integrate Microsoft Azure functions, as well as MongoDB atlas. What’s next for Tip Panda: We hope to fully build and deploy this out at a couple of pilot locations, and then go for VC funding into a full fledged platform. <div