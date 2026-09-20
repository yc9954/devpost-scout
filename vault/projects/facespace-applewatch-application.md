---
slug: "facespace-applewatch-application"
url: "https://devpost.com/software/facespace-applewatch-application"
title: "FaceSpace - Apple Watch Application"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 883
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/sensor_fusion"
  - "domain/transportation"
  - "user/frontline_worker"
  - "user/social_worker"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# FaceSpace - Apple Watch Application

> Facespace is a deep learning enabled Apple Watch app that helps people touch their face less often. Covid-19 often enters the body when people touch their eyes, mouth or noses with their hands.

[Devpost](https://devpost.com/software/facespace-applewatch-application) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**mechanism** [[on_device_local]] [[sensor_fusion]]
**domain** [[transportation]]
**user** [[frontline_worker]] [[social_worker]]
**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** applewatch, coreml, coremotion, keras, python, swift, watchkit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for facespace - applewatch application

## Body

Notification Mock-up Notification Mock-up Dashboard Page Mock-up Watch 8-Touches Watch Home-Screen Watch 4-Touches Watch 5-Touches Inspiration Decreasing Covid-19’s transmission rate, also known as flattening the curve, is critical to preventing healthcare system overload. Covid-19 can survive up to 72 hours on surfaces, and the virus can be transmitted from those surfaces to your hand when you come in contact with them. The virus can then enter your system when you touch your eyes, nose, or mouth (key areas). Research has shown that people touch their faces an average of 23 times per hour, and nearly half of those touches involve contact with the key areas, which are vital transmission points for viruses. What it does Facespace uses accelerometer and gyroscope data processed by a fully connected deep learning model to recognize when a user is moving their watch-hand toward their face or has touched their face. It both alerts a user that they are about to touch their face and then logs that touch on device. The machine learning model and watch app are complete and ready to beta. We plan develop a companion mobile application uses face touch data to make users cognizant of how often they touch their face, provide user-specific face touch trends and goals, as well as hand-washing recommendations based on users' face touching activity. How we built it Apple Watch Application We developed our watch application using Apple's WatchKit framework. Using the CoreMotion library, we gather gyropscope and accelerometer data and feed it directly into our deep learning model. Deep Learning Model We collected data to build our deep learning model from classmates and friends. We manually classified and processed the data they collected using sliding windows of 1 second duration and a stride of 20 milliseconds at a sample rate of 50hz. We then used a data augmentation technique to increase the number of positive examples in our dataset yielding a final dataset of around 9000 windows. We used Keras, a deep learning framework, to train a model including three relu activated fully connected layers, two batch normalization layers and a softmax output layer. After many hours of training set selection and parameter tweaking based on testing our model yields test set accuracy above 99% for motion not directly related to face touching and greater than 90% for near face-touching motions. We expect to improve performance as we collect more data. After developing a trained model, we used Apple's CoreMLTools Python library to transfer the model into the CoreML framework for use on the Apple Watch. Challenges we ran into We needed to run our application in the background, and therefore had to find a way to get around Apple's strict resource restriction rules. To do this, we needed to register our application as an exercise and severely reduce the computational power use in order to preserve application reliability and device battery life. Class Imbalance Our sliding windows method produced many, many more negative examples (i.e., the user isn't moving to touch their face) than positive examples (i.e., the user is moving to touch their face). As a result most all machine learning models will overfit to the over-represented class and perform poorly on the under-represented class. We used two techniques to solve for the class imbalance issue. First, we culled most negative example we weren't as interested in (i.e. very little motion) or those that were unlikely to trigger the model (i.e., moving a hand from face back down to side). Second, we used a data augmentation technique to increase the number of negative examples in our dataset. Limited Watch Compute Power Our first set of machine learning models relied on a set of signal processing operations to extract a set of digested features for use in algorithms like Support Vector Machines, Random Forest, or K-nearest neighbor. While these algorithms performed well on a computer, the pre-processing steps required to extract features were far too computationally expensive for the watch. As a result, we moved to a deep learning model that intakes raw sensor data. Accomplishments that we're proud of Model Performance We are happy that our model performs well, in testing it reliably detects movements toward the face without flagging non-face touch movements like drinking. Computational Efficiency Our app only uses around 30% of Apple Watch resources, making it a viable background application that doesn't impair the watch's performance. What's next for Facespace - AppleWatch Application Continue to Improve the Deep Learning Model We regularly come up with new ways to improve our model's performance. We will continue to implement them and push updated models to our application as well as collect additional data to make our model more robust to different users and activities. Develop an Accompanying Mobile Application Giving users access to their face-touch data through a mobile application is an important value-driver. We plan to build a fitness app inspired mobile application to help users understand their face touching habits as well as set goals to reduce the number of times the touch there face and increase the number of times they wash their hands. Implement our Solution on Additional Watch Platforms We hope to extend our solution to other popular watches such as Samsung's smart watches and Fitbit. Please note we have not yet explored the details of those implementations. <div