---
slug: "falcon-pos-add-vision-and-speed-to-your-checkout"
url: "https://devpost.com/software/falcon-pos-add-vision-and-speed-to-your-checkout"
title: "Aisle - Visionary POS"
hackathon: "Square + Google AI Hackathon"
organization: "Square"
winner: true
words: 484
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/retail_commerce"
  - "user/patient_family"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Aisle - Visionary POS

> Our AI-powered POS visually identifies products to automates the checkout process. No barcodes, no touch, just swift precision.

[Devpost](https://devpost.com/software/falcon-pos-add-vision-and-speed-to-your-checkout) · hackathon [[Square - Google AI Hackathon]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[finance_payments]] [[health_clinical]] [[retail_commerce]]
**user** [[patient_family]]
**substrate** [[financial_record]] [[video_visual]]

**stack** html5, javascript, jquery, php, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for aisle pos

## Body

The web based point-of-sale app The power of Google Vision AI can detect your products and speak them aloud.. Important testing snacks. Inspiration In today's fast-paced retail environment, we've all faced the frustrations of self-checkout scanners. The time-consuming hunt for that elusive barcode, the multiple attempts to get the scanner to recognize it just right, and the resultant queues forming impatiently behind us. It's a universal struggle rooted in a simple problem: each product only has one specific spot that can be scanned. This bottleneck not only dampens the shopping experience but also hampers the efficiency of modern-day commerce. Aisle was born from the desire to eliminate this hurdle, streamlining the checkout process for a swifter, more user-friendly experience. What it does Our point of sale operates similarly to others. However, with Aisle Vision mode activated, the webcam on your laptop, tablet, or phone interacts with the web browser to automatically identify your most frequently sold products. No need for barcodes; simply present the product to the webcam from any angle, and it's instantly added to your order. Give the webcam a thumbs-up 👍, and the order is transmitted to the Square Terminal credit card reader, eliminating the need for any physical interaction with the point of sale. How we built it We're passionate about crafting no-code solutions, so we were inspired by the simplicity and robustness of [teachablemachine.withgoogle.com]. With it, sellers can effortlessly create and train a TensorFlow image model for their top-selling items, tailored to the exact environment they'll be scanned in. We created a video on how we did that here . We designed a user-friendly point-of-sale web application that allows sellers to import their product catalog through the Square Product API. This system also interfaces seamlessly with the Square Terminal via the Terminal API. With Aisle Vision activated, the webcam begins to identify familiar products, instantly adding them to the register. Additionally, leveraging the Google Speech-to-Text API, our system verbally announces the products detected by the image model. Challenges we ran into We needed to add empty and common staff background states to keep the script from attempting to interpret background items between scans. Square Terminal API is not available in Sandbox so you need live transactions to truly test the flow end-to-end. Accomplishments that we're proud of Aisle is impressively precise. It can discern the difference between two similar silver cans or distinguish between various Clif Bars. Aisle is swift. In a direct comparison with the Square Register using barcode scanning, Aisle's AI Vision identification is twice as fast. What we learned We had not worked with Google AI products in the past. Speech-To-Text and Media Pipe were impressively straight forward to learn and deploy. What's next for Aisle POS We would love to build out more features and potentially import product catalog photos automatically from the Square Product Catalog, to train image models automatically behind the scenes. <div