---
slug: "ally-kmoagt"
url: "https://devpost.com/software/ally-kmoagt"
title: "Ally"
hackathon: "TreeHacks 2023"
organization: "Stanford TreeHacks"
winner: true
words: 1469
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/disaster_emergency"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "domain/security_privacy"
  - "domain/supply_logistics"
  - "user/frontline_worker"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/regulation_legal_text"
  - "substrate/video_visual"
---

# Ally

> Ally makes drone data management simple, giving non-technical people easy access to automated workflows for their drone data. Our drag-and-drop platform gives users critical time back to save lives.

[Devpost](https://devpost.com/software/ally-kmoagt) · hackathon [[TreeHacks 2023]]

## Facets

**mechanism** [[retrieval_grounding]] [[sensor_fusion]]
**domain** [[agriculture_food]] [[civic_government]] [[climate_energy]] [[disaster_emergency]] [[housing_homeless]] [[labor_employment]] [[security_privacy]] [[supply_logistics]]
**user** [[frontline_worker]] [[general_public]]
**substrate** [[geospatial]] [[regulation_legal_text]] [[video_visual]]

**stack** css, javascript, next, openai, python, react, typescript

## How they structured the write-up

- inspiration
- what it does
- what we learned
- future
- ethics

## Body

Our logo! The current problem with disaster management Splash page Choose your role Recommended workflow based on your role Drag and drop tasks of a workflow This is our team :) We are Ally. Our mission is to save lives by automating drone data management. Continue reading to see the ethical analysis of our project! Inspiration Tens of thousands of people are dying every year in natural disasters due to poor infrastructure. Months after the devastating 2008 earthquake in Sichuan, China, Mindy visited the region and witnessed the horrific consequences of lacking up-to-code infrastructure. She spoke with locals, meeting a grandmother carrying a baby whose father was lost in the rubble when she was only 10 days old. Fast forward to today, the death tolls are now in the tens of thousands due to the Turkey-Syria earthquakes, with at least 20,000 victims still lying beneath the rubble. More than 6,000 buildings collapsed in the region, but a lot of the damage could have been prevented with better infrastructure monitoring. These earthquakes were extremely deadly because these cities did not enforce building codes or treat safe housing as a human right (Vox News). Construction companies have been cutting corners and ignoring building codes for decades, and the government often just lets it slide. Through researching current processes rescue teams use to help on-site, we started piecing together how impactful drones can be in this space. Specifically, we decided to create automated workflows because we’ve worked with drone data before and know that it’s a lot to take on as a first-time user. What it does Ally makes drone data management simple, giving non-technical people easy access to automated workflows for their drone data. Commercial uses of drone technology have been most prevalent in fields such as agriculture, forestry management, urban planning, and disaster relief, where most users are not technically familiar with image processing. Our end-to-end platform allows users to drag-and-drop tasks (i.e. for our current focus of disaster management: locate people stranded under rubble; map 3D reconstructions of high-priority areas; annotate imagery and send to relevant teams) into a custom workflow. For example, a search-and-rescue official’s workflow could be [search(”people in rubble”), map/locate() results]. Our goal is to eliminate overhead and allow any users to efficiently comb through drone image data to make informed decisions. During the hackathon, we focused on connecting drone images to semantic search, using OpenAI’s Clip neural network that brings together text and images. Users can upload drone images, search for keywords to resurface important timeframes, and sort images based on how close their query is. What we learned Drones : Though we’ve worked with drones before, Treehacks was the first time we had access to such high-tech drones from Skydio and Parrot. It was super inspiring to learn about how fast the industry is advancing and see how passionate their teams were about their technology. Disaster Management : We learned so much about the problems surrounding disaster management and narrowed down one of the major pain points– bad infrastructure. It was disappointing to hear that many of the lives lost in these natural disasters were very preventable if all parties acted ethically from the start. OpenAI CLIP Model : Most models like ChatGPT use only one form of input: text. OpenAI’s CLIP model is one of the first to effectively connect images and text by embedding them in the same vector space. This allows us to basically map out not only how close images are to each other in meaning, but also how close they are to words and phrases. Treehacks was the first time we’ve worked with an existing ML model with pre-trained weights—setting up was definitely a challenge. Image search : We learned that image search is hard to do. We considered alternative image search approaches, like using keywords, or other current AI methods. However, the CLIP model seemed to be the highest performing one. At the moment, CLIP performs well out-of-the-box without fine tuning. In the future, we see ways to improve the search by training CLIP further. Future There are lots of interesting possibilities for the future. After we create the automated workflow platform, we can expand to different customer bases. Farmers can create workflows to monitor their land (identify areas with pests, monitor soil moisture, track movement and health of livestock) and alert relevant teams. City planners can create workflows to monitor urban growth, detect poor infrastructure, and report any damage. Construction workers can create workflows to send their drones on routine checkups, inspect infrastructure for potential problems, and send alerts to intervening teams. Business Model The current plan is a freemium approach, where we give away free 1GB accounts and charge for # of users, additional storage, number of integrations, and/or computer power. We plan on first giving our platform for free out to disaster managers so they can setup their workflows and start using it for prevention methods. This way they are setup for success in the case that disaster strikes. The global disaster management market is expected to grow to 5.2 billion by 2027. The global agricultural drone market is expected to reach USD 1.7 billion by 2025, and the global market for urban planning is expected to reach USD 7.6 billion by 2027. In addition, with the rise of extreme climate events, the need for disaster relief software and tools will only grow. Automating workflows for the current existing manual processes in these fields will save immense time that is currently being used to do mundane, repetitive, logistical tasks, giving back time to spend on growth and innovation. Though money is important to run a business, we’re currently focused on saving critical time from disaster managers who will in turn be able to save more lives. Ethics We strongly believe that governments should treat safe housing as a human right. After doing a lot of research into the space, we learned that construction companies have been cutting corners and ignoring building codes for decades, and the government often just lets it slide. This was one of the biggest reasons for the high death count after the recent earthquake in Turkey and Syria. It’s ethically wrong for us as a society to allow people living in bad infrastructure to constantly be in worry about their livelihood. Or worse, not even realize how dangerous their living situation is. Thus, for this hackathon, we focused on safety because it was the most high-impact in saving lives. The first step we took was building out the drone image search, giving disaster managers a quick way to sort through their large datasets. Not only will this be extremely useful post-disaster to filter out data, but also to help identify bad infrastructure areas and notify those in the area before it’s too late. Ally makes drone data management simple and easily accessible for non-technical users. With such a high-impact space, there exist many ethical issues to further explore: Privacy is an especially important consideration when using drones for data collection. The data collected by drones can be used to monitor people without their knowledge or consent, or to gain access to sensitive information. To ensure privacy, drones should only be used with explicit consent and with appropriate oversight or regulation. Additionally, all data collected should be treated with the utmost respect for the rights and privacy of the people involved. Accuracy is also a key ethical concern when using drones for data collection. If the data and images collected are not accurate, then decisions made based on this data could be wrong or misguided. To ensure accuracy, the designers of the drones must ensure that the automated workflows and algorithms used are reliable and effective. Safety and security are also important ethical considerations when using drones for data collection. If the data is used for disaster relief, for example, then there is the potential for drones to crash or malfunction, endangering the people in the area. Additionally, drone data is vulnerable to hacking, potentially leading to a breach of confidential information. To ensure safety and security, designers must ensure that the drones are equipped with appropriate safeguards and that the data collected is encrypted. Reliability is a major ethical consideration when using drones for data collection. If the automated workflows are not reliable, then the data collected could be inaccurate and ineffective for decision making. To ensure reliability, designers must ensure that the drones are equipped with reliable and accurate sensors and that the data is stored securely. By taking these ethical considerations into account when designing our product, Ally, we will ensure that the data is used responsibly and in the best interest of the public. Resources Applications of drone in disaster management: A scoping review Vox News: How these buildings made the Turkey and Syria earthquakes so deadly <div