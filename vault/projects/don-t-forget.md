---
slug: "don-t-forget"
url: "https://devpost.com/software/don-t-forget"
title: "Smart Elephant"
hackathon: "Amazon Alexa Skills Challenge"
organization: "Amazon"
winner: true
words: 1081
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "user/clinician"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Smart Elephant

> Smart Elephant uses Alexa to send timed reminders to your mobile phone.

[Devpost](https://devpost.com/software/don-t-forget) · hackathon [[Amazon Alexa Skills Challenge]]

## Facets

**user** [[clinician]]
**substrate** [[financial_record]] [[geospatial]] [[structured_db]]

**stack** amazon-alexa, amazon-web-services, moment.js, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- what's next for smart elephant

## Body

High Level Architecture Example of how reminders are sent Inspiration My kids have an uncanny ability to make requests of me at the most inconvenient times. They'll ask me to sign a permission slip while I'm washing dishes, talking with my wife, or walking in the door with a handful of groceries. I decided to use Alexa to create very simple reminders for the times I was unable to manually enter a reminder into my phone's reminder app. I first looked using "native" Alexa functions. I started with to-do list functionality, but (a) there is no date/time associated with the action and (b) you have to remember to check your to-do list to see what's on it. I also looked into using Alexa to create my reminders as calendar events. That works, but left my calendar cluttered with "events" that were "actions/reminders". I needed something simple that would: allow me to quickly (in one statement) record an action and a due date remind me at the appropriate time not clutter my work and personal calendars I didn't find an existing skill that met my need, so I built Smart Elephant . What it does Smart Elephant uses Alexa to send reminders to your mobile. You can tell it to "take out the trash at 6pm" and you'll receive an SMS at 6pm, telling you to take out the trash. You can also make requests without referencing a specific time: Call the doctor this afternoon Buy milk tomorrow at 5PM Write the check next Monday at 8AM You can delete reminders as well, by asking Alexa to delete the reminder ("Alexa, ask Smart Elephant to delete reminder to pick up the kids"). Finally, you can ask Smart Elephant to send your reminders to you by asking "list reminders". A user has to provide two pieces of information in order to use Smart Elephant a US mobile number (at this point in time, this skill only works in the US) a US Zip Code (used to determine the user's time zone) How I built it There are a number of challenges that I faced when designing Smart Elephant Time is absolute, but we talk about it in relative terms. 8AM in Dallas is 6AM in Los Angeles. I had to understand where the user was in order to convert their relative time request into an "absolute" time . A user could request to be reminded of anything , so I needed to build the skill to take any string of words. A user could request to be reminded at any time (5AM, 4:37PM, 2:23AM, etc), so I had to build a function that was always looking for reminders and sending them at the appropriate time. I had to be conscious of cost and performance. I could write a function that would constantly read a database for reminders, but (a) performance would be impacted as more records were added and (b) it would not be cost effective (AWS charges for the number of reads and writes to a database). Given that, I built a the following three system architecture: A: Main Lambda Function (triggered when the user invokes the skill through Alexa) This function's main purpose is to interpret the ask/request of the Alexa user and take action - typically: creating reminders and saving them to a DymanoDB table, or removing reminders. The process of adding and removing reminders required the special considerations listed below: Creating Reminders - Getting the Time Zone The lambda function uses Google Maps APIs to get the users timezone id. First, the user has to provide a valid zip code. This zip code is used to get the user's location (latitude and longitude) using the Geocode API. The Time Zone API uses the location coordinates to retrieve the timezone id. Creating Reminders - Converting to a Absolute Time As mentioned earlier, I needed to take the user's input (5AM) and convert it to a time that was universal. I used Moment.js for most of this work. Moment.timezone functions translate a datetime to UTC. From there, it was easy to convert the reminder datetime (in UTC) into the number of milliseconds since Jan 1, 2017 (similar to Unix epoch time). Deleting Reminders - Using fuzzy matching logic I needed the ability to delete reminders. Unfortunately, a simple database delete statement would not work (as the user might add the reminder as "take out trash" and request Alexa to delete " take out the trash". I needed logic that would find similar strings. I used the Fuse.js library for fuzzy search logic. If the match is extremely close, then "Don't Forget" assumes the match is the same and deletes it. If it is a "near match", then "Smart Elephant asks the user to confirm the delete. B & C: Second Lambda Function (runs every 15 mins to read reminders from DB and place into SQS Queue) and Python Script to read from Queue The reminders created by the main Lambda function are saved to a DynamoDB table. I needed to design a method to get the message and deliver them at the appropriate time. I felt that using a combination of a scheduled Lambda function, SQS, and SNS made the most sense. This Lambda function reads messages from the table, and if the message is scheduled to be delivered in 15 mins or less, adds it to the SQS queue. Each message is added with a delay seconds attribute, which allows the message to be make visible at the appropriate time to send. The Python script constantly polls the queue for new messages. When one is found, it removes it from the queue and sends it via SMS. See the diagram below for additional details. Notes A queue message can only be delayed up to 15 mins, which is why the Lambda function only runs every 15 mins. If a user created a reminder that is less than 15 minutes from delivery, then the reminder is directly added to the queue, with the appropriate delay seconds (instead of being added to the DynamoDB table) The skill was originally called "Don't Forget"; I changed to name to Smart Elephant it order to ensure that the skill was triggered, instead of Alexa "native" to-do functionality. What's next for Smart Elephant Over time, I'd like to add new functionality: Option to "acknowledge" reminder once received, or push reminded to another date/time Ability to edit reminders (right now, you can only add or delete. <div