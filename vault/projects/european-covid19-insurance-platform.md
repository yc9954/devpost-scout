---
slug: "european-covid19-insurance-platform"
url: "https://devpost.com/software/european-covid19-insurance-platform"
title: "enforce"
hackathon: "The European Commission's EUvsVirus Hackathon"
organization: "European Commission"
winner: true
words: 528
team_size: 6
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/patient_family"
  - "substrate/structured_db"
---

# enforce

> Easily accessible platform for immediate and affordable health coverage for people presenting already Covid-19 symptoms.

[Devpost](https://devpost.com/software/european-covid19-insurance-platform) · hackathon [[The European Commission-s EUvsVirus Hackathon]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[finance_payments]] [[health_clinical]] [[mental_health]]
**user** [[patient_family]]
**substrate** [[structured_db]]

**stack** r, rstudio, sketch

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for enforce insurance platform

## Body

Inspiration Our greatest glory is not in never falling - but in rising every time we fall. "Confucius" In these uncertain times, the anxiety for what tomorrow will bring has globally increased. Covid-19 causes various symptoms, while the way it evolves differs from patient to patient. We remove part of the anxiety by providing a solution that allows insurance companies to provide immediate and affordable health insurance coverage for people that are feeling ill. Learn more about Enforce platform What it does Enforce is a web/mobile application that provides easy access to health insurance coverage for people that are already sick by Covid-19. The user feeds the application with up to 2 symptoms he is suffering from, and the application responds with the best premium amount and immediately assigns a coverage. The application uses advanced statistical modeling to analyze Covid-19 relative data, to correlate Covid-19 symptoms, and to determine the probability of hospitalization. Furthermore, it calculates and minimizes the risk of loss for the insurance companies, with the intention to provide global minimized prices and to return the amount of the money saved back to the health care system. Reinforced learning from continuously updating the input data, allows automatic premium readjustment. Additionally, the application makes use of information provided by hospitals and mobile sensors (GPS, GSM signals) to provide feedback to the user on the closest hospital should there be a need for immediate hospitalization. Chatbots will provide one-click assistance to the low-Tech users guiding them through all the necessary procedures to get immediate access to health coverage. How we built it We have used the Bayes Theorem and calculate the opposite probability and therefore calculated if a specific symptom and age are known, the probability that the specific individual will hospitalize with Covid19 within the next days. We used Rstudio to create our Advanced Statistical Modeling. More details about the 'The mathematics behind European Covid19 insurance platform application' can be found here . Challenges we ran into 1. Since statistics differ across the affected countries, the data collection needs to be region-specific and thus the application should also be region-specific. 2. Patients struggle to identify the severity of each symptom and prioritize them according to their seriousness. A foolproof approach needs to be adopted to minimize user objectivity. To minimize user objectivity, a scoring algorithm is implemented for the weighting of the disease symptoms. 3. Some of the Covid-19 symptoms experienced may be caused by other diseases. There is a risk for the patient to pay for a premium contract that covers Covid-19, while he is suffering from a different disease. Accomplishments that we're proud of 1. The statistical analysis which provides clear evidence that health coverage with low premiums, is possible for all, even for those already suffering from Covid-19. 2. Statistical study indicates that not only is this coverage sustainable for insurance companies, but it can also return a significant amount back to the healthcare system for financing purposes. What's next for enforce insurance platform 1. We are going to use a complete dataset 2. We are going to reach out insurance companies kai medical providers to collaborate with Learn more about Enforce platform <div