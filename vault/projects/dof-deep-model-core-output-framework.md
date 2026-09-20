---
slug: "dof-deep-model-core-output-framework"
url: "https://devpost.com/software/dof-deep-model-core-output-framework"
title: "DoF - Deep Model Core Output Framework"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 908
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/legal_justice"
  - "user/developer"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/financial_record"
  - "substrate/regulation_legal_text"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# DoF - Deep Model Core Output Framework

> DoF is a highly scalable dataset format which helps deep learning scientist to work with foreign and/or sensitive data. DoF provides fast dataset sharing and data-secure at the same time.

[Devpost](https://devpost.com/software/dof-deep-model-core-output-framework) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**domain** [[developer_tools]] [[health_clinical]] [[labor_employment]] [[legal_justice]]
**user** [[developer]] [[patient_family]] [[researcher]]
  <sub>weak: clinician</sub>
**substrate** [[financial_record]] [[regulation_legal_text]] [[structured_db]] [[video_visual]]

**stack** python, pytorch, tensorflow

## Body

logo_white logo_landscape Normal train flow DoF train flow Imagine, the world is better tomorrow, than today. What is the difference? What if everybody tries to make something little change? The difference is this “what if”. There are two types of inventions. One group of them makes huge impact on the peoples daily routine. Those are a game-changers. The other type of ideas are different. These are very small and basic concepts with only one goal: made the piece of world a little bit better or effective. We do not want to revolutionize people’s life, we do not want to twist upside-down the world. We want to make a tiny but significant change with our idea. The born of the idea We are two deep learning developers who suffer from typical developer issues: the resource scarcity and legal boundaries like General Data Protection Regulation (GDPR) in European Union. We made a healthcare software to help doctors make a better, faster, and more precise diagnosis about pulmonary disease. For his point it sounds, there is no something unique in the software. Our intent was duplex: to build a robust model or maybe a chain of networks and to reach this target with using the software in resource-scare environment. In our country the computers in hospital are old without GPU and the hospitals do not have the necessary financial support to buy new ones or to pay for cloud-based solutions. Beside the financial issues, there is a legal burden. The data that come from healthcare system can be used very straight, clear and predetermined way due to data protection of patient. Health data is protected extremely in the most countries. We made an opportunity to train our model faster and be able to use the health data without violate the regulations and without the preliminary contribution statement from patient for deep learning usage. How can these goals be reached? We optimize the training and evaluation phase by calculating the repetitive tasks only once and we anonymize the data. Our software contains different and independent neural networks. Each of them is trained separately. Detecting pulmonary diseases on X-ray images is an image detection and image processing task. We use headless pretrained model to make the necessary detection and preprocessing tasks. However, we use different AIs, each of them builds up similarly: a headless pretrained model is connected to our network. We can save a huge amount of time with feed the pretrained model only once and save it’s output. There is no need to repeat over and over the same process on the same picture again since the result will be the same every time. Our idea is born here. If we save the output for example a ResNet or VGG network, why should we drop these data to trash at the end of the process? We decided to create a unique and new file format that not only contains the output data of headless network, but extra additional information. This container file is much more than a dataset. Let’s see an example. There is a COVID-19 X-ray dataset from github ( https://github.com/ieee8023/covid-chestxray-dataset ) that obviously contains images and metadata. However, it contains sensitive health data connected to patients. These pictures may be able to use scientific purposes, but a lot of country forbids using similar datasets for commercial usage. Using pretrained model with any type of pooling layer can anonymize the unique element of original dataset. From the result of pretrained headless model cannot be restored the original data since the pooling layers make reversibility proof destruction on data. However, there is necessary to get contribution statement from patient, but with this method the model easily wipes the dataset from personal or person-connected health. This part is very important if you handle data from patient connected to European Union due to GDPR. Advantages of our idea Using our container file has multiple advantages. A preprocessed data consumes less space than the original picture. The global internet bandwidth has it’s own limitation. During an epidemic crisis when people have to be at home and use the internet whole day to work or to get news, we have to spare with bandwidth. Big companies and web services like Facebook, Instagram, Youtube, Netflix announced to limit the dataflow in European Union by reduce quality of video stream. One megabyte of an uncompressed image 24bit-RGB image contains approximately 349 920 pixels, that equals to 486 x 720 resolution. With jpg compression the size can be reduced or the resolution can be increased. Comparing the size of image, the container file has very small size. The output of a headless model is under 10 Kilobyte. Whether we add a lot of information to it or not, the size of container file can be holded under the size of processed image and it’s metadata. Loading preprocessed data from container file reduces training time in two ways. First of all there is no need to run and to load the pretrained model into the memory. Secondly, we can use higher batch size which reduce the training time dramatically not just on expensive hardware but on low-end machines too. Preprocessors are able to comment notes and add additional information or data to the container file that helps the user to reproduce the training process or build something complex. For example, the preprocessor author can note the data as train, test or valid data, or can suggest network architecture. <div