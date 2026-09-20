---
slug: "tableau-permission-exporter"
url: "https://devpost.com/software/tableau-permission-exporter"
title: "Tableau-Permission-Exporter"
hackathon: "Tableau Hackathon"
organization: "Tableau"
winner: true
words: 402
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Tableau-Permission-Exporter

> Export and visualize Tableau permissions for compliance and security.An intuitive GUI tool that simplifies Tableau permission auditing.

[Devpost](https://devpost.com/software/tableau-permission-exporter) · hackathon [[Tableau Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** claude, csv, python, tableau-rest-api, tkinter

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tableau-permission-exporter

## Body

Inspiration Managing Tableau permissions at scale presents real challenges. Migration Verification: Checking permissions across numerous items after Server to Cloud migration was time-consuming. Organizational Changes: Large-scale changes require verifying access controls across many content items. Access Troubleshooting: No easy way to see what a specific user can access from their perspective. Tableau recommends the REST API for bulk operations—powerful for developers. Our solution: A GUI tool making permission management accessible to everyone—no coding required. What it does GUI tool for bulk exporting Tableau permissions with user-level analysis. Features: Tree-based project selection and one-click CSV export Optional group membership data Analyze by user: Combine exports in Tableau to see any user's effective permissions Zero coding required Use cases: Auditing, compliance, migration verification, troubleshooting user access. How we built it Tech Stack: Python, Tkinter GUI, Tableau REST API, CSV export Key Implementation: Administrator Template Expansion: Tableau API returns only "InheritedProjectLeader" for Administrator permissions. We tested in Tableau GUI, documented all capabilities across content types, and built expansion logic. On-Demand Loading: Instead of loading all content upfront, we fetch content only when users expand a project—reducing unnecessary API calls and improving responsiveness. API Limitation Handling: Some capabilities lack API endpoints. For example, Virtual Connection's "Overwrite" permission exists in Tableau's GUI but has no corresponding REST API endpoint. We identified these through testing and mark them as "No API Endpoint" in the CSV output to avoid confusion. Simple Architecture: Two modules— gui_app.py for interface, tableau_client.py for API interactions. Challenges we ran into Administrator Template Expansion Tableau API returns only "InheritedProjectLeader" for Administrator permissions. We systematically tested in GUI to map this to actual capabilities across all content types. Missing API Endpoints Some GUI capabilities (like Virtual Connection "Overwrite") have no API endpoints. After testing multiple variations, we explicitly marked these limitations in the output. GUI-API Name Mapping Tableau GUI uses user-friendly names while API uses technical names (e.g., "Download Image/PDF" vs "ExportImage"). Mapping these consistently required careful documentation and testing. Accomplishments that we're proud of Built a practical tool that solves real permission auditing challenges. We're proud it can help organizations with compliance, security reviews, and migration verification—tasks that were previously manual and time-consuming. What we learned AI-Assisted Development: First time using Claude for a project—it dramatically accelerated development, turning days of work into efficient collaboration. What's next for Tableau-Permission-Exporter More content types: Virtual Connections, Databases, Tables Permission import: CSV-based bulk updates (if demand exists) <div