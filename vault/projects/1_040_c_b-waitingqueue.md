---
slug: "1_040_c_b-waitingqueue"
url: "https://devpost.com/software/1_040_c_b-waitingqueue"
title: "040_medizinischesPersonal_1_040_qme"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 1423
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/immigration_refugee"
  - "domain/retail_commerce"
  - "user/clinician"
  - "user/developer"
  - "user/educator_student"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/document_pdf"
---

# 040_medizinischesPersonal_1_040_qme

> Our realtime queue system managers that people arrive just-in-time at the doctor

[Devpost](https://devpost.com/software/1_040_c_b-waitingqueue) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**domain** [[developer_tools]] [[education]] [[health_clinical]] [[immigration_refugee]] [[retail_commerce]]
**user** [[clinician]] [[developer]] [[educator_student]] [[patient_family]]
**substrate** [[code_repository]] [[document_pdf]]

## How they structured the write-up

- what is the challenge?
- what is our vision?
- who is our target group?
- what is our solution?
- what makes the qme service special?
- what state does the prototype have?
- what will be the next challenges?
- what else have we worked on?
- the team
- try it out

## Body

Qme Logo initial concept of landing page implemented landing page search for doctor get a slot Get your estimated time when you have to arrive. You will be notified via email if it changes. Doctors can view the queue, add emergencies and mark patients as done. Based on continous marking, we can estimate the arrival time. What is the challenge? People are queueing at different locations, like in doctor’s offices or in supermarkets for shopping. Social distancing is the best way to protect yourself and others from COVID-19 infections. However, avoiding crowds in waiting rooms is not easy. The challenge of “social distancing” and waiting lines has not been a relevant use case in the past. Despite telemedicine applications and reminder services for doctor appointments being increasingly common, the Qme service solves the new problem brought forward by the pandemic: Keeping your distance in queues. What is our vision? We want to create an easy-to-use solution to avoid unnecessary exposure to crowds in waiting scenarios and small spaces. We initially focus on doctor’s offices, while keeping other use cases for example testing facilities, pharmacies and supermarkets in mind. It was important for the team to come up with a minimum-viable-product, which can be developed within a week and is a quick-win for the current situation. We started to work on this journey at the #wirvsvirus hackathon where we had met as a team on Friday, 20th of march 2020. Our team of 7 people from Hamburg, Berlin and Munich defined the challenge we wanted to work on and quickly established a common vision. On saturday morning we started to scribble first ideas to visualize our vision and started the development from there. But we not only created the technical solution, but also thought about roll-out, training, marketing, user acquisition, support etc. We have come a long way: Between the first visualization on saturday morning and the version we presented in our video were not more than 36 hours! #wirvswarteschlange Our vision does not stop at the end of the hackathon on Sunday, 22th of March. We want to see the Qme service implemented and rolled-out to anyone who can use it for their waiting line purpose. Who is our target group? For the initially developed version, healthcare employees and patients are the target group. At the end of 2019 there was over 390.000 doctors in Germany. The Qme service is directly affecting them in their daily patient flow during the crisis and supports them in improving their precaution activities to protect their patients and staff. Additionally the Qme solution is created in a way that it can be used to serve any use cases to avoid crowds in waiting lines/rooms. For example supermarkets and customers. When enlarging the service to other use cases, the service can affect basically everyone in Germany. And for any other country - the virus is borderless, so are we! What is our solution? Social distancing is the best way of protection against COVID-19 infections. Qme enables patients to arrive at the doctor’s office “just-in-time”, avoiding crowded waiting rooms and thereby minimizing the risk of infection. Follow the link to our pitch video: https://youtu.be/9kVjIoGdUPc Patients can check into the queue line safely from home: They just enter their Zip code, choose a doctor’s office and check into the waiting line. The patient will be notified via email when it is time to go or if there is any delay at the doctor’s office. This minimizes the risk of infection not only for the patient but also for the medical staff. The doctor can easily manage her queue efficiently and add emergencies or prioritize non-digital risk group patients. The doctor and staff can check out patients when they are done and the next patients in line will be automatically informed. Qme’s basic principle can be employed and adjusted for different use cases, like testing facilities, supermarkets or pharmacies. Same as the virus, Qme is borderless. What makes the Qme service special? Our focus is avoiding crowds and queues while waiting for your turn. The Qme service focuses on patients staying at home while waiting and arriving “just-in-time”. To ensure the service can be used by digital and non-digital target groups in combination. The Qme service incorporates options for a manual functionality so the doctor can add non-digital risk patients onsite to skip the line. Our solution is based on solidarity and provides assurance to every user - patients and medical staff - that social distance can be maintained. What state does the prototype have? Our prototype consists of the following parts: A web application containing frontend and backend components running on Google Cloud https://queueme-dev.firebaseapp.com and build on top of react, material ui, nodejs/express, firebase functions, firebase firestore and firebase hosting. If you want to test it, search for doctors in the area code 22307 when registering as a patient. Visit https://queueme-dev.firebaseapp.com/doctorsqueue and see how doctors can checkout patients. A multistage automatic deployment process (Continuous Integration) based on GitHub Actions to integrate new features into the live system on daily basis Documented open source project hosted on Github https://github.com/CConnection/qme with the possibility to either get the code and host it yourself on firebase or contribute to the code via pull request. The pull request will be managed by us and directly integrated in our live system, so that we can grow it together. i18next ready - easy implementation of other languages. Can be done by contributors who speak the language. Currently only english but german language can be added within half a day. Design Mockups in Sketch files Although we did not finished the whole prototype, the base application works and the API’s are ready to be integrated with the frontend. As the code is available on Github, including a comprehensive documentation about how to contribute, it would be easy to take the project to the next stage with the knowledge and power of the community. We paid attention to automate many things, provided scripts to run different commands like testing, linting, building and deploying so that others can help us to bring Qme to the next level. What will be the next challenges? From the current state, we see the following main challenges when bringing the product out into the world: We need to build a network of doctors who offer this system in order to be valuable for the patients. We see that this is the most challenging next step. Further, as we developed a prototype, we need to ensure the quality and security of the code base by improving it before going live We need to finish the implementation of the administrative pages and polish the existing features When scaling out into the world and potentially millions of users we need to ensure that the financial base is ready to be able to pay for the infrastructure costs ( Funding needed for operational costs only ) The remaining technical polishing can be done within some days, max. up to a week, depending on the number of contributors. What else have we worked on? In order to create a comprehensive solution we have also taken time to think about topics related to the implementation and roll-out of the Qme service. We have thought about Adoption to more Use Cases Acquisition of medical institutions / doctor’s offices Marketing for end users / patients Training concepts Technical support for implementation Data protection Costs for providing the service International roll-out Please see more details to our thoughts and ideas for these topics in the attached document https://docs.google.com/document/d/1CkkJdTPMq8mfLNHowV8HpiTKg4rQanUSp8Ze58K5Lag To ensure our solution is scalable and can be applied to other use cases we have kept testing facilities, pharmacies and supermarkets in mind. The solution and all the surrounding documents are available in english, so they can be shared internationally for anyone wanting to avoid waiting lines at any scenario. The code is of course open source. The team Name Skills / Knowledge Role in the project Finn Christiansen Backend Development & DevOps (Java, Kotlin, Golang, Javascript, React) Product development Frauke Puttfarken BizDev, Marketing, Strategy, Ticketing, Telemedicine BizDev, text creation, marketing Jurga Kunze UI design Sketch UI design, video Sandra Classen PhD-Student in Radiobiology, Marketing, Organization, Healthcare Experience Marketing, text creation, voice of video Thomas Kunze Ex - Product Owner, Developer, React, NodeJS, Golang, Firebase (a little bit), Typescript, HTML5, CSS3, C++, Sketch Product development Christopher Biel Tech Lead, DevOps, React, NodeJS, Golang, AWS, Terraform, Typescript Product development Marius von Pawel Product Owner, healthcare experience Product Owner Try it out github.com <aside class="large-3 columns"