---
slug: "tashopping"
url: "https://devpost.com/software/tashopping"
title: "TAShopping"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 621
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/retail_commerce"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# TAShopping

> Tool Assisted Shopping; Accelerate your shopping to robot-like efficiency

[Devpost](https://devpost.com/software/tashopping) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[retail_commerce]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** amazon-web-services, firebase, gemini, google-cloud, lambda, reflex, s3, selenium

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tashopping

## Body

Web UI Inspiration Food is a basic human need. As someone who often finds themselves wandering the aisles of Target, I know firsthand how easy it is to get lost among the countless products and displays. The experience can quickly become overwhelming, leading to forgotten items and a less-than-efficient shopping trip. This project was born from the desire to transform that chaos into a seamless shopping experience. We aim to create a tool that not only helps users stay organized with their grocery lists but also guides them through the store in a way that makes shopping enjoyable and stress-free. What it does TAShopping is a smart grocery list app that records your grocery list in an intuitive user interface and generates a personalized route in (almost) any Target location across the United States. Users can easily add items to their lists, and the app will optimize their shopping journey by mapping out the most efficient path through the store. How we built it Data Aggregation: We utilized Selenium for web scraping, gathering product information and store layouts from Target's website. Object Storage: Amazon S3 was used for storing images and other static files related to the products. User Data Storage: User preferences and grocery lists are securely stored using Google Firebase . Backend Compute: The backend is powered by AWS Lambda , allowing for serverless computing that scales with demand. Data Categorization: User items are classified with Google Gemini API: AWS API Endpoint provides a reliable way to interact with the backend services and handle requests from the front end. Webapp: The web application is developed using Reflex , providing a responsive and modern interface for users. iPhone App: The iPhone application is built with Swift , ensuring a seamless experience for iOS users. Challenges we ran into Data Aggregation: Encountered challenges with the rigidity of Selenium for scraping dynamic content and navigating web page structures. Object Storage: N/A (No significant issues reported) User Data Storage: N/A (No significant issues reported) Backend Compute: Faced long compute times; resolved this by breaking the Lambda function into smaller, more manageable pieces for quicker processing. Backend Compute: Dockerized various builds to ensure compatibility with the AWS Linux environment and streamline deployment. API: Managed the complexities of dealing with and securing credentials to ensure safe API access. Webapp: Struggled with a lack of documentation for Reflex , along with complicated Python dependencies that slowed development. iPhone App: N/A (No significant issues reported) Accomplishments that we're proud of Successfully delivered a finished product with a relatively good user experience that has received positive feedback. Achieved support for hundreds of Target stores across the United States, enabling a wide range of users to benefit from the app. What we learned We learned a lot about: Gemini: Gained insights into effective data aggregation and user interface design. AWS: Improved our understanding of cloud computing and serverless architecture with AWS Lambda. Docker: Mastered the process of containerization for development and deployment, ensuring consistency across environments. Reflex: Overcame challenges related to the framework, gaining hands-on experience with Python web development. Firebase: Understood user authentication and real-time database capabilities through Google Firebase. User Experience (UX) Design: Emphasized the importance of intuitive navigation and clear presentation of information in app design. Version Control: Enhanced our collaboration skills and code management practices using Git. What's next for TAShopping There are many exciting features on the horizon, including: Google SSO for web app user data: Implementing Single Sign-On functionality to simplify user authentication. Better UX for grocery list manipulation: Improving the user interface for adding, removing, and organizing items on grocery lists. More stores: Expanding support to additional retailers, including Walmart and Home Depot, to broaden our user base and shopping capabilities. <div