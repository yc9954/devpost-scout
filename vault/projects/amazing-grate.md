---
slug: "amazing-grate"
url: "https://devpost.com/software/amazing-grate"
title: "Amazing Grate"
hackathon: "HooHacks 2021"
organization: "HooHacks"
winner: true
words: 1042
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/transportation"
---

# Amazing Grate

> The grate of the future. No Cap. Yes Accessibility and Environmental Conscientiousness.

[Devpost](https://devpost.com/software/amazing-grate) · hackathon [[HooHacks 2021]]

## Facets

**mechanism** [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[accessibility]] [[developer_tools]] [[transportation]]
  <sub>weak: civic_government</sub>
  <sub>weak: video_visual</sub>

**stack** arduino, autodesk-fusion-360, dht11, esp32, servo

## How they structured the write-up

- inspiration
- what it does
- how it functions
- what we built
- design challenges
- cad challenges and accomplishments
- electrical challenges and accomplishments
- what we learned
- what's next for amazing grate

## Body

Full CAD Model (based on one section of storm drain slots) CAD of Pivoting Slats and "Axle" CAD of Single Slat Image of Electronics Servo Close Servo Open Inspiration Drainage grates are everywhere and serve the essential purpose of redirecting runoff water. However, conventional grates are flawed since they are a hazard and inconvenience to wheeled transport such as wheelchairs, scooters, and skateboards. Additionally, these grates are direct paths to waterways and can serve vehicles for pollutants to end up in bodies of water. What it does The Amazing Grate can open or close depending on whether there is water present, which makes it easier for people to move over and harder for pollution to slip through. Because the Amazing Grate is closed by default, it gets rid of the uneven surfaces that people with wheelchairs, crutches, or other wheeled transportation usually have to navigate while also preventing trash from falling between the open slits of a normal grate. Because the holes in normal grates are always open, pollution is able to blow into them regularly, filling our waterways with trash. The Amazing Grate closes these holes except for when absolutely necessary, giving people time to pick up trash from on top of the grate before it opens to drain water and reducing the amount of trash that slips through the holes into our waterways. How it Functions When it’s raining the Amazing Grate appears to be a normal drain. That is because the slats that would normally fill the gaps on the grate are hanging down on pivot points. When the moisture is below a certain threshold and the raindrop sensor does not detect any rain then these slats rotate around the pivot point to close off the grate. How this occurs is the rotating slats are all connected by an axle. Similarly to how the air vents in cars work, the connecting axle causes all the slats to move even if only one slat is pushed. To close the grates we designed a lead screw mechanism to move a slanted block to push one of the slats which in turn causes the rest of the slats to close as well due to the aforementioned axle. When it once again rains and the slats must be opened, the leadscrew simply reverses and the slats drop down due to gravity What we built We designed and simulated the grate using a CAD program called Fusion360. Additionally, we made a demo of the electrical components using an Arduino, humidity sensor, a 3D printed linear actuator/servo, and various power sources. Design Challenges Our first challenges began during the initial planning stages. The reason for this was because of our self-imposed restraints (to increase the overall feasibility of the design and practicality to manufacture) of having only one motor and not using strings, belts, gears, or electro-magnets. What was particularly challenging was that movement around a pivot point is elliptical rather than linear and we wanted to use one motor to move multiple slats. Something important to note is that to make the design as feasible as possible, part of our design process was walking around grounds and looking/taking dimensions of various types of grates. CAD Challenges and Accomplishments While members of our team had previous CAD experience, using Fusion360 was a first for all of us. The different methods for creating mates in Fusion compared to software like SolidWorks, in particular, was something that initially threw us for a loop. In the execution of our design, the largest challenge we faced was avoiding overlapping components and making sure the tolerances between components were sufficient. Since this grate is something we intend to manufacture at Lacy Hall (local metal fabrication workshop) we wanted to make sure it would work in real life. The pivot point of the slats was something we struggled with because to prevent an overlap between the main grate and the slats we needed to create a slot in the main grate that the slats could rest in but if we were to do that then the part of the slat (think the inner part of a hinge) would have nothing keeping it from sliding out. Eventually, we came up with a pin-based modification to our design that allowed us to circumvent this major issue. Electrical Challenges and Accomplishments There were a plethora of hardships we faced because this was a hardware project. For the brains of our device, we chose to use an ESP32 which simply put is wifi enabled Arduino. Since this is not a device that is supported by default in the Arduino IDE we had to make configuration changes to the IDE so the board would be able to connect. We also faced issues with the wiring of our circuit. After sufficient debugging, we determined that the ESP32 board could not provide enough current to the humidity sensor and servo to work simultaneously. Since we didn’t have a benchtop power supply we decided to power one of the devices externally using just the 5V and GROUND pins of a raspberry pi connected to a battery pack. Another issue was contrary to every pinout diagram on the internet of the DHT11 sensor we used to sense humidity, the manufacturer we bought the sensor from had the data and power pins swapped. For the longest time no matter what pin or different libraries we used we were only able to get NaN values from the sensor. It was only out of the type of experimentation that results from sheer exasperation that this issue was discovered and resolved. What we learned Throughout this project, we have become seasoned users of Fusion360. Additionally, we learned how to configure and use the ESP32. This expands the possibilities of future projects to include Wifi and Bluetooth control and is something we are particularly excited about. What's next for Amazing Grate This is only the beginning for Amazing Grate. The next step is to waterjet the parts we designed and to construct a physical prototype. Then after submitting a provisional patent application, we will create a final, physical product. We hope to be able to replace old, regular grates with our Amazing Grates, making walkways more accessible and cleaner for everyone in our community. <div