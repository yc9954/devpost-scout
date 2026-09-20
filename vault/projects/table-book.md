---
slug: "table-book"
url: "https://devpost.com/software/table-book"
title: "Table Book"
hackathon: "Square Developer Hackathon 2023 "
organization: "Square"
winner: true
words: 690
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Table Book

> You choose your airplane and cinema seats. But with table booking you often just book a time and hope that you don't get the table by the toilets. This project tests a more interactive experience.

[Devpost](https://devpost.com/software/table-book) · hackathon [[Square Developer Hackathon 2023]]

## Facets

**substrate** [[financial_record]] [[structured_db]] [[video_visual]]

**stack** firebase, react-native, square, swift

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i’m proud of
- what i learned
- what's next for table book

## Body

Inspiration Too often I have booked a restaurant for a special occasion and even when booking far in advance you find your table to be less than the best when you arrive. I wanted to experiment with a table booking experience that was simple to setup and use but also offered the customer more power and choice with their decision making. Enter 3d table booking with AR assisted venue scanning. Want the table by the big window? Now you can see the big window and select the table next to it while you book. You can also 'test drive' a table and see what it's view looks like to really make sure it will be perfect, time travel to view availability’s of each table, and book the perfect table. What it does The venue manager can use the admin app to authenticate with Square, scan their venues floor plan and table layout with AR assistance, and then assign each table to a corresponding 'table' set up for Square Appointments. The customer can use the client app to browse venues, view the venue's 3d layout and tables, swipe through time to view availabilities represented by colours on the 3d tables (yellow for available, red for unavailable, green for currently selected), select a table to view more details including to 'test drive' the table by viewing a 360 perspective from the table and complete a booking. How I built it I built the admin app as a native iOS project using Swift. The scanning is achieved using Apple's RoomPlan and the 3d models rendered with SceneKit. The client app is built using React Native with a custom Swift native module for the 3d rendering. Firebase is used for the database, authentication, and cloud functions. The cloud functions handle transactions with the Square apis for authentication and bookings. Challenges I ran into I didn't realise the hackathon was live until 12 days before deadline so I had to sacrifice time spent on design to focus on implementation. The test drive feature had to be hard coded to a sample image to demonstrate. Unfortunately Square does not yet offer an API for integrating with the Square for Restaurant's table management. I had to spend some time understanding the Bookings api's limitations and scope to find a way to make it work for tables for this proof of concept. I managed to find a way to get it to correctly work with tables by creating a service called 'Table Reservation' which had a variation for each table and a 'staff' entry also for each table and assigned to the corresponding variation. This allowed for the system to know that a particular table could only be booked once for a time slot. I also had to tweak the RoomPlan scanning to only detect tables, walls, and windows and learn how to work with 3d models and scenes. These were all new to me. Accomplishments that i’m proud of I am very happy that I managed to get it working with the Square Bookings api without too many workarounds. There is only minimal setup required within Square before getting started with the Venue scanning and table booking. I am also very happy with the accuracy of the scanning. Every now and then it does pick up a side table or coffee table that you might not want included. If I had more time I would allow the venue manager to remove unwanted objects and manually add in tables that weren't detected. What I learned I learned how to use the Square Bookings api! Great work guys What's next for Table Book Allow the venue manager to remove unwanted objects and manually add in tables that weren't detected. Allow more details to be assigned to a table such as number of seats. Let the customer apply a filter for how many seats they need to find tables of the correct size. Integrate with Square for Restaurants table management? Give it a makeover and make the UI really nice. Up the quality of the 3d scene with materials and models Support for multiple rooms and levels per venue <div