---
slug: "collabright"
url: "https://devpost.com/software/collabright"
title: "Collabright"
hackathon: "DocuSign Good Code Hackathon"
organization: "Docusign"
winner: true
words: 1025
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/provenance_signing"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Collabright

> Work with people outside your GIS provider with integrated version management, approval and e-signature flow

[Devpost](https://devpost.com/software/collabright) · hackathon [[DocuSign Good Code Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[provenance_signing]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[labor_employment]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]] [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** python, react

## How they structured the write-up

- the problem
- the solution
- features
- how we built it
- source code
- what's next for collabright

## Body

[GIS User View] Dashboard [GIS User View] All Audits [GIS User View] Contact List [GIS User View] Org Settings [GIS User View] Integrations [GIS User View] Create New Audit [GIS User View] Version Release Confirmation [GIS User View] Audit Details [GIS User View] Interactive Map [GIS User View] Discussion [Reviewer/Signer View] Audit Details [Reviewer/Signer View] Discussion [Reviewer/Signer View] Interactive Map Collabright The problem Collaborative Conservation Planning is an important process in the Jane Goodall Institute. But the GIS users face a lot of trouble when they want to collaborate with external stakeholders and subject matter experts to improve a map. The inefficiency and manual handling of the collaboration process in the Institute's current workflow is the problem that we intend to solve. Even though they want to share an interactive mapping experience with the stakeholders, bringing people from different technical backgrounds over to a system as complex as GIS isn't the best of options. And making a work-in-progress map publicly available is not desired either. So they have to take a screenshot/ PDF export of the map and email it to everyone. Of course, they can't interact with an image/PDF file. And they can't annotate the map inside an email either. The only way to collaborate is to send emails back and forth. Multiple review cycles often mean going through a very long thread of emails and keeping track of which feedback have been addressed and which are left. It's very possible that some notes and comments get lost in the translation. Since there is no structured way to keep track of progress, it becomes very difficult to get a top-level view of the overall process. This can lead to human error, disagreements, and unnecessarily lengthy review process. Learn more about the obstacles the institute face during a Collaborative Conservation Planning process as described by Dr. Lilian Pintea in this video: The solution Collabright is a collaboration platform that sits right between the GIS and e-signature services with integrated version management, approval, and e-signature flow. It allows users to create a virtual audit based on a map and invite external stakeholders as reviewers. Reviewers can comment and annotate on each version of a map while each version and review history is kept in sync with the e-signature envelope for the final sign-off. See the full demo: https://youtu.be/75aKAiwrdYA?t=72 Features Simple integrations 🗺️ One-click integration with ArcGIS (OAuth 2.0) ✍️ One-click integration with DocuSign (OAuth 2.0) Audit 🖊️ Create an Audit based on a GIS map 🔗 Only the map URL is required to create an Audit ✍️ An audit will be associated with a DocuSign envelope for the final sign-off by reviewers Version management 📎 Unlimited versions of a map can be attached to an Audit 🌍 Map definition is fetched from ArcGIS when a version is released 🖱️ Interactive map is built based on the definition for each version 🖨️ PDF version of the map is generated to update the Docusign envelope 🚀 Release next version when ready 🤖 The latest map will be fetched automatically when you release the next version 📝 Release as many versions of the map as required 💬 Annotate and comment directly on the map in each version 🦖 All history associated with a version is kept 👀 Switch between map versions to see the review history and comments Reviewers 👥 Invite unlimited reviewers to review Audit ✍️ Signers will be able to review and will be added to the associated DocuSign envelope as recipients 👌 Non-signer reviewers will be only able to review 📧 Reviewers will get personal and secure review link 🙅‍♀️ Reviewers will not require accounts to review ✅ Reviewers are able to submit their reviews (Accept/Request Change) Comments and Annotations 💬 Both GIS User and reviewer can annotate and comment on each version of the map 🖍️ Draw circles, rectangles, polygons, etc on each version of the map 💭 Reply to comments and annotations ✅ Resolve comments, mark as complete 🦖 Can comment in a past version of the map Instant notifications 💬 Email and In-app notification to GIS user when a reviewer makes a comment ✅ Email and In-app notification to GIS user when a reviewer submits a review 🔃 Email notification to the reviewer when a new version of the map is released Integrated eSignature workflow ✉️ DocuSign envelope is created and Audit's metadata is added for future reference ✍️ Audit Signers are added automatically as envelope's recipients 🔃 Envelope is updated automatically with the latest version's PDF of the map 🖊️ GIS user can open and edit the envelope manually 🔐 Full privacy and control over the envelope Adding as contact 👥 Add repetitive reviewers as Contact, add name and email 🔎 Added contacts can be looked up using name and email during adding as reviewers 🤖 Contact automatically added when a new reviewer is invited to the system How we built it ArcGIS OAuth - https://developers.arcgis.com/documentation/mapping-apis-and-services/security/oauth-2.0/ Esri Viewer - https://github.com/Esri/Viewer ArcGIS API for JavaScript - https://developers.arcgis.com/javascript/latest/ ArcGIS REST API - https://developers.arcgis.com/rest/ DocuSign OAuth - https://developers.docusign.com/platform/auth/ DocuSign eSignature API - https://developers.docusign.com/docs/esign-rest-api/ DocuSign Embedded sending - https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/ DocuSign Webhooks - https://developers.docusign.com/platform/webhooks/ Webviewer - https://github.com/pdftron/webviewer-ui Source Code This project is open-source and available under the GPL-3.0 License. Clone using Git Clone the repository from Gitlab git clone git@gitlab.com:mehamasum/collabright.git Server Setup Python 3.6 or later needed. goto project root cd YOUR_PROJECT_ROOT_DIRECTORY setup python virtual environment for project virtualenv -p python3.6 .venv activate virtual environment source .venv/bin/activate # for linux .venv/Scripts/activate # for windowns set environment variables cp .sample.env .env Make sure postgress is running and set DATABASE_URL in .env Make sure mailhog is running and set EMAIL_* in .env docker run -p 8025:8025 -p 1025:1025 mailhog/mailhog Make sure redis is running and set REDIS_URL in .env docker run -p 6379:6379 redis install backend (api) dependencies pip install -r requirements.txt migrate database with the application models python manage.py migrate run backend server python manage.py runserver 0.0.0.0:8000 run celery celery -A collabright worker -l INFO Client Setup Node.js 10.13 or later needed. install frontend dependencies npm i run dev server npm start What's next for Collabright Search with ElasticSearch More secure Webhook deployment Some small TODO features <div