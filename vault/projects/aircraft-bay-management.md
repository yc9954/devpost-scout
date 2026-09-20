---
slug: "aircraft-bay-management"
url: "https://devpost.com/software/aircraft-bay-management"
title: "HAECO Bay Management System"
hackathon: "AWS AI Hackathon Hong Kong"
organization: "AWS Hong Kong"
winner: true
words: 1079
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "substrate/document_pdf"
  - "substrate/regulation_legal_text"
  - "substrate/web_dom"
---

# HAECO Bay Management System

> Web-based management system embedded with visualization portal & optimization engine to provide the most optimized suggestion for aircraft maintenance bay assignment and movements at HAECO hangars.

[Devpost](https://devpost.com/software/aircraft-bay-management) · hackathon [[AWS AI Hackathon Hong Kong]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
  <sub>weak: cross_origin_web</sub>
**substrate** [[document_pdf]] [[regulation_legal_text]] [[web_dom]]

**stack** css, html, javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what's next for haeco bay management system

## Body

Login Page Mainpage Dashboard Incoming Aircraft within 7 Days Automatic Bay Recommendation for Aircraft Bay Layout One-day Schedule of Maintenance Bays Real-time Summary Report for Bays & Work Type Inspiration As one of the world’s leading aircraft engineering and maintenance service providers, HAECO provides aircraft maintenance, repair and overhaul (MRO) services to enormous commercial airlines and private jets. Its hangars located at Hong Kong International Airport are one of the busiest aircraft base maintenance facilities around the world, offering services to over 20 aircraft at the same time. Assigning the aircraft into an applicable maintenance bay is essential. Each maintenance bay has its constraints on aircraft model and maintenance task nature. Besides, aircraft may be blocked by others in some locations, making some geographical dependencies during aircraft movements. Therefore, matching these environmental restrictions with the aircraft is a daily routine before each shift, while this complexity, together with frequent maintenance task reprioritization due to unpredictable external factors, creates a huge planning challenge for the responsible personnels to complete it manually with time pressures, as any human error may cause substantial breaching of related regulations. Nonetheless, it is difficult to prove that the current manual thinking methodology is the best solution for such almost mission-impossible work. With a daily maintenance environmental requirement for each aircraft input, there is an opportunity to assign aircraft maintenance bay automatically by a digital product. It can minimize the aircraft movements by suggesting the most optimized plans for the upcoming schedule. This smart tool enables a more organized and effective planning as well as minimal manual repetitive work, which supports the dynamic maintenance operations and avoids operational bottlenecks, driving for operational transformation and technology innovation cultivation ultimately. What it does HAECO Bay Management System is a web-based management system embedded with visualization portal & optimization engine to provide the most optimized suggestion for aircraft maintenance bay assignment and movements at HAECO hangars over a rolling 7-day window. Key features included as follows. Automated Assignment Aircraft are assigned to maintenance bays based on work type and maintenance bay type compatibility, ensuring that maintenance tasks are performed in applicable locations. Rule-Based Planning The solution incorporates a realistic set of rules, including: Geographical dependencies between maintenance bays Maintenance bay size limitations that restrict which aircraft model can be accommodated Restricted maintenance bay choices according to the type of maintenance tasks AI-Driven Optimization Instead of simply minimizing towing count or temporary bay usage, the movement plan is optimized using a pre-set rule in AI model that evaluates a comprehensive set of criteria, such as: Urgency of maintenance tasks Work type requirements Complexity of bay dependencies Other operational factors Interactive Visualization The product is presented as an interactive visualization in the web interface, allowing users to: Create maintenance environmental requirement for each aircraft (either by individual update or bulk import) Generate and apply the optimized maintenance bay allocation for each aircraft Modify schedules and allocated maintenance bays as needed How we built it To accelerate development and enhance solution intelligence, project team leverages Kiro throughout the project lifecycle. Requirement Documentation Kiro has been used to document system requirements by clearly communicating our expectations and specifying the planning rules through vibe coding. Kiro’s strong logical mindset enables it to understand and convert textual requirements into precise logical rules. Validation & Clarification Kiro is instrumental in checking for contradictions or vague requirements, prompting us to clarify and refine our specifications. This ensures that our design is robust and logically consistent before implementation. Development Support The web-based solution is built using HTML, CSS, and JavaScript, making it easily accessible for users without extra installations. Kiro’s support streamlines the process, helping us focus on the core logic and user experience. Accomplishments that we're proud of With the aid of Kiro, project team successfully develops the HAECO Bay Management System within 14 calendar days. The solution delivers a comprehensive set of functionalities that able to address our business pain points and operational needs, streamlining the aircraft allocation process. Dashboard The dashboard provides a real-time overview of maintenance bay utilization and displays historical aircraft arrangements. This well-organized summary enables users to quickly assess the current maintenance bay status within the facility, supporting data-driven decision-making process. Scheduling The product supports the importing of over 100 aircraft schedules for upcoming months. A user-friendly 7-Day Timeline visually displays incoming aircraft, helping users anticipate workload and maintenance bay availability. The Aircraft List presents all imported planes in a clean and structured format. With a single click on “Optimize Assignments” button, the system intelligently assigns aircraft to suitable bays across the entire scheduling horizontal timeline, maximizing efficiency and minimizing conflicts. Bay Assignment The product replicates the physical layout of the HAECO hangar at Hong Kong in a digital interface. Users can assign aircraft to different maintenance bays manually or relying on AI-powered recommendations. The system generates optimized maintenance bay assignments with a confidence score for each aircraft, factoring in aircraft model, maintenance task type, and movement cost. This approach enhances maintenance bay utilization and supports dynamic scheduling. Bay Status The Bay Utilization Timeline offers a detailed and day-by-day view of bay usage. Users can oversee which aircraft occupy which bays at specific times and access an overview of maintenance bay activity across multiple days. This feature supports precise planning and real-time operational awareness. Analytics & Reports The product provides real-time analytics based on imported and manually entered aircraft data. Key insights included as follows. Maintenance Bay Type Utilization : Tracks how many bays are used and what types are in demand. Work Type Distribution : Visualizes the breakdown of maintenance tasks across all aircraft. Recent Activity Log : Allows users to monitor the latest updates and identify steps that may require attention or revision. AI Assistant Chatbot An integrated AI-enabled chatbot helps users extract useful information related to the application. It is especially valuable for answering “how-to-use” questions and summarizing current bay utilization, making the platform more accessible and user-friendly. What's next for HAECO Bay Management System With the successful completion of this prototype digital product, the project team will scale it up with more constricts and dependencies. Data integration with exiting planning system and ERP system can be built to further streamlining the process and eliminate all non-value-added manual works. Besides, embedding it to the existing hangar visualization app provides up-to-date aircraft locations to the entire production team through mobile devices. These possibilities offer a solid digitalization roadmap that using innovative technologies to make HAECO a more modernized organization. <div