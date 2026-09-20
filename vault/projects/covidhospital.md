---
slug: "covidhospital"
url: "https://devpost.com/software/covidhospital"
title: "CovidHospital.org"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 956
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/educator_student"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# CovidHospital.org

> We match patients with the medical centers they need during the COVID-19 crisis while also balancing the stress patients will place on these hospitals if not intelligently distributed.

[Devpost](https://devpost.com/software/covidhospital) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**domain** [[education]] [[health_clinical]]
**user** [[clinician]] [[educator_student]] [[general_public]] [[patient_family]]
**substrate** [[geospatial]] [[structured_db]] [[web_dom]]

**stack** amazon-web-services, django, google-maps, google-places, javascript, python, sqlite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for covidhospital.org

## Body

Home Page Concept Medical Center Database Concept Medical Center Data Entry Form Patient Questionnaire The Team Current Heatmap of Medical Center Stress Level Patient Medical Center Suggestions Inspiration "We don't have the tools that we need " ~Dr. Colleen Smith, Emergency Room Doctor, Elmhurst Hospital, Queens Our team has a close connection to some of the worst hot spots for COVID-19 in New York State, and thereby the country. Hailing from a prolific medical research university which contains a student body with a significant number of students from NYC, the unfortunate tragedy playing out in the state hits close to home. This video posted last week on YouTube by the New York Times featured an emergency room doctor in Queens showcasing the overwhelming burden the SARS-COVID-2 outbreak is placing on her hospital. It was after seeing the sheer desperation for medical supplies and support that this doctor expressed that led us to act. If the medical staff around this state, this country, could put in countless hours to help lead us through this pandemic, most with a proverbial 'hand tied behind their back', we could find a way to put our various backgrounds in computer science, electrical engineering, and robotics to work to have even the slightest positive impact. Looking through the list of potential problems we decided that given our skill set, addressing the problem posited by the Center for Radical Innovation for Social Change (RISC) at the University of Chicago, of patients seeking out hospitals that would be most convenient for them, may not whats best for the medical system as a whole. If not handled carefully and in a logical fashion, Dr. Smith's reality of Elmhurst Hospital in Queens, may soon become the reality for many hospitals around the country. What it does The solution that we developed is a website, covidhospital.org, which leverages information from a patient questionnaire and up-to-date information from medical centers around the USA to provide optimized medical center suggestions to patients for their needs. The optimization algorithm that provides patients with options beneficial to themselves and medical centers alike is driven by how the patients answer our selection of questions. The answers to the question drive a set of weights in our heuristic that will impact medical center suggestions to the patient. For example, the question "do you have a car" will determine how feasibly far the patient can travel away from their location to possibly ease hospital load in their area. One of the things from the video that stuck out to me was that certain officials were suggesting the hospitals have the supplies they need for now, but the doctors and nurses on the ground, the ones actually fighting this pandemic, suggest otherwise. Our platform can provide a voice to medical centers in the here and now. In hope of working with medical institutions around the country, they will be able to provide critical up-to-date information such as: number of COVID-19 tests, number of available ventilators, PPE status, number of COVID-19 patients, type of medical facility(full care, testing only, non-COVID only) to help further guide our algorithm on matching patients with the correct hospitals. Furthermore, we hope to make this data accessible to all medical institutions accessing our database. With the likelihood of more drive thru testing centers and field hospitals popping up around the country, it is crucial to provide an easy and accessible method for medical centers to stay informed with the latest data. To still allow the public to get a sense of the stress on hospitals throughout the country, we provide a heatmap on the covidhospital.org homepage. How we built it We built this website using a Django back end hooked into a CSS and JS front end. The medical center information is stored on a SQL database using SQLite. To acquire a baseline of medical center information we access the Definitive Healthcare USA Hospital Beds Database . This information is then augmented with the information provided directly to us by registered medical centers. No patient information is stored on our website. Patient questions were motivated by information from both the Center for Disease Control and Apple which is in collaboration with the CDC. Patient answers adjust the weights in our heuristic. Most decisions on how answers impact the weights were driven by data provided by the Report of the WHO-China Joint Mission and Chinese CDC . All map related activity is powered by Google Maps API and Google Places API. Our web server is hosted on AWS. Challenges we ran into The overall web development bugs one runs into when assembling various APIs for a website. Providing a secure method to both verifying the legitimacy of a medical center and securely host their data Coordinating the many moving parts of a team Accomplishments that we're proud of In 72 hours we were able to get a promising website up and running that can hopefully make an impact during these uncertain times Creating a solid base to move forward with to transform our current concept into an impactful tool Providing a straight forward way for hospitals to inform, where there seemed to not have been one before What we learned That during this pandemic, the desire to make a difference and help those in need, like Dr. Smith, can lead to an amazing and productive outcome. What's next for CovidHospital.org Although some final work needs to be completed on the medical center page, the self geolocation feature, and fine tuning the optimization algorithm, we hope that through this hackathon we can be connected to the right resources to help us put the finishing touches on our platform to mobilize it as soon as possible to have the greatest positive impact . <div