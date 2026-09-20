---
slug: "photosearch"
url: "https://devpost.com/software/photosearch"
title: "Galudy"
hackathon: "AWS Artificial Intelligence Hackathon"
organization: "Amazon"
winner: true
words: 513
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/retail_commerce"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Galudy

> an online fashion discovery platform powered by AI

[Devpost](https://devpost.com/software/photosearch) · hackathon [[AWS Artificial Intelligence Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[retail_commerce]]
**substrate** [[video_visual]] [[web_dom]]

**stack** amazon-web-services, angular.js, aws-batch, cloudformation, python, rekognition

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for galudy

## Body

Galudy Application Infrastructure Inspiration The idea was inspired by my company's (Scout24) summer festival party. I wore a Nigerian outfit and people complimented the outfit and asked where they could get it. I knew it would be hard for any none Nigerian to know the names of these kinds of attires so I decided to build some image recognition tool to address this. What it does It simply allows a user to do a visual search for any African attire he/she likes, then the solution responds with similar attires. User can then click on any outfit of interest and proceed to buy from the seller. We also added a discovery feature where users can like or dislike pictures for instant recommendations - just like Amazon.com/scout. How we built it We built the prototype in 3 days. We didn't want to have anything to do with model training likewise managing any servers. Since, I was already familiar with AWS ecosystem, I looked at the available AWS solutions that would fit the architecture sketch on my notepad and went on to build. We also ensure all infrastructure was deployed via Cloudformation using AWS Serverless Application Model. The application was developed in two parts The background job which scrapes external data and indexes AWS Rekognition image detection labels into elasticsearch for querying The API which is served via AWS API Gateway and AWS Lambda The user facing which is a static website hosted on AWS S3 with which user interacts with the API We make use of AWS Comprehend to extract keywords from user search request and before querying our search. We use AWS Translate to localize product details when a user views it Challenges we ran into Main challenges were: Nigerian outfits are very peculiar in design and image detection, hence a bit on non matching responses from AWS Rekognition. However, this didn't stop the solution from recommending similar items. To our surprise, it performed better than we expected. Although we built for African outfits, we didn't think of a wider reach in terms of more popular clothe types Getting more users on board Accomplishments that we're proud of The fact that we were able to come up with a working prototype in 3 days We ran some ads and we had over 3k users test the solution out The fact that we were able to scale with usage with zero upfront cost We have also expanded to western outfits We have both web and mobile versions of the application. Our mobile app (Android APK file) is available for download here What we learned Build serverless first Have a repeatable infrastructure and architecture Image recognition does not have to start with knowing deep learning Leverage cloud economies of scale provided by using managed services from AWS What's next for Galudy Making it available for other outfits in other regions (/) Turn in to the most popular visual shopping platform Create a business model around the solution Raise funding to expand Train custom models (tensorflow or MxNet or Gluon on AWS Sagemaker) to improve recommendations. <div