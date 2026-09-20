---
slug: "thiea"
url: "https://devpost.com/software/thiea"
title: "Theia"
hackathon: "TreeHacks 2023"
organization: "Stanford TreeHacks"
winner: true
words: 424
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "user/researcher"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Theia

> A simple interfaced supervised model to build and filter Labeled Image Data Sets

[Devpost](https://devpost.com/software/thiea) · hackathon [[TreeHacks 2023]]

## Facets

**user** [[researcher]]
**substrate** [[structured_db]] [[video_visual]]

**stack** css, ddg, fastai, flask, pytorch, react, requests, selenium

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for theia

## Body

Theia Main Poster Inspiration Every Core Innovation in ML comes from a better architecture, more compute or more and better Data. While Architectures are freely published on the web and Compute, though expensive, is still accessible by anyone on the planet, the moat of most ML companies lies in Accessing Data. Even though most data is freely available on the web, most indie Researchers and Data Scientist have to drop the project, until the Dataset becomes publicly available on the internet. But What if Accessing Data was easier? What it does Introducing Theia: A simple interfaced supervised model to build and filter Labeled Image Data Sets. The easiest dev tool to Download and Filter Image datasets in Minutes not days! How we built it The front end is built using React. First the user simply inputs the keywords for the dataset, just like one would simply do in Google or any Search Engine Next, the user can adjust various parameters for the images, including colour, size, NSFW/NON-NSFW, Image Licences. We use Selenium, DDG and Request, to scrape the best matching images across the web. After that, the user selects the images he likes and dislikes and we use that as Input for the supervised learning Image Classifier built using transfer learning on top of ResNet34. Now the scraping bot built with Selenium, DDG and Requests, download the images and pass it through the and the supervised model built using transfer learning on top of ResNet34. And the user gets the images that classifies as the liked images (as selected by the user in previous step). That's it! Building Datasets has never been easier! Theia cuts out image filtering tasks by upto 90%! Download and Filter Image datasets in Minutes not days! Challenges we ran into CORS Issues are the worst Aligning Divs Web Dev is annoying as hell Next time we are building LLM guided frontend builder Accomplishments that we're proud of Coming up with an idea, that solves a very real problem and will be used by hundreds, if not thousands of people Integrating ResNet34 to apply Transfer Learning to filter image datasets Shipping the project on Time What we learned Having a clear roadmap and an idea of where you are heading is very important Simple Ideas, with high usability are perfect hackathon builds TL on ResNet34 work surprisingly well on a small batch size of 50-100 images What's next for Theia Adding more efficient image filtering options, better UI, and adding more image manipulation options from OpenCV2 Image manipulation capabilities <div