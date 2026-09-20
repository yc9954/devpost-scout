---
slug: "yogacam-live-map"
url: "https://devpost.com/software/yogacam-live-map"
title: "yogaCam: Live map"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 1123
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# yogaCam: Live map

> Feel the warmth of a mindful community with this AI-enhanced yoga experience. Twinkle twinkle little star (pose).

[Devpost](https://devpost.com/software/yogacam-live-map) · hackathon [[Azure AI Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[voice_speech]]
**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** azure, figma, machine-learning, react, speechapi

## How they structured the write-up

- inspiration
- yogacam: live map
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for yogacam: live map

## Body

System architecture Frontend prototype Running application - screenshot Inspiration Yoga is something I do for myself, however, I really appreciate the feeling of the quiet connection with others. Either someone at the mat next to mine, the instructor from a good video class, or simply just knowing someone else is probably doing the same. Given that, I came up with the idea of virtually share yoga sessions with others. Taking a glance in the comment feed of, for example, Yoga With Adriene , it's evident how these yoga sessions make an impact on many people's lives and well-being. Especially these times. At the same time, I feel inspired by virtual training apps like Zwift for biking and of course, yoga practice should have its own space as well. 🌠 yogaCam: Live Map The yogaCam Live Map is a web application for users to keep on while practicing yoga that will recognize and visualize all ongoing activity of a certain yoga pose in real-time. On a map, each individual sees a bright spot for all other people who do the same pose at that moment. Change pose and marvel at the new group of people you share the moment with around the world. How I built it The implementation has three main parts; 1. system architecture and setup of Azure resources, 2. training the yoga classification model, and 3. creating the user application and integrating the AI models and Azure SDK:s. (For more implementation details, please visit my GitHub repo SaraOlsson/yoga-map-ai where I've included a guide to reproduce the application) Azure resources Azure Maps Custom Vision Service Speech API (text-to-speech) Azure Storage Account with Blob containers Service Bus Topic Each client is a React application that communicates with a set of services that lives in Azure. The classification model is published as a Prediction API. Knowing what is the current position, data messages are read and written through an Azure Service Bus Topic. The camera snapshots are uploaded to a Blob Storage if the user agrees to train the model with new data (hidden feature in the live demo). I have provided an ARM template to provide reproduce the infrastructure under the AzureResourceGroup folder of the Github Repo. ARM templates use a declarative syntax to get the required inputs from the user, thus enabling the user to redeploy the infrastructure with minimal effort. Yoga classification model My process was : collecting a dataset (I used the images found here , collected by Anastasia Marchenkova). The training dataset has 10 classes and around 60 images per class. Each class also has 5-10 images to use for test or validation. I removed some images from the dataset that were sketches rather than real images, and instead created my own data to extend the dataset. uploading images and train classification model in the Custom Vision studio (using a Compact domain, with is optimized for the constraints of real-time classification) deploying the model as an API endpoint for usage in web application Map web application First, I created a quick prototype of the visual appearance I imagined of the application in Figma. From there, I created a React project and implemented a set of critical features: a map component, webcam access and capture, audio component, and SDK setups. Client communication I have prepared logic to send and receive messages to the cloud through a Service Bus Topic (however this feature is turned off in the published live demo). When the image analysis returns the current yoga pose, a message containing pose+coordinates is sent to the Topic which can have many subscribers. The client also receives messages from a subscription instance and will draw a dot on the map for each message which contains the same pose. Figure: peeking at a message in the Service Bus explorer Challenges I ran into Running inference locally. From the Custom Vision service, there are several options for model export. One option is to download the model to be used with Tensorflow.js which I managed to get running in a small javascript solution. However, I encountered some issues while trying to integrate with the React project. Instead, I deployed the model to a web service which is a good option too, although the user could more willing to keep the camera on if images were not sent to the cloud. I had some problems with the Azure map, where sometimes the dots did not clear from the previous rendering (or due to something I did not get right when implementing) Accomplishments that I'm proud of integrating the AI model to a working application using continuous image capture from a web camera. that I managed to make use of several Azure AI features, both custom vision and the speech API coming up with a suitable capture and analysis interval. As the image analysis triggers the voice synthesis, I had to either skip some voice playbacks or perform image analysis less often. In many yoga practices, there are short times of changing position followed by a longer static pose, and of course, the user doesn't need to hear 10 times that "warrior pose" was recognized. I added logic to deal with this issue, looking at the time difference and the previous position. What I learned Hands-on with Azure AI in a client application Working with Service Bus Topics Using the Azure Map resource What's next for yogaCam: Live map I feel eager to continue with this idea! Next steps would be: Model refinements. One option would be to improve the dataset for the classification model, especially by adding more training data and which also should include images from a home environment rather than with white background. Another option is to look into using a pose estimation model. Model customization. For a single person practicing yoga at home, the background and pose variations would be somewhat static, while it can differ from someone else. Letting users fine-tune a customized model with their own images could give them a more accurate model to use in return. Being able to extend classes for the model, which should of course also be a seamless experience. If the model doesn't recognize a certain pose, use the Azure AI speech-to-text to tell the application to start saving new training data for the specified pose - while performing it! Extending the application to be able to make summaries of yoga sessions based on recognized poses Adding more settings to the client application, like sign up/sign in, entering location, etc. Looking into scaling and ensuring performance (in the best of worlds the application goes viral..🌎) Hope you enjoyed this project and please let me know what you think :) Credits: open-source packages (listed in GitHub repo) and yoga illustrations created by monik <div