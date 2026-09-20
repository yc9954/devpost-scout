---
slug: "disc-golf-coach"
url: "https://devpost.com/software/disc-golf-coach"
title: "Spin Coach"
hackathon: "Junction 2017"
winner: true
words: 1067
team_size: 4
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
---

# Spin Coach

> A sports training service that gives advice in real time based on user's performance collected through motion sensors

[Devpost](https://devpost.com/software/disc-golf-coach) · hackathon [[Junction 2017]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[civic_government]] [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[sensor_telemetry]]

**stack** amazon-web-services, android, movesense, tensorflow

## How they structured the write-up

- find us
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for spin coach

## Body

Spin Coach gives you instant feedback on your performance Find us Come by our desk D2 in the Junction venue and see it in action! Inspiration The author of the idea was teaching a young group of disc golf enthusiasts and going through the motions with each and every person there, who all did the same little mistakes. This was the lightbulb moment – why couldn't a machine do all the coaching? It would be more precise, available all the time and definitely cheaper to use. He ran a small survey in his local disc golf group and within an hour had over 120 interested users who said they would definitely use a device that would analyse their throws and give suggestions based on the movements. Our team originally focused on creating an application specifically for disc golf players, that would help the amateur and professional athletes to improve their game. The sport is one of the fastest growing in the world and Tom's enthusiasm for it also infected the whole team. After having some time with Futurice, we figured that using Suunto's sensors had much bigger potential than just one sport, so we re-visited the idea and finalised our concept to what it is now. We figured that sports is lagging behind in learning technology and saw that there is a problem to solve. Now we feel that we are on to something revolutionary in sports. And that is no less than inspiring. What it does The application serves as a platform for users to learn to do any kind of sports. It gives a basic course of action for users to start with and collects information for instant feedback through motion sensors on the body. Spin coach processes information to give coaching, advice, tutoring videos or corrections to improve user's performance. This way users can master different sport courses, track their performance and get personalised feedback based on real life data. For the hackathon we have prepared proof of concept – how to improve disc-golf performance based on the acceleration for the long throws. Spin coach gives advice on how to improve user's drive in real time based on the data from the sensor. How we built it The process started with creating a desired concept goal to which we would get in our development. The actual work kicked off with extracting data from the sensor into an android application, while we worked on creating the machine learning algorithm that analyses the throws. We have prepared some sample data to use by performing many disc throws while wearing our sensor. Then we worked on creating the backend for the app and machine learning infrastructure in AWS. The backend is a NodeJS app using AWS SDK to push all the sensor data into S3. Another instance is running TensorFlow Serving to serve the model we train on a third instance (can also be done locally). At the same time we have worked on creating a lean business model, do financial projections and improve the solution from user's point of view, meanwhile pivoting towards a larger platform rather than a niche service. Challenges we ran into During the hack our main challenges started from dealing with the sensor and configuring it to adhere to our needs. The Movesense product is in early development and the documentation was a bit hard to follow at some points (pull requests incoming, Suunto!). Another part of the problem was, that the initially the sensor was clipping at 8g, which is too low for our needs, so increasing the limit to 16g and getting undistorted data was a tough one. After extracting the data, we encountered a mathematical problem of getting accurate position from the acceleration data - apparently it's a task nobody has yet solved perfectly, but we now have the bare minimum we need for a POC. Next, a particular challenge in building machine learning infrastructure was the feature extraction - getting the most important parts of the data. The infrastructure was also too demanding for a student account in AWS. We initially set it up using AWS Lambdas, but unfortunately the student account lacked all permissions needed to use the serverless framework for quick deployment of lambda functions, so we opted for an EC2 instance instead. From the business side, selecting a consistent business model to provide a sustainable revenue stream was the main challenge. Accomplishments that we're proud of Our main accomplishments were, first of all, visualisation of the acceleration data that we have successfully extracted from the sensor. The work on done on feature extraction (getting meaningful metrics out of raw numbers) was also an great accomplishment for our team as a whole, as nobody had ever done it before. The data pipeline that we have created in AWS was quite impressive: sensor -> mobile application -> back end infrastructure -> storage -> machine learning infrastructure -> local machines -> screen and all the way back to the mobile appication. We actually have data to back up the market need – we have created a lean business model canvas ( https://canvanizer.com/canvas/r9P7pfZdTfGfN ), done revenue projections and have more than 160 potential first customers who are eager to try out the service as soon as it comes out. What we learned Our main learnings included understanding of TensorFlow for machine learning and the application of machine learning to real world problems. The team work in multiple disciplines at the same time, and managing the workflow was a big learning point for us. We have refreshed our knowledge about handling 4 dimensional matrices during the work with the data. Additionally, we got to know the challenges of using acceleration data for calculating position from acceleration (frickin' hard). What's next for Spin Coach After validating the concept we would continue developing the machine learning models by going out in the field and gathering data. We will be creating and training our models one sport at a time, starting with disc-golf. After we get and calculate all the needed parameters from the sensor we would finalise the system to apply the trained models and useful suggestions for the users, finalising the basic concept of the app for a sport. Next steps in development would be aimed at polishing existing sports and gradually adding new ones into the system, developing user experience and creating sport courses that a user could take. <div