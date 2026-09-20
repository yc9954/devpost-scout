---
slug: "karinderya-bot"
url: "https://devpost.com/software/karinderya-bot"
title: "Carinderia PH"
hackathon: "Facebook Hackathon: Messaging"
organization: "Facebook"
winner: true
words: 1174
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "domain/retail_commerce"
  - "user/small_business"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Carinderia PH

> Carinderia PH is an on-demand food delivery service for the local Filipino eatery, similar to UberEats and Postmates. It helps small businesses like "Carinderias" during the pandemic.

[Devpost](https://devpost.com/software/karinderya-bot) · hackathon [[Facebook Hackathon- Messaging]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]] [[labor_employment]] [[retail_commerce]]
**user** [[small_business]]
**substrate** [[code_repository]] [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** amazon-web-services, facebook-graph, graphql, microsoft-bot-framework, next.js, node.js, react.js, typescript, wit.ai

## How they structured the write-up

- inspiration
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for carinderia ph

## Body

Inspiration Introduction There's nothing more essential to the Filipino food culture than the carinderia. It is the go-to place of every Filipino for homemade food on every occasion: from workers getting their lunch fix, to families taking out meals to eat at home. It is Pinoy-style fast food at its best. The COVID-19 pandemic has hit the food business here in the Philippines, with the small local eateries suffering the most; the entire industry is projected to lose 80% of expected revenue as the pandemic rolls on. While food deliveries are on the rise, most carinderias are left out of the top digital platforms, not able to reap the convenience and benefits they provide. Now, there's a way for these food stops to be part of the new normal. Carinderia PH aims to solve this problem by providing an easy-to-use digital marketplace for small local eateries and businesses to be able to serve their customers. With Facebook Messenger as one of the most used messaging applications in the Philippines with over 78.5 million users, small food businesses started creating their own Facebook Pages to be able to reach their customers and sell their products, especially during the pandemic. Customers can quickly engage with the Facebook Messenger chatbot without the need to download or sign up for a separate app or service. They can also find all the restaurants within their area, check all information about the stalls such as products, reviews, ratings, and map locations. Dashboard Through a dashboard that is viewable from both the web and inside the Chatbot, carinderia owners or even food enthusiasts can set up a virtual eatery in a few minutes. With a few clicks, photos are uploaded, and menus with prices are made. Instantly, these products are automatically learned by artificial intelligence to show it whenever customers are particularly looking for it. Inside the dashboard, owners can monitor visual analytics of sales, visitors, orders, ratings, reviews, and geographic reports to help them track profits and make adjustments or data-driven business decisions. Their outstanding performance is rewarded through free promotions across all the customers within the platform. Geographic reports - give stall owners a capability to see how their products are being patronized on certain areas that can be used for targeted marketing and business decisions. Visitor Hit Rate - metrics that show the trend of users as the stall goes live. This could be used by owners to schedule their promotions and see if their marketing efforts actually converts. Feedback - shows customers' satisfaction rates to help owners improve. Customer and sales reports - provide tracking of profit, customer acquisition, product quality, and store performance. The products page enables stall owners to set up their online menus. Menu and product creation. Variant Management - the capability of owners to add different variations of their products. They can also add separate images for each variant. The orders page displays the list of all orders from chatbot customers. Owners can manage the orders from this page such as accepting, declining, and tag ready for delivery/pickup. By also clicking the name of the customer, owners can start a conversation with the customer The Stall Setting page is where owners fill up information about their online store which shall also be visible to the customers. Chatbot Kayenna is Carinderia PH's very own virtual assistant that lives in Facebook Messenger. She will help users find their favorite local eateries, get info about their business, and showcase their products. Using the power of Natural Language Processing and Artificial Intelligence, Kayenna will be able to give users results on eateries that serve their current cravings. Some customers are very particular with the carinderias they patronize, so at the tip of their fingers, they can get notified if their go-to is ready to take orders or have a new menu to offer. Carinderia PH automatically sends these orders to the respective stalls while customers can track the progress of their orders in real-time or even start a conversation with the owner regarding their orders. Users can also help out their favorite local eateries by giving them ratings and feedback that will help other customers find their new favorite carinderia. Carinderia PH Chatbot in Facebook Messenger After clicking 'Get Started' Kayenna will welcome customers with menu options to choose from Customers can simply type in their cravings and Kayenna will find stalls that serve the food they're looking for. After clicking the 'VISIT' button, customers will be asked one time to set their delivery address by pinning their location on the map. After this, nearby stalls serving the searched food will be displayed. Stall information such as delivery hours, location, reviews is viewable by tapping the info button. Adding food to the cart and checkout process. Customers can view the progress of their order after receiving each order status notification Customers can type in their inquiries about their order. Aside from tapping 'OPEN STALL' in the main menu, stall owners can also type in their request to register their store in our platform. Conclusion As everyone adapts into the new normal, Carinderia PH will seamlessly connect patrons with their favorite carinderias with safety and convenience. Carinderia PH, digitizing local eateries. How we built it Chatbot - We created the Chatbot using Microsoft Bot Framework V3 on Node.JS and channeled to Facebook messenger utilizing Facebook GraphAPI.We integrated Wit.ai as our NLP and product entity training programmatically from the dashboard. Dashboard - We built the dashboard using typescript Apollo client, AWS amplify, GraphQL, base web as UI Framework. We used Cloudinary for image repository. Backend - We are hosting on different providers, our Microsoft bot framework bot service is deployed in Azure while the rest of the backend is running on AWS Lambda, Appsync. Challenges we ran into We initially had problems with how we are going to train each entity such as product and name of stalls; fortunately, Wit.ai can create objects and feed it to existing trained utterances programmatically. As we aim the customers to re-engage with the bot, the one-time notification had given us the option to subscribe users to unavailable products or currently closed stores then notify them once the product and stall are ready for orders. Accomplishments that we're proud of We have combined some of the most modern and advanced software development tools, services, and frameworks out there to create a platform with an impact on one of the most crippled businesses today, local dine in. What we learned For the dashboard, our team has explored and used some cool and convenient stuff such as codegen tool of Apollo GraphQL and entirely run its interface on Now serverless. It is also our first time implementing a one-time notification and the newer version of Wit.ai for a chatbot while the backend services are also running on serverless Lambda. What's next for Carinderia PH Keep it live for the food stall businesses and help communities share more of their delicacies to their neighbourhood. Should all goes well, add cashless payment integration and delivery service. <div