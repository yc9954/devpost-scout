---
slug: "torchexpo"
url: "https://devpost.com/software/torchexpo"
title: "TorchExpo"
hackathon: "PyTorch Summer Hackathon 2020"
organization: "Facebook"
winner: true
words: 818
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# TorchExpo

> Collection of models and extensions for mobile deployment in PyTorch

[Devpost](https://devpost.com/software/torchexpo) · hackathon [[PyTorch Summer Hackathon 2020]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]]
  <sub>weak: legal_professional</sub>
**substrate** [[code_repository]] [[video_visual]] [[web_dom]]

**stack** android, bash, ci, dropbox, heroku, jupyter, kotlin, node.js, pypi, python, pytorch, pytorch-android, react, torchvision

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for torchexpo

## Body

Python Library Docs - Landing Python Library Docs - Image Segmentation Python Library Docs - Image Classification Python Library Docs - Sentiment Analysis TorchExpo Website - Model Details Page TorchExpo Website - List All Models Page TorchExpo Website - List All Publishers Page TorchExpo Video Poster Android Application - Image Segmentation Output Android Application - List All Tasks Android Application - Image Segmentation Input Android Application - Sentiment Analysis Android Application - Image Classification Note: This project applies to both Web/Mobile Applications and PyTorch Developer Tools Category. Please judge it accordingly ☺️ Inspiration Main motivation behind TorchExpo was to simplify research to production deployment for mobile devices. It is inspired by PyTorch Forum's Mobile Category Questions and Tensorflow Hub . What it does TorchExpo is not just a web and mobile application but it comes with a python library as well. The Python library is available via Pip and it helps you to convert a SoTA model in TorchScript and ONNX format in just one line Read the Docs pip install torchexpo The website is for users who don't want to convert and explore all solutions. They can just download already converted models and start using. https://torchexpo.now.sh The mobile application is to support all the use cases where users can download and try all the SoTA models with just few clicks and no expertise. APK Download Link It currently supports Vision (Image Classification, Image Segmentation), NLP (Sentiment Analysis) models. How to convert a Vision model? from torchexpo.vision import image_segmentation model = image_segmentation.fcn_resnet50() model.extract_torchscript() model.extract_onnx() How to convert a NLP model? from torchexpo.nlp import sentiment_analysis model = sentiment_analysis.electra_imdb() model.extract_torchscript() model.extract_onnx() Note : Model variants are currently not supported on mobile and web application (i.e. when you see ResNet, its only ResNet18 on mobile and web, as support for variants is on the way ) How I built it After my work on proof of concept on PyTorch Android, I was exploring ways to try out more models, sadly I couldn't find any go-to solution. I came across the TF Hub website and got to know, PyTorch ecosystem really misses a platform like this! I jumped on to carving the website (backend with frontend) and the mobile application. I later carved a library from all my learnings and thought, instead of me hosting, how easy it will be if people can convert on their own? Python library is built on top of TorchVision and HuggingFace's Transformers. It gives API and modules for easy extension ( Source Code ) The website is built using React and Javascript and hosted on Vercel ( Source Code ) The backend which serves the REST APIs is built using Node.js, MongoDB and hosted on Heroku ( Source Code ) The mobile application is built using Kotlin, Android Architecture Components, PyTorch Android and lot of custom classes to support models ( Source Code ) Challenges I ran into One of the main challenge was to support SoTA models on Android which required lot of tensor-like operations to be written for Android. Another interesting challenge was to design the library to make it minimal, intuitive and still easy to use. Working on NLP tasks on mobile application along with HuggingFace gave lot of tough days. Apart from that, working on CI/CD for smooth deployments of both mobile application and website, working on CI for python package and the documentation was really challenging. Accomplishments that I'm proud of Releasing alpha versions of website, mobile and package all by myself on time. Challenges I overcame while building the mobile application's tough operations and python package. But also proud that I will be supporting this project full-time after this hackathon to improve it, make it open to community for contributions and also work with some core maintainers (I am looking for them!) What I learned I learnt alot about mobile deployment for machine learning models during this hackathon and how tricky it is on low resource devices, which helped me carve this solution. How tricky it is to launch a product was my constant feedback to myself. How to make a minimal yet pleasing(I think so) presentation video and that recording needs to be done late at night with silence :) I learnt failures are part of this new remote hackathon (being my first one), where you find yourself working on different things every new week. One has to tame their wild ideas and with proper care and training, turn them into magnificient beasts. What's next for TorchExpo Working on making the repository and the ecosystem around it stable (Looking for core developers to contribute to this project) Making SoTA model variants available on website as well as mobile Support much needed Caffe2 Mobile format (e.g. Advance Tutorial) for extraction along with Quantization (e.g. Dynamic and Static) Begin with iOS Development, followed by Google Play Store and iOS App Store Release Opening up to community for more official/research models <div