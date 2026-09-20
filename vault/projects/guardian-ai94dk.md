---
slug: "guardian-ai94dk"
url: "https://devpost.com/software/guardian-ai94dk"
title: "Guardeon"
hackathon: "Junction 2016"
winner: true
words: 786
team_size: 4
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/elder_child_care"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Guardeon

> A modular event driven approach to in-home care giving

[Devpost](https://devpost.com/software/guardian-ai94dk) · hackathon [[Junction 2016]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[elder_child_care]]
  <sub>weak: developer_tools</sub>
**user** [[general_public]] [[patient_family]]
**substrate** [[structured_db]] [[web_dom]]

**stack** arduino, c, flask, jelastic, mysql, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for guardeon

## Body

Guardeon Sensors Planning Deep in API design Coming together... Deep in Hardware design Guardeon UI Inspiration The lack of simple, cost effective and user friendly tech solutions to elderly caretaking inspired us to create Guardeon. Our solution efficiently tackles the aforementioned problems while maintaining an elegant, modular and scale-able form. The primary role of Guardeon is to maintain independence in later years living while still providing primary caregivers a means to keep an eye out for their loved ones. What it does Guardeon tells the story of each day by logging events that are registered through our array of sensors, allowing knowledge of the activities of those within its area. A plethora of sensors communicates with our cloud hosted database to keep track, in real time, of the cared for. The primary caregiver is also able to customize the number and type of sensors around the house to collect the most effective and meaningful data. Our demo exposes three inputs that can be used to monitor activities. First, a button represents a pressure switch that pushes an event to the database whenever a door opens or closes. Second, a raindrop sensor is analogous to the shower or a faucet running. Finally, a temperature sensor can be used to track whether or not the oven or stove is on. Together these points in time represent a breadcrumb trail of the residents’ activities while still preserving their privacy. After this data is collected insights can be made, anomalies can be detected, and most importantly safety can be ensured. How we built it A ESP8266 WiFi module, running a flashed Arduino script, was used to communicate between the sensors and the database. Our sensors, as mentioned above, consisted for the time being of a pressure sensor, raindrop sensor and temperature sensor. On the software side of things, Jelastic’s cloud service was utilized to implement the database. The web app was implemented using HTML, CSS, and the Javascript framework VueJS. And finally, our API interface, allowing access to the database from the web app and the hardware, was implemented using the Flask framework for the Python language. Challenges we ran into Some difficulties included creating the web API in Python because it required learning the Flask framework to create our RESTful API. The limited knowledge of this realm hindered our speed and accuracy in developing this portion of the project. Additionally, creating the Jelastic database was difficult due our lack of knowledge about the service. On the breadboard side of the equation, our WiFi module responsible for both running code and communicating with the database was finicky at best. Beyond that we also had to battle spikes in current that reset the system and disrupted sensory data transmission. Overall, we were able to overcome these challenges in one way or another. In the future a more cautious approach to both the backend software system and the hardware implementation would be beneficial. Accomplishments that we're proud of We built a really cool full stack IoT system! From circuit design to UI of a web interface we each brought our special talents to the table a developed something extraordinary. It was gratifying to see each component come together. To have the Arduino send a ‘POST’ request then to see the connection to the database and the subsequent actions involved in processing the request, was a great experience. Likewise designing a sleek UI that was able to utilize our backend to deliver a quality service was incredible. Join these together and Gaurdeon becomes a force to be reckoned with. Of course there is much more development before it is ready for release, but for only having a weekend, we did pretty well! What we learned So much. For each of us the knowledge gained was more concentrated in certain areas more than others, but it was because of this concentration that we were able to create Gaurdeon. Electrical engineering came into play designing circuits, Flask was a new framework to the members that worked on the back end system, and end-to-end implementation was a new experience for nearly all of us. What's next for Guardeon Guardeon’s use cases are not limited to only what we developed here, its set up can be configured through the user-friendly web app to tackle many different scenarios and thus serve a different purpose based on how the client sees its benefits. Additionally, the ever growing sector of machine learning has a very close tie to our system based on the quantity of data as well as the meaning behind it. We already have many ideas how we can implement these techniques to unlock a treasure trove of insights provide by the event data that Gaurdeon collects. <div