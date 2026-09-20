---
slug: "serverless-archi-fy-tool-for-aws-cloud-beginners-and-sales"
url: "https://devpost.com/software/serverless-archi-fy-tool-for-aws-cloud-beginners-and-sales"
title: "Archi-fy |Well-Architected Serverless Architecture Generator"
hackathon: "The PartyRock Generative AI Hackathon by AWS"
organization: "Amazon"
winner: true
words: 690
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/video_visual"
---

# Archi-fy |Well-Architected Serverless Architecture Generator

> Even with limited AWS knowledge, you can create serverless architecture diagrams, make AWS service selections, and estimate costs for your customers based on functional requirements.

[Devpost](https://devpost.com/software/serverless-archi-fy-tool-for-aws-cloud-beginners-and-sales) · hackathon [[The PartyRock Generative AI Hackathon by AWS]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[video_visual]]

**stack** amazon-web-services, partyrock

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for archi-fy | tool for aws cloud beginners and sales

## Body

Serverless Archi-fy GIF Logo GIF GIF Banner Inspiration Archi-fy is an inspiration for my personal story when I started the cloud journey, I used to ask solution architects about my designed solutions. And the answer was always "It depends" . After long frustration and hit & try on customers' workloads I learned how to design cost-optimised and performant solutions by using AWS services. Partyrock is a fun way of building low-code apps. When I heard of the hackathon and tried out partyrock by myself, my passion for creating Archi-fy urged me to develop the app. so here it is. Archi-fy empowers you to confidently design and sell serverless solutions on AWS, even with limited technical knowledge. What it does Archi-fy is a tool for cloud beginners and sales teams. Even with limited AWS knowledge, you can create serverless architectures for your customers. Simply input their functional requirements, and based on the AWS well-architected framework, Archi-fy will suggest: Required AWS serverless services: Get a tailored list of AWS services like Lambda, DynamoDB, and API Gateway to build your solution. Architecture diagram: Visualize how these services connect to form your application's backbone. Estimated cost: Understand the potential expenses associated with your architecture. Benefits: Fast and easy: Design serverless solutions quickly, even without deep AWS expertise. Customer-centric: Present clear proposals with architecture diagrams and cost estimates, tailored to your client's needs. Focus on solutions: Spend less time on architecture and more time understanding your customer's business. Who is it for? Cloud beginners or those new to AWS serverless. Cloud sales teams who want to create technical proposals for clients. App Capability After providing detailed functional requirements to Archi-fy, it will generate: Two lists of AWS services required for the Solution. Two solutions based on AWS best practices and AWS well-architected framework. Price estimation of both solutions. Architecture diagrams for both solutions. Archi-fy Assistant for architecture modification and other assistance. How we built it Tried out numerous prompts based on prompt engineering documentation provided in the resources. Partyrock has built-in Foundational Models (FMs) for text, images, and chat bot which is helpful even for naive cloud enthusiasts and developers. Challenges we ran into Though partyrock has all initial and sufficient Foundational Models (FMs) in place to generate a low/no-code app in minutes. Yet some limitations should be addressed to make it faster and more fun for app generation. Image Limitations Challenge In my app I tried to generate an architecture diagram based on the two solutions generated in response to customer functional requirements. For now, partyrock supports Stable Diffusion XL for image generation, which is awesome for generating images on predefined image generation "Style Presets" but it lacks the capability of generating architecture diagrams and user flow. I tried out different prompts like Generate AWS serverless architecture diagram for [AWS Serverless Services List 2] Added context for Prompt: Generate AWS serverless architecture data flow diagram for [Serverless Solution 1 Pricing] and [AWS Serverless Services List 1] . Added instructions for Prompt: Pretend you are an AWS solutions architect and generate AWS serverless architecture diagram based on [Serverless Solution 1 Pricing] and [AWS Serverless Services List 1]. Generate AWS serverless architecture data flow diagram based on [Services List 2] and [Cost Estimate 2] but I guess it needs more prompt details or refinement. or might need some other FM for generating architecture diagrams. Accomplishments that we're proud of Archi-fy is an accomplishment Learning prompt engineering and how to generate responses based on detailed prompts ( having user inputs, context, and instructions). Built an app for beginners under the category of Interactive Learning Experience. What we learned Learning in a fun way is the best way to learn. Through this hackathon, I learned: Prompt engingeeing, Foundational Models supported by partyrock (their usage and limitations) Out-of-the-box app generation with low code ;) What's next for Archi-fy | Tool for AWS Cloud Beginners and Sales A lot can be done to refine the Archi-fy App. Accurate and detailed architecture diagrams according to the proposed solutions. Export features for diagrams as well as text in PNG and doc formats for easy sharing. Archi-fy assistant could be more helpful. <div