---
slug: "monderstruct-tools-for-construction-field-workers"
url: "https://devpost.com/software/monderstruct-tools-for-construction-field-workers"
title: "MonderStruct - Tools for construction & field workers"
hackathon: "monday.com Apps Marketplace Challenge: solutions for teams "
organization: "Monday.com"
winner: true
words: 841
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/disaster_emergency"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/frontline_worker"
  - "substrate/document_pdf"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# MonderStruct - Tools for construction & field workers

> End-to-end OHS (Occupational Health & Safety) Auditing (fire alarms, fire exits, lift service, fire extinguishers) project management tool with real-time monitoring of sensors

[Devpost](https://devpost.com/software/monderstruct-tools-for-construction-field-workers) · hackathon [[monday.com Apps Marketplace Challenge- solutions for teams]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[disaster_emergency]] [[finance_payments]] [[labor_employment]]
**user** [[frontline_worker]]
**substrate** [[document_pdf]] [[video_visual]] [[web_dom]]

**stack** amazon-web-services, canvas, python, redis, vue, websockets

## How they structured the write-up

- inspiration
- what it does
- example use case
- challenges i ran into
- how i built
- accomplishments that i'm proud of
- what's next for monderstruct - tools for construction & field workers

## Body

Inspiration Several years ago I built a custom CRM system for fire safety auditing & compliance, I wanted to build a similar tool for Monday.com and expand its use cases to broader areas of construction and field worker industries. Using a bespoke real-time collaborative whiteboard as an intuitive and flexible interface and adding layers of functionality specific for construction and field workers on top. IoT and smart devices that are starting to make headway into these industries (smart fire alarms, security systems etc) integrating data from such devices MonderStruct also helps future proof Monday.com and adding IoT automation to the next level. Monday's platform is flexible, expandable easy to use, and has beautiful UI however CRM software is a competitive market and for new customers considering to switch MonderStruct adds specific functionality and key points of difference to help drive adoption for construction and field worker industries. What it does MonderStruct adds two new types of views:: MonderStruct Boards More than a whiteboard, a collaborative way to interact with floor plans, CAD files, electrical/plumbing schematic and much more General business admin features (Freemium): Collaborate in realtime with Multi-users (literally keep everyone on the same page) Support for many file formats including, Word, PowerPoint PDF, Google drive Embedded CAD viewer for Autodesk / CAD files. Multi-tab Free draw / Annotate Quickly and easily cut and paste content directly onto the whiteboard 2 way data binding with Monday.com “assign” users and “tag” content Per Board and Per Item View Save boards to PDF Reload past boards Industry-specific features (Premium plans): Embedded CAD viewer for Autodesk / CAD files. Floor plan icons (doors, windows, stair etc) OHS icons (fire exits, extinguisher etc..) HVAC/Plumbing icons Security icons (Camera, angle tool trip sensor) Ruler and angle tools Advanced calculator, conversions Use inbuilt Monday template -“Tag” and assign“user” to integrate into business workflows. MonderStruct Blocks Connect hardware and smart devices (IoT) to get real-time data, custom notifications and automate/escalation team assignment When trying the electrics, HVAC or plumbing for the first time is exciting & nerve-racking. When it comes to electric, plumbing and HVAC and site security prevention, monitoring & maintenance are key. Smart devices & IoT hardware is gaining traction in security, preventative maintenance and construction more generally MonderStruct makes it easy to integrate common sensors like for: Flood detection Fire detection Movement (security) Trip sensor (security) Or any other IoT device Example use case Occupational Health and Safety in many countries require regular audits of fire safety equipment, to check fire alarms are working, that fire extinguishers are in a good location, the right class of extinguisher (Water, Foam, Dry Powder, CO2 and Wet Chemical etc) and not expired. Field workers can now quickly audit sites on their tablet or mobile device based on floor plans that can be uploaded directly into Monday.com . Fire alarms, extinguishers & fire exits can be added or moved by simply dragging and dropping one of the many OHS-specific icon onto the MonderStruct whiteboard on either a tablet or mobile device, faulty, expired or obstructed equipment can be easily tagged for review and record keeping. Field staff can also use MonderBlocks when installing/upgrading smart hardware /IoT devices such as fire alarms and security systems to further automate the whole process of OHS audits/compliance. Admin staff can see all the changes in real-time, the data is both visually on the MonderStruct whiteboard and as Monday items that can then be used with automated workflows. Similar workflows exist for many maintenances, renovation, site audit and other construction tasks that can now be easily streamlined and automated using MonderStruct. Challenges I ran into Unlike a lot of "hackathon" projects, this is close to "production" ready, which meant considerable time was spent on the app infrastructure, making modular and serverless where possible to make it scalable and easy to maintain. How I built Leveraging my experience from previously building a custom solution for OHS auditing and compliance and more recent experience developing other real-time apps and whiteboards (for Edtech learncube.com) I've built a custom whiteboard solution to integrate directly into Monday. The backend is using Node and Python along with WebSockets, AWS API gateway and serverless lambda function to deal with realtime collaborative functionality, the front end is built in Vue and using Html Canvas (Fabric) for the whiteboard and we integrated with Cloudinary to support the conversion of different file formats. Accomplishments that I'm proud of A genuine business opportunity leveraging Monday's market place to help drive Monday and Monderful Apps user adoption in the field of Construction and Field Workers. What's next for MonderStruct - Tools for construction & field workers Currently freemium, working on automating the payments for the premium version which has more industry specific icons/symbols and better out-of-box support with MonderBocks for hardware and IoT device integration. Create industry-specific templates similar to Monday's templates for the MonderStruct Whiteboard. Find suitable hardware partners to bundle with MonderBlocks, selling the hardware devices adds another revenue stream for us (Mondeful.app) and also opens up potential channel partners for monday.com platform. <div