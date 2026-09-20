---
slug: "ai-for-outcomes"
url: "https://devpost.com/software/ai-for-outcomes"
title: "lighthouse AI for Outcomes"
hackathon: "Predictive AI In Healthcare with FHIR®"
organization: "Darena Solutions"
winner: true
words: 1146
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/medical_record"
---

# lighthouse AI for Outcomes

> We put AI into the hands of providers to build personalized care plans and drive practice revenue

[Devpost](https://devpost.com/software/ai-for-outcomes) · hackathon [[Predictive AI In Healthcare with FHIR-]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[document_pdf]] [[geospatial]] [[medical_record]]

**stack** fhir, meldrx, node.js, openai, python, tsx

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lighthouse ai for outcomes
- judging criteria

## Body

Inspiration We began with two related beliefs for what we wanted to build: we had to have big impact (either few patients/giant impact or many patients/meaningful impact) and providers had to use it. The best tool that sits in the tool box has the same impact as the worst tool. It turns out, none of us on our team use an EHR on a daily basis (or really, at all), so we didn’t have any great insights in support of Belief #2. 9 Doctors Surveyed in the lobby of Dignity/St. John's, top answers on the board: what describes a valuable tool, and what should we avoid Winning Plans Dangerous Pitfalls Repeatedly saves me time — key on the repeat, key on ‘does it do some activity that lets me spend more time with my patient’. For example, does it help me shift my seven minutes with the patient more quickly from ‘history’ to examination EVERY time they come in, or does it enable me to have shorter calls with patients over the weekend because it scripts a more effective call. Don’t be on my screen with nothing to say. Don’t alert me 99% of the time that “it isn’t lupus” or suggest “tell your patient that sleep is important”. If you do, I won’t notice when you do have something to say. Teach me, don’t tell me — I think I am smarter than I probably am. Your approach needs to be “here’s what we found, here’s how you can find it next time”. Your button can’t just say “It’s lupus”, it’s got to take me through the differential (because as a doctor, that makes me start to trust your AI “hocus pocus dominocus”) Fake or invaluable precision. High, medium or low is good enough insight. Telling me a patient has 62.5% likelihood of macular degeneration vs. 78.4% just makes me think “are those both high or both low or are they the same?” Repeatedly makes me more impactful with my patients — I have a lot of the medical knowledge, but my patients take all the action. I am only really giving “care” if they understand me and then do something. You’ve got about 10 seconds for me to make the decision of “do I believe this enough” vs. “what’s the risk of trust” before I move on with my packed schedule. I can’t figure out if you’re smart, but if you’ve got a Mayo Clinic logo I’ll Repeatedly makes me more money — my time is fixed, I can’t realistically work more hours. Can you repeatedly help me earn more for the care that I am delivering. Don’t make me leave the EHR if you could have provided the information in the EHR What it Does lighthouse puts predictive AI into the hands of care providers to turn care plans into care action Care Plan Generation Care Action Experience Generative AI : We use OpenAI, success frameworks from groups like the ADA, AHA, COPD Foundation, Cleveland Clinic, reference care plan targets and current patient data to build a structured chronic care plan encompassing building habits in diet, physical activity, taking your meds and capturing important health data. ML AI : The care plans and the EMR are connected to a home-based Amazon Alexa experience. Each day they "check in with lighthouse" we deliver an experience that is 3 parts education to 1 part each of data capture and adherence. We use AWS Sagemaker to build a machine learning model to help us determine what is the right next piece of content. Just like the Netflix prediction algorithm, except we are deciding on whether to offer up a story on "How can I order better in a restaurant" vs. "What are methods for dealing with stress with COPD" lighthouse deals different cards through CDS Hooks to match the patient and the doctor needs we use FHIR interaction to combine real time data from the EMR and home readings to select the "deck" to serve the physician Patient Groups Opportunity Patients Insights from Home Patients Admin Needed Patients Leave Me Alone Patients Eligible, but not part of a CCM/RPT/RPM program or with an active careplan Connected to a program, with meaning changes in home captured vitals Needs non-medical attention to serve their overall care plan or program participation Doesn't need to create extra work for the provider Show provider potential value of enrolling patient in RPM/RTM/CCM. Show changes in home readings Describes situation and physician action no cards the lighthouse SMART app uses FHIR to enable bulk creation of care plans How we built it Typescript on the front end (some regrets) and python plus nodejs on the back end. Needed the nodejs for the PDF plan generation Challenges we ran into Navigating the FHIR spec. It held a ton of information we didn't care about and we were constantly trying to figure out how to reference the correct nested piece of data we needed. A lot of the spec seemed designed for comprehensiveness, not accessibility. The other extreme is Twilio. When you hit their API spec page they have you making a simple call in 30 seconds. FHIR was closer to 30 minutes. The FHIR spec needs an intelligent meta layer so I do something as simple as adding a "weight" observation and it codes it automatically with all the SNOMED and other multi-layer details. Typescript was great on the local instance. Uploading to a live server took a looooong time. "Linting" is our new least favorite word. Accomplishments that we're proud of Corralling 9 doctors in a hospital lobby to get some product guidance Real time conditional CDS Hooks "decks" of cards The care plans look pretty What we learned Build lots of helper tools to bridge the experience between the super-technical FHIR text and regular humans, e.g., there are ten different "display" fields of 3 to 15 words that all map back to "Type 2 Diabetes". OpenAI has a lot of variance in how long it takes to complete the same task -- running the same care plan could take 10 seconds or 30. Real time expectations might make for a terrible experience, asynchronous might be better What's next for lighthouse AI for Outcomes Enable for Epic, athenahealth, and other major EMRs Enable direct provider tweaking of plan goals Do a thorough HIPAA review -- not familiar enough with typescript/meldrx to understand if we are passing data around the correct way Integrate with a practice dashboard (didn't include in this challenge, it's just reporting, not AI) JUDGING CRITERIA Potential Impact Creativity and Originality Physician interviews to understand end-user Revenue model to accelerate adoption Only home based voice-first program to turn care plans into care action Documentation Thoroughness and Transparency B11 review – complete FAVES review – complete Submission Requirements Patient FHIR Bundle: 100 patients with chronic conditions, longitudinal observations and medications source <div