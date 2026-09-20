---
slug: "training-ai"
url: "https://devpost.com/software/training-ai"
title: "ML Tools for Developer Professionals"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 972
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# ML Tools for Developer Professionals

> Developers of all skill levels can train neural networks to test their projects to extract valuable information without the hassle of building and training their own neural networks from scratch.

[Devpost](https://devpost.com/software/training-ai) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]]
**substrate** [[structured_db]] [[video_visual]]

**stack** apis, flask, javascript, keras, mongodb, next, postman, python, react, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ml tools for developer professionals

## Body

Our product Value of our product to developers Add layer and determine type of layer (Front end integrated with back end) Tree visualization of neural network (Front end integrated with back end) Main mechanism of product (Front end integrated with back end) Inspiration Machine learning is everywhere, and it is increasingly apparent how powerful machine learning can be in providing important information, predictions and decisions for the future when provided data from the past. However, in order to extract this necessary information, a developer must create their own neural network and train it from scratch, which is both a time-consuming and highly-skilled process. We created ML Tools for Developer Professionals to break the barriers of using machine learning for professional work and personal development so that developers of all skill levels can have access to the power of machine learning. What it does ML Tools for Developer Professionals allows users of all skill levels to build neural networks and have it trained with their data. Using the neural network, they are able to classify strings, integers, and images as well as build models that can be tested against our API to see how well a user’s API performs. We also integrated a few helpful datasets using chain calls to established Facebook and Yelp API for any users to practice our tools for retrieving information and training models for any specific need to offer a more ready-made experience. Overall, our tools allow any developer ranging from newly curious developers with no machine learning experience to seasoned developers who want the convenience of readily-trained models to harness the power of machine learning and extract insightful information from the datasets of their choice. How we built it We built our frontend with React and Next. Our design goals were focused on bringing users a sense of order and ease, and for this reason, we adopted a minimalist design that emphasizes readability and user-friendliness. Our backend was built with Flask and deployed on Heroku. We built our backed specifically for it to perform well as a Postman public workspace. We used Tensorflow and Keras to build our backend and train the model and MongoDB to store user data and user models. A user who registers to our API can create a model, in which they can associate a database. A database is made up of collections of data points that can store images, strings, and integers. Our layers are designed for classification and NLP as we gave the user an option to use embedded layers as well. We took full advantage of Postman’s feature set. First of all, we were able to write pre-request scripts to pull data from different APIs. We specifically worked with two APIs: Facebook and Yelp. For Facebook, as a key, a user can enter in a hashtag, and it will add the images and media associated with the hashtag to their dataset. For Yelp, given a location city, it will automatically classify all the one-star, two-star, three-star, four-star, and five-star posts -- a great dataset for natural language processing. Even though the user has the capabilities to add datasets manually, this will greatly speed up the process and give the user a way to automate testing on a trained model. We know the importance of training models over time as many datasets and machine learning problems are time-sensitive. For instance, we set up a monitor that will get the latest data of President Biden and former President Trump every week, train our model on the images, and give the user a report on how the model is faring with time. The feedback from this process would allow a user to know if retraining the model is necessary or if there needs to be a new algorithmic approach to solve the desired problem. Challenges we ran into While building the frontend with the API in mind, we ran into some trouble due to the intricacy of machine learning. It was difficult for us to come up with a simple and elegant integration that is not only beginner-friendly to first-time users but also would not harm the experience of constructing an actual neural network. In addition, it was also difficult to restrict the user from putting illegal layers together. In the end, we had to rely on the user to come up with a model with the correct dimensions. We also wanted to add convolutional and pooling layers. This would definitely be a point of improvement given more time! Accomplishments that we're proud of To get more precise predictions and results from our models, a developer who builds a program to conduct sentiment analysis on a group of people may have to test the program every now and then in order to affirm that the models are fit. We understand this may be a time-consuming process, so using our monitors on Postman, we made it easy for users to set up regular tests to gauge how fit the user’s models are. What we learned It was our first time using Postman, but with Postman tutorials and its user-friendly interface, we got excited to learn and navigate Postman’s features. By playing around with API calls in Postman, we learned how websites in our everyday life are able to fetch necessary information in an efficient and accurate manner. What's next for ML Tools for Developer Professionals So far, ML Tools for Developer Professionals only directly supports API calls to Facebook and Yelp APIs. While our features do make it easy for users to set up their own data from other sources, we’d love to directly incorporate and support a plethora of other useful and publicly available APIs for our users to easily play around with. Having a larger breadth of already-supported APIs would give our users a much easier time handling datasets and models. <div