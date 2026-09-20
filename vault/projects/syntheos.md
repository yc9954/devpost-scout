---
slug: "syntheos"
url: "https://devpost.com/software/syntheos"
title: "Syntheos"
hackathon: "brainrot jia.seed hackathon ($5,772) in prizes "
organization: "audrey chen host"
winner: true
words: 694
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Syntheos

> Syntheos optimizes social media posts for better engagement using PearAI. It analyzes content to provide actionable suggestions, helping content creators and marketers boost their presence.

[Devpost](https://devpost.com/software/syntheos) · hackathon [[brainrot jia.seed hackathon -5-772- in prizes]]

## Facets

**substrate** [[document_pdf]] [[sensor_telemetry]] [[structured_db]]

**stack** firebase, gemini, github, javascript, pearai, react, tailwindcss, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- track
- what's next for syntheos

## Body

Syntheos: Social Media Engagement Optimizer Inspiration The inspiration for Syntheos came from the realization that creating engaging social media content can be challenging. Many users struggle to understand what makes a post successful and how to improve their content to increase engagement. We wanted to create a tool that simplifies this process, making it accessible to everyone tailored for twitter. What it does Syntheos is an innovative tool designed to help users optimize their social media posts for better engagement. By leveraging the power of Gemini AI, Syntheos analyzes post content to provide actionable suggestions for improvement. Whether you're a content creator, marketer, or just looking to boost your social media presence, Syntheos ensures your posts reach their full potential. How we built it Technology Stack Frontend: React.js for building the user interface. AI: Gemini AI for content analysis and generating insights. Database: Firebase Firestore for storing user data and history. Authentication: Firebase Authentication for user sign-up and login. Key Features User Authentication: Users can sign up or log in using Firebase Authentication. User IDs (UIDs) are generated and used to track user history. Post Content Analyzer: Users can paste their post content into a text area. The content is analyzed using Gemini AI to provide engagement metrics, suggested improvements, hashtag recommendations, and a recommended post format. User History: User history is stored in Firestore, mapped to their UID. Each user action (e.g., signing up, logging in, analyzing a post) is recorded in an array within the user's document. Implementation Steps Set Up Firebase: Initialized Firebase and Firestore in the project. Configured Firebase Authentication for user sign-up and login. Backend Development: Created API endpoints using Node.js and Express to handle user authentication and post content analysis. Integrated Gemini AI to analyze post content and generate insights. Frontend Development: Built a user-friendly interface using React.js. Created forms for user input and displayed analysis results in a structured format. Data Storage: Stored user history in Firestore, ensuring that each user's actions are recorded and can be retrieved for future analysis. Challenges we ran into AI Integration: Integrating Gemini AI required careful handling of API requests and responses to ensure accurate analysis and insights. Data Handling: Ensuring that user data is stored securely and efficiently in Firestore, while also handling potential errors and edge cases. User Experience: Designing a user-friendly interface that is intuitive and easy to use, while also providing detailed and actionable insights. Error Handling: Implementing robust error handling to catch and log any issues that arise during the analysis process. Accomplishments that we're proud of Successfully integrated Gemini AI to provide accurate and actionable insights on social media content. Created a user-friendly interface that makes it easy for users to input their content and receive feedback. Implemented secure and efficient data handling using Firebase Firestore. Overcame challenges related to AI integration, data handling, and user experience to create a robust and effective tool. What we learned Throughout the development of Syntheos, we learned a lot about: AI Integration: How to effectively integrate AI models like Gemini AI to analyze and provide insights on social media content. User Experience: The importance of creating a user-friendly interface that makes it easy for users to input their content and receive actionable feedback. Data Handling: Best practices for handling user data securely and efficiently, ensuring that user history and preferences are stored correctly. Firebase: Utilizing Firebase for authentication and Firestore for data storage, which provided a robust backend solution for our application. Track PearAI (YC24) prize i’m just a chill guy sponsored by Build City (LAKOG) lowkey actually kind of good (IJAG) I’m Just A Girl What's next for Syntheos Add more advanced analytics and insights to help users further optimize their content. Continuously improve the AI models used for analysis to provide even more accurate and detailed insights. Incorporate user feedback to enhance the user experience and add new features based on user needs. Ensure the application can scale to handle a larger user base and more complex analysis tasks. We are excited about the potential of Syntheos to help users optimize their social media content and achieve better engagement. Thank you for considering our project! <div