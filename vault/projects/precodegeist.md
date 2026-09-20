---
slug: "precodegeist"
url: "https://devpost.com/software/precodegeist"
title: "Predictions for Jira"
hackathon: "Codegeist 2020"
organization: "Atlassian"
winner: true
words: 893
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "substrate/structured_db"
---

# Predictions for Jira

> Forge Jira app with Deep Learning to predict some properties of Jira issues

[Devpost](https://devpost.com/software/precodegeist) · hackathon [[Codegeist 2020]]

## Facets

**mechanism** [[retrieval_grounding]]
**substrate** [[structured_db]]

**stack** amazon-web-services, deeplearning, forge, jira, lambda, tensorflow, tensorflowjs

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for predictions for jira

## Body

How I built it (Part 1: get the data and train the neural network). How I built it (Part 2: Atlassian Forge & Jira). Use case 1. How I built it (Part 2: Atlassian Forge & Jira). Use Case 2. GIF Issues from Apache Project GIF CSV file with more than 100K Jira issues An user reads a Jira issue. An user creates a issue with "\p" (prediction) prefix. Issue created with "\p" (prediction) prefix. Issue type predictions, with tensorflow Issue priority predictions, with tensorflow Inspiration Is it possible to automatically fill in some of the fields for Jira's issues, based on the title of the issue? We can be more productive and avoid human errors if we do this automatically. Can we train a neural network with hundreds of thousands of issues to achieve this? Using Deep Learning to predict some properties of Jira issues, reading the summary of the issue. At this time, we will predict the type (bug or improvement) and priority of Jira issues (high, medium, low). What it does It predicts from the summary of a Jira issue, its type and priority. This prediction appears in the detail of the issue. Also, for users who prefer to use shortcuts, a trigger has been designed so that if the issue summary starts with "\ p", then a comment is automatically written to the issue with the prediction and the prefix "\ p" is deleted. This prediction is achieved thanks to a neural network that has been created and trained for this project, using Tensorflow. How I built it Part 1: get the data and train the neural network. First of all, I downloaded many real Jira issues projects, like apache projects ( https://issues.apache.org/jira ). After preprocessing the information, I created a CSV file with more than 100,000 real Jira issues. For each issue, we have its summary, type, priority, etc. Next, I've designed 2 neural networks with Tensorflow 2 and trained them to predict the type of an issue and its priority. I've done several experiments with different hyperparameters, up to over 75% accuracy with test issues. Afterwards, I exported the trained models so I can use them with TensorflowJS. This step is necessary because in the Forge FaaS (Function as a Service) I can execute code in javascript (node) but not code in pytyon (TensorFlow). However, I explain later that tensorflowjs didn't work in Forge FaaS and then I've fixed it with a workaround (AWS Lambda). Part 2: Atlassian Forge & Jira. Use Case 1 . An user reads a Jira issue. The “IssuePanel” of “Predictions for Jira” appears. If the predictions are cached in the issue property, the predictions are returned directly. If the predictions aren’t cached, the predictions are made in AWS Lambda functions created for this project. Part 2: Atlassian Forge & Jira. Use Case 2 . An user creates a Jira issue. He uses “\p” prefix, because he wants an automatic comment with the prediction. The "issue created" event triggers a function and checks “\p” prefix. The predictions are made in AWS Lambda functions. A comment is automatically published with the prediction, and the prefix "\ p" is removed. Challenges I ran into It is my first application for Jira, it has been a challenge :) Also, I have not used an existing neural network, but I’ve looked for actual Jira issue dataset (from apache opensource projects), I’ve preprocessed the dataset and I’ve trained 2 neural networks to predict specific properties of Jira issues: type and priority. The accuracy achieved is very good. TensorFlowJS didn’t work in Forge FaaS. “TextEncoder is not a constructor" error appeared during the deploy. As a solution, I did a workaround and setup TensorFlowJS with trained models on AWS, using AWS Lambda and AWS API Gateway. It has also been a challenge to cache the predictions in "Issue Properties" and use the Jira API to detect the "\ p" prefix in the summary and edit the summary. Accomplishments that I'm proud of I really think that deep learning is very useful in Jira. I am very proud to build a quality dataset, to train the networks to get very good results and to develop an application with Forge that is useful for work teams, because it reduces human errors and increases productivity. I am also proud of the workaround to be able to run tensorflowJS. Finally, I am proud of the idea of using a "\p" prefix in the summary, as a "shortcut" for advanced users. And very happy to complete the project before the deadline. What I learned I’ve learned to create applications with Forge for Jira. I’ve learned more about neural networks, and I’ve learned a lot about networks that work with text and I’ve practiced the "Word Embedding" method. I've also learned how to collect dataset and how to better pre-process data. What's next for predictions for jira In some scenarios it may be interesting that, some properties can be automatically filled in with the prediction of the neural network, when the user leaves theses properties empty. The neural network can be trained for specific Jira projects, so that it can even predict the person assigned to each issue. If the issue includes a "description", also use it for predictions. Be aware of the improvements in Forge, to be able to take advantage of them. <div