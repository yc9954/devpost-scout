---
slug: "parktimeanalyzer-dcli7b"
url: "https://devpost.com/software/parktimeanalyzer-dcli7b"
title: "ParkTimeAnalyzer (ParKello)"
hackathon: "Junction 2016"
winner: true
words: 365
team_size: 4
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/frontline_worker"
---

# ParkTimeAnalyzer (ParKello)

> Smart Parking Disc On Your Mobile Device. Parking Events Statistics: forecasting and info about parking places.

[Devpost](https://devpost.com/software/parktimeanalyzer-dcli7b) · hackathon [[Junction 2016]]

## Facets

**domain** [[finance_payments]] [[transportation]]
**user** [[frontline_worker]]
  <sub>weak: general_public</sub>

**stack** android, angular.js, java, ruby-on-rails

## Body

Logo ParKello (Smart oarking disc) Data Flow ParKello, step 1: park car ParKello, step 2: select car registration number ParKello, step 3: unpark your car Find parked car by registration number Grouped parkings Polygon Parking spots In Finland are already running many projects, which are a good basis for future transport communication and mobility development: on-line public transport ticket payments, on-line parking place payments, more and more parking slots and charging points for electric cars, two self-driving electric buses have rolled out on to the public roads of Helsinki alongside normal traffic, in one of the first trials of its kind etc. At the same time drivers should use parking discs (mechanical devices) for parking time control on free parking places. One more “bottleneck” of future mobility development is a lack of actual on-line information about available parking places and parking rules in big cities like Helsinki. We are developing an application for parking cars on free of charge parking places (smart parking disc) and a service for the analyzing of parking events and parking places : For drivers it is a convenient mobile application for parking their cars, with a reminder about parking time out, and a navigation to the parking place. Mobile application for parking wardens provides access to information about parking events (when and where it is started and finished). API will enable the possibility for automation of their work (Parking Events API). Parking events statistics (time, duration, place) is used for collecting data about parking places, providing on-line information about their capacity, forecasting available parking slots at some time-stamp (Parking Places API). We have already implemented: Basic functionality of Android mobile application for parking cars. Events are send to server (Rails Back-End). Basic functionality of Rails Back-End (server side for tracking parking events, API for access to information). AngularJS Web application, which provides access (for parking wardens) to information about parking events and parking time control. This is also used for data visualization and analyzing. We have designed algorithms and implemented some functionality of Java Back-End -- service for analyzing parking information and forecasting the parking situation (based on parking events from Smart Parking Disc + Embers parking events API). <div