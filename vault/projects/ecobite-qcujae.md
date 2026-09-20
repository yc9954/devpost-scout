---
slug: "ecobite-qcujae"
url: "https://devpost.com/software/ecobite-qcujae"
title: "EcoBite"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 1088
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "domain/climate_energy"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# EcoBite

> Track your food waste in a gamified way— EcoBite aims at combating global food waste by allowing its users to upload images of their food, eaten or uneaten, to determine the weight of what is wasted.

[Devpost](https://devpost.com/software/ecobite-qcujae) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[agriculture_food]] [[climate_energy]]
**substrate** [[structured_db]] [[video_visual]]

**stack** flask, flutterflow, gemini, perplexity, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ecobite

## Body

EcoBite System Design EcoBite Logo Manually tracking food from TreeHacks '25 Landing Page Image Upload Food Waste Analytics Member Benefits Inspiration In the USA alone, food waste makes up 22% of landfilled solid waste, and “globally, food loss and waste represent 8 percent of anthropogenic greenhouse gas emissions” (EPA 2021). Our inspiration for EcoBite was an interest in this incredibly relevant issue within our world, as well as the Stanford Sustainability Challenges , specifically Challenge #3: the development of a program for determining the weight of food in an image. From a technical standpoint, this challenge aligned greatly with our interests: full-stack application development the use of AI / large language models generalized machine learning Our team felt we could each bring our strengths into this project, with the significant added benefit of creating a tool that could make an impact in combating food waste and therefore helping our planet’s environment. We also resonated greatly with the message of S tanford’s Ecopreneurship program , of accelerating environmental and sustainability efforts fueled by passions within the field of climate change or tech. What it does EcoBite is a mobile app meant for users to take pictures of their leftover food for the main purpose of estimating the food’s weight. After this action on the user’s end, the app will analyze the weight of the food in the image along with classifying its type. On top of being able to record and display this data to users, EcoBite keeps track of individual progress when it comes to food waste, allowing for milestones to be reached when individuals to a good job not creating as much food waste. This information is recorded and held in a backend to be analyzed for generalized food waste trends, all of it location-based. This process of recording images is also great for businesses that produce much food waste in their day to day in order to better keep track of food costs as well as intercept food waste. How we built it EcoBite utilizes a variety of sponsor technologies to complete this project. For a professional responsive frontend, we leveraged FlutterFlow to rapidly develop a polished mobile application that enables users to track their food weight, view detailed analytics of their consumption patterns, and participate in an engaging points-based reward system. FlutterFlow's intuitive low-code platform streamlined our development process, enabling us to rapidly create a polished mobile app with professional UI components and functionality that would have otherwise required significantly more development time. Various API endpoints were created to retrieve any necessary information the user may need. For the backend, we used Flask as the AI APIs perform best in a Python environment. Google Gemini was used to perform essential functionalities such as food classification and segmentation, volume estimation, and weight calculations. Our team learned prompt engineering principles to optimize these AI interactions, ensuring accurate and consistent responses while minimizing token usage and processing time. For obtaining the density of different food items, we used the Food and Agriculture of the United Nations' Official Density Database as our primary source. If the database did not contain a food item, we relied on Perplexity's Sonar Pro model to determine density values. Challenges we ran into On top of using Google Gemini for estimating the density of food via prompt engineering, our team wanted to use a food volume estimator deep neural net trained on many food images to assist with the classification of food items and estimation of their weights. There were many great examples of older work being done in this field, however a lot of the code was incredibly difficult into modern python / usability standards to this day, so our team ran out of time when it came to implementing this model alongside the AI model. This neural net would have been trained on 100100 images of food , using ResNet50 for image classification. Accomplishments that we're proud of Our team is most proud of our development of EcoBite using a tool none of us had worked with previously: FlutterFlow. Thanks to TreeHacks for hosting the company as a sponsor, we were given a perfect opportunity to pick up the tool and became highly motivated to try our best to master it over the weekend. Overall it was an amazing to learn how to use, all employees present helping us out greatly throughout countless steps of our app development process; end-to-end! Thanks to all of the assistance, as well as FlutterFlow’s user friendliness, we have a great looking mobile application that was incredibly straightforward to learn how to build. What we learned Thanks to Keegan Cooke , the head of Stanford's Sustainability Challenge #3 and Director of Stanford Ecopreneurship, our team gained valuable insights about the challenge and received a food scale for our preparations. Through our research, we discovered previous attempts to estimate food volume (rather than weight) using image classification. Along the way, our team quickly picked up and mastered several technical tools, including the Perplexity API, Google Gemini API, FlutterFlow for app development, and Flask for backend implementation. What's next for EcoBite We believe a great product is one that listens to its users. We look to gain as much feedback from users on their experience using EcoBite and what features have been useful and those in need of improvement. Through our beta testing phase, we will actively collect user feedback through in-app surveys, user interviews, and analytics tracking to understand usage patterns and pain points. This data will guide our development roadmap, ensuring we prioritize features that provide the most value to our users while continuously refining the app's functionality and user experience to better serve our community's needs. Some future goals include expanding to helping out businesses interested in keeping track of their food waste for the sake of improving sustainability and helping with professional costs. We would also love to expand the backend model used from AI tools to an actual existing estimation model trained on real images, both ones found in existing databases and those taken by users of the application. A big goal of EcoBite would be to create a data expansion pipeline wherein which the food density estimator could continuously train on new datapoints. EcoBite aims to counter food waste and instill better practices in how we prepare and consume food. Through our gamified approach and real-time food tracking, we empower users to make more conscious decisions about their portions and develop sustainable habits that benefit both their personal well-being, community, and environment. <div