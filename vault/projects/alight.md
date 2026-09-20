---
slug: "alight"
url: "https://devpost.com/software/alight"
title: "Alight Docusign"
hackathon: "DocuSign Good Code Hackathon"
organization: "Docusign"
winner: true
words: 1093
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "domain/housing_homeless"
  - "domain/immigration_refugee"
  - "user/clinician"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Alight Docusign

> An Interactive Web Applications that Connects Refugees with Nonprofit Alight Refugees Supports Team Powered by Docusign Signature API,Google Map, Google Chart Statistics, Email and Twilio SMS.

[Devpost](https://devpost.com/software/alight) · hackathon [[DocuSign Good Code Hackathon]]

## Facets

**mechanism** [[provenance_signing]]
  <sub>weak: on_device_local</sub>
**domain** [[developer_tools]] [[housing_homeless]] [[immigration_refugee]]
**user** [[clinician]] [[developer]]
**substrate** [[code_repository]] [[document_pdf]] [[geospatial]] [[structured_db]] [[web_dom]]

**stack** docusign-e-signature-api, email-server, google-address-geocoding-api, google-chart-statistics, google-maps, mysql, php, twilio-sms-api

## How they structured the write-up

- inspiration
- what it does
- how to prepare and test the application online:
- how to install application locally:
- how we built it.
- license
- what we learn
- what's next for alight docusign

## Body

Refugees Application Dashboard Refugees Signed Documents Sample Refugees Signed Document Summary Refugees Form Registration Sampling System Admin Docusign Access Token Generation System Refugees Docusign Details Sampling Refugees Geolocation Google Mapping System Refugees Email Messaging System Refugees SMS Messaging System Refugees Statistics and Chart distribution Analysis Application Landing Page Inspiration As Ukraine is being attacked and invaded by Russians, Most of Ukrainians home are destroyed and many people are displaced. With Refugees looking for Shelter elsewhere, Alight Refugees Supports Non Profit Organizations help large number of Refugees who flees their home to settle down by providing Foods, Water, Shelter and Financial Assistance etc. Alight(wearealight.org) was founded in 1978 as the American Non Profit Refugee Committee, by Neal Ball, to assist refugees that had been displaced or were resettling. With Millions of Ukrainians and Refugees around the world desperately looking for help, it become a heavy work for Refugee Teams in handling their request/applications. Realistically, most of the form/application submissions, processing and agreements are done manually on Paper or over an email which sometime creates monotony in the work task especially in emergency critical situations. we develop this applications using Docusign Signature API, Google Map, Google Chart Statistics, Email Server and Twilio SMS to help Refugees who Needs urgent help to easily connect and submit their application and have it agreed, signed and reviewed by Alight Refugee Team to help provide humanitarian assistance urgently. By Providing an application coded with Refugees Application forms and by integrating DocuSign's eSignature, it makes application processing and agreements signing between Refugees and Refugees Team super fast. In addition to Alight Refugee Teams ( https://wearealight.org/ ) , this application can also be leverage by Other Refugees Team Non Profit Organization like 1) International Rescue Committee (IRC): https://www.rescue.org/page/history-international-rescue-committee 2.) Lutheran Immigration and Refugee Service (LIRS): https://www.lirs.org/a-brief-history-of-lirs/ 3.) Doctors Without Borders (or Médecins Sans Frontières): https://www.doctorswithoutborders.org/who-we-are/our-history 4.) Save the Children: https://www.savethechildren.org/us/about-us/why-save-the-children/history 5.) RefugeePoint: https://www.refugepoint.org/about/organization/ 6.) Jesuit Refugee Service https://www.jrsusa.org/about-us/our-history/ and many more....... What it Does On the Part of Refugees: 1.) Alight Docusign is an application that allows Refugees who is looking for urgent help to fill out a Refugee Request Form. The application leverages Docusign Signature API to sign and process the request form so that the Refugee seeking for assistance can agree to the terms and conditions of Alight Refugees Team and to also agree and sign that all the information submitted are truths and valid. 2.) The applications automatically send the processed form details to the Refugees email address for document signing and completion leveraging Docusign E-Signature API On the Part of the Admin 1.) Alight Refugee Teams can Signup and Login into the applications as Admins to View and Review All the Registered Refugees information Documents Signing Details. 2.) The Application allows Alight Refugee Teams to View, Check and Update Refugees Sign Documents Status. 3.) The Alight Refugee Teams can also download and Review each of Refugees Signed Documents along with the summary of the Signed documents all in PDF Formats 4.) The Alight Refugee Teams can also Updates Refugees Status from Awaiting Approval/Acceptance to Accepted once the Refugees issues has been Resolved and has been accepted 5.) The Alight Refugee Teams can also track registered Refugees Details on Google Map to pin points its Geo-location Address Mapping. 6.) The Alight Refugee Teams can also communicate and exchange information with Refugees via Email Messages Campaign and via SMS Text Messages leveraging Twilio SMS API Gateways. 7.) The Alight Refugee Teams can also visualized the Total Registered Refugees Vs Refugees Awaiting Approval/Acceptance vs Refugees Already Accepted via Google Chart/ Graph Distributions Analysis. How to Prepare and Test the Application Online: 1.) The Admin Will First Need to Signup/Login and Click on Generate Docusign Token . Once the Token is generated by Admin/Alight Refugee Teams, the Application is set for usage. If Docusign Access Token get expired, the application will automatically leverage Docusign Refreshed Token to generate new Access token and thus the application will automatically continue to work. How to Install Application Locally: 1.) This application was written in PHP and thus ensure that something like xampp server is install. Ensure that PHP and Mysql is running. 2) The Alight Refugee Teams/Admin will need to Edit Settings.php file to update all Requirements like Docusign Credentials, Google Map API Key, Twilio SMS API, Email Server Configurations etc. 3) Edit both data6rst.php and db_connect_map.php to update database Credentials respectively. 4.) Export docusign_db.SQL which contains database Table. 5.) make sure to configure Token Generation Redirect URL to point to Eg. http://localhost/alight_plus/docusign_token_generate.php for your App Settings at your Docusign Developers Account. 6.) Call up the application at browser and it will be running at http://localhost/alight_plus/index.php How We built it. 1.) The Application was Built with PHP, Mysql, Bootstraps, Ajax/Jquery, CSS etc. Technologies used includes Docusign E-Signature API, Google Map Javascript API, Google Address Geocoding API, PhpMailer, Twilio SMS, and Google Chart/graphs etc. 2.) It uses Docusign E-Signature API and all API request were made via CURL Request in php . You don't need to install any Docusign E-signature SDK. All Refugees Form Signing data are processed by Docusign E-signature API before being sent to Refugees Email Address for Signing and Completion. 3.) We Used Twilio SMS API to Allow Alight Refugee Teams to send and recieve SMS messages campaign within the application to registered Refugees. We are currently using Twilio Test/Sandox API Credentials and thus can only send and recieve SMS to only numbers (Eg. +2349135775247) configured on Twilio Dashboard. In For your own testing , You will need to enter your Twilio Test/Sandox API Credentials OR Production/Live Twilio SMS Credentials at settings.php files to enable you send and recieve SMS Message to any Refugees mobile contacts across the globe. 4.) We used Google Address Geocoding API to convert published Refugees Home address to Latitude and Longitude to enable his/her Geolocation Address to easily appear on Google Map. 5.) We used Google Map Javascript API to pinpoint the exact location of the Refugees Geolocations on the Google Map 6.) We used PhpMailer to allow Alight Refugee Teams to send and receive email messages to and from all Registered Refugees. 7.) We used Google Chart/graphs to be able to visualized the Total Registered Refugees Vs Refugees Awaiting Approval/Acceptance vs Refugees Already Accepted via Google Chart/ Graph Distributions Analysis. License This Application is MIT Licensed. Free to be used for any purposes What We Learn Working with Docusign E-Signature API via Curl Request in PHP is very simple and easy to integrate into our applications. What's next for Alight Docusign More Features Coming soon <div