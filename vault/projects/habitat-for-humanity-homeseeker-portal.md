---
slug: "habitat-for-humanity-homeseeker-portal"
url: "https://devpost.com/software/habitat-for-humanity-homeseeker-portal"
title: "Habitat-Portal"
hackathon: "DocuSign Good Code Hackathon"
organization: "Docusign"
winner: true
words: 1221
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "domain/housing_homeless"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Habitat-Portal

> A Web Portal that automates the application form signing and uploading process for families applying for a new home with Habitat for Humanity

[Devpost](https://devpost.com/software/habitat-for-humanity-homeseeker-portal) · hackathon [[DocuSign Good Code Hackathon]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]] [[housing_homeless]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** axios, docusign-esign, express.js, mongodb, node.js, react

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for habitat-portal

## Body

Homepage Upload page Embedded form Admin Login page Admin Dashboard Inspiration The need for affordable housing has never been greater. That’s why Habitat for Humanity partners with working, low-income families to help them build strength, stability and independence through affordable homeownership. However, there lacks a standardized system for families finding homes across the world. Currently, different locations have different application processes, with different mail-in forms that usually require handwritten signing and multiple documents to be uploaded with it. For already burdened families, this long, manual application process only adds to the burden and lacks transparency. Habitat-Portal is a web portal that digitalizes the entire application process, applicants can easily fill, sign, and upload all the required documents digitally and efficiently. This system ensures all documents are uploaded and instantly stored in the admin portal database for instant access and review. By giving families around the world a standardized and efficient digital application method, Habitat-Portal will reduce wait times, prevent ineligible or unreadable applications and save over 2 million pieces of paper for 175000+ families annually. What it does Habitat-Portal provides families applying for a Habitat for Humanity home a digitalized system for securely signing and uploading all their documents in one place. The web application leverages DocuSign's eSignature API for embedded signing so that an applicant can securely fill out home application forms for their family and upload all the documents that need to be submitted with it. It uses the eSignature API to accomplish this entirely through the web, and the application portal enables authentication that only allows a user to access the DocuSign embedded form as long as all the required documents have been uploaded. Any location can adopt this portal to their liking, and any location's application form can be embedded with this portal. All documents must be uploaded before continuing to sign the form, taking the burden off applicants worrying about forgetting any documents as the portal takes care of the confirmation for them, and by digitalizing the process the need for printing, struggles of reading handwriting, and the fear of an application getting lost in the inbox disappears. My e-signing platform rids these burdens by providing a simple paperless system where applications can easily be submitted and instantly reviewed, all while ensuring any submitted files are securely stored in a database. How I built it The frontend was developed with a React.js frontend and Axios for API methods, and the backend was written in node.js with MongoDB to store the files users upload, all files and form information is organized and stored by user/submissions. There is also an Admin portal which is linked in the Navbar with both admin login and registration functionality using JWT authentication. This is only for demo purposes, and in the future the workflow will be updated such that the Admin portal is independent from the Habitat Portal, so that only admin's can create admin accounts and the portal and admin registration system is hidden from users. Admin's have access to the user/submission info stored in the database, and is displayed on the admin page for the frontend in an organized dashboard-like manner. I leveraged the DocuSign eSignature API for the form to be fillable and allow for embedded signing. I am also deploying the application to production using Heroku, so that it can be viewed and used by anyone from anywhere. Challenges I ran into Since I was competing on my own, I was in charge of everything from the frontend to the backend and am responsible for deploying this application to production. This posed critical time management challenges and building both the frontend and backend from the ground up put me through quite a time crunch. I had to navigate myself through lessons on concepts like react routing, hooks, and components and it took a while to ramp up and implement the react development cycle from scratch. I had to learn to leverage a basic login/registration system with JWT authentication and MongoDB. It was a significant learning curve, having never worked with MongoDB and JWT before, and took around 7+ hours of Youtube tutorials. Working with the node.js quickstart to implement the embedded signing feature of my application required a significant amount of refactoring and along the way I ran into many bugs that required hours of debugging to finally create a pure backend integration of the node.js quickstart. When implementing the DocuSign API, I ran into troubles with URIs on both the proxy and client ends, and it took a while to figure out how to navigate the client, server, and database all at once. A lot of debugging and playing around with the ports, as well as thoroughly looking through documentation of the Authorization Code Grant went into correctly configuring my application. Deploying the application to production was/is the final hurdle, with so many dependencies and a lack of experience with full stack deployment to the cloud, I had to pick a cloud service that allowed for both frontend and backend deployment, settling for Heroku and debugging and deploying over 70 versions of my app just to get it to successfully deploy on the cloud. Accomplishments that I'm proud of I'm proud of successfully integrating the backend and deploying it to production and for refactoring my schema to load and store applicant information and files into a MongoDB cluster in an organized and easily retrievable manner. I am also happy about implementing the DocuSign eSignature API for embedded signing, as well as implementing an encrypted login system for admins for accessing submissions for their instant viewing and review. I am glad I had this opportunity to create a novel approach for one of the largest registered 501(c)3 non-profits to help reduce the burden of families trying to find a new and affordable home. I hope to continue to stay in touch with Habitat for Humanity to see this application reach more scalable production systems and be used in the non-profit's actual application system. What I learned I got a significant refresher on the React development lifecycle and learned how to successfully integrate a backend with multiple integrations into a single port for databases, authorization, and API implementation. Learning how to independently develop a full stack application from start to finish has given me critical insights into the development life cycle, and these are skills I can carry with me throughout my career life. Furthermore, understanding customer needs for a good cause taught me how to understand customers and translate client needs into reliable, efficient software systems as solutions to their problems. What's next for Habitat-Portal Improve UI components for greater professionalism and readability, as well as fixing minor problems such as enhancing styled components, and re-positioning certain features for a better look. Reach out to Habitat for Humanity for implementing this portal and look into scaling this application for customization and use from any location, or to create a dropdown for any location, updating the form, documents, and tabs to tailor to each Habitat for Humanity location in Canada. Updating the workflow to separate the Admin portal from the main application. Changing the current demo envelopes into legally binding DocuSign envelopes. Using DocuSign ID authentication for user's to login to the application system. Improving the database-frontend integration for a more functional dashboard, and implementing better search methods. <div