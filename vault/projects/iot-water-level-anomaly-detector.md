---
slug: "iot-water-level-anomaly-detector"
url: "https://devpost.com/software/iot-water-level-anomaly-detector"
title: "Water Level Anomaly Detector"
hackathon: "Microsoft Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 1231
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "user/developer"
  - "user/frontline_worker"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Water Level Anomaly Detector

> Monitor water levels with an IoT sensor connected over cellular to Azure Anomaly Detector API

[Devpost](https://devpost.com/software/iot-water-level-anomaly-detector) · hackathon [[Microsoft Azure AI Hackathon]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[agriculture_food]] [[developer_tools]] [[disaster_emergency]]
**user** [[developer]] [[frontline_worker]] [[general_public]]
**substrate** [[code_repository]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** anomaly-detector-api, azure, cellular, python, raspberry-pi, soracom

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- what i learned
- what's next for iot water level anomaly detector

## Body

Water Level Anomaly Detector IoT Device Setting up Soracom Beam to append Subscription Key as Header Setting up Endpoint URI in Soracom Beam Grabbing Subscription Key and Endpoint URI from Azure Portal Inspiration For this Hackathon, I knew that I wanted to accomplish the following three goals. Gather data from our environment to make a positive ecological impact. Leverage Azure Anomaly Detector API to identify outliers in the data. Build an IoT device which uses an ultrasonic sensor to measure distance. Water level monitoring is a great fit for the Anomaly Detector API and ultrasonic sensor, as the sensor readings should be fairly consistent unless a serious event takes place. I began thinking about what would have the most beneficial environmental impact, and saw potential in monitoring remote lakes and rivers. This could be great for detecting flash floods or natural disasters. This system could also aggregate data daily, which would be beneficial for long-term analysis, such as measuring the effects of global warming. Since this device will be deployed remotely, cellular connectivity is a must. Cellular dramatically expands the options of where this device can be used, as it will not require a WiFi or Ethernet connection. What it does This project uses the Anomaly Detector API to identify drastic changes in water levels from an ultrasonic sensor which is plugged into a Raspberry Pi and communicating to the cloud over a cellular connection via Soracom. Every minute, a timestamp and distance reading from the ultrasonic sensor is taken, and stored on the device. Once enough data points are stored (Anomaly Detector API currently has a minimum of 12) the data is sent to the Anomaly Detector API to analyze the latest value against the previous ones. When an uncommon event occurs, the Anomaly Detector API will return a message to the Pi letting it know that an anomaly has been detected. This message can then be used to trigger any type of action that you can think of. Currently, it will make the Pi illuminate a red LED. For sending the sensor readings from the Raspberry Pi to the Azure Anomaly Detector API I used Soracom Beam. This service sits within the Soracom cellular network and allows you to send plain HTTP messages to it. Since cellular connectivity is encrypted at the SIM card level, we do not need to manage our API keys on the raspberry pi. From the Soracom User Console, I added my Azure Anomaly Detector API endpoint and API key to my Soracom Beam configuration. This allows Beam to take the plain HTTP message over cellular and then encrypt it into HTTPS and send over the public internet to Azure Anomaly Detector API. How I built it Hardware I used a Raspberry Pi Zero, along with an ultrasonic sensor, LED, cellular modem usb dongle, and a Soracom SIM card for the hardware. All of these items are available in Soracom’s IoT Starter Kit found here: https://www.soracom.io/store/soracom-cellular-iot-starter-kit/ I then used a Dremel, drill, soldering iron, and copious amounts of hot glue to incorporate all of this into a basic project box. Cloud Azure Firstly, I headed over to Azure and set up the Anomaly Detector API. I followed along with the Rest API for Python Quickstart Guide . Please see my screenshot in the gallery for where to find your Subscription Key and Endpoint URI within the Quickstart tab under the Getting Started section. Soracom The next step was to go over to the Soracom User Console and configure Soracom Beam to convert the HTTP Posts from the Raspberry Pi into HTTPS Posts to my Anomaly Detector API endpoint. Please check out the image gallery for what my configuration looked like when setting up an HTTPS endpoint, using the endpoint URI from my Quickstart settings from Azure. I also have a screenshot showing how to configure Soracom Beam to append my Subscription Key as a header. Software Once that was complete, the last step was to set up the Python scripts that loop on the Pi every minute to collect the sensor data and then post via HTTP to beam.soracom.io. If an anomaly was detected, the script then turns on a red LED which I have plugged into GPIO port 18. The full code for this project can be found in this GitHub Repository . Challenges I ran into The hardest part of this project was deciding how best to store the readings from the ultrasonic sensor. I struggled with whether or not to use a small-footprint database, or keep recent readings in memory. I settled on writing the readings to a CSV file and then using Python’s csv package’s DictReader function to turn those readings into JSON so that it could be delivered. Another challenge was coming up with an enclosure for the physical device. While it works perfectly on the breadboard, it is quite jiggly and the jumpers could easily fall out. However, I decided on keeping it like this due to time constraints and also because it’s easier to explain since you can see every piece clearly. Accomplishments that I'm proud of This was my first time using Anomaly Detector API, and I was really impressed with how quickly I was able to create my own endpoint and start hacking. This allowed me to spend much more time on the creative side of the project rather than configuration. Besides time saved on configuration, not having to worry about writing any custom logic to detect anomalies means that I can get familiar with this one API and then use it in any similar project without reinventing the wheel each time. Also, getting the LED to blink for the first time after it detected a real anomaly (coffee levels running low in my coffee mug) was very rewarding. Note to self: maybe I should make a coffee level detector? What I learned The Azure Anomaly Detector API can be a great solution for IoT developer who offload complicated logic from their devices to the cloud. This API allows device manufacturers to limit the amount of heavy lifting that the device needs to do, which can increase battery life and decrease the overall cost of the unit. It also saves tons of time writing logic and algorithms to identify outliers in your sensor’s data set. With the Anomaly Detector API, there is no need to reinvent the wheel and code your own solution. What's next for IoT Water Level Anomaly Detector The next feature that I’d like to add to this project is some form of data visualization so that I can easily see at a glance what my device has been up to. One way to do this would be to use Soracom Harvest, which would allow me to view sensor data in various types of graphs directly from within my Soracom User Console. Another next step is to do something more than just turning an LED red when an anomaly is detected. I’d like to expand this out further and send an alert via text or email. Also was not joking about making a coffee level detector! Finally, I’d like to explore 3D printing and create a custom enclosure. One that supports different clips and attachments so that it can be deployed remotely without a technician having to make multiple trips back and forth from the site just to pick the best attachment. <div