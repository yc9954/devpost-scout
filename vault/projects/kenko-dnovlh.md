---
slug: "kenko-dnovlh"
url: "https://devpost.com/software/kenko-dnovlh"
title: "Kenko"
hackathon: "PennApps XII"
winner: true
words: 672
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "user/social_worker"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Kenko

> Snap a photo of any food and receive health insights

[Devpost](https://devpost.com/software/kenko-dnovlh) · hackathon [[PennApps XII]]

## Facets

**mechanism** [[on_device_local]] [[vision_ocr]]
**domain** [[agriculture_food]]
**user** [[social_worker]]
**substrate** [[structured_db]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** azure, cloudsight, css, html, ios, javascript, node.js, nutritionix, objective-c, shell, xcode

## How they structured the write-up

- what it does
- how we built it
- challenges we ran into
- accomplishments that we are proud of
- what we learned
- what's next?

## Body

What it does Take a picture of any edible item, regardless of whether it is packaged or not, and receive and track nutritional data. Using image recognition, Kenko allows you to track your daily intake of various nutrients including calories, sodium, cholesterol, etc. The application also has Apple Health Kit integration, allowing the app to store your health info in a centralized location. In addition, when you scan a food item, you also have the option of ordering more of that food item from a local restaurant. How we built it The main iOS app frontend is built in Objective-C, and the backend is written in Node.js. We realized very early on, after several attempts, that writing our own image classifier to recognize a variety of foods would be too expensive in terms of time and computational power. Instead, we decided to use the CloudSight API to help make this process a lot easier. We then used the context provided by the CloudSight API, and used the Nutritionix API to grab information about the food's nutrition data. The architecture of the app is very simple. The user takes a picture of some food with the iPhone app, which then sends a POST request to our Node.js backend (running on a Microsoft Azure VM). The Node.js backend then handles all of the communication with the various image recognition APIs and nutrition APIs. In addition, the backend also manages all user data and stores all past queries locally. The backend also aids the iPhone app in processing nutrition requests in the background, by allowing the iPhone app to send multiple images, and then receive the nutrition data the next time the user opens the up. Challenges we ran into We originally started by trying to write our own classifier using OpenCV. As we mentioned earlier, we realized very early on that building and training an image classifier that would identify various foods would be too difficult, time consuming, and computational expensive, as there was simply too large of a training data set to be processed and evaluated. As a result, we decided that using the CloudSight API would make our lives much simpler. We used the CloudSight API's Visual Search APIs to get context about food-related images and then later grab nutritional data. In addition, we also ran into latency issues with the CloudSight API, as the image recognition was a long, expensive process. We realized that part of the reason why the process was taking so long was because the images that were being sent by the iPhone app were very high-resolution, and also very large. We learned that bringing the resolution down brought the size of the image down significantly, and as a result we were able to get the CloudSight classifier to speed up a slight amount. The latency issues became less of a problem when we decided to change the intent of the classifier, being that the classifier would look for the main object within the image (in this case, the food), and not try and analyze all details of the entire image (e.g. the classifier would recognize additional, unnecessary, features such as the color of the table or plate that the food was sitting on). Accomplishments that we are proud of We are most proud of the fact of how well-designed and efficient the app is, as well as the fact that Kenko is now able to identify almost all foods, as well as retrieve the relevant nutritional data with a fairly small margin of error. What we learned We learned many things throughout the hackathon, but the big lesson of the day was that image classification requires a lot of computational power in order to train accurate identifiers (especially when it comes to training against a data set as large as the amount of food on Earth). What's next? We are thinking of continuing further with this project, as well as possibly shipping this app to the App Store in hopes of improving the lives of many. <div