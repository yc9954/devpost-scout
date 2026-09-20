---
slug: "mercado"
url: "https://devpost.com/software/mercado"
title: "Mercado"
hackathon: "ShellHacks 2024"
organization: "init"
winner: true
words: 641
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/general_public"
  - "user/small_business"
  - "substrate/structured_db"
---

# Mercado

> "Empowering Latino Businesses, One Investment at a Time."

[Devpost](https://devpost.com/software/mercado) · hackathon [[ShellHacks 2024]]

## Facets

**domain** [[developer_tools]]
**user** [[general_public]] [[small_business]]
**substrate** [[structured_db]]

**stack** ai, firebase, python, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what we learned

## Body

picture for background Inspiration The idea behind Mercado was sparked by the desire to address a gap within Latino communities—particularly Latino-owned small businesses. We often see these businesses struggling to access the same investment opportunities as others. As a result, many never get the chance to scale up. I wanted to create a platform that empowers not only business owners but also everyday people from the community who want to invest in and support local Latino businesses. Mercado represents not just financial markets but also local businesses—our “supermarkets” of culture and innovation. During Latine Heritage Month , this felt like the perfect opportunity to combine technology with community values to close the digital divide and support local entrepreneurs. What it does Mercado is a micro-investment platform that allows users to browse and invest in Latino-owned small businesses. It connects local businesses with investors who want to support their growth. Users can filter businesses by category, view their fundraising goals, and contribute investments in small amounts. The platform also has a community feature to foster networking and collaboration between business owners and investors. How we built it We built Mercado using: Streamlit for the user interface, providing an easy-to-use web app framework for rapid prototyping. Firebase Firestore for the backend, handling business data storage, including business names, descriptions, fundraising goals, and investment tracking. Python for fetching data from Firestore, processing user investments, and integrating backend logic. Firebase Admin SDK to securely interact with the Firestore database and manage user actions. ## Challenges we ran into Building MercadoVest presented a few significant challenges: User Authentication : We initially planned to integrate Firebase Authentication for personalized user experiences. However, due to time constraints, we simplified this feature and used placeholders for user IDs. Database Structure : Managing data for multiple businesses while ensuring scalability for future growth required careful planning. We had to structure our Firestore database in a way that allowed for efficient querying and filtering by business category. Duplicate Widget IDs : In Streamlit, we encountered issues with duplicate widget IDs when creating sliders for investments. We resolved this by using unique keys for each widget, based on the business IDs. ## Accomplishments that we're proud of We are incredibly proud of several aspects of MercadoVest : Creating a Platform for Latino Entrepreneurs : Empowering Latino businesses and giving them access to investment opportunities is the core goal of our project, and we successfully built a platform to achieve this. Streamlined Investment Process : Users can easily browse businesses and invest directly from the platform, making the investment process seamless and user-friendly. Dynamic Data Integration : We built a system where businesses can be dynamically fetched from Firestore, allowing for future scalability without hardcoding businesses into the app. What we learned Throughout this project, we learned a great deal about building community-driven applications: Free Tools Can Be Powerful : Using tools like Streamlit and Firebase, we realized how easy it is to build, deploy, and scale a web application on a limited budget. UI/UX Is Crucial : Providing a simple and intuitive interface was a key takeaway. We learned that ease of use is essential in encouraging users to engage with the platform. Community Investment : We also learned how important community-driven investments can be for helping small businesses flourish, especially within underrepresented communities. ## What's next for Mercado Looking forward, we plan to: Expand Features : We aim to integrate user authentication and personalized investment tracking. This will allow users to log in, view their past investments, and track their impact. Community Building : We want to add more features to foster community interaction, such as discussion forums or business-owner profiles where users can connect and share advice. Expand Business Listings : Our goal is to grow the database to include more Latino-owned businesses from various regions, not just Florida. <div