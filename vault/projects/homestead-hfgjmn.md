---
slug: "homestead-hfgjmn"
url: "https://devpost.com/software/homestead-hfgjmn"
title: "Homestead"
hackathon: "HackUTD X"
organization: "hackutd"
winner: true
words: 698
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Homestead

> All in one, data-driven mortgage assistance and calculation

[Devpost](https://devpost.com/software/homestead-hfgjmn) · hackathon [[HackUTD X]]

## Facets

**domain** [[finance_payments]] [[immigration_refugee]] [[supply_logistics]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** flask, javascript, python, reactnative

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for homestead

## Body

Home Page! Static Analysis Enter your own stats! PCA analysis Interesting result! Homestead: Empowering Financial Mortgage Decisions Inspiration The inspiration behind Homestead stems from the need to simplify and empower individuals in making informed decisions about mortgage assistance. We aimed to leverage data provided by Fannie Mae to build a comprehensive financial mortgage assistance calculator. Our goal was to make a mobile application that made it easier for immigrants and others who might not be familiar with the complicated landscape that is mortgage financing in an all in all platform. What it does Homestead is a robust application designed to calculate crucial financial metrics such as Loan-to-Value (LTV), Private Mortgage Insurance (PMI), Debt-to-Income ratio (DTI), and Federal Debt-to-Income ratio (FedDTI). The application utilizes Flask for the backend and React Native for the frontend, providing a seamless user experience. Users can input various parameters, including credit score, monthly mortgage payments, appraisal value for the home, and additional factors like car payments. The app then calculates the likelihood of loan approval based on these parameters, offering users valuable insights into their financial eligibility. To further enhance user experience, we integrated OpenAI to provide personalized recommendations for users aiming to improve their chances of loan approval. This allows people a direction in which to look for possible improvements and concrete actions they can take without feeling lost. Moreover, we hand crafted a tutorial section to help explain the basics of the finances and statistics that might be lost on a beginner. Additionally, a resources tab offers hard links for more information, and a direct link to Zillow generates a map showcasing homes with appraisal values eligible for loans. Then, users can see locations of homes based on where they are and what they can afford. In addition, we performed analysis on many of the different features, their imporance, and their distributions when comparing them to which people were able to get approved loans. From XGboost decision trees to logistic regression to simple probability distributions, we sought to scour the data for any trends we could find. We created a decision tree and performed logistic regression just to create visualizations and determine the most "important" features when creating a model to represent the values. Then, to provide more visualization of the data as well as the seperation between the two classes utilizing the processed features, we utilized PCA. Finally, we analyzed distributions of different features, and wanted to display one here - We found a direct correlation between higher gross monthly incomes and loans, which seems to make sense! How we built it Homestead was built using Flask for the backend, handling data processing and calculations as well as any processing. Feel free to check out our Jupyter Notebook to see our statistics and the results of our analysis! React Native was employed for the frontend, ensuring a dynamic and user-friendly interface. Challenges we ran into Navigating the vast dataset provided by Fannie Mae presented a significant challenge. We struggled to find many correlations as well as come up with innovative ideas to push the dataset forward in a transformative manner. Moreover, it was our first time working with React Native and mobile app development which posed a significant learning curve for the first few hours of our event. Moreover, utilizing a number of API's was both interesting and a challenge. Accomplishments that we're proud of We are proud to have successfully developed Homestead, a powerful tool that empowers users to understand their financial eligibility for mortgage assistance. We're glad to have hosted the backend as well as made it available on multiple mobile devices in order to make it accessible. What we learned The main takeaways were a better understanding of loans and mortages that we ourselves had to research. Moreover, being able to create apps in React Native is super fun! What's next for Homestead The journey doesn't end here. Moving forward, we plan to refine and expand Homestead's features. This includes incorporating additional financial metrics, enhancing the AI recommendation system, and collaborating with more external services to provide users with a comprehensive tool for navigating the mortgage landscape. We hope to host the application for others to utilize! <div