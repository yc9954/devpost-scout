---
slug: "project-platypus"
url: "https://devpost.com/software/project-platypus"
title: "The Platypus Project"
hackathon: "PennApps XII"
winner: true
words: 782
team_size: 4
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/web_dom"
---

# The Platypus Project

> Our project analyzes and produces real-world data which we collect and express through platypuses.

[Devpost](https://devpost.com/software/project-platypus) · hackathon [[PennApps XII]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[web_dom]]

**stack** arduino, electric-imp, myo, objective-c, processor, squirrel, stock-market-data, twitter

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the platypus project

## Body

Inspiration When we arrived at PennApps, we had a ton of ideas floating around our heads. Maybe we should build a web app? A mobile app? Maybe we should play with some cool hardware? Maybe integrate some stock market data? So, we tried to design a project that would fill all the above requirements and incorporates one central theme: platypuses. What it does Our hack has a few elements. The first is a platypus-themed video game called _ italics _Platypus vs. Stocks _italics _ that's coded in Objective-C and uses stock market data (provided by FINRA) to generate each level. The player controls a flying platypus with a Myo armband as he flies through stock trends looking for love. The next element of our hack is our "enhanced" platypus plush dolls; there are three in total. The first platypus, the Cyborg, has a force-sensitive resistor in his belly, a piezo buzzer in his armpit, and two LEDs for eyes. Plus, he's got an Arduino strapped to his back. The second platypus, Maze, has an Electric Imp wifi-enabled micro-controller in his back and a Hall effect sensor in his arm. The third platypus, Lovebird, has a magnet in her arm that activates Maze's sensor. When Maze and Lovebird "hold hands", the Electric Imp chip tweets one of 200 programming-themed pick-up lines from Maze's Twitter account. However, the Cyborg, who is all alone, is jealous of their romance and feels the need to respond. Whenever Maze tweets, one of the Cyborg's eyes glows red until he is urged to respond to Maze's tweet with a quote from _ italics _ Terminator _ italics _. Then his eye will stop glowing red and his other eye will glow green. How we built it We built our video game in Objective-C using code from Myo's developer website and ten years' worth of stock market data from FINRA. We let the user select which level (each level trends stocks from a particular company) they want to play and then import the data from that company. Our plush dolls were built using various sensors and indicators along with two different micro-controllers. The Cyborg has a Spark Core on his back, two LEDs for eyes, and a force-resistant sensor in his abdomen. Maze has a Hall effect sensor in his hand and an Electric Imp WiFi enabled micro-controller embedded in his back. The micro-controllers allow the Platypuses to interact with Twitter. Challenges we ran into The biggest challenge we ran into was getting the Cyborg to recognize Maze's Twitter posts and allowing him to post responses. First, we tried using an Arduino Leonardo to pull and push data to and from Twitter. However, the Arduino library we were using relied on an old version of Twitter authentication. This forced us to move from Arduino to Spark Core which precipitated more problems. Specifically, we had a lot of trouble syncing our Spark Core to the online IDE. Another challenge we ran into was converting the stock market data we received from FINRA into a useable form. This required us to build a script that scraped the text file and wrote the relevant data to new files. These files were then used by Objective-C to create the levels of our video game. Accomplishments that we're proud of We are most proud of the Twitter integration we included in our project. Although our project is a little goofy, this component has a lot of real world applications. Sending tweets in response to physical (Hall effect sensor) and digital (other tweets) stimuli is something that can be applied to a variety of situations What we learned Besides learning how to stay awake for absurdly long amounts of time, we learned a lot about a variety of programming languages and hardware devices. Each of us programmed in a language he had never programmed before. But most importantly we learned to search before you code. Most of the time, somebody has already figured out a solution for what you're trying to do. This can drastically decrease time spent on coding and dramatically increase efficiency. The answers are out there; our job as hackers is to synthesize all those answers into one, giant creation. What's next for The Platypus Project Well, for one thing, sleep. We need it and we need a lot of it. We will be the first to admit that the Platypus Project is not especially useful for anything. It wasn't created to solve any pressing issue, rather it was built to introduce our team members to various pieces of software and hardware at their first hackathon. Our goal is to use this new knowledge at future hackathons to make awesome hacks. <div