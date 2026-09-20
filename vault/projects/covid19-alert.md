---
slug: "covid19-alert"
url: "https://devpost.com/software/covid19-alert"
title: "Covid19-Alert"
hackathon: "The European Commission's EUvsVirus Hackathon"
organization: "European Commission"
winner: true
words: 1147
team_size: 7
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/immigration_refugee"
  - "user/developer"
  - "user/general_public"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Covid19-Alert

> Contact tracing

[Devpost](https://devpost.com/software/covid19-alert) · hackathon [[The European Commission-s EUvsVirus Hackathon]]

## Facets

**domain** [[civic_government]] [[developer_tools]] [[finance_payments]] [[health_clinical]] [[immigration_refugee]]
**user** [[developer]] [[general_public]] [[patient_family]] [[researcher]]
**substrate** [[geospatial]] [[structured_db]]

**stack** java, kotlin, swift

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- comparison to other parties that provides similar contact tracing solutions
- accomplishments that we're proud of
- what was done during hakaton
- what we learned
- what's next for covid19-alert. readiness to launch and roadmap

## Body

Inspiration Today, manual contact tracing used for preventing COVID19 spread, is very inefficient and slow. We decided to develop an APP that can backtrace, alert and advise people who have been recently in proximity of a “confirmed” Covid19-victim in a few seconds time. Intelligent logic should calculate the risk level of being infected and provide appropriate messages. WHO ARE WE? We started as a consortium of top-developers and scientists in Europe who saw the urgent need for this APP and felt we had to put our skills at the disposal of society now. We all worked pro-bono. Most of the developers are from Poland. Most of the communication, UI/UX specialists and scientists are from Belgium. Meanwhile we have been joined by companies and Universities. University of Antwerp has put epidemiologists, virologists, sociologists and ethical teams at our disposal. The companies Vidicom and SmartAR in Poland at the disposal of governments for after service and upgrades of the APP. The code can be given FOR FREE to any government that wants it. What it does This APP can trace back the persons that a Covid19-patient has been in close proximity with during the past X days and allows them to send them a message. It is explicitly designed to preserve the privacy of every user. In order to achieve this, no personal information is collected. Users are also able to opt out at any time. To trace users the app algorithm issues time sensitive anonymous temporary IDs that are used to identify the patient to all third parties. When two users of the app pass by, the devices exchange temporary IDs and store them in a contact history log. This log chronicles every user the patient has encountered in the last X days, and is stored exclusively on the user's device. Once a user tests positive for infection he can optionally share their log, it is sent via API to other devices where they match the stored temporary IDs with contact information. If a user opts out, their contact information is deleted from API database, meaning any log entries they appear in can no longer be matched with them. How we built it First PoC app was built within a week-end of hard work of a team consisted of two IOS developers, two Android developers, one back-end developer and UI designer. App could trace contacts, persist data and exchange tracing results via API. From that point we continued with digging into Bluetooth, improving protocol with security, discussing algorithms for risk analyses with virologists, ways of alerting with psychologists .... Challenges we ran into We already have initial application flow completed, and now we need to improve the algorithms for risk analysis and the messages that are being sent to the users. We are looking for help of virologists and psychologists to continually update the app with new findings about the virus. The biggest challenge for this kind of APP was to be accepted and used by the public. We need a penetration of >60% in the population to have a useful APP. Convincing governments and after that the public is the most difficult part. To have a larger market penetration we have the solution to make an SDK to hang the APP behind widely used existing APPS such as newspaper or banking APPs. We have put a lot of importance on a privacy, accuracy, panic prevention, appropriate communication in order to make the APP worthwile to use. Recent days we made an elaborate communication plan to convince users to download and use the APP. Comparison to other parties that provides similar contact tracing solutions Advanced protocol to communicate Android - iOS with the application running in the background. Integration and compatibility of the protocol with the DP-3T protocol and future google/apple API allowing cross-border talking between different apps in the world. Advanced algorithms to reduce false positives alerts by including situational parameters, variable backtrace time based on contagious period, reset of risk status after negative lab test result, immunity period, mask wearing, etc ... Detailed professional communication plan to make the population trust, download, use and understand the APP. An APP is only useful when over 60% of the population is using it. Therefore we are making a secure SDK to hang the APP behind famous apps, for fast and wide adoption. Option for location and heat maps based on public beacons, GPS and QR-code check-ins. This means we could possibly also warn people who do NOT use the app. Dashboard and control panel for medical authorities to adapt alert parameters and produce extra insights for decision making and follow up. Possibility to warn people who do not respect social distancing. Blockchain technology, to ensure that the validated code cannot be adapted any more and to report labtests in the APP. 9.Cooperation with Virologists but also with sociologists and psychologists from University of Antwerp. Ready to lauch in 5 days time. The basic App is under consideration with WHO and about 20 countries. Accomplishments that we're proud of We designed and implemented the combination of BT protocols that achieve the widest coverage of Android-IOS communication variants. Introduced additional parameters that impact level of risk of contagion and reduce false positive alerts. What was done during Hakaton We designed and implemented the combination of BT protocols (our extension for DP-3T) that achieve the widest coverage of Android-IOS communication variants (IOS in background -> Android is additional case that was not covered before). For now it is the best coverage of existing SDKs Brainstormed new ideas on improvements of algorithms for risk-assessment. New parameters that impact level of risk were introduced Optional functionality for location check-ins for data collection for medical authorities. Data aggregation for heat-maps presentation Elaborate communication plan to convince people to download and use the APP. What we learned We developed tracing solution based on Bluetooth and now we are experts of BT limitations of IOS and Android OS. Starting with technological ideas and straightforward approach we came across the challenges connected to psychological aspects of the solution. Now we are more busy talking with scientists than writing code What's next for Covid19-Alert. Readiness to launch and roadmap 3-5 working days. Current application contains IOS, Android apps and back-end API. Is fully functional and running in a test environment. Is ready to be launched in production within 1-2 days “as it is” or + time required for requested customisations, UI tuning etc. Road map 5-10 days Integration into DP-3T SDK to get our solution being acceptable by several governments that declared DP-3T as a requirement for contact tracing apps. 5-10 days for design and implementation of embeddable SDK as add-on to popular apps for spreading coverage. 7-10 Design and implement UX/UI and logic for collection of parameters that impact level of risk and algorithms for calculation. 10-15 Days for location collection logic and heat maps presentation. <div