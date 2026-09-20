---
slug: "kegomate"
url: "https://devpost.com/software/kegomate"
title: "Kegomate"
hackathon: "MongoDB World Hackathon"
organization: "MongoD"
winner: true
words: 1395
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "user/developer"
  - "user/general_public"
  - "user/small_business"
  - "user/social_worker"
  - "substrate/financial_record"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Kegomate

> Kegomate collects data from a flow sensor to track coffee consumption by individuals then informs the office admin via a slackbot when coffee is running low to place an order. Never run out of coffee!

[Devpost](https://devpost.com/software/kegomate) · hackathon [[MongoDB World Hackathon]]

## Facets

**mechanism** [[sensor_fusion]] [[vision_ocr]]
**domain** [[civic_government]] [[developer_tools]] [[labor_employment]]
**user** [[developer]] [[general_public]] [[small_business]] [[social_worker]]
**substrate** [[financial_record]] [[video_visual]] [[web_dom]]

**stack** angular-material, angular.js, arduino, bootstrap, c, compass, html, mongodb, ngx-charts, python, raspberry-pi, sass, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for kegomate

## Body

Inspiration The entire Kegomate team works for 540.co , a small business (of ~30 developers) that helps the DoD and Federal Government #getshitdone. Corporate culture is important to keep our team happy and at the center of the company's "snack area" are the 3 cold brew coffee kegs (supplied by Snowing in Space ) Problem Statement - The 540 crew consumes cold brew coffee at a rapid pace, and we never know when a coffee keg is running low on coffee until the coffee stops flowing. Then we have to re-order and we could be without coffee on one of the taps for a few days. What it does The 2 main epics that we had for our MVP (for this hackathon) were to: Monitor real coffee consumption across the 3 corporate cold brew coffee lines Know when a keg was almost empty (and alert our corporate #kitchenrequest Slack channel that one of the kegs was low) Backend Functionality - The typical drink event flow goes as follows: A user begins to pour coffee by pulling on the selected coffee tap Coffee travels through tubes in the kegerator and through the flowmeter sensors that we installed on each keg line (these sensors are capable of capturing liquid events at 1/5000 of a gallon granularity). Two (2) Arduinos running Kegbot software process the 5v pulses from the flowmeters and transmit Little Endian encoded messages over the serial port as a flow is present in the tubing (each Arduino is capable of handling 2 flowmeter sensors... so, we have the capacity to handle an additional keg line in the future) Custom Python code running on a Raspberry Pi monitors the Serial output via a USB connection and processes the messages being sent from the 2 Arduinos. Once a drink event has ended, the Raspberry Pi sends a request to a Mongo Stitch function to save the drink event. The Stitch function will then check the levels of the keg to see if it is low (< 10% full), and send a message to a corporate Slack channel (via an incoming webhook) to alert the appropriate folks. Frontend Functionality - (By the way, we didn't submit the live URL for our application because it's a production/working system that we are currently using and the Admin area isn't password protected, so all users could update our keg installation). We will provide the URL upon request. We built an activity stream that shows the most recent drink events (the coffee that was consumed... and the amount) We built a Caffeine Meter to showcase the amount of caffeine that the company has consumed in the current day. There are 4 levels of the meter ("ZZZZ Face" (< 25 fl oz), "Meh Face" (25-99 fl oz), "Smiley Face" (100-199 fl oz), and "Brain Exploding" (200+ fl oz). We created a graph that tracks the daily consumption trending for each keg over the last couple of weeks We created a visual representation for the current volume in each keg We created an administrative area that can update the keg setup when a new keg is installed (and even adjust the level manually if Kegomate ever unexpectedly goes offline). How we built it There were 4 main areas of focus for delivering the capability: The Sensors / Hardware - We spent a significant portion of time testing with flowmeter sensors and getting the flowmeters to connect to our Arduinos... and to get the Raspberry Pi to read the Little Endian encoded messages from the Arduinos. We realize that this aspect of the project didn't have much Mongo relevance, but it was new and challenging to our team, and the necessary functionality to get the data to Mongo/Atlas/Stitch. We purchased 3 flowmeters , and installed them into We used the schematics in the Kegbot project to connect the flow sensors to the hardware (but stripped out the hardware that we didn't need) We connected the Arduinos to the Raspberry Pi with USB cables The Raspberry Pi / Python - We developed software in Python to run on the Raspberry Pi to decipher the incoming serial messages and to send drink events to the post_drink Stitch function. Process messages sent from the Arduino (based on 5v pulses sent to the Arduino as coffee was passing through the sensor) Detect the end of a drink event (once a pour event begins... if there is ever a 2-second stoppage in flowmeter readings coming over the serial port... the Raspberry Pi considers the event complete. At the end of a drink event, the Raspberry Pi sends a drink event to Mongo via the post_drink Stitch webhook. Backend (Stitch) - Initially, we were going to create a Node.js backend API tier to connect to our Mongo datastore and enable data transport to our browser-based application; however, we decided to use Stitch in lieu of a custom backend. We created 9 incoming webhooks for our front-end and back-end to use to retrieve and manipulate data: get_setup get_coffee update_setup update_level get_users get_reports post_drink post_coffee get_drinks Additionally, we created 9 reusable functions for our Stitch services/web hooks: deactivateKeg activateKeg getCoffeeById getCoffee getCoffeeByTapId updateKegDetails addDrinkEvent adjustLevel checkIfKegIsLow Frontend (Angular App) - Lastly we built an Angular application to visualize and administer the keg data collected by the sensors. This browser-based application runs on a tablet mounted to the coffee keg to give convenient access to coffee consumers and admins (when kegs are swapped out) Challenges we ran into The main challenges we ran into were with hardware. First, it took us a while to make a final decision on what hardware solution we would implement and would accurately detect the coffee volume of the keg. We settled on the flow meter solution, but we were unsure if it would be successful. When we placed an order on the flowmeters, the shipping timeline was tight. The metal barbed connectors used to connect the tubing to the flow meter were not shipped until a week before the hackathon concluded. To ensure our hardware solution would work, we installed the flowmeters using temporary plastic connectors which were shipped overnight. The plastic connector snapped on 3 separate occasions, one of which caused us to lose 50 oz of cold brew coffee (yes... on the floor of our kitchen area). Now, the metal connectors are in place and are ensuring a successful (leak-free) Kegomate. Accomplishments that we're proud of We're extremely happy that our team successfully delivered on the 2 main MVP goals that we set out to accomplish. We were able to implement a hardware solution that accurately detects the volume of coffee moving through the lines, as well as providing new and valuable insights into when a coffee keg needs to be replaced. After we had everything set up, it was awesome to see co-workers use the kegs and get a kick out of the new dashboard that we display in the office kitchen area. Our teams crowning achievement had to be the joy, mixed in with a little relief when we started getting legitimate readings from the sensors on the kegs. Mission Accomplished. What we learned Even though we didn't have the chance to use it before the hackathon, Stitch ended up playing a huge role in our success. The fact that we could entirely remove the need for a traditional backend and simply write a few Stitch functions is a tribute to the ease and flexibility of the Stitch offering. We also learned a lot about the hardware that went into our project which included flow sensors, Arduino kits, and a Raspberry Pi. What's next for Kegomate We plan to add additional features to kegomate including facial recognition to track individual coffee consumption, monitoring the consumption rate to determine when to reorder coffee, visualizations to track coffee trends, and monitoring the nitrogen canister. Our plan is to look into using image recognition, a beacon, sensors, and/or an RFID reader to determine who is consuming the coffee from which keg. This will allow us to notify users which coffee they consume the most, when they've consumed more caffeine than recommended, and more. We plan to create further visualizations and charts to display coffee and caffeine intake of the company. Lastly, the coffee kegs require a nitrogen canister which also requires reordering. We would like to monitor the nitrogen to automate the entire keg maintenance process. <div