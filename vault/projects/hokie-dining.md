---
slug: "hokie-dining"
url: "https://devpost.com/software/hokie-dining"
title: "Hokie Dining"
hackathon: "Alexa Skills for Students – Powered by AWS Educate"
organization: "Amazon"
winner: true
words: 897
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Hokie Dining

> Use this skill to find out which dining halls are open on Virginia Tech's campus before you go out for food!

[Devpost](https://devpost.com/software/hokie-dining) · hackathon [[Alexa Skills for Students - Powered by AWS Educate]]

## Facets

**domain** [[developer_tools]] [[education]]
**user** [[educator_student]] [[general_public]]
**substrate** [[financial_record]] [[web_dom]]

**stack** alexa, amazon-web-services, api, python, virginia-tech

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for hokie dining

## Body

Inspiration As a student and Resident Advisor on Virginia Tech's campus, I find myself eating at on-campus dining halls quite often. I enjoy eating at several places on campus; however, traveling to a dining hall can take upwards of 10 minutes of walking due to the large size of our college campus. For this reason, I like to be able to plan where exactly I want to eat before I leave. On a few occasions, however, I have walked to dining halls to find that hours of operation have suddenly changed or that I simply forgot the differences in business hours on different days. In order to solve this problem that I and many of my friends have, I created this Alexa Skill. What it does Hokie Dining utilizes an API from Virginia Tech's dining facilities in order to check on the hours of dining halls all across campus. This allows one to ask if a specific dining hall is open before they leave or to ask which of all the dining halls on campus are open. If a dining hall is open, the skill will also tell you how long you have until the dining hall closes so that you can make an informed decision. How I built it Utilizing Python, I set out to create a skill that would use web-scraping to read Virginia Tech's dining website and produce information regarding hours of Virginia Tech's dining halls. As I was setting up a web-scraping agent, I found an Application Programming Interface in the JavaScript of the site that I could use to simplify my skill! I did some more research and learned about _ requests _, a Python package that can be used to interact with APIs and to parse through JSON data. Once I was able to obtain the necessary data, I worked on creating algorithms to parse through dining hall hours, as one dining hall can open and close several times throughout the day, in order to correctly identify if a given dining hall is open, as well as to be able to calculate the amount of time left until an active dining hall closes. I also spent time adding in synonyms and nicknames for names of popular dining establishments around campus so that people can ask Alexa about their hours in the same way as they would ask a friend. Challenges I ran into I initially struggled with accessing the data for dining halls on Virginia Tech’s campus. I began by utilizing web scraping techniques before I found that utilizing an API that I found in the site’s code would make the process much faster and simpler. I also struggled with utilizing Alexa’s slot components in order to create flexible commands that allow the user to simply insert the name of the dining hall they want information for in an otherwise standard sentence. Through reading of online documentation as well as trial-and-error, I was able to get this feature to work as well as fallback-statements for when a user asks about a dining hall that doesn’t exist. Another thing I struggled with briefly was referencing to the current time in the local time zone. This was solved through some online research. I ended up utilizing a _ datetime _ package that allowed me to convert the default universal time into Virginia Tech’s local time zone. This local time was essential in determining which of the dining halls was open at any given time. Accomplishments that I'm proud of This was the first time that I had created an Alexa skill on my own. I am very proud of my ability to think of an idea that would be beneficial to the 10,000+ students that live on Virginia Tech’s campus, and to move through several barriers in order to create the final product. On a few occasions while creating this skill, I found myself having issues that were not addressed in Amazon’s documentation, nor on Stack Overflow. I am proud of myself regarding how I was able to think creatively and find my way around issues I was having regarding utilizing imports, debugging my skill, and using Amazon’s cloud development platform. What I learned Through developing this skill, I learned more about the importance of architecture and planning when creating a program. Through proper planning and trial-and-error, I was able to create a set of helper functions that I found useful when building up to the skill’s full functionality. I also learned more about cloud computing, as I read about Amazon Web Services, their Cloud9 online development platform, and how lambda functions are utilized. I also learned that when creating an Alexa skill, it is very important to think about the end user and their experience, whether that means keeping their time zone in mind, or just thinking about the most efficient and user-friendly way of delivering information. What's next for Hokie Dining Currently, Hokie Dining can be used for asking which dining halls are open, and for asking if a specific dining hall is open. I hope to expand functionality to include more complex requests, such as “Where can I eat for breakfast?”, “When does this place close?”, and “How long until this place opens?” I have contacted the Dining Services division of my university to ask what sorts of added benefits they think my skill could give students across campus. <div