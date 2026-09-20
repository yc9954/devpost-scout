---
slug: "diet-plan-to-reach-your-weight-goals"
url: "https://devpost.com/software/diet-plan-to-reach-your-weight-goals"
title: "Diet plan to reach your weight goals"
hackathon: "The PartyRock Generative AI Hackathon by AWS"
organization: "Amazon"
winner: true
words: 884
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "substrate/video_visual"
---

# Diet plan to reach your weight goals

> Quickly knowing a diet plan without booking an appointment with a personal trainer is in high demand. And, a diet advisor assistant created with AWS PartyRock can address your problem with few clicks.

[Devpost](https://devpost.com/software/diet-plan-to-reach-your-weight-goals) · hackathon [[The PartyRock Generative AI Hackathon by AWS]]

## Facets

**domain** [[agriculture_food]]
**substrate** [[video_visual]]

**stack** amazon-web-services, generative-ai, partyrock, promt-engineering

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for diet plan to reach your weight goals

## Body

Menu of two (2) dishes. Inspiration It was not easy to have an effective diet plan to help me reach my weight goal at 70 kg from my current weight at 66 kg. I was miserable to try with different plans recommended by different people. It took time and significant effort to have those experiments. And, I believe that this problem is not only encountered by me but also many other people, especially women. This problem inspired me to create an online assistant with AWS PartyRock to allow people to easily access and inquire a reliable healthy diet plan to achieve their weight goal. What it does The application has the following features: Require 4 inputs, including your current weight, target weight, gender, and expected duration to achieve the goal. Able to evaluate if your goal is achievable, or healthily by checking with the condition an increase/decrease of weight per month not greater than 4 kg. Able to recommend the average gained/burned calories per day to achieve the goal. Able to suggest a menu in a day to achieve the recommended calories demand. Able to illustrate images of the recommended menu. How we built it I built the application with the following steps: Step 1: Press 'Build your own app' using short description "Get personalized nutrition recommendations to help you reach your weight goals." Step 2: Create 4 input text widgets to take the inputs, including currentWeight, targetWeight, gender, and timeframe. Step 3: Create text generation widget checkPlan to evaluate if the plan is achievable and healthily before moving to next actions, using prompt: Knowing that target weight is [targetWeight] , the current weight is [currentWeight] , the adjusted weight per month is calculated by using formula (target weight minus current weight) divided by number of months determined from [timeframe], no explanation is written. If the absolute of the adjusted weight per month is more than 4, then conclude that the plan is not healthily recommended, no explanation is written. Otherwise, it is concluded that the plan is achievable, no explanation is written. Model: Claude Temperature: 0 Top P: 0.2 Step 4: Create text generation widget neededAverageCaloriesADay to determine the average amount of calories to be gained/burned per day to achieve the goal, using the formula: (targetWeight - currentWeight)/0.00013 (1 kcal = 0.00013 kg)/days + average consumed calories by gender (2500/2000). Prompt: If the conclusion of [checkPlan] indicates the plan is not achievable (or not healthily recommended), then stop, show only conclusion. If the conclusion of [checkPlan] indicates the plan is achievable, the following action is performed: Knowing that the average consumed calories of Male is 2500, while the average consumed calories of Female is 2000. And, the target gap is ([targetWeight] minus [currentWeight]) divided by 0.00013, which is then divided by (number of days converted from [timeframe]). The target gap is positive if [targetWeight] is greater than [currentWeight] . The target gap is negative if [targetWeight] is smaller than [currentWeight]. Determine the average calories needed per day by using formula: the target gap is added with the average consumed calories of [gender]. Model: Claude Temperature: 0 Top P: 0.2 Step 5: Create text generation widget recommendedMenu to recommend a menu of 2 dishes in a day to gain/consume calories suggested from Step 4. Prompt: Recommend a menu of only two (2) dishes, named "Dish 1" and "Dish 2", to provide suggested calories per day from [neededAverageCaloriesADay] Model: Claude Temperature: 0 Top P: 0.2 Step 6: Create image generation widgets recommendedMenuImage1, recommendedMenuImage2 to illustrate the images of 2 dishes suggested by menu from Step 5. Prompt: An image of dish "Dish 1" suggested from [recommendedMenu] An image of dish "Dish 2" suggested from [recommendedMenu] Challenges we ran into Challenges which I encountered are: Write prompt to instruct the app to perform accurate numerical calculations. Fine-tuning model with temperature, top P experiments to improve model performance. Accomplishments that we're proud of My application is able to deliver promising result. For example, I fill in my current weight at 66 kg, my target weight is 70 kg, gender is Male, and my expected time to achieve the goal is 2 months. The app shows my plan is achievable because the average weight gain per month is 2 kg (less than 4 kg as prior defined). And, it returns the calories needed in a day for me is 3012.82 (accurately calculated with my mentioned formula). The menu recommended 2 dishes with nice images. What we learned My lessons are: Prompt engineering for accurate numerical calculations in all cases is not easy. In real life, I recommend to connect LLM models with an external compute source for numerical calculations. Even making small changes such as adding/removing a dot, comma can change your model result. So, be concerned with words/punctuations you choose. The results can be different when the application is refreshed. The platform sometimes can not generate results and returns error for images generation. What's next for Diet plan to reach your weight goals Enrich the application's knowledge with more customized menu and aim to make a chatbot with having knowledge like an expert in nutrition. The idea of the application can be acquired by corporates like HelloFresh to improve personalized recommendations for customers' meal to help their customers achieve their health plan with maximum of convenience. <div