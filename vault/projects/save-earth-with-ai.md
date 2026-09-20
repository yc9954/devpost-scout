---
slug: "save-earth-with-ai"
url: "https://devpost.com/software/save-earth-with-ai"
title: "Save Earth With Azure AI"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 609
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Save Earth With Azure AI

> With the power of AI, help create and *save* entries of newly discovered, rare, or near-extinct life discoveries on earth for the world to see!

[Devpost](https://devpost.com/software/save-earth-with-ai) · hackathon [[Azure AI Hackathon]]

## Facets

**mechanism** [[sensor_fusion]]
**user** [[researcher]]
**substrate** [[document_pdf]] [[structured_db]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** azure, azure-blobclient-api, azure-custom-vision, css, google-geocoder-api, html, javascript, mongodb, netlify-cli, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for save earth with azure ai

## Body

SaveEarth Architecture Home Page Custom Vision UI Inspiration For the joy of a new discovery!!! What's a better way to describe the beauty of life on earth than with a simple picture? I wanted to create a project that could create awareness on rare, unique, endangered plants and animals. It's vital that people understand the impact we have on the natural world around us with respect to extinction of other species. What it does It allows any one on earth or beyond 👽 😉 To feature their discovery! And with the help of AI, The app can help detect high priority images, add it to a special collection which the admin can easily utilize. It also creates a community for we, the environmental/nature freaks, NGOs, scientists, researchers, explorers, adventurers of the world who care about nature... etc... To come together and feature, discuss something weird you saw from some where on earth and save it. Hence, Save-Earth get it... 😁😊😓😓 It allows any one to send image datasets to custom vision for training. How we built it Save_Earth_AI Architecture 👇 A user fills the form at the upload page, includes an image but first, sends the image data to Custom Vision AI If the image is detected by AI, It is prioritized and sent to a blob container User receives response and can continue with uploading data The data is then stored in the database (Blobs go the Blob container; documents go to NoSQL) Challenges we ran into Gathering the right image datasets was almost a nightmare. Getting the right datasets: I found out the hard way that the images required for training were actually rare, unique or nearly extinct...😉. After scouring the internet for suitable images for rare animals, like the White Bengal Tiger , to build and train a model; I faced challenges such as Maintaining a uniform datasets since such image datasets were mostly rare or insufficient Time consuming process of checking if images were free to use or met specification. Ensuring that the images were diverse enough. Had to Settle: So I had few opportunities to train images for rare species and I had to settle for more common images such as bird species (e.g. parrot) to train the AI models. AllUser Access Restriction I discovered that allowing access to all users to train the model through the frontend would have been costly both financially and data quality in the sense that not all users could easily identify the right image datasets to use and may require supervision. Accomplishments that we're proud of The app, with the help of the Custom Vision Prediction API was able to detect and then classify images returning a probability percent and give responses based on the probability. The app was able to automatically store high priority images that were detected by the Custom Vision AI by creating and saving it into Blob Containers. It also allowed people given admin access to tag and send image datasets for training. What we learned Custom Vision: The first time I ever used custom vision was about 4weeks ago and it's amazing how useful and easy to learn it is. I was able to integrate it to the app thanks to the following resources. Cognitive Services' Custom Vision Cognitive Services Quick Start Azure Blob Container: I also learned how to utilize blob containers to easily store files and create logically isolated containers. BlobStream Azure Samples BlobServiceClient class What's next for Save Earth With Azure AI To see the feasibility of implementing Azure IoT Edge with smart wearables in a case of tracking the progress of rare discovered animals. Enterprise Scalability for production. <div