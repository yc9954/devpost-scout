---
slug: "global-fire-spread-prediction-system"
url: "https://devpost.com/software/global-fire-spread-prediction-system"
title: "Global fire spread prediction system"
hackathon: "AWS Disaster Response Hackathon"
organization: "Amazon"
winner: true
words: 882
team_size: 9
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/disaster_emergency"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "user/frontline_worker"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Global fire spread prediction system

> The tech team at Satellite Vu applied our knowledge of wildfires, satellite imagery and machine learning to demonstrate a fire spread prediction system which could be applied globally

[Devpost](https://devpost.com/software/global-fire-spread-prediction-system) · hackathon [[AWS Disaster Response Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[disaster_emergency]] [[finance_payments]] [[supply_logistics]]
**user** [[frontline_worker]] [[researcher]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** keras, numpy, python, s3, sagemaker, scikit-learn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for global fire spread prediction system

## Body

GIF Fire prediction mapping on Sentinel-2 layer GIF Fire prediction mapping on top of open street map Predictions of the deep learning model Inspiration For this challenge, the tech team at Satellite Vu applied our knowledge of wildfires, satellite imagery and machine learning to demonstrate a fire spread prediction system. Satellites offer wide area coverage in near real time, and can access even the most remote locations. Accurate prediction of fire spread could improve disaster response, for example to identify towns or properties in the greatest immediate risk What it does We used data from the MODIS and VIIRS satellite sensors, which provide long-term observational records in multiple spectral bands, as well as elevation and land cover data to make predictions with both traditional machine learning and deep learning models. The models predicted the next day's fire pattern with higher precision and recall than the baseline model of fire persistence. How we built it We used open access data hosted by AWS combined with fire mask data to create a generic training dataset consisting of stacks of images. We then trained two kinds of model on the dataset; classical logistic regression & random forest models using 3x3 patches of pixels, and a deep learning model using a custom u-net on the entire image. We then created web apps to visualise the model predictions, which consists of the predicted fire movement overlaid on a map, with towns & buildings at risk highlighted. All processing was performed using python, with AWS Sagemaker Studio Labs providing compute & GPU time, and using AWS S3 for storage of data. Challenges we ran into The main challenge from a machine learning perspective is that the dataset is very imbalanced. Roughly 99% of pixels in an image did not contain fire, leaving only 1% of pixels with fire which we wished to predict the movement of. Without accounting for this imbalance, a naive model will simply learn to predict all pixels as not containing fire, resulting in meaningless predictions! Some experimentation was required to determine approaches to dealing with this imbalance, as documented in the project notebooks. Additionally, we had time-boxed the hackathon to 2 weeks duration, which resulted in quite a limited amount of time for model training since this could only begin once the dataset was created and data quality checks completed. Nevertheless we successfully trained models which beat the baseline persistence model and managed to complete all activity within the 2 weeks. Accomplishments that we're proud of This was the first project that the entire tech team had contributed to, with some team members having only joined the company a couple of days prior to beginning the hackathon. Owing to having time-boxed the hackathon to 2 weeks, careful planning of all tasks was required prior to kicking off the hackathon. During the hackathon itself there was vibrant and energetic collaboration between team members over Zoom and Slack, with very limited office time for more traditional styles of working. Overall the team showed they can work effectively together, under challenging remote conditions and to a deadline. We particularly wish to highlight the incredible work of our junior team members Jade & Isobel who took on the challenge of creating the 3 minute video. A presentation of this video to the wider company was received with very high praise for the videos quality and effectiveness; an achievement which is all the more impressive considering neither Jade or Isobel had worked on a video like this previously What we learned To quote President Eisenhower, 'plans are nothing; planning is everything', and this proved very true in our experience during this hackathon. Particularly with machine learning projects, there is no simple formula which can be followed to generate a plan, but what is crucial is the effective communication and collaboration between the team members during the planning phase and after, during execution. For example during planning, multiple rounds of discussion took place in order to identify all assumptions about the data quality and characteristics, and this conversation continued during exploratory data analysis (EDA) and model training. Without this attention to detail during planning, the issues which inevitably arose during modelling could have been far more significant, and easily derailed the level of success achieved in a 2 week sprint. What's next for Global fire spread prediction system The fire imagery used in this project was relatively coarse in spatial resolution, with pixels being 500 meters in dimension. Satellite Vu will soon be launching a constellation of high resolution thermal imaging satellites, enabling a resolution of fires with 3.5 meter pixels, representing a huge improvement in spatial resolution. We hope that this will enable a significant improvement in the accuracy of fire prediction models, enabling first responders to make better judgments in fast moving fire situations, particularly around densely populated areas where high resolution predictions are crucial. Since the project was time-boxed to 2 weeks, there remains significant scope for improvement in the accuracy of the models, by exploring approaches such as adding new features to the dataset and experimenting with model architectures and parameters. By open sourcing the dataset, code & models we hope to enable more researchers to engage with this crucial application for machine learning; to predict the path of fires and ultimately to save lives <div