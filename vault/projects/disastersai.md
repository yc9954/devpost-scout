---
slug: "disastersai"
url: "https://devpost.com/software/disastersai"
title: "DisastersAI"
hackathon: "Hack the Northeast: Beyond"
winner: true
words: 1005
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/civic_government"
  - "domain/disaster_emergency"
  - "user/frontline_worker"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# DisastersAI

> Revolutionizing Catastrophe Prediction with Machine Learning

[Devpost](https://devpost.com/software/disastersai) · hackathon [[Hack the Northeast- Beyond]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[civic_government]] [[disaster_emergency]]
**user** [[frontline_worker]] [[general_public]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** ai, cnn, css, flask, html, javascript, jupyter-notebook, keras, ml, opencv, python, random-forest, regression, sklearn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for disastersai

## Body

Home Our Project Our Inspiration Fires Hurricanes Earthquakes Inspiration This past summer, wildfires spread through thousands of acres across Northern California, leaving people with no other choice than to evacuate. Additionally, several years back in 2017, a devastating Category 4 hurricane swept through Texas and many other states, destroying thousands of homes and facilities. It is crucial for these disasters to be predicted on short notice with great accuracy, and current methods for predicting catastrophes are either too slow or ineffective. Seeing the detrimental effects of these natural disasters and lack of potential from current methods, our team decided to create DisastersAI: a machine learning web app that utilizes a variety of state-of-the-art models to revolutionize the Catastrophe Prediction field. With our scalable web app made in Flask, our models can provide key insight into natural disasters within seconds, which is substantially faster than current methods. Not only can our web app help facilitate decision-making on an even playing field amongst natural disaster experts, but it can also help citizens on a day-to-day basis be aware of surrounding environmental risks. What it does DisastersAI provides functionality for three main natural disasters: wildfires, hurricanes, and earthquakes. For the wildfire aspect of our web app, we constructed two models to detect wildfire presence based on an image of smoke and predict the putout time of a fire based on the surrounding information regarding the fire. The smoke detector is a Convolutional Neural Network (CNN) that takes in an image and determines if the source of the fire is a wildfire. This function can be extremely beneficial and conserve resources if a firefighter is unsure about the source of the fire. It can also help stop wildfires before they become extremely large as they can predict them from the start. The putout time detector uses surrounding information about the fire such as the location, discovery month, temperature, humidity, wind speed, and vegetation to predict the amount of time it will take to put out the fire. Learning the predicted put out time before the fire happens can be extremely important for allocating the right number of resources and not underestimating or overestimating the severity of the fire. It also gives people an idea of how long they have to evacuate their area. The hurricane part of our app predicts flood damage using a CNN and determines whether or not a building has experienced flood damage based on its respective satellite image. This is beneficial to both individuals and the government, as they can efficiently decide the necessary resources to repair the damage. Not only can this save money and resources for hurricane repair services, but it can also make our constituents aware of possible damage that could take place during a hurricane. Lastly, the earthquake section of our web app can predict the magnitude of an earthquake based on location, as well as predict the chance of a tsunami occurring as a result of the earthquake, based on the date, location, and amount of deaths from the earthquake. Predicting the magnitude of an earthquake given the location can help the government plan their resource management and evacuation protocols to mitigate the threats of imminent earthquakes. This can save countless lives and help minimize monetary damage. Predicting whether or not a tsunami will come as a result of an earthquake is extremely important as it can help the government plan what they should do after an earthquake happens. They won’t have to unnecessarily evacuate and waste resources, as they will know if a tsunami is coming or not. How we built it Our website was built with four main languages. We used HTML, CSS, and JS for our frontend and Python and Flask for our backend/model development. We used many different machine learning models created from the Python libraries Scikit-learn and Tensorflow. All of our data was found on Kaggle. To start on our wildfire section, we used a CNN to classify wildfires from non-wildfires. For our CNN we had to resize all the images and our model had 12 layers, as that produced the highest accuracy. We tried different amounts of layers and found 12 was the best for time and accuracy purposes. Our Flask backend downloads the image locally from the user input and transforms the image into RGB values, resizes it, and then feeds it into the model. Our put-out time predictor is a regression model. We tested a Neural Net, however, because the data was quite simple and not extremely large, it did not perform very well. Next, our Hurricane flood damage model was also a CNN. We resized the images and created a model with 10 layers. Our process of getting the image to the model is very similar as we download the image locally, resize it, transform it, and feed it to the model. Lastly, we used a regression model for our earthquake magnitude predictor and a random forest classifier for our tsunami predictor. We used a regression model for our magnitude model as our data was continuous, and we tried an SVM for the tsunami predictor as well; however, the RF model produced better results. Challenges we ran into One of the main issues we had was with data preprocessing. The data we found had a lot of missing features and variables making it hard to run the models. Accomplishments that we're proud of We are proud of creating a fully functional app within the allotted time frame. We weren’t entirely sure if we would be able to create 5 different machine learning models as well as clean the data in such a short time, so completing the entire project was extremely exciting. What we learned We learned a lot about machine learning as well as how it can help the world. What's next for DisastersAI In the future, we would like to continue to improve our models and find better and more data to make them even better. We would also like to add even more features to the app. <div