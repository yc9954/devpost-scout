---
slug: "chapchap-elogistics"
url: "https://devpost.com/software/chapchap-elogistics"
title: "chapchap e-logistics"
hackathon: "Atlas Madness"
organization: "Google"
winner: true
words: 920
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "user/frontline_worker"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# chapchap e-logistics

> Mobile platform using data to identify patterns and insights related to food production, distribution, and consumption.

[Devpost](https://devpost.com/software/chapchap-elogistics) · hackathon [[Atlas Madness]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[agriculture_food]] [[finance_payments]] [[supply_logistics]]
**user** [[frontline_worker]] [[general_public]]
**substrate** [[code_repository]] [[financial_record]] [[structured_db]] [[video_visual]]
  <sub>weak: geospatial</sub>

**stack** google-compute-engine, google-maps, mongodb, mongodb-atlas-search, mongodb-charts, node.js, react-native, realm, redux

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chapchap e-logistics

## Body

Chapchap elogistics Inspiration My inspiration for this project comes from the challenges faced by farmers in Africa. They often have to travel long distances to sell their produce, and they often face exploitation by middlemen. I believe that an e-logistics mobile application can help to address these challenges by providing farmers with a platform to sell their produce directly to consumers. This will help to improve the livelihoods of farmers and make food more accessible to consumers. We are also inspired by the potential of technology to solve social problems. I believe that e-logistics can be a powerful tool for social change, and we am committed to using our skills to help build a more sustainable and equitable food system in Africa. What it does See the app in action on app store https://play.google.com/store/apps/details?id=com.imbuga.chapchap Connect farmers with consumers: The app allows farmers to list their produce for sale on the app, and consumers will be able to browse the listings and purchase produce directly from the farmers. This eliminates the need for farmers to travel long distances to sell their produce, and it will also give consumers access to fresh, local produce. Reduce food waste: The app uses real-time data to track the movement of food, ensuring that it is transported and stored in a way that minimizes waste. This helps to reduce the amount of food that is wasted in Africa, which is a significant problem. Improve the efficiency of the agritech supply chain: The app makes it easier for farmers to find buyers for their produce, and it also makes it easier for consumers to find fresh, local produce. This improves the efficiency of the agritech supply chain, which benefits both farmers and consumers. Weather forecasts: The app provides farmers with weather forecasts, so they can plan their crops accordingly. Market prices: The app provides farmers with market prices for their produce, so they can get a fair price for their crops. Disease and pest identification: The app uses artificial intelligence to help farmers identify diseases and pests in their crops. Financing: The app connect farmers with lenders, so they can get financing for their crops. How we built it The app leverages a combination of MongoDB Atlas, Google Cloud products, and other relevant technologies to deliver a seamless user experience. It incorporates authentication for security, generative AI for personalized recommendations, MongoDB Atlas Search and Google Cloud NLP for efficient search, a reliable payment gateway for seamless transactions, and offline functionality to overcome connectivity challenges. We used React native this allowed us to offer a multi-platform (iOS/Android) user-friendly interface with intuitive navigation, making it easy for users to access various features. The app's layout and design are optimized for mobile devices, ensuring a seamless experience. we used Realm for offline Functionality:The app includes offline functionality to address the limited internet connectivity in some African regions.Users can access certain features and data offline, such as viewing previously accessed information, composing messages, or drafting content. When internet connectivity is restored, the app synchronizes the offline data with the back-end, ensuring data consistency. Search and Discovery: MongoDB Atlas Search is integrated into the app to provide fast and accurate search results.Users can search for specific data or information within the app, such as products, articles, services, or user-generated content. Generative AI Application:The app incorporates generative AI capabilities, which can offer personalized recommendations, generate content (text or images), or provide language translation services.Users can interact with the generative AI feature to receive tailored suggestions, creative outputs, or translation assistance. Compute engine is used to give the app security and to scale and a MongoDB database running on GCP, we are using a google compute engine to run the web-server with load balancing Challenges we ran into We ran out MongoDB quota so we had to upgrade to get a better experience with a bigger logical disk, this hindered our app, sync stopped, but after upgrading everything worked out alright Time management We are all working full-time in our respective work places getting time to work on the app, finding time to attend MongoBD university to learn the technology to use was hectic and tiresome, but we prevailed Unable to get access to Palm APi to build generative AI feature we wanted like personalized recommendation, we have however been put on the waiting list, hopeful we will implement it a soon as it get here. Accomplishments that we're proud of Build a team for future products, we loved working together and we plan to continue this collaboration in the future projects. We build a lunched a mobile app on play store using a short time despite all the constraints that we had, this was huge! What we learned Learned a ton especially by Attending MongoBD university to learn more about MongoDB Atlas, Aggregation analysis, Realm, and also Generative AI from Google skill boost, and we even got a $500 cloud credit from MongoDB to help build our startup. We also learned that MongoDB has so many other awesome services like App services that makes development and building mobile apps that require offline functionality and poor internet connection easier What's next for chapchap e-logistics Build Chapchap to be Africa's leading Agro-trading space by creating a market place that links farmers and buyers all over Africa. To integrate mobile payment to enable subscriptions based model for premium features and make the project sustainable To add Google Cloud's Natural Language Processing (NLP) capabilities analyze the data to provide contextual search results, enhancing the search experience. <div