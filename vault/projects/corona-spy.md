---
slug: "corona-spy"
url: "https://devpost.com/software/corona-spy"
title: "Corona-Spy"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 530
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/labor_employment"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Corona-Spy

> A smartphone app aimed at tracking the spread of COVID-19 among its users by forming links among them as they come in close contact with each other.

[Devpost](https://devpost.com/software/corona-spy) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**domain** [[civic_government]] [[labor_employment]]
**user** [[general_public]]
**substrate** [[geospatial]] [[structured_db]]

**stack** android-studio, ble, bluetooth

## How they structured the write-up

- inspiration:
- what it does:
- how it does it:
- challenges we ran into:
- our specialty:
- what's next for corona-spy:

## Body

Inspiration: In the fight to quell the spread of COVID-19, containment is currently the best weapon the globe has in its arsenal. The inspiration for Corona Spy came from the issue of inefficiency in tracking the spread of COVID-19 among citizens. Once an infected individual is identified, they're quickly placed in self-quarantine, as experts trace their prior whereabouts to disinfect those areas and to test anyone else that the person has come into close contact with. That's a labor-intensive process, prone to errors in memory, not to mention the potential privacy concerns What it does: Corona Spy is a smartphone app aimed at tracking the spread of COVID-19 among its users by forming links among them as they come in close contact with each other. WIth the forming of such links, a web structure gets formed which links users infected by the virus to those who are at maximum risk of getting infected due to contact. This structure extends furthermore to track users who may need to be tested or quarantined in the near future. The objective of the web structure is to make tracking of potential victims of COVID-19 streamlined and efficient which will help reduce the R0(R-Knaught) value of the disease significantly. How it does it: Corona-Spy makes use of the BLE(Bluetooth Low Energy) beacon technology of a smartphone to detect other BLE beacon equipped smartphones in a defined range of area around it. The range of area is defined by setting an RSSI threshold to limit the range of Bluetooth signals fetched by the beacon. This will ensure that users who are not in the close vicinity of a particular user remain undetected. To form a link between two users, a unique ID of the two users is exchanged via the BLE Beacon and gets stored in each other’s databases along with the time, date and geolocation information of the location where the contact occurred. Every user of the app has his/her unique ID associated with their account, which will help identify them during the tracking process. The UUID of every app user’s beacon will be the same to distinguish the BLE signals received by the users of the app from any stray bluetooth signals. Challenges we ran into: Establishment of a unique serial number to help distinguish stray bluetooth signals from signals received by users of the app. Our Specialty: 1) We made use of BLE(Bluetooth Low Energy) beacon instead of standard Bluetooth as it consumes significantly lesser amount of power, helping curb power consumption due to bluetooth being constantly turned on. 2) Curbing of the range of Bluetooth signals so that distant bluetooth devices remain undetected and only devices very close to the user get detected. 3) The web structure formed due to linking of users makes it extremely easy and efficient for the tracking of victims and potential victims. 4) Geo-location of the point at which two user's come in contact is recorded. This data can help the authorities in finding out COVID-19 hot-spots. What's next for Corona-Spy: 1) Government portal backed by MongoDB to make user tracking and management systematic. 2) Heat map integration to show user areas majorly affected by COVID-19. <div