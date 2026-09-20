---
slug: "measuring-taste-to-diagnose-diseases"
url: "https://devpost.com/software/measuring-taste-to-diagnose-diseases"
title: "Measuring taste"
hackathon: "The European Commission's EUvsVirus Hackathon"
organization: "European Commission"
winner: true
words: 1437
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/accessibility"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "domain/scientific_research"
  - "user/clinician"
  - "user/educator_student"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/regulation_legal_text"
  - "substrate/structured_db"
---

# Measuring taste

> You might have measured your eyesight or your hearing, but have you ever tested your taste ?

[Devpost](https://devpost.com/software/measuring-taste-to-diagnose-diseases) · hackathon [[The European Commission-s EUvsVirus Hackathon]]

## Facets

**mechanism** [[sensor_fusion]]
  <sub>weak: cross_origin_web</sub>
**domain** [[accessibility]] [[education]] [[finance_payments]] [[health_clinical]] [[mental_health]] [[scientific_research]]
**user** [[clinician]] [[educator_student]] [[patient_family]] [[researcher]]
**substrate** [[regulation_legal_text]] [[structured_db]]

**stack** bluetooth, fhir, iot, json, kotlin, node.js, omop, react.js, swift

## How they structured the write-up

- inspiration - the problem your project solves
- what it does - the solution we bring to the table
- how i built it - what have we done during the weekend
- the solution’s impact to the crisis
- business model
- challenges i ran into - the necessities in order to continue the project
- accomplishments that i'm proud of
- what i learned
- what's next for measuring taste
- value of our solution after the crisis

## Body

New design of our device New design of the electrode going on the tongue New design of our device and electrode Our device fully deployed Mobile App - Result Page Mobile App - login page Mobile App - area of the tongue to test Mobile App - automatic protocol with double blind measure Mobile App - Bluetooth Connect Mobile App - Choose your protocol Web app - list of patients Web app - evolution of taste for a patient Existing prototype Existing prototype Mobile App - Summary of screens Inspiration - The problem your project solves A scientific study carried out in 7 different countries on COVID-19 patients shows that: • 86% of infected patients will present partial or complete disturbances of smell and 88% of partial or complete disturbances of taste . These disturbances of smell occur either before the onset of symptoms (general and ENT) (in 12% of cases), or during (65% of cases) or after (23% of cases). • 44% of patients have already recovered their sense of smell within a short period of 15 days. The rest of the patients should be hopeful of recovery, which could happen within 12 months of the onset of symptoms (nerve recovery is a slow process) . • Anosmia and / or dysgeusia which has occurred in the past few weeks in patients with no previous ENT history (chronic sinusitis, nasal polyps, nasal or sinus surgery) should be considered as a specific symptom of COVID-19 infection and should be officially added to the list of other symptoms listed by WHO But doctors don't have any scalable, non expensive and reliable way to get a quantitative taste measurement . What it does - The solution we bring to the table Several taste measurement methods exist today, via different psycho-physical tests which are complicated to set up and analyze, mainly due to the lack of repeatability and the duration of analysis of the measurements. Other methods of measuring taste exist, in particular by means of electric currents in order to cause electrolysis of the saliva and thus make a taste appear , just like a battery on your tongue. The intensity of the electric current causes a more or less intense taste, so we can measure the taste sensitivity of a person. The goal of our device is to measure the lowest current possible that will trigger the smallest taste possible that a patient can taste on any of the nine areas of the tongue, and by doing so every week/month/year, we can follow up how the taste sensitivity evolve and thus diagnose diseases like COVID-19. This last method is the device we will begin to build during this hackathon. The device will be composed of a connected device, linked via Bluetooth to a mobile application which will control the device using different protocols (like a manual setting protocol or a double blind automatic protocol using a specific algorithm developed by doctors and researchers). An electrode and an electrode holder will allow doctors to test taste on one of the nine area of the patient's tongue. All those data will then be saved on a secured cloud and accessible only by healthcare professional in order to monitor patient health in order to better diagnose diseases or side effects of some drugs. By using FHIR and OMOP database architecture , we will also be able to cross reference medical data from other devices or electronic health record, in order to define patterns which will allow use to better diagnose some diseases, even do some preventive medicine. How I built it - What have we done during the weekend It is a IoT device composed of a connected object, controlled by bluetooth (BLE 5.x) by a mobile application and connected to a secure approved health data host in order to be able to follow the progress of a patient. All web development is done in javascript (Node, KOA2 and React), on a MySQL database (OMOP and FHIR architecture, GraphQL API). All mobile development is done in native language, Kotlin for Android and Swift for iOS. All hardware is fully proprietary, as well as the firmware. During the week-end, we have: • entirely redesigned the device • entirely redesigned the mobile application • entirely redesigned the web application • coded a new protocol to automatically measure taste with double blind measurement in order to avoid false positive results. • defined our market access strategy, especially about the creation of the medical act • defined our medical device certification strategy and done extensive research in research papers • began to define our distribution strategy, especially the negotiation of INCOTERM and the different strategies we need to establish when working with medical device distributors We now have a fully functional prototype for the device and mobile applications and we need to keep coding the web application. The solution’s impact to the crisis By measuring taste sensitivity, we will be able to: • better diagnose COVID-19 patients • better follow-up for COVID-19 patients in order to monitor how the disease evolves • improve deconfinement strategy as we can monitor with our device COVID-19 health easily • improve preventive campaigns if COVID-19 virus comes back Business model Our device will be mainly for healthcare professionals (researchers and doctors), so we will have a B2B business model with medical device distributors in order to get the fastest way possible to multiple markets, either geographic or healthcare specialists. Our business model will be a big one-off sale of our device and recurring revenue will come from consumables (we have sterile electrode which will be used only once as you have to put it on the patient tongue), which will be around 1€. Then, by creating a medical act , we will also be able to get a refund code from insurance and/or social security in order to spread that medical test faster. By doing so, it means that our test will cost roughly about 1€ per patient, which is one of the cheapest specific medical act you can get to diagnose COVID-19 patients . Cost and timeline to get that product to market will be high (around a year before finishing industrialization and then about 6-8 months before getting the medical certification process . Cost will be varying according to where we do the industrialization and the technical choice we will make - but we intend to manufacture the device and the electrode in Europe, mostly for quality reasons and certification process). Challenges I ran into - The necessities in order to continue the project Creating an IoT device is complicated and takes an enormous amount of time, even more when it is a medical device, especially because of the regulations and clinical trials necessary before being able to put the product on the market. Necessities to continue the project will be to have access to healthcare professionals who are willing to do clinical trials in order to get clinical proof for our device and funding to pass the certification process and industrialization phase. But it is definitely a challenge we are willing to push, to make that device come true and definitely save life in the process. Accomplishments that I'm proud of My prototype is working, our new designs are stunning and our team is the best! We already have tested our product on more than 800 students, and we intend to keep that database growing! What I learned It is definitely one of the worst and most difficult areas because of all the technical challenges and regulations, but there is no better challenge to create something really new which can help save lifes. I also learned that despite all the challenges that have already been achieved, there is so much more to come and we need everyone who is passionate about medtech and challenges! What's next for Measuring taste • Keep developing our solution • Improving features thanks to feedbacks from doctors • Developing interoperability process to cross-reference our information with other medical data • Listening to patients and experts in order to make the product always better! Value of our solution after the crisis There are also many environmental (i.e cigarettes) and medical (chemo and radiotherapy, nerve operations, diabetes, neurodegenerative diseases, oral hygiene ...) factors that can affect our taste and can lead to irreversible changes. These taste disturbances can be the first symptoms of more serious pathologies or side effects (such as peripheral neuropathies for example) and subsequently lead to many other disorders if they are not considered in time (i.e cholesterol, obesity, heart problems, due to excessive consumption of salt or sugar). <div