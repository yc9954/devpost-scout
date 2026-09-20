---
slug: "foodflow-gwrxai"
url: "https://devpost.com/software/foodflow-gwrxai"
title: "FoodFlow"
hackathon: "GNEC Hackathon 2025 Spring - Compete For UN-Affiliated/NGO Internships & Prizes"
organization: "Global NGO Executive Committee"
winner: true
words: 1320
team_size: 0
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "domain/agriculture_food"
  - "domain/education"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/frontline_worker"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# FoodFlow

> Turning excess into access, where tech, timing, and compassion move food to those who need it most.

[Devpost](https://devpost.com/software/foodflow-gwrxai) · hackathon [[GNEC Hackathon 2025 Spring - Compete For UN-Affiliated-NGO Internships - Prizes]]

## Facets

**mechanism** [[benchmark_measured]]
**domain** [[agriculture_food]] [[education]] [[supply_logistics]] [[transportation]]
**user** [[frontline_worker]] [[general_public]]
**substrate** [[financial_record]] [[geospatial]] [[video_visual]]

**stack** ai/ml, apis, cloud), cloudinary, css, data, dbscan, dijkstra's, fastapi, firestore, google, gps, knn, mobilenetv2

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for foodflow

## Body

Inspiration The idea behind our initiative came to us as a result of what we observed - the US is wasting 120 billion pounds of food every year whereas at the same time 44 million Americans do not have enough to eat. This drastic difference is at the same time reminding us of the rule of nature - just as people need plants for the oxygen, the hungry people also need a fair way to get the extra food. Nevertheless, the leave of humans and plants is not alike, our method of sharing food is terribly defective. While doing the research, we realized that the extra food in the Central Jersey area was not being distributed by any local organizations. Therefore, the local problem was a good illustration of the much larger unfairness that the UN's Sustainable Development Goal 10 was aiming at. Our plan was to create the technology - a system to make sure that perfectly edible food is not being thrown out when there are hungry people nearby. What it does FoodFlow serves as a flexible system where food donors and recipients are brought together through a self-running, user-friendly, and automated algorithm—let's say, an app that connects customers in need of a meal with restaurants that have food that will go to waste. The users go to our marketplace and the donors will post food pictures and quantity and state their preferred time and place for pickup, while the recipients will browse the items that match their needs in the marketplace. Our geolocation technology ensures finding the right matches between donors and recipients and the use of AI to check food quality as well as making the best matching recommendations, and lastly, the inclusion of weather data for the securing of reliable deliveries. Green posts are identified for urgent attention in which a tight-knit group of people are managed in such a way by the system that they instantly respond to the needs of the community while also reducing differences in food access. How we built it The React Native frontend with Expo Router and Tailwind CSS for creating a clean interface was our way of implementing the frontend. Python and its AI-based image classification and weather response pipelines have become the powerful tools for the backend. To make the right pairings of donor and recipient for future blood transfusions, we employ KNN as a recommendation system that is a classic of its kind. The spoilage detection model, based on the MobileNetV2 architecture and trained on a set of 3,000+ images from 8 food categories and 6 spoilage levels, was developed by us to be used for the quality assessment of the food products. To cover data augmentation and hyperparameter tuning, the accuracy of 93.7% was achieved in the testing process through the weather service's API. When the weather situation changes, the weather forecasting pipeline gets data from the OpenWeatherMap and the NOAA for scoring the points, and doing it faster, the method of DBSCAN geospatial clustering with Dijkstra's shortest path works well. On the other hand, we have been working for the user and transaction data storage in Firestore, the AI model evaluations in Cloud Functions, and structured relational data in Supabase. After that, the image is sent to Cloudinary where a FastAPI backend is responsible for predictions. Apart from the infrastructure of Google Cloud, the deployment of the system also involves features like scalability, fast response times, and even data security. Challenges we ran into Our largest challenge was to create a user interface that would be equally used by people having different technical knowledge and resources. The first versions of our Machine Learning models were actually making mistakes by classifying a fruit as a food that is not fresh, which, in turn, could increase the amount of dumped food significantly, and we really wanted to do just the opposite. Thus, their correction was carried out to a large extent by using F1 scores and matrices of confusion. The problem of weather-responsive routing was likewise very tricky, as it implied that the system had to possess the ability to be quickly adjusted without interrupting the deliveries of perishable food. DBSCAN clustering was the method we chose to do the routing, but this had first to undergo many optimizations in usability to ensure that it can work adequately on the mobile phones which the drivers use. Arguably, our main difficulty was to provide access to people from various communities. We came to realize that technology could not solve the problem of systemic inequality by itself. We had to integrate the community's opinion in each development cycle and keep changing our approach to the demands of every community if we want to achieve equity. Accomplishments that we're proud of We have managed to put together a working platform that has not only been of a practical use but has also made a big impact by connecting 5 donating businesses with 6 collecting charities and rescuing 1,000 pounds of food from being simply thrown away. Moreover, our machine learning (ML) model has a food quality detection rate of 93.7%, is in full compliance with the UN's Sustainable Development Goal (SDG) 12, and becomes the forerunner to a circular economy by securing food safety and reducing food loss. Our community-centric strategy is a source of our deepest satisfaction, as it is more than just a direct feedback from local food pantries in the underserved areas of the city. This open collaboration method has borne a tool that is suitable for the lack of resources felt by those people living in unequal conditions, and it directly ties in with the purpose of the Sustainable Development Goal 10 of the UN, which is to decrease inequalities. What we learned The creation of FoodFlow helped us realize that the fundamental basis of any technical solution should be equity. We got to know how AI could be useful in solving intricate logistics issues, as well as, how AI could involve some constraints when the training data is not diverse and does not reflect the real-world complexities. It was realization for us when we brought into practice the biweekly development sprints gathering feedback directly from the communities we serve ensuring the technology remained undeniably current and inclusive. But the most significant thing that we came to acknowledge was that the existence of hunger did not mean the supply was a problem only—it was the issue of justice that, through creation of poverty and health disparities, had a more significant impact on the communities affected, who have also been marginalized. What's next for FoodFlow We are creating a new "Flowcast" model which is a forecast AI that is aimed at understanding the patterns of the seasons to allow for optimal distribution. In the next phase, we have in mind the publication of a public API and the establishment of FoodFlow chapters in schools other than the New Jersey locations to govern the local branches of our platform. The immediate aims are to add multiple languages, so a customer feels comfortable regardless of their native language, to upgrade the embedded picture recognition system to a level that meets the needs of different literacy levels, and to reach a compromise with ride-hailing services in the outskirts of the town where people are limited in their transportation capability. By removing such barriers, every extra improvement is a step towards reaching a balanced food supply network, where food-surplus will be easily available to a shortage area regardless of the community's resources or geographical location. Our vision is still quite optimistic, yet, at the same time, it is quite realistic that we can achieve a world where the flow of food from producer to consumer is not obstructed, where it is also just and equitable and in the utmost need. By using technology, the idea of the more equality world written in UN Sustainable Development Goals could be built. <div