---
slug: "save-earth-with-celo"
url: "https://devpost.com/software/save-earth-with-celo"
title: "Save Earth with Celo"
hackathon: "Celo's Make Crypto Mobile Hackathon"
organization: "Celo"
winner: true
words: 446
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "user/researcher"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Save Earth with Celo

> Create entries of newly discovered, rare, or near-extinct life discoveries on earth with the help of `AI` 🤖 for the world to see and get rewards for prioritized discoveries.

[Devpost](https://devpost.com/software/save-earth-with-celo) · hackathon [[Celo-s Make Crypto Mobile Hackathon]]

## Facets

  <sub>weak: finance_payments</sub>
**user** [[researcher]]
**substrate** [[structured_db]] [[video_visual]]
  <sub>weak: document_pdf</sub>

**stack** azure, celo-contractkit, datastax, google, netlify, react

## How they structured the write-up

- inspiration
- for the joy of a new discovery!!!
- what it does
- how we built it
- - the data is then stored in the database (blobs go the blob container; documents go to nosql)
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for save earth with celo

## Body

Architecture Details Inspiration For the joy of a new discovery!!! What's a better way to describe the beauty of life on earth than with a simple picture? I wanted to create a project that could create awareness on rare, unique, endangered plants and animals. It's vital that people understand the impact we have on the natural world around us with respect to extinction of other species. What it does It allows any one on earth or beyond 👽 😉 To feature their discovery! And with the help of AI, The app can help detect high priority images, add it to a special collection which the admin can easily utilize. It also creates a community for we, the environmental/nature freaks, NGOs, scientists, researchers, explorers, adventurers of the world who care about nature... etc... To come together and feature, discuss something weird you saw from some where on earth and save it. Hence, Save-Earth get it... 😁😊😓😓 The app, with the help of the Custom Vision Prediction API was able to detect and then classify images returning a probability percent and give responses based on the probability. Reward users with CELO tokens when a prioritized discovery is found How we built it A user fills the form at the upload page, includes an image but first, sends the image data to Custom Vision AI If the image is detected by AI, If it is prioritized, it is sent to a blob container. Prioritized images have at least +99.5% accuracy allowance. The CELO reward is then released User receives response and can continue with uploading data - The data is then stored in the database (Blobs go the Blob container; documents go to NoSQL) Similar step involves creation of Image Datasets. Anyone can create dataset (provided they have admin access) but only Root Administrator can train the customvision AI. This was put to in place to prevent common mistakes like: Using bad data Overfitting the model Using unbalanced data Challenges we ran into Accomplishments that we're proud of The app was able to automatically store high priority images that were detected by the Custom Vision AI by creating and saving it into Blob Containers. It was able to communicate with the blockchain accept donation and give rewards What we learned I learned a lot from the Celo community What's next for Save Earth with Celo It was so much fun implementing CELO contracts to this project. The vision ahead is to allow creation of NFTs for user discoveries While the world slowly transitions in to web3 cloud providers cloud providers are relied on for blob storage. In the future images will be added to the IPFS network instead <div