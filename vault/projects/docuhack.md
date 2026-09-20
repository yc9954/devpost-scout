---
slug: "docuhack"
url: "https://devpost.com/software/docuhack"
title: "DocuSign For YRDSB"
hackathon: "DocuSign Good Code Hackathon"
organization: "Docusign"
winner: true
words: 701
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# DocuSign For YRDSB

> A platform for more efficient document signing for YRDSB.

[Devpost](https://devpost.com/software/docuhack) · hackathon [[DocuSign Good Code Hackathon]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[web_dom]]

**stack** bootstrap, cdnjs.xlsx, css3, docusign, ejs, express.js, google-fonts, google-icon, html5, javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned

## Body

E-Signature Process Completed Welcome Page Sending out field trip forms Adding volunteer forms submitted documents upcoming documents Inspiration We’ve all been students at one point. We remember the countless field trip forms, consent forms, disclosure forms, and volunteer forms we’ve had to submit time and time again. Some of these forms would rarely get signed on time, and often they get lost or forgotten, and all the time, they would be a hassle for administrators, teaching staff, and students alike. For the 122,000 students in the York Region District School Board, this hassle is the reality. This is why we leveraged the Docusign e-signature API to create a product that digitizes and automates much of the form signing process. What it does Digitalizes document signing processes for the York Region District School Board by providing a web app that uses DocuSign. Admins are able to easily send forms to any number of students. Students are able to easily sign those forms. Additionally, to confirm their hours, students can send out forms to places they volunteered, which is then cc'd to the school once signed by the volunteer organizer. How we built it For the frontend, we used Embedded JavaScript (EJS) and CSS. The backend is set up with Express.js. For sending documents to students, we used the e-signatures API’s BulkSending feature to enable sending documents to many students at once. The student dashboard frontend retrieves outstanding documents with the ListStatusChanges endpoint and EmbeddedSigning . Lastly, we used the EmbeddedSending API to allow students to send a preset volunteer document to the place they volunteered at, and once that is signed, it will be cc’d back to the school. Challenges we ran into Since all of us had minimal previous experience working with CSS and coding a website, it was quite challenging for us to understand the layout and the different functions we are able to use to best format our website. Properly aligning text and boxes and the design of our web interface was another large obstacle that took us a significant amount of time to overcome. Additionally, merging the work of each team member through git was another challenge we faced. Understanding the API endpoints was a big challenge as they had numerous different fields and configurations; for instance, setting up the embedded signing with email authentication rather than having a captive recipient was difficult to figure out as we had to dig through the documentation. Accomplishments that we're proud of Throughout the majority of this hackathon, our team watched a large number of YouTube videos to learn about the different functions in DocuSign as well as the different coding techniques for CSS and HTML. We are very proud of the fact that we were able to incorporate several small UI designs such as the hovering effects that make our website more user-friendly. Moreover, we were also proud of the fact that we were able to get all our functions to work and develop a complete product despite all the challenges we face throughout. We also spent a large amount of time coming up with an impactful idea. To ensure the feasibility of our idea, we’ve also reached out to the Board of Trustees in YRDSB who oversee all the schools within the region. We were really happy to receive positive feedback from the board and hearing that they strongly support our idea and are also hoping to shift toward more digitalization. What we learned To start off, we came in without knowing much about how to code a website. Throughout this journey, not only did we gain a better understanding of the different functions in different coding languages, but we were also to gain a holistic view of how the front-end and back-end come together and establish a complete website. More importantly, we learned the importance of perseverance and staying open-minded. While there were countless times that we faced difficult technical challenges, we did not give up. Instead, we focused on leveraging all the online resources we could to acquire enough knowledge to overcome the obstacles. In the end, we were able to develop a user-friendly product that we believe will make a significant impact in the community. <div