---
slug: "chedli-taxi"
url: "https://devpost.com/software/chedli-taxi"
title: "ChedliTaxi"
hackathon: "Ford Code for Taxicabs Mobility Challenge"
organization: "Ford"
winner: true
words: 763
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/frontline_worker"
  - "user/legal_professional"
  - "substrate/geospatial"
---

# ChedliTaxi

> ChedliTaxi is the “snap-cab” application that lets you instantly catch a taxi without having to wave your hand !

[Devpost](https://devpost.com/software/chedli-taxi) · hackathon [[Ford Code for Taxicabs Mobility Challenge]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]] [[transportation]]
**user** [[frontline_worker]] [[legal_professional]]
**substrate** [[geospatial]]

**stack** android, android-studio, google-maps, java, mysql, php

## How they structured the write-up

- who are we?
- inspiration and background
- what chedlitaxi does
- challenges we ran into
- accomplishments that we're proud of
- what's next for chedlitaxi

## Body

DriverScreen4 DriverScreen1 DriverScreen3 DriverScreen5 DriverScreen2 PassengerScreen1 PassengerScreen2 PassengerScreen3 PassengerScreen4 PassengerScreen5 PassengerScreen6 PassengerScreen4 Who are we? Our team is made of two young motivated entrepreneurs: Ali Hammouda and myself, Mohammed Bakr Sikal . We provide each other with complementary skills in order to ensure the development of quality applications Inspiration and Background In Morocco , cabs are allowed to have multiple stops to pick up a maximum of three passengers. Therefore, a taxi driver who already has a passenger aboard is constrained to only pick up other passengers _ going the same way_. Eventually, before getting into the cab, the passenger has to ask the driver if they are both going the same direction , which can be exhausting for both passengers and taxi drivers. In mid-August, my teammate and I came across the Code4Cabs Challenge and found it a great opportunity to contribute to enhancing the taxi-driver/passenger experience in Morocco. In fact, before starting the development of the project, Ali and I have conducted a survey where we have asked more than 120 taxi drivers from Rabat and Casablanca about their preferences about applications they may need. This experience was very enriching as it allowed us to study the real need of taxi drivers which inspired us to come up with ChedliTaxi. According to our survey audience, here is the taxi-driver's wish list : I do not want to stop if the client is not getting into the cab. I need a way to know the client's destination before stopping. I do not want to be stopped by two people when I have only one free seat. I need a service that will tell me where the nearest next potential clients are. I do not want to make detours to reach to clients and find out they are going to a different locations. Unfortunately, all the applications available to users and taxi-drivers are based solely Google Maps and Geocoding APIs, which do not give precise information in Morocco (wrong direction, nonexistent streets.) Worse, although these services can be very efficient when used in developed countries, using them in Morocco just makes the driver's wish list longer. Our idea is to make use of the most powerful CPU in the business, the driver's brain, to judge whether a client is worth picking or not. In fact, the process was mainly inspired from the wish list above; ChedliTaxi lets you send a request with a vocal message to drivers that are on the same street as you, or at most 300 meters away from you. What ChedliTaxi does The application comes in a passenger version and a taxi driver one. The typical Chedli Taxi workflow is as follows: The application set the departure point to the current location of the client The client records a Voice Message about the destination and chooses the number of seats needed (1 to 3) The application's algorithm takes care of broadcasting the request to only cabs who are in the same street as the client, or those who are at most 300 meters away . The drivers receive the request, see the client position on the map and the number of seats, listen to the voice message, judge the route (as if they were stopped, but without wasting time) then either Accept or Decline the request. The client can track drivers on the map The client can choose to send a new request, in which case, the previous request expires Challenges we ran into As we only found out about the project one month and a half ago, developing ChedliTaxi was not a straightforward job. As you may know, proper Android development takes time especially when dealing with a Real-Time communication application (synchronization of tasks...). In fact, we have received many returns with nonexistent streets and wrong directions that made the Exception Handling process very tiring. Accomplishments that we're proud of We are glad that the application made it through almost all the tests, from sending the request until having it accepted by a driver. The minimal bugs reported during the testing phase are to be fixed and patched in ChedliTaxi V2. What's next for ChedliTaxi Actually, clients will fall in love with ChedliTaxi if there is a big number of drivers using it as well. The client would ideally use the application to find available taxis instantly. Therefore, the next phase is application marketing; we need to have as many drivers and clients using the application. Concerning the future of the application development, as mentioned previously, we will be accordingly releasing patches to bugs discovered by users. <div