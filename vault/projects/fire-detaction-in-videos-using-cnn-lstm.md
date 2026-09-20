---
slug: "fire-detaction-in-videos-using-cnn-lstm"
url: "https://devpost.com/software/fire-detaction-in-videos-using-cnn-lstm"
title: "violence Detection in videos using CNN + LSTM"
hackathon: "2020 Facebook Developer Circles Community Challenge"
organization: "Facebook"
winner: true
words: 392
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/web_dom"
---

# violence Detection in videos using CNN + LSTM

> violence detection in videos is a hot topic in ML , here in these work we will focus on the import blocks for building such video based model

[Devpost](https://devpost.com/software/fire-detaction-in-videos-using-cnn-lstm) · hackathon [[2020 Facebook Developer Circles Community Challenge]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]] [[researcher]]
**substrate** [[web_dom]]

**stack** flask, pytoch, pytorch

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for violance detaction in videos using cnn + lstm

## Body

Inspiration PUBLIC SAFETY , and AI for good is one of my goals when i strated learning ML in 2014 , my country (iraq) face a lot of problems regarding security and public safety , i did published a paper for violance detacton in videos a year ago during my master study and figured out that many other developer and researcher have used my paper and code the old code was in tensorflow i decided to build one in pytorch , i do find many developer have faced problem with build such video based model in pytorch , if we do search for (timedistributed in pytorch) you can get alot of urls which many developers asked for implmention that can warp a 4d tensor into normal Conv2d and all awnsers either not work or not give a councrate example to others so thy can use it here is some of these url ( https://discuss.pytorch.org/t/any-pytorch-function-can-work-as-keras-timedistributed/1346/22 , https://discuss.pytorch.org/t/timedistributed-cnn/51707/2 , https://discuss.pytorch.org/t/solved-concatenate-time-distributed-cnn-with-lstm/15435/6 , https://stackoverflow.com/questions/62912239/tensorflows-timedistributed-equivalent-in-pytorch , https://stackoverflow.com/questions/61372645/how-to-implement-time-distributed-dense-tdd-layer-in-pytorch ) also using lstm within Sequential pytorch model found to be rare used case and there is some developers asked for help in this What it does the final model can be used as api for violance detection in videos while the tutorial is pointing out and explain the main blocks for build such model which is time warper and video dataloader How I built it using pytorch to build a video action recogantion model using a pre-trained Conv2d model with LSTM Challenges I ran into it is rare that you find a problem that is general and yet no concrete solution or code for it in the internet so these let me do alot of search and reading in the pytorch refreance and also keras repo to mimic it way of doing this ( keras time distrbution warpper ) Accomplishments that I'm proud of wrtting my first tutorial , and build some custom code not writing before in stackoverflow or main tool fourm and helping other What I learned pytorch is very open to do any customization and that can help me do advance research topics in it instead of using tensorflow What's next for violance Detaction in videos using CNN + LSTM build larger one with more classes not only give if there s a violance or not also recognize the violance action type trying different algorithms <div