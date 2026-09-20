---
slug: "food-forward-c2swnz"
url: "https://devpost.com/software/food-forward-c2swnz"
title: "FoodForward"
hackathon: "FusionHacks 2"
organization: "FusionHacks"
winner: true
words: 1129
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# FoodForward

> FoodForward is an app that reduces food waste by enabling users to buy and sell food in their community. Using AI, the app lets users scan their food to put on sale and find the food they want to buy.

[Devpost](https://devpost.com/software/food-forward-c2swnz) · hackathon [[FusionHacks 2]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[agriculture_food]] [[developer_tools]] [[finance_payments]] [[retail_commerce]]
**substrate** [[video_visual]] [[web_dom]]

**stack** css, firebase, gemini-2.0-flash, geminiapi, genkit, genkitapi, googleai, javascript, json, lucidereact, markdown, next.js, react, reacthooksapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for foodforward

## Body

Inspiration I was inspired to create FoodForward by my research. In the summer before 8th grade, I was in the Stanford Global Qualia Research Program. The main topic for this program was to find a major problem and come up with concepts of a plan to make a solution. The major problem I found was the issue of food waste in the world. 92 billion pounds of food are wasted yearly, in the United States alone, and this is extremely harmful for the environment. The main goal of the research program was to write a paper detailing how you would fix the problem, but not construct the solution right away. I chose to research an app similar to Food Forward for the solution in the research program, which would enable businesses and users to sell food to each other to reduce the amount of waste. This year, using Firebase Studio, I built the app I had researched previously to turn my idea into reality. While developing this app, I also sent out a survey to 60+ organizations and local restaurants to see how interested they would be in working with this app. Finding organizations and restaurants that wanted to use this app was helpful in my journey to create the final product. What it does FoodForward is an application designed to reduce food waste by creating a marketplace among a community where users can buy and sell surplus food. Currently, the functionalities of the app include AI-Powered Item Scanning, Marketplace and Searching, User Accounts and Profiles, In-App Messaging, and a Shopping Cart and Checkout. The AI-Powered Scanning feature allows sellers to scan their food items, using AI to analyze the item’s freshness and automatically fill in listing details such as the title, description, suggested pricing, amount, and ingredients. The In-App Messaging allows sellers and buyers to easily communicate to ensure the quality and delivery of the food is top-notch. How we built it This app was built with Firebase Studio, using TypeScript as its primary language. The foundation is built with Next.js, with Tailwind CSS for the User Interface and Google’s Genkit framework integrated with Gemini for the AI features. The application uses Firebase App Hosting for its deployment. The AI model used for scanning the food is Google’s Gemini-2.0-flash model. I built it using generative AI prompts and editing the code myself in Firebase Studio. Challenges we ran into The main challenges faced while creating the app were fixing the errors, as many popped up during the developmental process. There were many “hydration errors” initially, where components would try to render before their necessary data was loaded in. This occurred on the main marketplace, leading to 404 errors. Many “param issues” occurred as well, where pages attempted to execute their functions before the parameters were available. Since the parameters were missing, many functions prematurely triggered the notFound() function, leading to missing items. To resolve this, a strong loading state was implemented, making sure the component would wait for the URL parameter to be correctly run and parsed before attempting to get data. Another challenge was designing effective prompts for the AI, since Firebase Studio’s AI had difficulty understanding how to run the marketplace. Populating the marketplace with sample food items on sale with images was challenging, and I had to manually implement the image and food details for the sample items on the marketplace myself, adjusting the expiration dates as well, to make sure they all appear on the main page. The AI had set the expiration dates for some of the sample items as dates passed, and expired food items don’t show up on the app’s marketplace, so I had to adjust the expiry dates. Accomplishments that we're proud of Accomplishments that I'm proud of are getting the marketplace to work, enabling the chat feature, and creating the sell feature. Initially, the marketplace wasn't getting populated with artificial food items, and the generative AI couldn't figure out how to solve the problem. I went into the code and found out it had set expiration dates for months ago, and expired items don't show on the marketplace, so I manually fixed all the expiration dates. Next, the images for the foods weren't working, and the AI couldn't fix those, so I had to manually set images for all the sample foods. Afterwards, the marketplace was functional, which solved the major issues. My next issue was figuring out how to demonstrate the chat feature, as we didn't have any other real users on our app. I solved this through AI chatbots, which are used solely for demonstration purposes. They show how our real-time communication is efficient and allows both the seller and buyer to convey their needs. My third accomplishment was successfully getting the AI scanning feature up and running. Through this, the AI easily identified which type of food it was, the amount, the freshness, a reasonable price, and the ingredients, highlighting just how convenient and quickly AI can sort food, saving the time of users wanting to list their items. What we learned By building this app, I learned how to use powerful generative AI to create an application that could be used to help the community. I learned how to use Genkit for different tasks, from image analysis to data outputs, and how they can be connected to a frontend. The process of debugging and resolving the 404 errors showed me how to properly handle parameters and manage data to avoid them, and through Firebase Studio, I learned how effective AI can be in helping create an application. I learned how to operate Firebase and the parts of code involved in creating the application, and how to combine a user-friendly interface with efficient backend functionalities. What's next for FoodForward The next steps for FoodForward would be adding payment credentials, a way to verify your email, and outreach. The first two steps would increase the validity of my app for future publication, ensuring that everything works and all the details have been taken care of. They would also allow users to buy and sell their food for money, fulfilling the primary function of the application. The last step would allow real users to use the app, increasing community impact and allowing local groups to combat food waste, one sale at a time. This would decrease the amount of food thrown away in many areas, and with real users, my communication feature would be rid of any AI chatbots, instead allowing sellers and buyers to speak to each other directly. Real users on my app would increase awareness and benefit the environment, which is the primary goal of my app. Food wastage would be decreased, and many more would be able to enjoy food for affordable prices. <div