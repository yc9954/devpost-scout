---
slug: "debug-d5cypg"
url: "https://devpost.com/software/debug-d5cypg"
title: "Debug"
hackathon: "Hack the Northeast"
winner: true
words: 636
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "user/frontline_worker"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Debug

> Using machine learning to increase farmer profits by determining whether or not observed bugs are beneficial for their crops. Slogan: Don't let bugs eat your profits!

[Devpost](https://devpost.com/software/debug-d5cypg) · hackathon [[Hack the Northeast]]

## Facets

**domain** [[agriculture_food]]
**user** [[frontline_worker]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** apache, bootstrap, css3, html5, javascript, tensorflow.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for debug

## Body

Logo GIF Pest Image Classification (Website Version) GIF Debug (Mobile Version) Inspiration Farmers rely heavily on crop yields as their main source of income. However, many pests can get in the way of optimal production yields as they can eat and harm the field crops. Pesticides are commonly used by many farmers to get rid of them. Despite that, the large quantities of pesticides used to spray on acres of farmland can be expensive, and many times, farmers misuse pesticides on the wrong bugs. The overuse of pesticides has many consequences which can cost farmers money, time, and resources: First, the EPA estimates up to 70 million pounds of pesticides are lost to drift each year , a common issue in which extra pesticide chemicals are carried by the wind, hurting the ecosystems, the farmer's wallet, and human health. Second, an overabundance of pesticides on the wrong species can lead to pesticide resistance . As a result, pesticide costs should be expected to increase as new variations of the pesticide are more expensive. Third, spraying pesticides on beneficial pests can negatively impact the production rate of the farmer's crops, which is a waste of money. These effects worsen each year, causing rural/small farmers to lose thousands of dollars, as on average, they spend around $21,000 on pesticides alone as of 2019. This number will only increase in the coming years. What it does This is where the Debug application comes into play. Using Debug, farmers can upload a picture of a recurrent bug they observe in their fields. Once uploaded, they are provided with a summary of the pest and whether it is harmful or not, along with some potential pesticides or alternatives they could use. This way, the farmers can reduce the money spent on warding away bugs that appear to be pests but are not. How we built it HTML5 and CSS3 were used for structure and styling. Javascript was implemented for responsiveness, in particular for the drag and drop/upload feature. Tensorflow.js was used for the image classification machine learning feature. To obtain the images used for training, a mixture of the ImageNet library and Google Images were used. The datasets were trained using Teachable Machine . We used Cordova (an open-source software that creates mobile applications using the HTML, CSS, and Javascript code of web applications) to make the Android version of Debug. Challenges we ran into The most challenging component of this project was definitely the machine learning aspect. There were many image Javascript libraries available, so it took time to find the best fit for this application, which turned out to be TensorFlow. Another complicated feature turned out to be the drag and drop feature. There were not many resources online. Despite this, Daniel found a way to implement it with some scrounging. Overall, many of our issues were quickly solved as each of us had varied skills and open minds. Accomplishments that we're proud of We are proud to have implemented an image classification model to real-world applications such as the ongoing food crisis and the overuse of pesticides in a short amount of time. All of us applied our strengths and learned lots of new skills along the way! What we learned This was the first time many of us have attempted machine learning, so we learned a lot about model training, incorporating datasets, and integrating it into a user-friendly platform. What's next for Debug As of now, Debug can only classify locusts, armyworms, honey bees, and earwigs. We are planning on expanding our database of bugs and making the algorithm more accurate. Additionally, we will include an option for farmers to input the crop on which they found the insect so pesticide recommendations do not harm the crops. We will also develop an iOS version of Debug. <div