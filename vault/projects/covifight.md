---
slug: "covifight"
url: "https://devpost.com/software/covifight"
title: "CoviFight"
hackathon: "The European Commission's EUvsVirus Hackathon"
organization: "European Commission"
winner: true
words: 1384
team_size: 14
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/civic_government"
  - "domain/disaster_emergency"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/transportation"
  - "user/educator_student"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/geospatial"
---

# CoviFight

> CoviFight showcases how the integration of Bluetooth with Social Networking Analysis makes contact tracing highly effective and the world can come to a working state of normalcy as early as possible.

[Devpost](https://devpost.com/software/covifight) · hackathon [[The European Commission-s EUvsVirus Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[structural_withholding]]
**domain** [[civic_government]] [[disaster_emergency]] [[education]] [[health_clinical]] [[transportation]]
**user** [[educator_student]] [[general_public]] [[patient_family]]
**substrate** [[geospatial]]

**stack** android-studio, blockchain, bluetooth, dockers, firebase, google-directions, graphdatabase, har, ios, java, kubernetes, machine-learning, maps, neo4j

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- our journey so far
- what we learned
- what's next for covifight
- the necessities to continue the project:
- the value of our solution after the crisis:
- what we have done during the weekend

## Body

Inspiration The virus has affected humanity in various ways, be it our economy, our freedom of movement, and the loss of loved ones. Then how do we live on, comfortably, and safely with this virus around? Even after the lockdown is over, there is a massive possibility that traces of the virus will remain, and it can spread again. We wanted to bring people back their mobility and keep them safe at the same time. We wanted people to know about their status while they leave their houses. What it does CoviFight is not just a contact tracing application. It is a 3-tier solution which:- • By using Machine Learning and Social Networking analysis, CoviFight alerts the users the risks of catching the virus if they have come in contact with an infected person within the past three weeks. • Identifies the public place or the transport mode, be it a bus, a metro, or a McDonald's restaurant, that needs sterilisation. No other application in the world is capable of doing so. • It informs the medical system accurately about the spread of infection. The medical system rather than individuals handle data, and authenticity is maintained. • It generates a map with hotspots for what places have virus traces so that people can prevent travelling at these places and authorities can sterilise or lockdown these places efficiently rather than having a complete lockdown of a country. • CoviFight does not even need to compare data between people, thus making computation very cheap and exponentially faster and efficient. If Contact tracing apps already exist: Even if you have a contact tracing application launched in a region, our second and third-tier may supplement the existing application. These tiers may add to the architectural ecosystem of the app without modifying the app at all. It creates a supplementary layer of the architecture of the existing contact tracing apps and creates an ecosystem. We create an environment where devices connect independently and irrespective of their running OS and the contact tracing app installed. All our apps can seamlessly integrate with any existing app's architecture. Our apps are capable of detecting and communicating with other apps like Aarogya Setu and COVIDSafe. The flexible nature of CoviFight provides the user with a choice of selection. The dynamic nature of our product gives the users a choice to use our app with or without GPS tracking. Currently, the global market is saturated with many products claiming efficient contact tracing, but not a single app in the industry is capable of detecting aggregation points. Our architecture is developed to flexibly integrate with the existing system created and adopted by the government. Apple and Google Guidelines: Tracking of aggregation points( stores and public transport) is a difficult task to perform. Tracking people who have access them is also a challenging task. Before it was feasible, though very complicated and requiring complex computation, these were feasible by geo-location and time stamping. But the recent guidelines issued by Google and Apple prohibit the use of these techniques, making indirect contact tracing infeasible. The fantastic thing is, our three-tier solution allows us to do so even while following the concerned guidelines. How we built it We develop a three-tier app: • A user's app • A provider's app • An official's portal. Privacy: While utilizing Bluetooth of your phone, CoviFight makes sure that the confidentiality and privacy of every individual are secured and can not be compromised. Data is encrypted using a secret key, and no one can view it without your permission. It only traces the past data of positively tested patients. This way, CoviFight also meets the GDPR compliance. Hence, we have made sure that the privacy of every individual is maintained and can not be compromised. The encryption algorithms meet the standards of the leading social networking apps existing in the market. Provider's app: A provider's app for aggregation points like shops, restaurants and public transport synchronizes with the nearby user app. This interface is the key to the detection of infection points, be it a stationary workplace or a moving vehicle. If a restaurant installed CoviFight and had an infected customer in the past 15 days, all the customers after the positive tested patient would get alerted, and hence the restaurant can be sterilized. Official's Portal/ Doc App: Only the medical system may update a person's status over the official's portal, and the authenticity of the app is maintained, hence preventing false positives or self-reporting, which might lead to falsification of records. No one else can manipulate the data. Hence, people can move around while being alerted about their status. They can stay away from the virus, and be free from the worry of their privacy maintenance at the same time. Challenges we ran into To maintain the authenticity of the predictions and analysis, we were initially in a fix as to how to update a person's status as positive or negative. Then we decided to come up with a three-tier system, and we developed a Doc App or official's portal, which is only accessed by the medical system so that the authenticity is maintained. No one else can manipulate the data. Accomplishments that we're proud of • We have made sure that the privacy of every individual is maintained and can not be compromised. The encryption algorithms meet the standards of the leading social networking apps existing in the market. • CoviFight not only alerts people about their own risks but provides heatmaps of the traces of the virus too. CoviFight also shows what specific restaurant or public transport( like a bus or a train) may be infected precisely. • We do not need to compare data between people, thus making computation very cheap and exponentially faster and efficient. Our Journey So Far • Winners( Runner up) in the #EUvsVirus, a Pan-European Hackathon Organised by the European Innovation Council to counter COVID-19 pandemic with more than 9k participants and 2000 teams. We stood second in the Real time Communication and Prevention challenge. • Top 6 finalists of The Global Hack, by Garage48, April 2020 The Global Hack is a hackathon designed to share and rapidly develop ideas for urgently needed solutions in the face of the COVID-19 crisis, and to build resilience post-pandemic, with over 12k participants from 100+ countries. The team developed a mobile application solution for the containment and tracking of this virus. We were in the top 6 teams in the Crisis Response Track. • Top 23 Student Innovators in COVID-19 SAMADHAN MHRD( Ministry of Human Resource Development, India) Mega Online Challenge What we learned It has been an enjoyable experience to work with people who have not even met each other before and still successfully develop this amazing app. We learned a lot through the hackathon, from interacting with the mentors and getting their guidance, to develop the app. What's next for CoviFight We plan to get this deployed at its earliest so that people may get their safe mobility back. We plan to deploy this on the Play Store and make a version for iOS as soon as we can. We are also in touch with the Indian Government and we might be able to save lives in India also. The necessities to continue the project: • Approval from government authorities to implement and track data. • Participation from Hospitals/government bodies to update the status of a patient so that system can generate realtime alerts and mark hotspots. • Cloud resources to scale up the project. Currently limited by the free tier of cloud infrastructure. The value of our solution after the crisis: • This application can be used for any contagious disease management. • It can be used in disaster management to understand the right victims and relief reaches all rightful beneficiaries( such as in the case of floods and storms). • It can be used by Providers such as McDonald's and Public transport systems to implement targeted location-based marketing complying with data collection practices. What we have done during the weekend • Implemented masked identities for users to comply with GDPR and privacy requirements. • Identification of hotspots in realtime based on the patient status update. • Fixed bugs in the flow and to make it work E2E. • Produced a product demo. <div