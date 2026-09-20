---
slug: "timewise-cqb25n"
url: "https://devpost.com/software/timewise-cqb25n"
title: "TimeWise"
hackathon: "HackSwift 2024"
organization: "hackswift"
winner: true
words: 932
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
---

# TimeWise

> Maximize Your Day Using Personalized Time Management for Success

[Devpost](https://devpost.com/software/timewise-cqb25n) · hackathon [[HackSwift 2024]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** api, google-calendar, googlecloudplatform, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that i was proud of
- what i learned
- what’s next

## Body

TimeWise Inspiration Managing my time was one of my biggest problems during my sophomore year. I tried balancing sports, clubs, classes, and personal projects simultaneously, but I needed help to get it right. Because of these simple mistakes, my performance in my sports, clubs, and classes back then suffered and was lower than I hoped for. Looking back, it was obvious how disorganized I was or how much I would get distracted on my phone or doing some random, arbitrary task. I have already learned how to balance many responsibilities at once, and I want to teach that to other people by making an add-on that people can rely on. What it does I made a front-end UI to capture users' preferences and tasks for time management. The algorithm will consider those preferences and come up with an efficient time management plan that provides requirements and blocks the time and events needed to do those tasks efficiently. It offers personalized recommendations for time management strategies based on users' productivity patterns and goals, such as scheduling regular breaks, setting time limits for tasks, optimizing meeting durations, etc. How I built it The main idea was the Google Cloud Platform (GCP) by setting up a Google Cloud Platform project called TimeWise, installing the Google Calendar API client library with Secret Manager and Connector APIs, authentication with the Google Calendar API, setting up the OAuth consent screen, creating OAuth credentials, and integration in my application. The Python script collects user data related to tasks, breaks, preferred working hours, distractions, deadlines, sleep hours, and mood levels using if, elif, and else statements. It then generates personalized recommendations based on this data for time management strategies. Finally, it updates a Google Calendar using the Google Calendar API to reflect these recommendations as events. Collecting the user's data: The collect_user_data function asks the user to input data regarding different aspects of their productivity and well-being. I used for i in range loops to use the specific data points or lists based on user input, which is later used in the analysis and recommendation generation sections of the script. Generating recommendations: The generate_recommendations function analyzes the user's input data and generates specific recommendations for managing tasks, breaks, meetings, distractions, deadlines, sleep quality, and mood management. Displaying recommendations: The display_recommendations function displays the generated recommendations to the user. Updating Google Calendar: The update_calendar function is designed to update the user's Google Calendar with events based on the recommendations generated. However, some bit of code relating to Google Calendar integration is commented out in the provided script because the connection wouldn’t work with the necessary API credentials and calendar details to function correctly. Challenges we ran into When I originally came up with the idea, I tried to make an actual app from scratch that acted like Google Calendar and add on from there. The options I had were on Apple’s App Store or Android’s Google Play. Still, Apple requires you to spend $99 a year on a developer account and Android by paying a fee of $25, so I decided not to make an app but make a Google Calendar add-on instead. We had technical issues or glitches in GCP and could not fully enable our APIs to update the calendar. When authorizing the connection, we did everything right, but when GCP tried to authorize it, it would load for 3-5 minutes, but nothing changed. When I was coding in Python, connecting the code to the Google Calendar was also not working, and in the update_calendar code, you can see """" event_2 = service.events().insert(calendarId='primary', body=event_1).execute() print('Event created: %s' % (event_2.get('htmlLink'))) """" are commented out because they were causing errors with the connection, but I ran out of time. I plan to continue this project on my own time, outside of the HackSwift Hackathon, and try to improve on it. Accomplishments that I was proud of I was proud that I was able to set up GCP in the first place because normally people get certifications for GCP and coding in Python. I heard that GCP certification exams can be challenging, but they are achievable with proper preparation, study, and hands-on experience so I'm really happy that I get to experience this early on in my computer science career as a high schooler. It has been 1 or 2 years since I’ve coded in Python because I’m currently using Java and GML (Gamemaker) so the fact that I was able to relearn Python so fast and do it even better than when I was a freshman and sophomore showed me how much I was improving by and that made me feel very accomplished and proud. What I learned In Google Cloud Platform, I learned how to do API integration by linking my server to Google Calendar using the Google Cloud Platform's Service Market Place APIs. The main idea that I learned was the GCP setup, APIs, their functions, and integration, while also brushing up on my Python and learning even more in Python, such as the pip import I downloaded and used called “import pandas as pd.” What’s next My plans for the future are to update Google Calendar using the Google Calendar API to reflect these recommendations in the Python script as an event and figure out all the errors. I also plan on using GCP more often and even updating my application by adding AI-powered schedule optimization and AI algorithms that analyze users' schedules, habits, and priorities to suggest optimal time allocations for tasks and activities. (The app could learn from user feedback to continually improve its recommendations). <div