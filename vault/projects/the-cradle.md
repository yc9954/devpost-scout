---
slug: "the-cradle"
url: "https://devpost.com/software/the-cradle"
title: "The Crib - Crash anxiety ​through easy guiding"
hackathon: "Pega Community Hackathon 2022"
organization: "Pegasystems"
winner: true
words: 1216
team_size: 6
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/immigration_refugee"
  - "domain/mental_health"
  - "user/developer"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/geospatial"
---

# The Crib - Crash anxiety ​through easy guiding

> You are expecting a baby? Congratulations, this is a special endeavour. You worry about missing an important step in birth preparation incl. the required administration? We guide you through it!

[Devpost](https://devpost.com/software/the-cradle) · hackathon [[Pega Community Hackathon 2022]]

## Facets

**domain** [[civic_government]] [[developer_tools]] [[health_clinical]] [[immigration_refugee]] [[mental_health]]
**user** [[developer]] [[general_public]] [[patient_family]]
**substrate** [[document_pdf]] [[geospatial]]

**stack** 8.7.3, appstudio, cosmos-react, pega

## How they structured the write-up

- inspiration
- how we built it
- challenges we ran into
- lessons / achievements
- what is next for the crib*

## Body

Case Life Cycle - Pregnancy process Enter Data - Parental acknowledgement Uploads - Birth registration Mobile View - Survey Inspiration Germany was aiming to implement the European Online Accessibility Act (OZG Online Zugangsgesetz) by December 2022, but is very late with this. This has inspired to see which processes are still not online and where Pega can help. The need I am pregnant: now what? It is important to create a healthy environment for the mother of an unborn child during the time of pregnancy. Key topics in creating a healthy pregnancy for you and your baby include managing personal health concerns, reducing stress, and preparing without stress for the child's birth. Stress during pregnancy has been linked to adverse birth outcomes ( Coussons-Read , 2013). The reality (some facts about Germany) In 2021, almost 800.000 new living babies were born in Germany and while an average woman bears 1,53 kids here, 360.000 children were first born in 2020 (Statista). The preparational medical and administrative procedures add stress to the already under pressure "to be" parents. Women and their partners are mostly lost in a labyrinth of mandatory procedures, or they are further confused because of the vast availability of providers and services. Things are getting complicated when applying for specific benefits in the German bureaucracy . There is even a 4-hour course offered to help parents-to-be in finding out how to properly move through the bureaucratic jungle to do with the birth of a kid. Gynecologists, obstetricians, and midwives are also being suffocated by bureaucracy, spending a lot of time on administrative tasks, or explaining these tasks to their patients . There is also a lot of people coming to Germany as financial or war refugees or asylum seekers. For those people it is an additional stress to have to contact with German system in a language that cannot be learnt quickly. 'Constant fear' leads to high-risk pregnancies . Our solution Our application provides all the needed information, guides the user through the adequate steps that must be followed, enables straightforward ways to reach the appropriate providers, stakeholder, or services (for example search for a birth preparation course) or communicates officially with them (for example sending an E-Mail to an employer or informing the Patient Allowance Office). Our solution is built using APP Studio only and PEGA Cosmos React. We believe it crashes complexity in the process flow of many different administrative options during pregnancy. It has the following advantages: Quick to use and easy to explain Detailed advice and variable information Can be used on all current Internet-capable browsers It is mobile phone optimized. It can be easily used by diverse groups such as refugees, who use only their smartphone for communication. The new normal after pandemic crisis also has strengthened mobile phone use, any time, in any place. Ensures the user does not get lost along the way thanks to reminder emails Doesn't ask for the same information twice How we built it We started by designing the microjourneys and aligning them to a happy path within the case lifecycle. Based on these we prepared our product backlog with all the needed user stories using agile workbench. At the build phase we started feature-driven development suitable to our user stories and recorded bugs using that tool too. Features that have been implemented only using APP Studio Mobile view Agile Workbench Collect information steps Send E-Mail Automation Create Document Automation Questionnaire Routing Decision shape Visible when Calculated fields Expressions built in app studio only, used for calculated fields and custom wait steps Picklists dropdown with autocomplete Date fields with validations Notifications Wait Shapes Reused fields Validation rules SLA Challenges we ran into Cosmos React environment None of us were familiar with Cosmos React or had developed in Pega before. We all learned Pega 8.6 or 8.7 in Theme Cosmos. As such we had to unlearn old habits, adjust our expectations of what is possible and find ways to realize our ideas using the Cosmos React Framework. Compared to Theme Cosmos, Cosmos React is more consistent, but also more restrictive if you are used to Theme Cosmos. But that was exactly the beauty of this development because we found ways to make it work. We found when composing Emails, not the full list of properties was available, it cut off around 40-50 properties, the available list was listed in alphabetical order. So we had to redo properties we needed for emails, so we would be able to select them for composing Emails. We started out using a process-oriented tool (Cosmos React) not only for processes digitalization but as an informational copy on screens, which compromised some usability. Due to the lack of some kind of information smart shape and lack of access to customize the UI to provide customer facing information, we had to resort to properties that we used with read-only to display guiding information. It can be challenging to work in parallel, when only using App Studio and the Case Life Cycle. Luckily, we had a good group collaboration and exceptional team communication and project leadership. Using only App Studio To create a time calculator to provide exact days of deadlines we needed an expression that we have found on the internet from other developers, so it is not an easy solution for citizen developers. Also, even though we created the expression in App Studio, once saved it automatically became Dev Studio only. At the end of our initial production, we implemented a parallel processing in our first app, which somehow broke our entire application, we could not even access views anymore. So, we ended up having to rebuild our App in 4 days. Despite our challenges we believe it is a great tool for Citizen Developer, and will encourage our clients to utilse its power. Lessons / Achievements All the above-mentioned user needs and challenges enabled us to create an agile way of thinking and to respond quickly and adequately to demanding situations. During this effort we have learnt a lot about Cosmos React and the differences to the Cosmos Theme. We also managed to create a copy-rich process using only App Studio. This citizen developers adjusted tool serves all the needs of an application to enhance data collection, easily set automations, make available more information through integration and so many other things. By using App Studio only, the product development is much quicker, service delivery was enhanced and we manage to align application design with user needs. What is next for The Crib* Sky is the limit and through our application and using PEGA Cosmos React we have found that there are no limits during the attempt to simplify processes for the benefit of the customer/user. Even though all of us have only theoretical experience with PEGA environment, we are certain that we are able to do more, using more features and provide easier solutions. Our application is scalable and expendable. We are ready to plan our next Minimum Lovable Product implementing more integrations, and improvement of user interface. Our final intention is to create an all-inclusive application with translations which is also adjustable for the needs of public services as well as for a human resources department in a company. Thank you, Pega Hackathon 2022, for triggering this chance! <div