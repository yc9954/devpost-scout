---
slug: "ml-in-ml"
url: "https://devpost.com/software/ml-in-ml"
title: "AI-Powered Mortgage Advisor"
hackathon: "Hack to the Future 2020"
organization: "Finastra"
winner: true
words: 812
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "user/developer"
---

# AI-Powered Mortgage Advisor

> Using Machine Learning to Predict Mortgage Loan Approval -- a Loan Prediction Model beneficial to Applicants, Brokers and Lenders.

[Devpost](https://devpost.com/software/ml-in-ml) · hackathon [[Hack to the Future 2020]]

## Facets

**domain** [[finance_payments]]
**user** [[developer]]

**stack** flask, keras, machine-learning, python, tensorflow, vue.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what’s next for ai-powered mortgage advisor:

## Body

Loan Approved? (Y/N) Inspiration Imagine you are a mortgage broker using ExpertPro (a Filogix's mortgage application solution), about to submit a loan application to a lender on behalf of your client. But you're unsure if the loan request will be accepted or denied if you go ahead and submit your client’s application. Repeatedly sending applications is taxing for the system to process, and it would be time consuming for the lender to keep re-evaluating your applications. This scenario inspired our hackathon team to create a proof of concept for an AI-powered mortgage advisor, with the goal of advising mortgage brokers the chances of their mortgage application being accepted or denied by a lender, which will provide the mortgage applicants a faster turn-around for their application hence improve the efficiency of application process. Filogix is a Finastra company, which has been the technology hub of the Canadian mortgage industry for over two decades, offering secure and reliable software and solutions to mortgage brokers and lenders. Our open platform enables the effective management of the sales process from origination through underwriting, allowing mortgage professionals to seamlessly submit mortgage applications to our lender network from their choice of front-end systems, and for lenders to receive applications regardless of the broker’s platform of choice. What it does By leveraging data driven, machine learning technology, we aim to demonstrate a Proof of Concept to predict the probability of the application being approved by a Lender, via a simple button click from a Mortgage application system, for example Filogix’s ExpertPro. This change will bring at least 2 major benefits to existing mortgage application solutions: 1.Improve the efficiency of application process to better serve the applicant; 2. A faster turn-around for Applicant’s application. How we built it We used the Customer Loans and Demographics datasets from FusionFabric.cloud to train our model with specific features in these datasets and were able to train the model to output a “yes” or “no” with 91% accuracy. The accuracy of a model is determined after the model parameters are learned and fixed and no learning is taking place. Then the test samples are fed to the model and the number of mistakes the model makes are recorded, after comparison to the true targets. Then the percentage of misclassification, as known as accuracy, is calculated. We tried several loss functions to help improve model accuracy and achieved about 91%. We then created an API to consume our model using Flask, which we connected to a simple web-app containing a form made with Vue.js. When a user enters data into our form, the data is sent to the API, which processes it returning a status code of either “1”- the loan will probably be accepted, or a “0”- the loan would probably be denied by the lender. Challenges we ran into The biggest challenge we’ve run into is about the negative scenario /rejected case: the existing datasets at FFDC consist of 90%+ positive cases which made our model always gets positive/Yes result; we then reached out to Chirine (the Hackathon organizer), she immediately connected us to Adam (the head of AI and Machine Learning) who responded promptly to our email proving us with the useful link and information we need 😊…So Yue managed to make a synthetic datasets with both balanced positive data and negative data (50% for each), and re-trained the model, hence our model is able to work for both positive and negative scenarios . Accomplishments that we're proud of --From technology perspective, we have managed to train the model to output a “yes” or “no” with 91% accuracy; --From the business perspective, we have presented our hackathon idea to Filogix team and the business are very interested in it and provided very valuable feedbacks to hack team: Our idea is exactly what our customers have been asking for...!; Last but not the least, by leveraging the existing FFDC sample Datasets in our Model building process, our project scope is NOT limited to only Canadian Mortgage Market. What we learned In addition to Machine Learning expertise, we have learned, by our personal experience, the spirit of Hackathon: the passion for new ideas, new technologies; determination and teamwork, most important of all: Never give up! What’s next for AI-Powered Mortgage Advisor: To bring our proof of concept to the next step, we would require the use of production data to re-train our model and re-engineer our model’s features so it can output a more realistic prediction. We would do this by creating unique models for each lender, as different lenders have different requirements to grant a loan. There is a lot of potential with this POC. We believe our hack idea can provide mortgage brokers using ExpertPro with the right business intelligence at the right time to be able to work more efficiently and effectively which would deliver faster turn-around to the applicant. <div