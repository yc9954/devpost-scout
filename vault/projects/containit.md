---
slug: "containit"
url: "https://devpost.com/software/containit"
title: "ContainIt"
hackathon: "Pandemic Response Hackathon"
organization: "Datavant"
winner: true
words: 1197
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/on_device_local"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/legal_justice"
  - "user/clinician"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# ContainIt

> We are motivated to help the global community contain the spread of COVID-19 by using contact tracing. We want to securely and intelligently provide users key insights on their risk of being infected.

[Devpost](https://devpost.com/software/containit) · hackathon [[Pandemic Response Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[on_device_local]]
**domain** [[civic_government]] [[developer_tools]] [[health_clinical]] [[legal_justice]]
**user** [[clinician]] [[researcher]]
**substrate** [[code_repository]] [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** amazon-web-services, gps, javascript, mongodb, react-native

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for containit

## Body

Welcome Nav bar Reporting Result Sign in Sign up How it works How it works About us FAQ React Native Icon Inspiration Finding novel and impactful ways to help fight the spread of COVID-19. We wanted to find a way to alert individuals who had possible contact with carriers of COVID-19. Because of the long incubation period of COVID-19, many users who were exposed to the virus might not know that they were and can spread the virus. This is why it grows so rapidly, and we wanted to innovate a secure, precise, effective contact tracing solution. Through our app, we can provide content for researchers in the future to fight diseases like COVID-19 with user permission. We envision giving data to CDC, WHO, state/federal public health authorities, universities, which can be crucial to understand how diseases spread and how to contain them. What it does We have developed an app that will use location data over a period of time to help notify others if they have been in close proximity of a victim of coronavirus while also providing them with key insights on their probability of being infected. The app notifies and redirects exposed users to proper resources based on feedback we received from public health directors, surgeon generals, and government officials. The app uses contact tracing is an effect way to mitigate the spread of infectious diseases and #flattenthecurve How I built it We built the app using React Native, MongoDB, and a variety of Amazon AWS services. Data Types Location Point: data points collected by a user’s phone which include location (with measures of uncertainty) and a timestamp; has a unique location ID, associated with users through user ID Data: Location ID (unique) User ID Location Latitude, Longitude Measure of Uncertainty: radius in which the user was likely located Time Uncertainty: the measure of uncertainty can be interpreted as the variance of a 2-dimensional Gaussian distribution, which can help determine the probabilistic density that the user was at a particular location. We can use this uncertainty to develop a threshold which thus can be used to notify users. User Health Condition State Transition: indicates the change of a user’s health condition over time; the health condition of the user can be interpreted as a finite state machine in which this data structure indicates a transition to a new state at a certain time; this is manually recorded by the user through the app Data: Condition ID (unique) User ID New State Time of Transition Time of Modification States: Asymptomatic Unknown: the user does not have COVID-19 symptoms and has not been recently tested This is the default state Asymptomatic Positive: the user likely became contagious with COVID-19 at the given time but did not show symptoms Asymptomatic Negative: the user tested negative for COVID-19 at the given time and does not show COVID-19 symptoms This state does not carry much meaning since COVID-19 tests are optimized for low false positive rates (and consequently have higher false negative rates) and users may be exposed shortly after receiving a test Symptomatic Unknown: the user developed COVID-19 symptoms at the given time but has not yet been tested (or never was tested) If the user is tested, they should update this transition Symptomatic Positive: the user developed COVID-19 symptoms at the given time and later tested positive Symptomatic Negative: the user developed COVID-19 symptoms at the given time and later tested negative Recovered: the user was previously tested positive with COVID-19 and became no longer contagious at the given time This is the terminal state Using a simplified model with unknown, positive, and recovered states currently. Users when they have symptoms will be told to consult physician if they have been in close proximity with an infected individual Asynchrony: since users should be able to retroactively update their state on testing positive for COVID-19, the algorithm must be able to have the tolerance to trace back several days for its search. This will enable us to make a more precise tool and enable users to gain more autonomy. After consulting with health professionals at Duke Infectious Disease Program and Duke Global Health, we have concluded using 14 days of location data prior to the test and 10 days after testing positive is most relevant for determining exposed individuals After consulting with public health officials, we determined the algorithm should notify users who have been less than 6 feet for more than 10 minutes. Users should be able to update states ultimately and Positive/Negative states should replace Unknown states whenever possible Initialization: all users receive a condition upon registration; the time is the time of registration, and the state is asymptomatic negative Time-Space Block: data structure for use in the database to quickly look up and compare location points. We reference this block by id, and we use the data here to determine which agents to ping. Data: Location Bounds: e.g. 500 meters by 500 meters Time Bounds: e.g. 5 minutes Data Collection Location data is collected continuously in the background of the user’s app. This data is stored locally on the user’s device. The user’s device periodically polls the server If a user marks themselves as infected, their location data from the past 14 days is sent to the server. Once an infected user’s location data is sent to the server, their current state and a 5 kilometer pull request for users within that location is sent out to all active non-infected users Non-infected users that overlap that time and location block get their data sent to the server Event Trigger at Block Contamination: Whenever someone gets infected all blocks they have been in are contaminated Contaminated blocks automatically are pinged for data to be sent to the server The phones in these blocks are evaluated Using gaussian distribution/other metrics and compared with a threshold The potential contacts are notified and directed to official resources Communication with User How users are notified Users are notified through email or phone Notified with a risk factor and future steps and to Challenges I ran into Some of the biggest challenges were initially building the app using AWS, going through the legal process in getting support, and making sure we were being fully secure and HIPAA compliant. Accomplishments that I'm proud of We have formed partnerships with local governments in North Carolina, Alabama, and other states where there aren’t as many cases yet. We are also reaching out to various local governments as well to help promote this in their community. We formed partnerships with Duke, and we are working with the NIH and CDC as well to gain their feedback and support on the app. We have received great support from accelerators as well and many online communities. Our proudest accomplishment is our rapid development of this application and how effective and precise it is. We use HIPAA compliant services. What I learned We have learned a lot about networking, reaching out, development in AWS, mobile app development, and public health in general. What's next for ContainIt Deployment and Distribution, Scaling, Growing, Adding features, providing predictive modeling if you need access to github, email me at ssm80@duke.edu <div