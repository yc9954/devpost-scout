---
slug: "intelliscraper-yolov3imagescraping"
url: "https://devpost.com/software/intelliscraper-yolov3imagescraping"
title: "IntelliScraper-YOLOv3ImageScraping"
hackathon: "MLH Local Hack Day (2018)"
winner: true
words: 141
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# IntelliScraper-YOLOv3ImageScraping

> IntelliScraper scrapes images from any website and then refines them using ML to produce accurate datasets.

[Devpost](https://devpost.com/software/intelliscraper-yolov3imagescraping) · hackathon [[MLH Local Hack Day -2018-]]

## Facets

**mechanism** [[benchmark_measured]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** machine-learning, opencv, python, urllib, yolo

## How they structured the write-up

- what is intelliscraper
- how to run

## Body

IntelliScraper Sub-folder containing intelligently refined dataset. IntelliScraper-YOLOv3ImageScraping What is IntelliScraper This is an intelligent image scraper for the web that uses a simple python web scraper to generate images which are then refined based on output from a YOLO v3 Deep Learning model that extracts only the required images of objects and stores them in a separate sub-folder. How To Run Download weights of model from the following link and paste in IntelliScraper folder: https://pjreddie.com/media/files/yolov3.weights Run the following command for searching for some image on google for e.g. apple: python script.py --search apple Or add optional parameters like the number of images to download: python script.py --search apple --num_images 20 Run the following command to refine the acquired dataset intelligently: python yolo_opencv.py --apple The "yolo_opencv" will create a subfolder "Intelliscraped" inside the fodler with the images with refined images automatically. <div