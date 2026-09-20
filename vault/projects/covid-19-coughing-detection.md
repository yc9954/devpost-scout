---
slug: "covid-19-coughing-detection"
url: "https://devpost.com/software/covid-19-coughing-detection"
title: "Covid-19 Coughing Detection"
hackathon: "AWS Deep Learning Challenge"
organization: "Amazon"
winner: true
words: 556
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/video_visual"
---

# Covid-19 Coughing Detection

> Project Covid-19 Coughing Detection aims to prescreen Covid-19 patients through Smartphone-Recorded coughs using Artificial Intelligence.

[Devpost](https://devpost.com/software/covid-19-coughing-detection) · hackathon [[AWS Deep Learning Challenge]]

## Facets

**domain** [[education]] [[finance_payments]] [[health_clinical]]
**user** [[patient_family]]
**substrate** [[video_visual]]

**stack** amazon-web-services, lambda, python, s3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for covid-19 coughing detection

## Body

Inspiration It's all started when the Vietnam covid cases rise sharply and Dr Nguyen Dinh Son, resided in DaNang, Vietnam, wanted to dive into the world of Machine learning and was stuck on what project he should apply his new found knowledge. Due to the low supply of PCR test kit and the overloaded hospital, many patients had to stay at home and were only brought to the hospital when their health deteriorated and their lungs have been severely damaged. It was getting hard for people at frontline to manage their patients and determine who requires immediate attention. Many lives were lost due to shortage of oxygen tank and equipments. Covcough machine learning model was born right the middle of the pandemic. What it does Covcough DOES NOT replace PCR test. Although not intended to be a reliable diagnostic system for COVID-19 that can replace PCR or RAT tests, covcough can be used for monitoring of people on a very large scale, in a short period of time (e.g. at university, schools, supermarket). This application is still highly experimental; however, with enough training examples it can be tuned to a reasonable performance, and potentially become a valuable tool for disease screening. How we built it The model was first trained on Google Colab and after hearing about Dr Son's idea, the results of his test on real patients and, San Tran joined the team to built a simple web application hosted on github page with low cost API hosted entirely on AWS to evaluate users' recorded coughing sound. Challenges we ran into In term of machine learning, Dr Son identified that the sample set he obtained from AI competition was quite small and it was an not a simple task to ask the people working at frontline to collect sick patients' coughing sound samples. Due to this reason, Dr Son came up with an idea to introduce background noises to all existing samples and multiply his training data to reasonable amount. AWS lambda size limit was one of the problem we ran into when building the backend but this was easily overcome by pushing a custom ECR image and use it for the processing lambda function. Due to joining this competition late and unable to convert our model to use Horovod library and train the model in distributed fashion, we decided to pivot and used our AWS credit to train 8 different models, each in single thread but with different hyperparameters. This way we can tune our training code better. Accomplishments that we're proud of Dr Son received honorable mention for the paper related to this research last year at IEEE. Being able to handle thousands of connections without a hiccup or spending much as our application runs far below AWS free tier. What we learned A lot of machine learning for Dr Son and how to build serverless application in AWS for San Tran What's next for Covid-19 Coughing Detection We are putting our code out there as open source project to show others how they could do the same. Dr Son is also in the process of getting hospitals to help with getting coughing samples from sick patients to help him train the model better. Our aim is to help healthcare system and if this app even helps 1 person, it's a success. <div