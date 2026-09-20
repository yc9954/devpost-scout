---
slug: "shopsafe-21onk6"
url: "https://devpost.com/software/shopsafe-21onk6"
title: "ShopSafe"
hackathon: "Hack the Northeast"
winner: true
words: 1088
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/elder_child_care"
  - "domain/retail_commerce"
  - "substrate/geospatial"
  - "substrate/regulation_legal_text"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# ShopSafe

> Convenient and Safe Shopping for Everyone

[Devpost](https://devpost.com/software/shopsafe-21onk6) · hackathon [[Hack the Northeast]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[elder_child_care]] [[retail_commerce]]
**substrate** [[geospatial]] [[regulation_legal_text]] [[structured_db]] [[video_visual]]

**stack** arduino, dlib, flutter, keras, opencv, python, sg90, tensorflow, webcam

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for shopsafe

## Body

Hardware Mask Detection Population/Capacity Regulation Home Screen Google Maps Local Stores First Joined Queue Enter Store Prompt Thank You!!! <3 Inspiration Social Distancing is the new norm, and maintaining optimal crowd levels in public places like shops, supermarkets, etc. has become a challenge. We present a high tech solution to address these issues. Capacity regulation and standing in lines at supermarkets and grocery stores is a prime example of how COVID-19 has changed society. For many people, these lines are the only places where they interact with random people or even come close to others. This situation is thus one of the only places where they have a slight chance of becoming infected. This can be dangerous to many people with underlying health issues or the elderly. We aim to increase preventative measures at stores and decrease contact duration in order to maximize the safety of our users. What it does We have two parts to our product. The hardware component uses a machine-learning algorithm to detect whether a person entering the store has a mask on or not. The detection is paired with a servo motor that opens the door if a mask is detected or stays closed if no mask is detected. The system also has an automated voice to tell users to come back with a mask on or if they are good to enter the store. We used OpenCV to capture each frame of the video stream from a webcam and applied the ML algorithm to it, which returns the corresponding signal via a serial port to the hardware. The hardware component also regulates the population of the store in order to minimize store capacity while keeping a steady and fast flow of customers. Using the same webcam, we detected whether a user has passed the boundary lines and increments the population depending on the total amount entered and total amount exited. We can then pass the population and the entrance/exit rates to a backend where the front end could use to calculate the estimated wait time for each store. For the software component, we used Flutter, Google Maps API, Tensor Flow, Keras, OpenCV, and Python. Flutter was used to build the front end, which utilized the google maps api for the Search Stores function. We created the ML algorithm using tensor Flow and Keras. With OpenCV, we captured a video stream from a webcam and processed every frame, then passed each frame into a neural network that was trained on a dataset of face images, both with and without masks. This was a Hard cascade type of classification, which made a detection of a face, outlined the mouth region of the face, and tried to detect a mask object. The algorithm ran through each frame and if it detected a mask, it would send a signal via a serial port to the hardware. Our system used a python library called pyserial to communicate between the software and hardware. How we built it Machine Learning: Tensorflow with keras frontend OpenCV Dlib Frontend: Flutter Google Maps API Python Hardware: External webcam Arduino Uno microcontroller SG90 Low power servo Cardboard Algorithm Face Mask Detection To train any machine learning model, a good a reliable dataset is the first and foremost requirement. To generate a dataset for this problem, an image of a mask with a transparent background is superimposed on multiple faces. This way we could have multiple images of people wearing a face mask. (Note: do not use the same image for with and without mask dataset. USE DIFFERENT IMAGES). Once the model is trained, OpenCV is use to get the video stream and analyze it frame by frame. In each frame of the video, the model is run to see if the person is wearing a face mask or not. People Counter The code first identifies the people in the video stream and form a bounding box around them. This bounding box is then used to find the centroid of the person. This centroid determines the relative position of the person in the frame. An imaginary vertical line is drawn using OpenCV. The position of the centroid and the line are stored as pixel position values. If the centroid position crosses the imaginary division line the person has either entered or exited the store. This way we can calculate how many people have entered and exited the store and keep a population count of the people inside. Challenges we ran into Overall system integration Optimal training, dataset augmentation Live camera stream lighting adjustment affects accuracy significantly Mask detection is very janky if the person is not close to the camera People tracking needs to be implemented where there aren't people randomly standing around, a smarter approach needs to be taken to account for randomly moving and standing people who occlude views Need to test (and train) with more diverse set of people (due to social distancing only 2 of us could test the live mask detection) Frame by frame detection is ineffective when attached to a physical process (like opening a door), so we skipped frames and introduced deliberate delays in the video stream processing to allow the user time to walk through the door and have a safe distance from the next/previous person Accomplishments that we're proud of Our system works! We incorporate different systems and components together, with 2 separate machine learning based sub modules We identified some issues with real time video stream analysis and were able to figure out how to address these issues. We are also proud that the application works and is capable of queuing up your position in multiple stores. What we learned We learned how to integrate the Google Maps API into our code, which we have never done before. This allowed us to use location services to determine the user’s location and nearby stores. We also improved our ML skills by working with image detection this time. Integrating the overall system was a challenge and we learned many things along the way. What's next for ShopSafe We hope to actually implement our service in stores around the country, but we need to reach out to local stores to agree to use our service. The queuing system can only work when the store agrees to only let users in through the queue. We also need some funding in order to distribute our hardware system. We hope to benefit the world with our creation because our solution can actually have a huge impact in the world. <div