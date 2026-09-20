---
slug: "flatten-2o6rlq"
url: "https://devpost.com/software/flatten-2o6rlq"
title: "Flatten QR"
hackathon: "Pandemic Response Hackathon"
organization: "Datavant"
winner: true
words: 1001
team_size: 11
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/scientific_research"
  - "user/general_public"
  - "substrate/structured_db"
---

# Flatten QR

> White label solution for rapid identification of infection chains

[Devpost](https://devpost.com/software/flatten-2o6rlq) · hackathon [[Pandemic Response Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[scientific_research]]
**user** [[general_public]]
**substrate** [[structured_db]]
  <sub>weak: document_pdf, geospatial</sub>

**stack** docker, flutter, nestjs, node.js, postgresql

## How they structured the write-up

- short summary
- virtual handshake
- reports
- dashboard - health department coordinates tests
- potentially infected citizen is advised to get tested
- overview: process diagram
- technologies in comparison
- whats next:

## Body

White label solution for rapid identification of infection chains App prototype: Adobe Xd Whitepaper: PDF Short Summary Our project can be used by all responsible crisis managers and citizens worldwide. It describes a complete white label solution for anonymous tracking of citizens and the coordination of test stations and health authorities: Data-protection-compliant, anonymized tracking in real time System works as mobile app as well as without a smartphone. Infection chains are identified in real time and potentially infected persons are directly transmitted to the system in anonymized form. Systematic organization of people who need to be tested via dashboard (own login for health departments) Automated system that is monitored by health departments in order to use the existing test capacities 100 % effectively People who need to be tested receive perfectly customized information Potential opportunity to support the revival of economic systems The project is 100 % open source and can be reviewed at GitHub . The concept illustrated in this paper represents a basic possible version. It is a variably adaptable concept. Please regard the inserted screens and explanations as a white label solution, which will be individualized to your situation. Virtual Handshake To create contact chains our solution uses "virtual handshakes": There are three possibilities to do a virtual handshake: Smartphone to Smartphone Every citizen has their own QR code, which is permanently stored in his app and will be shown for scanning in a contact situation. Alternatively, the citizen can also scan the QR code of their contacts. This way a "virtual handshake" will be created, which is stored in both of their "handshake lists". Thus there is one person scanning and one that is being scanned for each meeting process. Offline QR is scanned For people without a smartphone there will be printed out QR-Codes which contain their offline IDs. All "offline citizens" permanently carry their printed out QR code with them. Citizens with smartphones scan the "offline citizens" so that the encounter is recorded in the system for both. Check-In-Point Supermarket employees (etc.) scan QR codes as people enter and leave, so that they will be tracked in the system. This can be realized directly by all companies and institutions. It is possible to automate this manual work process with a built-up scan station. Citizens with smartphones can check in by themselves. This is a huge opportunity especially for companies with several offices. They attach such check-in-point (in the form of a printed QR code) on each office door. If an employee has been tested positive for Covid-19, then only those employees who were in the same office-rooms at the same time, will be tested. Additional possibillity: Offline meets Offline In case two offline citizens meet, there is the possibility to use lists where they can put their offline-IDs, so that possible infections chains can be identified later as well. However, it is most likely a better idea to initially allow younger people more freedom of movement. In this case it can be assumed that offline-to-offline-encounters will be rare and thus the whole system can provide a very good coverage. Reports If a citizen has been tested positive for Covid-19, he uploads his test results in the app which will be confirmed by a health care manager. Users without smartphones use an automated phone hotline of their health department in order to report their results. Alternatively test results can be put into the database directly by laboratories. In this case a tested person will get notified about their results. If there is a positive result, all people linked to the infected person‘s contact chain, will be notified without revealing the identity. Dashboard - Health department coordinates tests The responsible health department receives the test results of the infected citizen and verifies them. A dashboard anonymously lists people who have had contact with infected citizens in the last two weeks. They are sorted in descending order according to their current health status, which is documented by a health diary of each citizen in a side area of the app. Here, further variables can be defined, according to which people can be sorted and prioritized for the test places (and possible treatments). For the assignment to test stations, a dashboard is displayed, which shows the current capacity utilization of the respective health institution, so that all institutions can be coordinated and thereby they are equally utilized. Potentially infected citizen is advised to get tested Citizens who have had contact with newly infected people in the past two weeks, will be informed via a push notification in the app. They will receive information about a test point to which they are supposed to go. The citizen then logs in with his QR code at the test point and the test will be performed. Overview: Process Diagram Technologies in comparison We thought a lot about which technologies to choose in order to have a working corona tracking app, which is accurate, compatible with a lot of devices and even works without smartphones for older people as well. Also privacy protection is a huge issue, which only can be solved in a satisfactory way if we use QR-code-scanning. This might not be the case everywhere, but in Europe the rules and guidelines are too strict for passive tracking of all movement profiles. To sum up and futher compare, we provided this comparison graphic: Whats next: We hope that our solution will have great benefit in the process of getting back to „normal“ life. This was our motivation to get as far as we are right now. If you are interested in this project, make sure to check out our complete whitepaper and feel free to contact us if you have further questions or feedback. Make also sure to check out our project on GitHub. If you want to support us further, please let us know or spread the word about this project, so we can go as far as possible and hopefully finalize it even after this hackathon. Stay healthy! <div