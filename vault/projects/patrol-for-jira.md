---
slug: "patrol-for-jira"
url: "https://devpost.com/software/patrol-for-jira"
title: "Patrol For Jira"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 593
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "substrate/structured_db"
---

# Patrol For Jira

> Security scanner for Jira - detects hard-coded passwords, 3rd party apps vulnerabilities, misconfigurations and much more. Keeps Jira and its users secure allowing organizations to move fast.

[Devpost](https://devpost.com/software/patrol-for-jira) · hackathon [[Codegeist 2021]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[accessibility]] [[developer_tools]] [[security_privacy]]
**substrate** [[structured_db]]

**stack** forge, javascript, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for patrol for jira

## Body

Inspiration The amount of cyber attacks and security threats break records every year. In high-tech organizations, Jira has become one of the key resources when it comes to intellectual property, trade secrets, and sensitive data. While Jira Cloud is secure out-of-the-box and well-protected against external threats, the content of Jira issues, actions of users and admins are being the responsibility of each customer. We wanted to address this challenge and provide organizations with a tool to secure the internals of their Jiras and add an extra level of security. What it does Patrol continuously scans Jira instances for various types of potential problems, vulnerabilities, suspicious actions. These categories include: Instance misconfigurations, publicly shared projects, dashboards, filters Top-100 third-party applications with known vulnerabilities and fixes available Suspicious administrator behavior (adding users from external domains, security group modifications etc) Actions conducted from non-approved locations and IP addresses Newly added organization API tokens and ones that were added a too long time ago Sensitive data saved in Jira issues - hard-coded passwords, tokens, personal data. How we built it I have been working in information security for many years and have observed how Jira became one of the crown jewels that are in the crosshairs of attackers - as it may contain valuable information and business secrets. Nowadays, with most organizations moving to SaaS products, they often take security for granted and expect everything to be taken care of - instead, they may put their users and company data at risk and overlook their responsibility for security of how the Jira is used by their users. I wanted to create a tool that would help administrators, IT and DevOps teams secure their Jira Cloud against internal and external threats that may have breached the perimeter and compromised one or more accounts. The core of Patrol is the asynchronous scanner that performs a scan daily and consists of 5 independent modules. Each module calls Jira, Atlassian Access, Atlassian User Management APIs and compiles results into a single list. Each issue gets a severity score based on its potential impact to the business, and a joint risk score is compiled based on the total risk score from all issues. The app relies heavily on Forge Storage, scheduled jobs, and various Atlassian APIs. Also, with previous experience in building 3 Forge apps, I was able to utilize previously made modules and quickly create the UI and scan visualizations. Challenges we ran into Integrating with various Atlassian API (Jira, Atlassian Access, User Management and Provisioning) required exploring various API schemas, authentications types and figuring out how to process and reconcile the data. Another challenge was about utilizing Forge Storage - it required building a pagination mechanism to store issue descriptions and control for the size of each storage entry. Accomplishments that we're proud of The time it took to build with Forge was cut in half due to reusing previously coded primitives and helper functions. The final result, in my opinion, provides real value to organizations and removes a potential blind spot in their defences when it comes to internal threats and compromised accounts. What we learned Prototyping quickly with Forge is a great opportunity for small teams to try out their ideas and deliver MVPs to the Marketplace in the shortest time span. What's next for Patrol For Jira Advanced intrusion detection based on audit log Integrate more Atlassian APIs Improve performance and application resilience Add analytics and historical graphs to better visualize risk Add more third-party products to our vulnerability database And most importantly, Patrol for Confluence! <div