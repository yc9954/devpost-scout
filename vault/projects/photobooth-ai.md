---
slug: "photobooth-ai"
url: "https://devpost.com/software/photobooth-ai"
title: "PhotoBooth AI"
hackathon: "2019 Developer Circles from Facebook Community Challenge"
organization: "Facebook"
winner: true
words: 623
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# PhotoBooth AI

> A web photo booth that awards points when it detects smiles and a charity's logo to encourage folks to promote charities on social media.

[Devpost](https://devpost.com/software/photobooth-ai) · hackathon [[2019 Developer Circles from Facebook Community Challenge]]

## Facets

**mechanism** [[vision_ocr]]
**substrate** [[video_visual]] [[web_dom]]

**stack** azure, azure-custom-vision, azure-face, azure-functions, canvas, cdn, css3, html5, javascript, webcam

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for photoboothai

## Body

Landing page Capture screen Detected smile and logos Logo rejected because, although it is similar, it is the wrong one Tagging the placeholder logo on my training images in the Custom Vision Portal Inspiration Reading about social media influencers and thinking about how to "gamify" promotion of charities. What it does Allows users to take a picture of themselves smiling with the logo of a charity and gives them a score depending on if they are smiling and the charity's logo is present in the photo. I didn't have permission to use a real charity's logo so I used a placeholder one for now. In practice the logo might be on the user's t-shirt, a mug, etc. How I built it I built the website in Visual Studio Code. It uses vanilla HTML/CSS/JavaScript. The site uses getUserMedia to get the user's webcam video and pushes it over to canvas where I can draw annotations. Here is how I built my custom vision model: I edited the placeholder logo by inverting it (black print on white background and vice versa) and changed the color to red on another variation. I printed out the different variations of the placeholder logo and some incorrect logos to indicate what shouldn't be tagged. I took about 90 photos of the logos in different contexts (I.e. on a chair, me holding them, my kids holding them, etc). In some cases I mixed in incorrect logos. I batch resized the photos to get them under the 4 meg limit and uploaded them all to the Azure Custom Vision portal. Using the Custom Vision portal, I tagged all my photos by outlining where the logo was and then clicked the train button. The tagging process is pretty quick and easy. :) The resulting model/API is not only able to consistently spot the logo in a photo but also scores the prediction probability on incorrect logos low enough so I can easily filter them out. Here is the behind the curtain process when you take a photo: It calls an Azure function to get a shared access signatures (SAS) url that will allow the user to upload/write the image from the browser. The frame is then upload to the SAS url. Another Azure function (analyzeimage) is called and the UUID of the photo is passed along so it can find the image in storage. The analyzeimage function gets an SAS url to will allow Azure cognitive services to read/get the image. The analyzeimage function then calls the Face and Custom Vision apis passing in the SAS url and returns the data to the user's browser. Rectangles are drawn on the qualifying smiles and logos using the returned data and the results are scored and displayed to the user. Challenges I ran into I am having some performance issues with the Azure functions. I think they take a while to cold start if they haven't been used in a bit. I will look into this. Accomplishments that I'm proud of I am super happy the logo detection works so well. Microsoft Custom Vision is super easy to use relative to the Jupyter Notebook approaches I have tried in the past and the accuracy of the object detection is great. What I learned Setting up file uploads from the browser and trying to make it relatively secure on Azure is tough. Azure Custom Vision is probably the best kept secret in the machine learning world. What's next for PhotoBoothAI First some performance fixes. After that I have a few ideas including user accounts, authentication, badges/trophies/loyalty points, and easy social media share options. Face API could be used to recognize known influencers. Azure image moderation can be used to detect offensive images. Commercial applications. <div