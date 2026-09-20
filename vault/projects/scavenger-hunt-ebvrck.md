---
slug: "scavenger-hunt-ebvrck"
url: "https://devpost.com/software/scavenger-hunt-ebvrck"
title: "Scavenger Hunt"
hackathon: "Amazon Alexa Skills Challenge"
organization: "Amazon"
winner: true
words: 684
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Scavenger Hunt

> Play the classic game using your Alexa and mobile phone. Image recognition software in the cloud tracks progress.

[Devpost](https://devpost.com/software/scavenger-hunt-ebvrck) · hackathon [[Amazon Alexa Skills Challenge]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[developer_tools]]
**substrate** [[video_visual]] [[web_dom]]

**stack** amazon-alexa, amazon-dynamodb, amazon-web-services, aws-lambda, aws-rekognition, javascript, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for scavenger hunt

## Body

Game Goals Example of Website Inspiration I've always loved to play scavenger hunt with my family and friends. With all of the advances in artificial intelligence, I started to wonder - how could technology enhance the game that has been around for generations? What it does There are two pieces to this game. First is an Alexa Skill called Scavenger Hunt . When initially loaded, instructions are given to the user on how to play the game, and two pieces of information are given - a four digit game code, as well as a set of ten items to go find. A timer is initiated that gives the user one hour to complete the "mission", to capture and upload photos of the items. Second is a companion website called scavengerskill.com . This is used to upload photos of the objects that are provided by the Alexa skill, ideally from a mobile device that has a camera. The game code is provided as part of the upload, which enables this to be a team activity versus just a single player. Once the images are uploaded, they are scanned, and matched back to the ten items that were read by Alexa. At any time the user can go back to the Alexa skill to get a game update. The skill will check to see what images have been uploaded for the particular game code, and compare back to the original set given at the onset. It's using image recognition software in the background to determine what is in the actual photos. How I built it The Alexa skill has been published to the Amazon store, and can be found here . It makes extensive use of SSML to merge together short sound clips with the Alexa voice. The skill is written in nodeJS, and hosted on Amazon Lambda. The sound clips are stored in the Amazon S3 object storage service. Here's the interaction between Alexa and the AWS services. The website is hosted on AWS, and uses a javascript library called formidable that enables images to be uploaded from a mobile device to an EC2 instance, then to an AWS S3 bucket. The backend is a serverless framework, and gets driven by the event of images loading into the S3 bucket. A Lambda function invokes the AWS Rekognition service to scan the image, and record which items have been found in a AWS DynamoDB table. This is then made available to the Alexa skill when the user checks back in for a status update. Here's how it all ties together with the different services. Challenges I ran into Image recognition is still maturing, so it was important to test out actual scenarios of different objects versus just picking things that were around me. Some common items were difficult to do image matching, for example a fork, scissors, and cereal were all items that I couldn't reliably get the service to recognize. Accomplishments that I'm proud of The game was published on the Alexa platform in both the US & UK, and is being actively used. It's fun to create a game like this that others can enjoy, and many have completed the challenge of finding ten objects in under an hour! The voice user experience is really solid. It demonstrates how flexible the Alexa SDK is, and how advanced of interaction you can create for users. In addition to the Alexa voice, the skill plays sounds and incorporates one of the voices from the new Polly service. What I learned Mixing together sounds and voice using SSML improved the gameplay, and was great to learn. This is not just a programming challenge, rather it also includes sound editing. I also used the new AWS-Polly service for the first time to record some short audio clips of a "partner" for Alexa that has an English accent. What's next for Scavenger Hunt I'm tracking usage of it, and based on analytics, adjusting the parameters of the game. As the image recognition software improves, I will be adding more items that can be randomly selected for the game. <div