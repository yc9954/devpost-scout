---
slug: "for-a-cause"
url: "https://devpost.com/software/for-a-cause"
title: "For A Cause"
hackathon: "Amazon Raise-up Buildathon"
organization: "Amazon"
winner: true
words: 1236
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "user/legal_professional"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# For A Cause

> Donate to a cause that speaks to you!

[Devpost](https://devpost.com/software/for-a-cause) · hackathon [[Amazon Raise-up Buildathon]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]] [[legal_professional]]
**substrate** [[code_repository]] [[financial_record]] [[structured_db]] [[web_dom]]

**stack** alexa, amazon-alexa, amazon-dynamodb, amazon-pay, amazonpay, application-load-balancer, aws-certificate-manager, aws-cli, bootstrap, css, flask, github, google-meet, html

## How they structured the write-up

- about this project
- inspiration
- what it does and how we built it
- how to use it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for our project
- how to test it

## Body

For A Cause - How It Works For A Cause - Charity Fundraising Eco-system For-A-Cause Please refer to our repository for detailed documentation. About this project Inspiration What it does and How we built it How to use it Challenges we ran into Accomplishments that we're proud of What we learned What's next for our project How to test it About this project This project is part of the AWS Hackathon submissions that enables users to discover and donate to charities that speaks to them (yes, literally!) via any Amazon smart device with voice enabled capabilities! We have developed a full eco-system to support charities to help raise funds: A front-end for charities to register with us and provide us with their information to share with users An AWS DynamoDB database that stores the information An Alexa voice skill that allows the users to easily discover charities that are meaningful to them with an option to make a donations via Amazon Pay. The entire eco-system for our app is shown here . Inspiration Our project’s inspiration came from when we were looking for a way to donate to a certain charity in a quick and easy manner via voice interactions. In this world of technology, we did not come across any skill that was comprehensive enough to support both users and charities while allowing donations to be made via voice commands. Once we discovered this gap, we quickly brainstormed some ideas and decided to create a blueprint for this project. We wanted to provide charities with an avenue of voice activated donations that would help charities of any size, location, technology, and type, and our eco-system does just that! What it does and How we built it Our design is broken into three tiers: Charity Interactions: A front-end is dedicated for the charities to register with us and provide us with valuable information to share with users. Storage: An AWS (DynamoDB) NoSQL database is utilized that stores the information provided by the charities and later retrieved by the Alexa skill. User Interactions via Alexa voice skill: The user interacts with the app using an Amazon smart device via Alexa voice skill - For A Cause . Python is used for the back-end logic for the skill development. The back-end retrieves necessary information from the database, uses Amazon Pay for processing donation payments, and handles other requests as made by the users. Amazon Pay is integrated in the Alexa Skill to enable seamless payment processing between the user and us. The system architecture and data flow is available here . We used the following technologies: Alexa ASK (Alexa Skills Kit) Python AmazonPay AWS DynamoDB HTML CSS Jquery Bootstrap Flask Route53 Application Load Balancer AWS Certificate Manager AWS CLI noSQL Workbench Slack Google Meet Github How to use it Please refer to the "How to test" section before testing it. Judges are given beta tester and developer level access to the Alexa skill. A user access is created for the judges for DynamoDB and Amazon Pay. The user ID and passwords are provided in the original hackathon submission. For donors/users, the skill can be used by invoking the wake word "Alexa, open for a cause", the user can simply get started. The app provides necessary help instructions as the users interact. It handles various situations, such as exploring more charities, donating to a charity or providing more information about charity, processing payments using Amazon Pay, etc. The charities can access the registration form www.for-a-cause.net . The charity form collects various information from the charity for the Alexa skill to use and their e-mail address to arrange for the funding to be distributed periodically. Challenges we ran into All of our team members do not have extensive experience in developing an Alexa skill and integrating it various AWS services, such as DynamoDB, AmazonPay, AWS certificate manager, etc. The challenge was to familiarize ourselves quickly with new concepts/technologies, research, build and test a fully functioning application. We found this challenge to be fun and rewarding and hoping that it would help charities to raise funding in future. Accomplishments that we're proud of We feel proud to be able to develop a multi-facet system that the charities can use to raise funding, while making it easier for the users to donate to their favorite charities! We also learned a ton (as listed below)! What we learned We learned an abundance of things from where we started. A few of the highlights are as follows: Alexa Voice Skills AWS DynamoDB and its integration to Alexa skills AmazonPay and its integration to Alexa skills Various front-end technologies Research Skills Collaboration Time management Communication/interpersonal skills What's next for our project We would like to add features such as monthly subscription, ability for charities to obtain user addresses to send appreciation gifts, and so forth. We think this app has a huge potential to help non-profits! How to test it Alexa Skill Since this app has not been published to public, but only published to the beta testers, there are two ways to test the app (besides having to set it up using the files provided in the repo using the instructions under how we set it up): Using Console: The hackathon judges have been provided the access to Alexa Developer Console . Once logged into the account using the e-mail addresses provided on the Hackathon page, they should be able to see a skill called Cause on their console. There will be a live skill and one under development. Since AmazonPay has been set up under the SandBox mode, click on the one that is labelled as under development. Click on the test tab and start testing it away! The best way to test the app is by speaking to it rather than typing to avoid any non-word inputs (i.e. $1 instead of one dollar). As a beta tester: Using the e-mail addresses provided on the hackathon page, login to your accounts. Go here Enable the skill called Cause Be sure to enable Amazon Pay permission in the skill Use any associated device or Alexa App on the phone to start interacting with the app and test it away! DynamoDB DyanmoDB can be accessed on AWS Management Console using the account number, username and password provided in the Devpost submission. Under search area, search for DynamoDB Make sure your region is set to US-East-2 Click on Tables on the left and CharityInfo on the right Click on Items to see the database entries Here is where you can see the charity information being stored Amazon Pay Amazon Pay can be accessed on Seller Central using the username and password provided in the Devpost submission. Select sandbox view upon login Click on Orders and Manage Transactions to see the transaction history Here is where you can see the donation payments being processed under a sandbox environment Flask App Relevant Elastic Beanstalk information can be accessed on AWS Management Console using the account number, username and password provided in the Devpost submission (same login info as DynamoDB). Search and find Elastic Beanstalk, and take note that it is hosted in US-East-1, unlike our other services The app is named "ForACauseFlaskApp", and the environment is named "flask-env" for that app The website is fully deployed at www.for-a-cause.net All the testing can be performed on the live website All the relevant documentation is available in our repository <div