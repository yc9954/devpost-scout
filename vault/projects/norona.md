---
slug: "norona"
url: "https://devpost.com/software/norona"
title: "ContainCovid"
hackathon: "Hack Quarantine"
organization: "Hackathons UK"
winner: true
words: 1143
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/developer"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# ContainCovid

> A web application that enables users to securely upload their location history data via Google Takeout to assist public health officials with contact tracing and community-level risk assessments

[Devpost](https://devpost.com/software/norona) · hackathon [[Hack Quarantine]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]] [[developer_tools]] [[health_clinical]]
**user** [[developer]] [[general_public]] [[patient_family]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[web_dom]]

**stack** atlas, meteor.js, mongodb, react, safetrace, webflow

## How they structured the write-up

- inspiration
- problem
- value proposition
- core competencies
- how i built it
- what we built this hackathon
- timeline

## Body

Inspiration After I lost my phone a few weeks ago, I realized I could track it down in real time using my google maps location history. Our team discovered that, by default, "Google Timeline" logs all of our location data unless the smartphone user opts out. We also discovered that this is all downloadable via "Google Takeout". If this data could be aggregated and secured in a user friendly way, the public health implications are astronomical. Problem While we may think that we are safe in the confines of our homes, we can't self quarantine forever. The national attitude towards social distancing is shifting, and some states are already opening back up. To prevent outbreaks in the future, there is a dire need for contact tracing programs that identify potential carriers of COVID-19 based on their interactions with positively diagnosed patients. However, health departments are severely understaffed. It is projected that America needs 300,000 additional staff to conduct contact tracing interviews, but only 1000 have been hired so far. Value proposition ContainCovid is a web application that helps contact tracers identify and isolate individuals at-risk of carrying COVID-19. These individuals may choose to anonymously share their location history data, which can help prevent community-wide transmission. These individuals may also share the contact information of people they have recently interacted with. As such, ContainCovid streamlines communications between contact tracers and their clients, effectively reducing the transmission of COVID-19. Although many “risk exposure notification” mobile applications exist, they either continuously collect sensitive GPS data (ie SafePaths) or log interactions via bluetooth (ie apps using the Google/Apple API), the latter of which being quite useless for public health authorities to communicate with and serve their communities. These mobile apps also require ~40% of the population to download a single solution to be effective. However, only ~17% of the Singapore population downloaded an app endorsed by the national government, and the US has dozens of such competing apps that don’t cross-talk. Fortunately, ContainCovid does not need a large critical mass of users to be effective. Our solution does not log data in real time, but rather looks back in time at existing data stored on any Google Maps user’s smartphone. As such, we don’t require anyone to download an app preemptively. Furthermore, we don’t require a huge critical mass of users. Instead, we can simply partner with healthcare organizations to share the platform with COVID-19 patients. These patients’ location trails are readily available, and this data is useful even if accessed post-diagnosis. We can then encourage these patients to invite their contacts to the platform, perhaps anonymously with a public health official as an intermediary. This will ensure that the “primary” contacts of COVID-19 patients are informed of their risk of exposure. Core competencies Out team's competitive advantage lies in our incredible development speed, made possible by our development stack— Webflow + meteor.js (and MongoDB) + React. We are also partnered with professionals who are leading contact tracing efforts in Massachusetts, as well as the UC Berkeley Department of Public Health to pilot our launch within the UCPD and the Berkeley campus Tang Health Center. Through these channels, we will pilot our technology and acquire location history data from confirmed COVID-19 patients. This can all be done without accessing sensitive patient health records; in this initial phase of our launch, we will only distribute this technology through healthcare providers' communication channels, circumventing the need to verify self-reported positive tests with EHRs. How I built it The web application was designed in Webflow and implemented with Meteor, React, and MongoDB. We chose this stack because it would enable the designer, front end developer, and back-end developer to work in parallel for most of the process. We are currently hosting our site on Galaxy and MongoDB Atlas; both can be scaled at the click of a button. What we built this hackathon We restructured our entire codebase to make it more modular, allowing this project to be truly open source and ready for anyone to use. To do this, we ran a security audit of the code as well as our hosting providers. This security audit included: defining rate limits for requests checking for exposed client side database method calls enabling strict browser policies on what content type from which origins can be loaded in the app whitelisting which IPs can talk to the database enabling two-factor authentication requiring difficult passwords when creating an account checking for potential NoSQL injection points. We also fixed numerous bugs and incomplete features, such as the inability to log out links for web pages were inconsistent with the user flow disjointed front and back end elements, such as the "check risk" button and the risk assessment algorithm lack of clarity in the user flow for undiagnosed individuals Notably, our team also doubled in size from 6 to 12 members. We worked meticulously on the UX of our contact tracing dashboard in Webflow based on feedback from various mentors and newly recruited designers. However, perhaps our most significant accomplishment this hackathon was our sprint to create a web application tailored for use in a UC Berkeley public health study . Finally, we began our customer discovery process with a Facebook ad campaign to survey whether people would be comfortable sharing their location data through a web portal, which to our surprise was over 50% of randomly sampled respondees. Timeline As of June 10th, 2020, ContainCovid is working towards a soft-launch as a data collection platform for a UC Berkeley study. If all goes well, ContainCovid will be used to assess the feasibility of opening up campus. ContainCovid is also working to make a centralized contact tracing portal with the aforementioned chatbot functionality. Our self-imposed deadline for this contact tracing portal is June 15th. By early July, we hope to show proof-of-concept to public health organizations, either through the UC Berkeley study or a public soft-launch. We strongly believe that rapid contact tracing is crucial to adapting to a new normal, and by mid July, we expect to integrate our platform with existing state-imposed contact tracing platforms. To reach this endpoint, we hope to form crucial partnerships beyond our UC Berkeley network. We are currently in touch with MIT Safepaths, and we hope to partner to inform public health officials with actionable data on population-level transmission. We are also partnering with CoVis, a data intelligence platform that provides deep insights into population-level immunity. In terms of organizational structure, we are fiscally sponsored by The Youth Project USA, a 501(c)(3) nonprofit. Finally, we hope to form meaningful relationships with contact tracing organizations like Partners in Health, provider networks like Kaiser Permanente, and CROs like Curebase to distribute our platform COVID-19 patients. These patients have the most powerful and actionable data, as well as the strongest incentive to anonymously share this data to protect their communities. <div