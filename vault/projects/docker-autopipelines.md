---
slug: "docker-autopipelines"
url: "https://devpost.com/software/docker-autopipelines"
title: "Docker ML Studio"
hackathon: "Docker AI/ML Hackathon"
organization: "Docker"
winner: true
words: 871
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "user/developer"
  - "user/general_public"
  - "user/researcher"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Docker ML Studio

> A Docker extension for building PyTorch machine learning models without coding.

[Devpost](https://devpost.com/software/docker-autopipelines) · hackathon [[Docker AI-ML Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[vision_ocr]]
  <sub>weak: cross_origin_web</sub>
**domain** [[developer_tools]]
**user** [[developer]] [[general_public]] [[researcher]]
**substrate** [[structured_db]] [[video_visual]]

**stack** docker, python, pytorch, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for docker ml studio

## Body

Home screen Model builder Main page of the Studio Training process Docker ML Studio Docker extension to build and run PyTorch machine learning models. Inspiration The inspiration for Docker ML Studio stems from a fundamental desire to democratize the field of machine learning. We recognized that while the potential of AI and ML is boundless, the complexity of coding and deployment is a significant hurdle for many enthusiasts, researchers, and businesses. This inspired us to create a platform that would break down those barriers and make machine learning accessible to a wider audience. We wanted to empower individuals and organizations to harness the power of machine learning without the need for extensive technical expertise. Our vision is to bring the future of machine learning into the present by streamlining the entire ML lifecycle, making it intuitive and user-friendly. Through Docker ML Studio, we hope to inspire a new wave of creativity and innovation in the field, driving AI solutions across various domains with ease and efficiency. What it does Docker ML Studio is your gateway to the future of machine learning. Designed to streamline the entire ML lifecycle, our Docker extension empowers users to effortlessly create, train, and deploy models with unprecedented ease. Say goodbye to coding complexities; our user-friendly interface paves the way for designing neural networks without the need for coding expertise. With just a few clicks, you can deploy your models, eliminating the hassle of traditional deployments. How we built it We create a Docker extension with the ability to make deep learning models without the necessity of programming. All the code runs on Docker containers, and the data is shared through Docker volumes, allowing us to combine datasets and models on the same computer. Challenges we ran into We ran into several challenges, mainly related to communication between datasets and models and making a user-friendly interface. For example, we can mention the next challenges: Create the datasets : we need to find a way to save the user dataset in a persistent way to avoid changes or deletions. We find valuable the use of Docker volumes that allow us to quickly share datasets between models. However, due to the restrictions of React, we find problems (and possible future bugs) accessing to the file system of the user. Save the model : our interface allows the user to use only drag and drop to create deep learning architectures. However, we need to transform this model in PyTorch's code in order to execute it. We decide not to build the model in the frontend but in execution time; therefore, we save the model as a JSON that, because of time, we only allow sequential models. Launch experiments : initially, we want to use TorchX to run our models, but we face several problems launching torchx using only React (maybe we need to use the Go backend in the future), so we decide to create our own image to run PyTorch models using only the packages that we think are essential. Deploying models : we use TorchServe to deploy our models, and with a few configurations, we were able to deploy our models easily. Accomplishments that we're proud of Although we couldn't finish our project as we wanted, we were able to create a prototype with the basic functionality that we wanted. Our project is helpful for people who don't want to code in PyTorch and only want to add layers after layers in a very friendly interface. We consider that our prototype has the ability to be extended in order to create a tool ready for the industry, and this can help people that don't know anything about PyTorch or want an interface and user experience similar to products like Amazon SageMaker or Google Vertex but running locally. If our final user has installed Docker Desktop, then he or she will potentially have a tool to create any deep learning model he or she wants, and we are proud of our small contribution to democratizing machine learning. What we learned Both developers have only an intermediate knowledge of Docker and PyTorch. This project was an opportunity to learn new technologies like React, and although we are not very confident as frontend developers, we were able to build a user-friendly interface. Docker extensions were one technology that we loved, and we hope to contribute in the future to the Docker community creating new extensions. What's next for Docker ML Studio As we mentioned above, this is only a prototype with very limited capabilities. We are pound of our project, and we want to see it released to the public. At the moment, our project only works for image datasets and sequential models. We want to extend our project to work with multimodal architectures and complex neural networks. Also, we find it useful to have pretraining models and pre-defined architectures, so, in the future, we want to add more vision models, add NLP architectures and try to add hugging face pretrained models to our interface. Finally, we know that the information shown while we are running containers is not very informative, it would be better to find a way to show the logs in a user-friendly way for non-coding users. <div