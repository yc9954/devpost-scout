---
slug: "pixelart-97woqd"
url: "https://devpost.com/software/pixelart-97woqd"
title: "pixelart"
hackathon: "Go Hack"
organization: "Google"
winner: true
words: 302
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "substrate/video_visual"
---

# pixelart

> Generate old school / arcade pixel art from your mobile pictures and so on

[Devpost](https://devpost.com/software/pixelart-97woqd) · hackathon [[Go Hack]]

## Facets

**domain** [[developer_tools]] [[education]]
**substrate** [[video_visual]]

**stack** css3, github, go, heroku, html5, javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pixelart

## Body

me eiffel_tower mario_90 milano Inspiration Actually building poln.org , I want to provide something funny for profile pictures. There are many solution on the web but I don't trust them: not performant, no open code sources, etc. So I've decided to build mine. What it does It takes a png or jpeg picture and apply many filters on it in order to generate a pixelart. It's a simple open and free open web service. Just pick up your picture, select your filter and it will do the job. You can rotate the picture if the orientation is not preserved. btw, rotation is animated. How we built it At first, it was a command line tool and then a web service. Using golang, its goroutines, templates, Gin, heroku, javascript, etc. The best language for this kind of tiny side project. Challenges we ran into image processing is always hard, I've made it many years ago using C/C++ and it was hard. Very easy with golang and very performant as well. Coding old filters (CGA4, EGA) or more recently (convolution) was the harder part. Graceful shutdowns were also very fun to code. Configuring Heroku was not so easy as well (at first, build an exec and then a docker image that other can reuse on their k8s clusters for eg.). Accomplishments that we're proud of Many people play with it and I can generate pictures like in the 80's :-) What we learned I've learnt to use Gin, awesome package and the validators. Oh and it was my first time with golang 1.18 and generics. What's next for pixelart Could be cool to generate NFT from pixelarts... the devops pipeline produces docker image so the microservice can be deployed and used everywhere, planning to deploy it on a more resilient platform than Heroku <div