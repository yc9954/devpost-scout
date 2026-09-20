---
slug: "qr-code-api"
url: "https://devpost.com/software/qr-code-api"
title: "Quick QR Code API"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 307
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "user/general_public"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Quick QR Code API

> Want to generate QR Code quicky on the go and save it on cloud ? The try this QR Code API.

[Devpost](https://devpost.com/software/qr-code-api) · hackathon [[The Postman API Hack]]

## Facets

**user** [[general_public]]
**substrate** [[structured_db]] [[video_visual]]

**stack** cloudinary, express.js, javascript, mongodb, node.js, postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what we learned
- what's next for qr code api

## Body

Inspiration While creating web applications, many times we need to generate QR Codes. There are many ways to generate the QR Codes, like using the modules and libaries available for that, or any thirparty API. But these takes time to generate the QR Code and doesn't allow us to retrieve it later if required. This gave me an idea what if an API is available which generate the QR Code and saves it also on the cloud. Then using the link provided we can get the QR Code via CDN directly into our web application and also delete the code. What it does The API upon recieveing a POST request with the text to be encoded into QR code generates an unique ID and generates the respective QR Code. Then it converts the QR Code into PNG format, renames it with the same as UID and saves on the Cloudinary. It gives back the respnse which consists of the UID and the link for the code. To get the QR Code from the UID we can send a GET request to the API which in response sends the public link of the code image available via CDN. To delete the QR Code from the cloud storage we can send a DELETE request to the API. How we built it I built it using Javascript running on NodeJS runtim. For the database, I have used MongoDB Atlas as NoSQL database and Cloudinary as the Image storage and CDN. The API is hosted on Heroku free tier. What we learned Working on this API project I learnt to create API and also how to test the API effectively using the Postman. What's next for QR Code API More features such as modifying the qr code so that link remains same, rate-limiting based on IP to prevent server overload. <div