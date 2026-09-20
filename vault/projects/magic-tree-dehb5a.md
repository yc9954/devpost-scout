---
slug: "magic-tree-dehb5a"
url: "https://devpost.com/software/magic-tree-dehb5a"
title: "Magic Tree"
hackathon: "Amazon Raise-up Buildathon"
organization: "Amazon"
winner: true
words: 776
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "domain/finance_payments"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# Magic Tree

> Make Fundraising "Fun"raising ! Engage and excite your donors by glowing a light on the Magic Tree instantly after they donate.

[Devpost](https://devpost.com/software/magic-tree-dehb5a) · hackathon [[Amazon Raise-up Buildathon]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]]
**domain** [[finance_payments]]
**substrate** [[document_pdf]] [[web_dom]]

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for magic tree
- try it out

## Body

The Solution Donation Page: Magic Tree and Fundraising Goal Progress Donation Page: Donate with Amazon Pay Donation Page: Live Streaming Video Conferencing and Magic Tree Inspiration Most non-profits have online presence and solicit donations from a donation page. According to a 2020 M+R Benchmarks study (ref 1.0), the average conversion rate of the donation page is merely 22%. The low conversion rate is attributed to lack of donor engagement. We wanted to develop a solution that helps non-profits drive up donor engagement and make fundraising fun and easy for the donors and non-profits alike. ref 1.0 : https://www.mrbenchmarks.com/data/web-engagement What it does This solution makes fundraising more effective. "Magic Tree" is a smart device in the shape of a tree with LEDs installed. A new LED lights up with every donation. A non-profit can live stream their Magic Tree on their fundraising page. Donors get excited about making a donation to see the Magic Tree light up. This drives more users to donate. Magic Tree can also be lit up when a customer buys merchandize through the "Magic Tree" Alexa skill. In addition, non-profits can broadcast their fundraising event through a video conference which is streamed live and embedded on their fundraising/donation webpage. This enables them to showcase their work and solicit donations. On the fundraising page, an "Amazon Pay" button allows donors to instantly donate with the payment method tied to their Amazon account. "Amazon Pay" is also used by the "Magic Tree" Alexa Skill for conveniently making order payments via voice. How we built it Magic tree is a NodeMCU based IoT device with 10 LEDs. This device is registered on AWS IoT Core, and we use AWS MQTT server to allow applications to interact with it. The device is programmed to light up a new light every time a message on a particular topic (inTopic) is published. The WebRTC video conferencing solution is based on an open source video conferencing software - Jitsi. The solution is hosted on AWS EC2. The live streaming of the conference to YouTube is enabled by another software known as Jibri that is hosted on another EC2. The YouTube live stream is embedded into the fundraising page. An "Amazon Pay" button was generated and embedded into the donation page ( https://www.dillilabs.com/donate ). The redirect url was configured to be the donation page. The donation page gets a callback upon a successful payment at which point it invokes the REST APIs to signal the AWS MQTT Server to light up the Magic Tree. A multi-modal Alexa skill was developed that integrates with Amazon Pay and Alexa Presentation Language (APL) to allow a user to enlist the products, purchase them and to open the Magic Tree URL on the browser of the video enabled Alexa device. The order confirmation e-mail is sent via AWS SES. The Alexa skill leverages AWS S3 to store product list. The current count of lights on the Magic Tree is saved in AWS DynamoDB. Two REST APIs (using AWS API Gateway) and AWS Lambda functions are built to fetch the count and to increment it. The progress bar showcasing the goal tracker on the donation page leverages these two REST APIs. The donation page ( https://www.dillilabs.com/donate ) is a Wordpress page that uses HTML, JS and CSS on the client side and PHP on the server side to integrate the solution. Challenges we ran into We wanted to open a URL using the Amazon Alexa skill on a video enabled Alexa device. Apparently, its not supported. So, we worked around it by using an APL document to have a button that opens the URL in the browser once the user taps it. We wanted to embed "Donate with Amazon Pay" but apparently, its enabled only for registered 501c3 Non-profits. So, we worked around by embedding the regular "Amazon Pay" button. Accomplishments that we're proud of Seeing a physical device being controlled seamlessly by multiple remote application. An end to end selling and fundraising platform What we learned AWS IoT Core provides seamless and secure PUB-SUB integration Integrating Amazon Pay in an Alexa skill Physically assembling and programming an IoT device Sending e-mail wih AWS SES Live Streaming a video conference What's next for Magic Tree We want to deploy Magic Tree on as many non-profit donation pages and drive up their conversion rates. We want to upgrade the EC2 instance hosting our video conference in order to support multiple simultaneous conferences at any given time. The prototype uses 10 LEDs. These would be replaced by WS2812B Individually Addressable RGB LED strips to add visual effects and scale infinitely. Try it out www.dillilabs.com github.com <aside class="large-3 columns"