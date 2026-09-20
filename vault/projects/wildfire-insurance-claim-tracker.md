---
slug: "wildfire-insurance-claim-tracker"
url: "https://devpost.com/software/wildfire-insurance-claim-tracker"
title: "Wildfire Insurance Claim Tracker"
hackathon: "Nosu AI Hackathon $11,300+ in prizes"
organization: "nosu"
winner: true
words: 758
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/disaster_emergency"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "substrate/document_pdf"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Wildfire Insurance Claim Tracker

> Streamline your wildfire insurance claims with easy tracking and secure document uploads.

[Devpost](https://devpost.com/software/wildfire-insurance-claim-tracker) · hackathon [[Nosu AI Hackathon -11-300- in prizes]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[disaster_emergency]] [[finance_payments]] [[supply_logistics]]
**substrate** [[document_pdf]] [[video_visual]] [[web_dom]]

**stack** css3, html, javascript

## Body

Inspiration The Wildfire Insurance Claim Tracker was inspired by the devastating impact of wildfires on families and communities. After seeing the challenges faced by victims trying to manage their insurance claims, I recognized the need for an organized way to track all items lost in a wildfire. My goal was to create an app that helps users easily document and manage the process of submitting their claims by keeping track of their lost items and their related details in one secure place. What it does The Wildfire Insurance Claim Tracker helps users keep a detailed log of items lost due to wildfires. By allowing users to enter key details such as the item name, description, and value, and upload relevant photos, the app provides an organized inventory that is easy to update and manage. Users can delete or update entries as needed, ensuring they always have an accurate and comprehensive list of items to submit with their insurance claims. The app also ensures that the data is saved even after the browser is closed, thanks to local storage functionality. How I built it I built the Wildfire Insurance Claim Tracker using HTML, CSS, and JavaScript for the front-end. The app's user interface was designed using simple HTML and CSS to make it clean and responsive. I used JavaScript to handle the functionality of adding, updating, and deleting items in the inventory. To handle image uploads, I used basic file handling in JavaScript, allowing users to select and display images associated with their lost items. The data is saved locally in the browser's local storage so that it persists even if the user refreshes the page or closes the browser. This ensures users don't lose their information and can come back to it later. To save the data locally, I used the browser's local storage API to persist the user's input even after the page is refreshed or closed. This ensures that users don’t lose their information and can come back to it later without needing to re-enter their data. Challenges I ran into Data Persistence: One of the key challenges I faced was ensuring that the user data remained intact even after refreshing or closing the browser. I solved this by using local storage to save the user's inventory. Handling File Uploads: Implementing a smooth file upload feature for photos was a bit tricky, especially when dealing with larger files. I had to make sure that the app only accepted specific file types and sizes. UI Consistency: Designing a simple and intuitive user interface while making sure it remained aesthetically pleasing was challenging. I had to carefully balance the app's functionality with its visual design to make sure users could easily interact with it. Accomplishments that I'm proud of I was able to create a fully functional inventory tracker where users can easily add, view, and delete items with photos. The app works seamlessly across browsers and devices, ensuring accessibility and convenience for all users. The data persistence feature, which saves user entries even after a page reload, works as intended and significantly enhances the user experience. The app’s design, while simple, is visually appealing and ensures users can navigate the tracker with ease. What I learned I learned a lot about managing state and data flow in React, as I initially tried using it for development, but later switched. In particular, dealing with local storage and understanding how to persist data on the front end gave me valuable experience in working with web applications. I also gained insights into user-centric design and how important it is to keep things simple and intuitive, especially for users in stressful situations like insurance claims after a disaster. Handling file uploads and ensuring the app only accepts valid files was a practical challenge that helped me dive deeper into JavaScript and the browser’s file API. What's next for Wildfire Insurance Claim Tracker Real-Time Collaboration: While this version doesn’t allow multiple users to collaborate in real-time, future versions may include a collaborative feature where multiple users can access and update the same inventory list. Cloud Storage: I’m considering integrating cloud storage solutions like Firebase to enable more robust data storage and synchronization across devices. Analytics and Reports: To further support users in their insurance claim process, I may add features like generating reports of their inventory or tracking the progress of their claims. Mobile App: I aim to expand the functionality of the tracker by developing a mobile version of the app, making it more accessible for users on the go. <div