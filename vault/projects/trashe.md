---
slug: "trashe"
url: "https://devpost.com/software/trashe"
title: "Trashé"
hackathon: "Microsoft Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 1157
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/sensor_fusion"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Trashé

> Trashé is a SmartBin which aim to help you get better at recycling. Making use of Azure IoT Edge we're able to leverage our trash detection model to detect plastic, glass & metals in realtime.

[Devpost](https://devpost.com/software/trashe) · hackathon [[Microsoft Azure AI Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[sensor_fusion]]
  <sub>weak: realtime_stream</sub>
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** azure, azure-iot-suite, docker, raspberry-pi

## How they structured the write-up

- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for trashé

## Body

Trashé Dashboard Trashé Architecture Diagram Trashé Trashé is a SmartBin which aim to help you get better at recycling. Making use of Azure Cognitive Services to create a deep learning model to detect plastic, glass and metal recyclables in real time, using Azure IoT Edge to perform inference and transport predictions to other Azure Services. How we built it Software Architecture At a high level this diagram can be broken into three distinct sections Custom Vision & Model Building a multiclass predictor using customvision.ai , one of Microsofts Cognitive Services. IoT Edge Using Azures IoT suite to do edge inference on live images provided by a camera connected to a Raspberry Pi Web Frontend Creating a nodejs backend, using azure functions to write data from the IoT Hub into a CosmoDB instance. Hardware Architecture Our initial hardware design for this project is to attach the Raspberry Pi, Camera and light to a bin, to do inference on a bins content to see what is recyclable and what isn't. Challenges we ran into There were a number of challenges that we ran into during the design and execution phase of this project. Gathering the Dataset A key part of our design was to incorporate a custom Machine Learning model that could classify different kinds of trash. While we could have gone the time consuming route of collecting our own images / scraping the internet for images and building our own dataset, we decided to repurpose two existing MIT licensed datasets: garythung/trashnet pedropro/TACO These models were built to detect the presence of trash, not to try to classify trash into recyclables and non recyclables, so some manual annotations were required to build the required classes of images. We classified all our images by hand using the drop and drag interface on https://customvision.ai . After classifying over 2500 images into 14 classes we had a usable dataset. After doing the labeling, customvision.ai made it easy to train our model, automatically doing the model selection, test/train split and model training processes. The output of this was a set of predictions and a docker container targeted towards our desired architecture (ARM for a Raspberry Pi). Based on our results, the outcomes seem perfectly reasonable for the current use-case, especially for a proof of concept of "is this actually possible", and gives us a baseline to move forward from. Model Deployment We'd set ourselves a bit of a challenge: for the actual creation of everything IoT related we would try to do as much service creation and deployment as code, trying to keep our steps repeatable. Dark Bin Surprisingly with all of the technical challenges, one of the problems we encounted was actually simplistic. Our model did not perform well when we attempted it in real life because the lighting of the bin was insufficient to get a clear image. We wanted to avoid manual interaction so a simple lighting system was cobbled together using a small USB LED light we had laying around. Accomplishments that we're proud of End to End Solution Initially we only planned to work on a Vision model, however as we progressed we became more ambitious and eventually built out the end-to-end solution we're submitting now. We feel there was a lot more to learn in building a pipeline that included model creation, deploying the model on the edge and building a web application than just building a web application to consume an external API. Open Sourced Guide Another thing we're really proud of is the level of details put into the guide written as we built out this system. Not only should all steps be automated, but they give a good understanding of the decisions made during the development of Trashé. 01_custom_vision 01_custom_vision_model 02_container_registry 02_iot 01_raspberry_pi 02_azure_iot_edge 03_azure_iot 04_blinker 05_usb_camera 06_camera_capture 07_image_classifier_service 03_web 01_service_bus 02_queue_process 03_cosmos_db_webapp 04_queue_processing_revisited What we learned This was the first time using Azure and it was great to experience some of the details in using the platform. We particularly found it surprisingly easy to create a containerised machine learning model using the Azure Cognitive Vision service. Not having to worry about manually deciding a neural network architecture (or reading papers on architectures that are well suited to our specific task) allowed us to remove distractions and focus on how to get to our goal of an end to end system faster. Azure Resource Manager We loved being able to use Azure Resource Manager in order to repeatably deploy the entire backend stack. It really helped when co-working on this project as it meant that both of us knew with certainty that we had the same setups. Azure IoT Edge We learnt that Azure IoT Edge was a great platform to work with in respects to managing containerised deployments to the edge. It was fantastic to be able to setup the Raspberry Pi on the bin with IoT Edge and then fully manage deployments to it using VSCode and deployment templates. What's next for Trashé The big next technical step for a proper production system is to investigate how to use gathered predictions to further improve the vision model and how to automatically train the model using new data and push to the IoT device if our desired metric has increased. We would like to increase the number of labels and dataset that we use to do a better job of detecting things that people constantly get wrong when recycling. Eg plastic bags often aren't accepted as recycling, bottles need to have their lids taken off. It would also be useful to have Trashé be more of standalone unit. We see it being useful for recycling centers to be able to get a better idea of what the composition from each truck is to get a better idea of specific areas where councils can target education programs. It could also be more useful to monitor the metrics of the kinds of materials coming in vs the materials that are actually recycled to monitor things like contamination rates for specific classes of materials. Further Training Model As mention above, the model currently has a reasonable accuracy that works fine for this proof of concept, however incorporating more and more annotated data would only further better the product. The TACO dataset will be a good group to work with as we can leverage their crowd sourced data, whilst also feeding back in the work we do on annotation. Frontend & Mobile Experience We would like to improve on in the frontend and mobile experience of the system. Most of the work around this project initially has been on the IoT Edge system, and the model for inference; however if we are to productionise this it will need a better user experience for monitoring and resolving recycling events. We would also like to build in some dash-boarding and stats to help users understand what they are throwing away and the impact they can have by recycling. <div