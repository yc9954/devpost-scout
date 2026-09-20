---
slug: "smart-checkout"
url: "https://devpost.com/software/smart-checkout"
title: "Smart Checkout"
hackathon: "AWS Marketplace Developer Challenge: ML Powered Solutions"
organization: "Amazon"
winner: true
words: 433
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/retail_commerce"
  - "substrate/video_visual"
---

# Smart Checkout

> Machine learning & computer vision work together to display personalized ads to customers at the grocery store.

[Devpost](https://devpost.com/software/smart-checkout) · hackathon [[AWS Marketplace Developer Challenge- ML Powered Solutions]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[retail_commerce]]
**substrate** [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** css, html, javascript, rekognition, sagemaker

## How they structured the write-up

- you're scanning your items at the self-checkout...
- improving self-checkout helps both businesses and customers.
- how does it work?
- see it for yourself!
- and that's not all...

## Body

Smart Checkout uses machine learning to display advertisements that are likely to interest you. The application uses Amazon Rekognition to extract visual info, and then passes that on to the propensity models. You're scanning your items at the self-checkout... ...when you see an advertisement about something you love. How did the machine know? It doesn't have access to your Instagram likes or your YouTube search history. The answer is: it simply guessed. Using only basic variables like your gender and age, machine learning models can guess what types of advertisements you would enjoy with surprising accuracy. And that's the principle behind Smart Checkout. Improving self-checkout helps both businesses and customers. As an ML-powered self-checkout system, Smart Checkout helps make everyone's shopping experience a little bit better. It extracts gender & age information about the user from the system's security camera, feeding it into several propensity models to determine which advertisements would resonate most with each shopper. As a result, businesses can promote products more effectively, and customers can see & purchase products they care about rather than randomly-chosen ones. This software doesn't require any new hardware, as it takes advantage of the security cameras that are already installed in most modern self-checkout systems. That way, business owners can focus on improving revenue by having their systems make smart guesses about their users' interests. How does it work? First, an image of you is taken from the security feed and sent to Amazon Rekognition , which uses computer vision image analysis to extract your gender and age. That information, along with your household income, is sent via POST request to the Amazon API Gateway , which is integrated with Amazon SageMaker , where the propensity models are hosted. The models return the probabilities that you are interested in different things, like fashion or sports. Based on those outputs, the system displays a personalized advertisement for you on the screen. See it for yourself! You can watch a brief demonstration & explanation of the system here . Furthermore, if you would like to deploy and test the application yourself, feel free to follow the instructions here . And that's not all... As I learn more, I want to add new features to this application, including: The ability to derive your household income from your checkout total or the average item price in your cart An option to tap the advertisement and instantly purchase it (to be shipped to your home or brought to you by an attendant) Integration with emotional analysis so the system can adjust the advertisements based on how calm you look <div