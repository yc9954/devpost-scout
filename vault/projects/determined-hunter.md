---
slug: "determined-hunter"
url: "https://devpost.com/software/determined-hunter"
title: "Determined Hunter"
hackathon: "Determined AI Model Training Hackathon"
organization: "Determined AI"
winner: true
words: 702
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/security_privacy"
  - "domain/transportation"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Determined Hunter

> We teach our GPUs to bust Malware!!

[Devpost](https://devpost.com/software/determined-hunter) · hackathon [[Determined AI Model Training Hackathon]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[security_privacy]] [[transportation]]
**substrate** [[structured_db]] [[video_visual]]

**stack** bash, determined, determinedai, docker, kubernetes, python

## How they structured the write-up

- introduction
- network data and graph convolutions
- determined ai
- the core api
- pytorchtiral
- accomplishments
- what's next for determined hunter
- acknowledgements

## Body

Determined Hunter Logo. Model capture with checkpoint monitoring. Hyperparameter search-space. Confusion matrix and heatmap in synergy! Validation-loss graph uncovering overfitting Hyperparameter choice made easy. Determined write-up TLDR: We teach our GPUs to bust Malware!! Introduction In this project we explore the capability of ML to detect Malware. In-Memory The first step focuses on the detection of malware in memory dumps. Malware often resides in the memory of a computer to avoid detection from anti-virus software. The memory dump is a snapshot of the memory of a computer at a given time. Since this is boring tabular data, we normalize the numeric columns and use a simple MLP to classify the data. Once training the MLP yields success, we move to the coolest trend of the century: throw transformers at everything 🏌🏽‍♂️ MalMem Dataset No, this is not an Altzheimer dataset! This dataset consists of memory dumps, labeled as malware or benign. Each Malware is categorized further into subclases. More info Network data and Graph Convolutions In a second step we focus on network data. This step requires more prior worq since curated datasets are not available. The approach is to gather pcaps from incidents, extract the network data with zeek , and label the data according to the incident. From here on we can build a graph dataset using the IP addresses as nodes and the network traffic as edges. Now the power of Graph Convolutions can be fully released ❤️‍🔥 Determined AI The author of this repo dreamfully wishes to have had access to the Determined AI platform during this thesis-project. Determined AI enables distributed training and hyperparameter search/tuning, while adding minimal overhead. Ode 2 Determined AI A homenage to the Determined AI platform. The following are cherry-picked screenshots of the Determined UI during the experiments of his project. The descriptions are of both explanatory and insightful nature. Written in colabotration with Captain Obvious . The Core Api The core api offers us extended flexibility, on the costs that it is slightly more complicated to set up. The first view shows the validation loss over epochs. Here we can see how our model overfits on out dataset. Obviously it should go down correlating with the training loss. Arguably the most valuable plot are the hyperparameter plots over validation loss. The versus plots help us to easily detect the better params. Dropout is a special case as a high dropout might need more epochs to proof beneficial. The hyperparameter search space is my favorite!! I always wanted to play around with these filters on my own model. The classic confusion matrix. The heatmap makes this the most appealing plot! Personally is scores second on the added-value scale. Undoubtfully it will benefit from more runs aka more data-points. It would be cool to be able to drag-drop them around to change the position of the plots. PytorchTiral This is the easy-going way which also lets you register your model on the Determined UI. For this experiment we set normalization and the granularity of the labels as searchable hyperparameter. Again, the beautiful search space, this time with even more hyper-parameters. Results show that not normalizing does not hurt the binary classification. The vs plots, always a win: The confusion matrix seems to not work for values of different types, such as float and bool. The author of this repo considers opening a feature request for this. Finally the model hub. Only thing missing here is a hotlink to upload our model to huggingface 🤗 Accomplishments While it took a couple hours of deep-diving into the Determined Documentation, we are proud to have set up the Cluster locally with both Docker and Kubernetes. This sets us up for a whole new type of ML meetups where everyone brings the GPU along, connects to the local network and participates in hyperparameter-search. A working docker-compose.yml is included in the projects repo. What's next for Determined Hunter step-one: Objective Secure ✅ step-two: engaging target 🎯 Step one of detecting malware in memory dumps has been a success! We move on to unchartered territory and engage with networq data. Always on the hunt for bad-guys! Acknowledgements Thanq you Determined AI team for this flabbergasting platform! 🤍🐧🤍 Stay secure! <div