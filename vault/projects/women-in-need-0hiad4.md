---
slug: "women-in-need-0hiad4"
url: "https://devpost.com/software/women-in-need-0hiad4"
title: "Women In Need"
hackathon: "Quick Base Virtual Hackathon"
organization: "Quickbase"
winner: true
words: 1124
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/labor_employment"
  - "domain/mental_health"
  - "user/patient_family"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Women In Need

> A one-stop solution for victims of Domestic Abuse during Covid-19 to Log incidents, ask for assistance and request for extractions out of their homes via partnering NGO-verified volunteers.

[Devpost](https://devpost.com/software/women-in-need-0hiad4) · hackathon [[Quick Base Virtual Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[labor_employment]] [[mental_health]]
**user** [[patient_family]]
**substrate** [[structured_db]] [[video_visual]]

**stack** mailgun, nexmo, pipelines, quickbase, webhooks

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for women in need

## Body

Admin Dashboard showcasing an overall view of everything that's going on in the app. The Administrative Pane of adding a partner NGO How the NGO control centre looks. They can see their volunteers, and can check on the status of the extraction reports of their volunteers How the process of Adding a volunteer by the NGO looks like The command centre of a registered volunteer. They can see their pending extraction requests and can find the contact details of the victims Volunteer panel of changing the status of the extraction request An end user's dashboard, They can add/update their details, file incident reports and request for extractions. User's view to adding an incident report. They can select from a various choices of category of abuse and provide a detailed description Victim Panel for adding an extraction where they can specify the emergency level. Their location is automatically captured using IOL module. Inspiration We realised, amongst all the problems that arose during Covid-19, the worst was the one that resided at home - Domestic Violence . WHO estimates that approximately 35% of women, all across the world are victims of Domestic Abuse, and worst of all, most are abused by their own intimate partners . These numbers were only amplified in the tough times of Covid-19, when more and more women needed to stay and work from home. We wanted to address this sensitive issue while ensuring that the affected victims can safely recording their incidents, and can request home extractions or ask for in-person help via the support of our partner NGOs What it does This app helps to provide a platform that brings together NGOs, their verified volunteers, and the people in need of help to escape the domestic violence they face at home. Victims, once onboarded on the platform, can quickly add their details, including their address, emergency contact number, and an emergency signal that they might use during a video call with their volunteer. They can additionally keep a log of any incidents that happen at home and the same are sent over to the NGO when requested. If things at home escalate, or the matters get out of hand, they can additionally file for an extraction that will alert a volunteer of their choosing to come and pick them up or provide medical assistance. The platform also seamlessly integrates the role of an NGO, which are only added upon verification from the Administrators. These NGOs can then set up their virtual workforce on the platform, and have an army of volunteers ready to help any victim in their vicinity. The volunteers added to the platform get their own dashboard, and can get the details of the extraction requests filed by the victims in their vicinity. The volunteers also get an SMS and an email on their registered contact details whenever a new extraction is filed that requires their assistance, and can immediately see all the details of the extractions on their dashboard, grouped by their emergency level and status. The notification triggering is completely handled by the Pipeline architecture of the QuickBase app, removing the need for any human intervention on the application whenever a new extraction is filed. How we built it The whole product was built on the QuickBase platform, and used its advanced features such as In-form formulae, Pipelines and IOL module calling to ensure the platform was intuitive, easy to use and fully functional. We additionally used technologies like Mailgun and Nexmo's SMS capabilities to send notifications to the concerned volunteers to ensure they can act on the information as quickly as possible. Challenges we ran into Getting functional with QuickBase! We were a team of new QuickBase builders and had to spend quite some time getting used to building apps on it, but we're glad we finally made it with the help of the amazing support team on QuickBase's slack! From having trouble adding database relationships to User accounts to having complex formulae drive our buttons so that the product was as intuitive as possible to embedding a real-time location in forms, we had a hell of a ride getting here. Accomplishments that we're proud of We're really proud of having the app up and running! At first, we were unsure of this idea and were not sure if we would help make an impact, but the more we read about this sensitive issue, the more we understood how important it was to address this and build a platform that helps women or in fact anyone who has to face such a problem every day in their own homes . We're also extremely proud to have worked on a new tool like QuickBase and have become adept with most of its complex feature set in such a short period! What we learned I think one of the biggest revelations we had was how huge the problem of Domestic Violence was. As we continued our research for actually making the app, we went through tons of websites, blogs, and counts of existing survivors, and were taken aback by the sheer scale of them. We additionally learned a ton about what goes into helping and rescuing such survivors, and were made aware of many different NGOs that are working towards women empowerment. For anyone trying to understand the scale of the problems and what they can do to help out such victims, we suggest the WHO's official Primer on violence against women and their FAQs Additionally, QuickBase being a completely new platform for us, certainly raised a lot of issues for us while creating our application, but with the help of the support team, we crossed every hurdle that came by, which helped us enhance our problem-solving skills, despite being exposed to a completely unknown territory. What's next for Women In Need The journey of Women In Need has just started! This project is currently no more than just a small prototype of what we actually have in our minds. There are tons of fixes and feature additions that need to be done, including but not limited to the ability to auto-select the closest volunteers based on their live locations, the ability to add in-app video conferencing for counselling sessions and to even build a full-fledged Reddit-styled community inside the app to provide peer to peer support to the victims of domestic abuse. Additionally, we're planning to start getting in touch with a few NGOs nearby to understand and get feedback from them about our application about how we can make it more suited to their needs. We're more than excited to see this project to move forward and hope that we make an unforgettable impact on those who have to go through this terrible ordeal. <div