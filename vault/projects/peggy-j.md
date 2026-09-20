---
slug: "peggy-j"
url: "https://devpost.com/software/peggy-j"
title: "Peggy J."
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 558
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Peggy J.

> So you've got a lot of pixels in your image but you want less pixels. Peggy will resize your image with a single simple request. No login and no setup. Give us an image URL, get a resized image. Done.

[Devpost](https://devpost.com/software/peggy-j) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[agriculture_food]] [[developer_tools]]
**user** [[developer]]
**substrate** [[video_visual]] [[web_dom]]

**stack** amazon-web-services, babel, cli-progress, codebuild, cron, elastic-beanstalk, express.js, jimp, moment.js, mongodb, mongoose, node.js, s3, webpack

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for peggy j.

## Body

Peggy J. Inspiration I've used media management software like Cloudinary for years and while that sort of software is feature rich and works well, most of the time it's just too heavy duty for my needs. 99% of the time I don't need to crop images or detect animals or make the background transparent. Most of the time I just need a tool that can resize my images on the fly so that my site can load as fast as possible. That's why I built Peggy J. (named after the JPEG). What it does Peggy J. is an API that takes an image URL and returns a resized version of that image at a specified width. If Peggy has already seen that image at the requested size, then the image is just returned immediately from storage. Otherwise the image is resized, saved, and returned. Let's say you're writing some HTML like so... <img src="https://www.w3schools.com/w3css/img_snowtops.jpg"> Now let's say that image is 3000x3000 but you want it to be 200x200. Peggy J. to the rescue! Just write some code like this... <img src="http://peggy-j.ap-southeast-2.elasticbeanstalk.com/?w=200&url=https://www.w3schools.com/w3css/img_snowtops.jpg"> Done. Now Peggy J. will serve that resized image and hold on to it for speedy future requests. Images that haven't been accessed in over 7 days are periodically removed from storage. How I built it Peggy J. is an open source Express.js application that is backed by AWS S3 and MongoDB. Check out the repo https://github.com/PreslandBoy/peggy-j . I used Postman throughout the project to test my API as I built it. Peggy J. also utilises a number of open source projects including: jimp, mongoose, moment, babel, webpack. The application is currently deployed to AWS Elastic Beanstalk and is built using AWS CodeBuild. Challenges I ran into I've never done any sort of programmatic image manipulation before so it was interesting to learn that side of things. I also had some trouble finding the right way to run the application in development mode. After fiddling around with Webpack hot reloading I eventually went with the simple solution of just using Babel with Nodemon. Accomplishments that I'm proud of 1) The name. I chuckle every time. 2) It's fast! I was concerned that I wouldn't be able to make my application fast enough to be used in a production setting however I was pleasantly surprised with the results. 3) It's simple. It was my goal from the beginning to make my API mind-bogglingly simple to use and I feel I've accomplished that. What I learned This project gave me the chance to explore some open source projects that I haven't looked at before. Specifically jimp and cli-progress. Jimp is an incredibly powerful image manipulation tool and cli-progress is a simple way of displaying progress bars in a CLI. I also got the chance to dive a bit deeper into Postman. Previously I've just used Postman here or there to test endpoints however I now see how it can be used to really dig deep into an API. What's next for Peggy J. I plan on turning Peggy J. into a simple online service for front-end developers. I'll maintain the open source project while running a managed version of Peggy. I'm considering adding a simple account system to track usage and potentially charge a modest fee for higher tiers of usage to cover the cost of running Peggy. <div