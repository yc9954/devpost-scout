---
slug: "trafficai-t25ebd"
url: "https://devpost.com/software/trafficai-t25ebd"
title: "TrafficAI"
hackathon: "HooHacks 2021"
organization: "HooHacks"
winner: true
words: 862
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# TrafficAI

> Building safer cities, one road at a time.

[Devpost](https://devpost.com/software/trafficai-t25ebd) · hackathon [[HooHacks 2021]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[transportation]]
**user** [[educator_student]] [[researcher]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]
  <sub>weak: sensor_telemetry</sub>

**stack** flask, machine-learning, python, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for trafficai

## Body

Time series plot of frames vs crash likelyhood Test dataset confusion matrix Example frames from the CADP dataset An example frame from a CADP dataset video An example frame from a CADP dataset video CNN-LSTM training logs: loss vs epochs CNN-LSTM training logs: accuracy vs epochs Inspiration According to the Federal Highway Administration, there are 6 million car accidents and 36,000 car accident deaths in the United States annually. 25% of these deaths could have been prevented had the police and ambulance been informed earlier. Serious car crashes are extremely brutal events, where seconds can determine the difference between life and death. However, at the moment, the average time to report a car crash to emergency services is between three to five minutes. These accidents affect not only the directly injured and their close ones but also Americans as a whole. More accident-related injuries result in an overall increase in healthcare costs, which the average American has to bear as tax and insurance. Therefore, a reduction in the severity of injuries would be of benefit to everyone. What it does TrafficAI is a software that detects car crashes by analyzing spatiotemporal features of a sequence of image frames over time. We used machine learning to train a CNN-LSTM machine learning model to detect car accidents over a sequence of frames. We also prototyped a web app where this could be used. From CCTV footage, the model predicts if there is a car crash in each frame, and when there is, the web app audibly alerts a security guard and provides them with real-time traffic camera footage of the crash. The guard also has a button they can easily click to alert authorities once the crash has been confirmed. This button can be repurposed to collect data in the field for continuous training and deployment. How we built it We built a CNN-LSTM (Convolution Neural Network - Long Short Term Memory) model for identifying whether a crash had occurred given frames from CCTV footage. The model consists of a CNN portion, for which we used a pre-trained ResNet (the latest and greatest CNN variant) and an LSTM portion. The CNN extracts key spatial information from each of the frames and returns a feature vector for each frame. These feature vectors are then processed by the LSTM model, which is excellent at analyzing data over time due to it's recurrent structure. Once the model was trained, we saved it into an h5 file format which we could then use in our Traffic AI web application. The web application was created with the Flask web framework. HTML, CSS, & JavaScript were used to import in the videos, show whether or not the model believed there was an accident and play an audio cue if there was, and create a button that could be pressed to alert authorities. Challenges we ran into Managing 48 gigabytes of data was cumbersome so data pre-processing and training took a long time. Transferring data between our laptops (where we preprocessed it) and the cloud (where we could use GPUs for training) was also pain. Another challenge we ran into was with loading the h5 model file into our Flask application. We kept getting errors regarding our pip environment. None of us had ever trained a CNN-LSTM model and we were a little rusty with the TensorFlow/Keras stack so it was challenging to debug our model when it was not improving. We ended up watching hours of youtube tutorials in order to be able to finish it. Accomplishments that we're proud of By reducing the response time for car accidents to nearly instantaneous (25-30 frames --> ~1s), TrafficAi can help promote safer roads, saving lives and livelihoods. It was a difficult task to process then train the model on CCTV footage alongside create a web application. Looking at our final product, we are amazed as to how we had overcome our challenges to create this prototype of a life-saving product. Although it is not production ready, we believe it has great potential to help build smarter and safer cities. What we learned Flask, a framework that was new to some of us Transfer learning with keras LSTM networks, theory and implementation in TF/Keras Composing multiple ML models together (CNN+LSTM) How h5 files work (while debugging errors) 3 cups of coffee is enough to get through the night What's next for TrafficAI Database: A database can be integrated with an application to capture the data for each accident, such as the time, and location. Using the data, analysts can look for patterns and act accordingly to further reduce these accidents and deaths. Continuous machine learning: At the end of the day, the model can ask the user to confirm which accidents were true and which were false positive. Using this field data, we can use continuous training and deployment to keep generating smarter models. This allows for our system to be more sustainable and self-sufficient. Google App Engine: it can be used to meet the growing usage of servers and clients, allowing there to not be too much of a load on any one client machine due to its automatic scaling. <div