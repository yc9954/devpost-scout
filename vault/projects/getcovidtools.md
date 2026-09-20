---
slug: "getcovidtools"
url: "https://devpost.com/software/getcovidtools"
title: "GetCovidTools"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 1129
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "user/clinician"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# GetCovidTools

> An open platform that empowers makers and suppliers to offer PPE supplies to validated health professionals.

[Devpost](https://devpost.com/software/getcovidtools) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**domain** [[health_clinical]] [[labor_employment]] [[supply_logistics]]
**user** [[clinician]] [[developer]]
**substrate** [[financial_record]] [[structured_db]] [[web_dom]]

**stack** bootstrap, html5, javascript, lamp, mysql, npi, php, ssl

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for getcovidtools

## Body

GetCovidTools Homepage GetCovidTools Campaigns GetCovidTools Objective GetCovidTools Features GetCovidTools Dashboard Inspiration The novel coronavirus is a disease that has affected many people across the world. There are many news media outlets that report the data sources which account for the community's spread of the virus. However, there is little to no recognition given to positive measures and contributions made by makers or those in communities who want to do their part in providing supplies that could prevent the spread of the virus. Although some have donated PPE supplies such as masks, face shields, gloves, and more, these donated supplies are often unaccounted for. Additionally, there is little to no community interaction or transparency when it comes to a transaction between hospitals or healthcare providers. For all we know, some hospitals could be receiving unexpected donations of PPE materials while other hospitals forever wait for materials and never receive them. Our goal was to make a platform similar to that of a crowdfunding site such as Patreon, Indiegogo, or similar but instead of using money as the goal, we use PPE items as the goal. Moreover, users can engage with the campaigns similar to Instagram such as "liking or watching". This in turn helps medical facilities get supplies that they need as well as encourage makers/suppliers to ship supplies where it counts the most. Additionally, this platform would allow medical professionals to first review and approve donations instead of randomly getting them. The current existing methods of donations are merely based on Google forms, Facebook groups, forums, and phone calls. This makes things very disjointed and sometimes it is a hassle for both the contributors and medical professionals to keep track of items and progress. There is much manual labor involved in the existing processes. We envision our platform to be fully automated and require minimal hassle. In other words, healthcare providers such as hospitals, clinics, and physicians should be able to sign up and instantly get validated. This provides security for the transaction of the supplies. Also, healthcare providers get to review shipments and donation offers before they are made. Healthcare providers who do accept shipments can choose to tip the maker/supplier however they like. This ensures that donations are consistent and that contributors are appreciated for their efforts. What it does The goal of the GetCovidTools platform is to achieve the following: Validate Health Organization Requests for COVID19 Supplies Validate Maker/Supplier Shipments in a unified consistent way To Account for Resource Donations and Fulfillments (Donation notifications) To Give Recognition and Reputation for Key Contributors To provide Insights that Correlate the number of actions vs. the number of cases in specific locations (as a means of indicating urgency and progress) To provide community transparency and connectivity To provide a means for healthcare organizations to tip makers and give feedback To give positive morale in a situation where the statistics are generally negatively aimed How we built it Our team is comprised of graduates from Purdue University. We are passionate engineers with experience in developing innovative solutions to help the community. The solution we proposed was written out in pseudocode and then coded in HTML using Bootstrap, Javascript, PHP, and MySQL. There will be mainly two user-types: Makers/suppliers and Hospitals/physicians. The makers will be those who create or have the PPE supplies to donate. The hospitals would be the providers that would create requests, or campaigns, in need of the supplies. To demonstrate our solution, we purchased a domain (getcovidtools.com) and set up a LAMP environment to host our solution. SSL was established for a secure connection to the server. Then we set up a database schema such that we can store data properly. Our team built the layout pages such as the homepage, signup page, dashboard, campaign page, makers, FAQ, and more. The interface was designed to be easy to use and minimal, but still providing insightful data. We then proceeded to write a script that can be modular and used in other hosted environments if necessary. The rest of the workflow is built, including the backend. The logic was handled through object-oriented PHP classes and a couple of important APIs. The full implementation is a work in progress, but many parts of the website are already functional now. Challenges we ran into Building a versatile platform with so much logic was not an easy task. We had to revisit the database schema a few times to optimize and improve the way that the system is structured. The layouts took much effort to optimize as well since the website needs to be responsive in various mobile environments. Our team took notes from other platforms that were used for non-related causes. We also had to do some research on how to automatically validate the data submitted by users. Overall, we solved our challenges as intended. Accomplishments that we're proud of We are honored and blessed to contribute to the betterment of society and to do our part to help those in need during COVID19. There are many unsung heroes in our world and we believe that everyone deserves some appreciation and encouragement even in difficult times. In efforts to finalize our means to validate physicians and hospitals, we have reached out to a few doctors who have personally suggested that we can use the NPI public registry to get a proper validation. GetCovidTools is our way to give back to the community and empower every individual and organization to do their part to make a positive impact. What we learned We found an insightful Facebook group called "Open Source COVID19 Medical Supplies". There is another movement comprised of some doctors called "Getusppe.org". Although we found some common areas and interests, the ultimate goal of our solution, GetCovidTools, is to build community engagement, validation, and give acknowledgment to the makers/suppliers. We learned that the smallest contribution can go a long way and possibly save many lives. Therefore, our goal for the platform is to encourage many individuals to make the decision to contribute. From technical standpoint, we needed to validate medical providers to make sure supplies are not wasted or sent to spammers. We learned that hospitals and medical facilities can be validated through CCN. Physicians and hospitals can also be validated through NPI. Although these are not entirely full-proof on a global basis, they will suffice for the majority of entities. What's next for GetCovidTools We aim for GetCovidTools to be a great platform. However, there is room for improvement to bring functionality to what we envision and proposed. We will continue to update our platform as needed and grow our community on the platform. We hope you'll support us and be a part of this exciting effort. Please feel free to reach out if you have further suggestions! <div