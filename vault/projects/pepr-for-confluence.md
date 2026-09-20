---
slug: "pepr-for-confluence"
url: "https://devpost.com/software/pepr-for-confluence"
title: "PEPR for Confluence"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 1056
team_size: 10
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/document_pdf"
---

# PEPR for Confluence

> Get the right Confluence documents to the right people. Reorganize your Confluence documents into PEPR libraries and collections, so you can easily share related content with the appropriate users.

[Devpost](https://devpost.com/software/pepr-for-confluence) · hackathon [[Codegeist 2021]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[document_pdf]]

**stack** amazon-web-services, chakra-ui, forge, forge-ui, graphql, react, typescript

## How they structured the write-up

- inspiration
- what it does
- what problems does it solve?
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next

## Body

View of the existing collections and documents of the space The library view in the Space Settings only accessible by Space admins View of a document containing confluence macros in a Collection Global PEPR Collections view on the right sidebar of the dashboard Inspiration Confluence is an amazing tool for collaboration, allowing teams to build documentation at lightning speed. This rapid content creation can introduce a complication - in a sea of pages, how team members know which ones are the right ones? How do they separate draft content from the "source of truth"? That's why we created PEPR for Confluence. What it does PEPR for Confluence lets you separate your draft from your finished content. Your teams can collaborate freely on documents inside Confluence, then publish those documents to PEPR Libraries, cleaned of any old comments, page history, or other unapproved draft content. From there you can organize those documents into Collections that can be accessed by team members. End users don't need to wade into a complex wiki navigation tree to see the right documents, Collections bring together everything they need in one spot. What problems does it solve? For years, users of our other apps have told us how important it is to keep their draft and published content separate. We know there are many teams that could make use of the functionality, but the one that inspired us most was related to Human Resources documents. HR teams need to create a myriad of documents for their teammates. Employee manuals, policies, updates, and more. Adding to the complexity is that there might be different documents for different regions; the employee handbook for team members in California could be different than the handbook for Texas. These teams need a way to clearly define which policies belong to which members, and to that we say "just add PEPR for Confluence!" With PEPR for Confluence, the HR team will work together drafting documents in a specific space. They'll choose documents from the space that belong to the "HR Library", and publish them, effectively separating them from the original draft document. End users who read the document in the Library won't see the original document's comment, page history, or anything else you don't want them to see. How we built it Taking lessons from our experiences at previous Codegeists, we knew we needed to assemble a seasoned team to be dedicated to the project. We settled on tasking one team dedicated to learning/developing in Forge, while another was in charge of the Amazon platform. It took some careful management to keep everyone moving in the same direction, so the project was overseen by one of our Product Managers, and our Head of Product kept a close eye on everything. Once this framework was in place, we took our usual development process and condensed it to fit within the timelines of Codegeist. Doing so always has some interesting side effects, but we've learned over time that as long as we stay dedicated to our vision of the MVP that we will be successful in the end. Challenges we ran into A big challenge for us was Forge's handling of email. A key part of the communication process with end users is that when a publish action is invoked we need to notify the right stakeholders that the document's state has changed. We typically do this through an email notification. With Forge we had to rely on triggering the user's email client to send this message; with Forge we are not able to send emails directly from the Confluence instance. This would be a killer feature that will allow app developers to engage with key actions from the application. Our app works directly with user generated content, and one idea we had to allow better functionality is to maintain Confluence macros styles when exporting a page. At this time we are using the Confluence export feature that does not have API access, so we had to code our own solution. We believe that the platform should allow app developers access to export resources. Exposure of an application's key activities and outcomes is critical for user adoption. One easy way to provide a channel for engagement with end users is access to the General Page Module. This will allow any application to showcase its value to every user on a Confluence instance. Enabling better app adoption throughout an organization would be much easier if applications can be granted access to the Main Menu Bar of Confluence. In Comalatech we do take time off seriously, and having the hackathon run through the summer made us get creative with team allocation (wink) We believe that Forge has the potential to support business critical applications and we have shared with the Forge team the requirements in order for that to happen. We are excited about the roadmap and we are looking forward to their next releases bringing us closer to that reality. Accomplishments we're proud of A key part of how an app is exposed to a Confluence user base is through the menu bar, which is not accessible in Forge. So, our team implemented it in the General Page Module, which is a good way to create awareness of the application to all users in a Confluence instance. Our whole Cloud team is now aware of the potential for Forge and what Function as a Service (FaaS) means. Thanks to Codegeist 2021, we have a complete understanding of the software lifecycle for a Forge app; how you can design, deliver and launch an app built in the latest Atlassian technology. What we learned Our hands-on time with Forge really gave our team time to discover the possibilities and the potential of the Forge platform. We also learned (again) what a wonderful curse tight timelines can be; always a great exercise in proper project management and development agility. What's next We're excited for the future of Cloud apps, especially now that Forge has opened up new possibilities. We will not be stopping development on PEPR for Confluence now that Codegeist is done. In fact, we have some exciting ideas about where we can take the product. There are plenty of use cases that could use a solution like this one, and so keep on eye on the Atlassian Marketplace for further updates. <div