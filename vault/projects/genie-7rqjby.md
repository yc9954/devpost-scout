---
slug: "genie-7rqjby"
url: "https://devpost.com/software/genie-7rqjby"
title: "Genie"
hackathon: "AWS Graviton Hackathon"
organization: "Amazon"
winner: true
words: 407
team_size: 6
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Genie

> Deep Learning powered image credibility checker

[Devpost](https://devpost.com/software/genie-7rqjby) · hackathon [[AWS Graviton Hackathon]]

## Facets

**mechanism** [[cross_origin_web]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** amazon-ec2, amazonelasticip, chromeextension, django, fetchapi, javascript, pytorch, rest

## How they structured the write-up

- inspiration
- what it does
- how we built it
- deployment
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for genie

## Body

Approach logo GIF Result Inspiration CGI (Computer Generated Imagery) which is the use of computer graphics in art and media. Many 2D and 3D visualizations can be done using CGI. It is an leading edge technology in media. But it has the same level of menace to the society. The variation between the the CGI and standard images is minute which helps criminals to to cheat and harass others. What it does The chrome extension takes input the cynical images and makes prediction using the pretrained model. The result comprises of two components: Photographic confidence Tampered confidence How we built it We have fabricated a CNN and trained it on several image datasets containing both tampered and non tampered images. The CNN model with least generalization error is chosen and saved for transfer learning and implemented for faster processing, therefore the accuracy and time efficiency is achieved. Using EC2 instance for hosting the Pre-trained model and API call . From chrome extension, through API call the input image passed and the image confidence is revealed in % Deployment The entire magic happens in the PyTorch Convolutional Neural Network model which is made suitable for inference using transfer learning. The pretrained model is put into action using a django server hosted on the all-powerful T4G (small) instance powered by AWS Graviton processor's. Since model works by performing CPU based inference, we thought that the inference time might be long. The powerful Graviton processor proved us wrong by sending responses in less than a second (may vary based on the user's bandwidth). Deployed on - link . Microsoft Edge link - link Mozilla Addons Store Link - link Challenges we ran into While installing the required libraries, installation of PyTorch requirements was not compatible with the products requirements. For biniding the our custom domain and AWS EC2 instance for single IP address for the our domain, we used Amazon elastic IP for accquiring SSL certifications. Accomplishments that we're proud of Hosted successfully in AWS With a positive result, we have successfully hosted our extension in Microsoft Edge Add-ons store and Mozilla add-ons What we learned To integrate Google extension with Hosting website AWS EC2. To host a pretrained model in AWS EC2 instance. What's next for Genie Planned to refine our model for instant result by racking up more sample dataset and pondering to incorporate with the deep fake detection algorithm for a powerful system for image falsification. <div