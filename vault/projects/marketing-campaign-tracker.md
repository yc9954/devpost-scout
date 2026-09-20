---
slug: "marketing-campaign-tracker"
url: "https://devpost.com/software/marketing-campaign-tracker"
title: "Campaign Analyser"
hackathon: "Codegeist 2024"
organization: "Atlassian"
winner: true
words: 861
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Campaign Analyser

> Unify Google Analytics & Jira to plan, track, and manage all marketing initiatives in one view. Use ROVO AI for insights to maximize campaign impact and optimize resources and customer value.

[Devpost](https://devpost.com/software/marketing-campaign-tracker) · hackathon [[Codegeist 2024]]

## Facets

**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** atlaskit, forge, forge-storage, google, jira-api, react, redux, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for campaign analyser

## Body

Manage and access all campaign performance reports with ease Integrate Jira and Google Analytics to view metrics that matter Track Jira issues, team efforts, hours logged, and task completion in one view Sync Google Analytics to monitor user engagement, new users, and revenue alongside Jira data Rovo agent: Smart campaign assistant Analyze campaign data to get insights Plan, track, and optimize marketing campaigns with data-driven insights Inspiration Campaigns are one of the biggest growth accelerators for businesses, but they also pose significant challenges for marketing teams and leadership. Many teams rely on separate tools like Google Analytics for performance metrics and Jira for task tracking, making it hard to connect campaign results with the resources invested. This disconnect prevents leaders from seeing the full picture, which is crucial for setting strategies and optimizing customer value. The idea for Campaign Analyser came from our own marketing team's experience. We regularly monitor and analyze campaigns to scale successful initiatives and minimize the risks of running ineffective ones. However, we often found ourselves facing a challenge: while Google Analytics showed us the results, we lacked insights into the resources spent — like time logged, people involved, and overall effort. We realized that bringing all these metrics together in one place could solve a major pain point, making it easier to assess, optimize, and replicate high-performing campaigns. To take it further, we integrated Atlassian Rovo into Campaign Analyser. Rovo provides insights by processing data from campaigns, resources, and tasks, helping teams and leaders make data-driven decisions. This combination of unified data and AI-driven insights became the foundation for Campaign Analyser — an app designed to empower marketing teams and leadership to drive maximum value from their campaigns. What it does Campaign Analyser bridges the gap between campaign results and resource tracking by integrating Google Analytics and Jira into a single, streamlined platform. It provides: In-time insights into campaign performance, resource usage, and team efficiency. AI-powered recommendations using Rovo to identify best campaigns and optimize resource allocation to align strategy with business goals. A unified view of all marketing initiatives, enabling leaders to manage their portfolios more effectively. By combining data, Campaign Analyser allows marketing leaders to make context-based, data-driven decisions with clarity and precision. How we built it Technology Stack Language: TypeScript Frameworks: React + Redux Platform: Atlassian Forge Database: Forge storage (Custom Entity Store) APIs: Google API, Jira API Atlassian UI Library: Atlaskit Development Approach We used Atlassian Forge for secure and scalable integration with Jira and relied on Feature-Sliced Design methodology for the custom UI. Rovo AI was incorporated to analyze and process campaign data, providing insights. We explored different storage solutions and selected Custom Entity Store for its flexibility to handle dynamic campaign data. Challenges we ran into Learning Forge: This was our first time building a fully Forge-based app, and we faced initial difficulties with typing methods and adapting to the platform's structure. Dynamic Data Handling: Campaign data is constantly changing, requiring us to implement flexible storage solutions using a mix of indexed and dynamically typed attributes. API Integration: Ensuring that the Google API could fetch the required data with the permissions provided by Forge Providers required extensive testing and adjustments. AI Implementation: Fine-tuning Rovo AI to provide accurate, actionable insights was a complex but rewarding process. Accomplishments that we're proud of Successfully building a fully functional app on Atlassian Forge, leveraging its security and scalability. Seamlessly integrating Google Analytics and Jira, offering a unified view of campaign performance and resources. Implementing Atlassian Rovo to deliver impactful, data-driven recommendations that align strategy with business goals. Creating a user-friendly interface that simplifies complex data and enables in-time and fast decision-making. What we learned Building Campaign Analyser taught us valuable lessons about solving problems faced by marketing teams and leaders. From our own experience managing campaigns, we understood the importance of unifying fragmented data — performance metrics, resource usage, and team efforts — into a single platform. This realization shaped the app’s core functionality. Along the way, we learned how to: Balance flexibility and precision when working with dynamic campaign data structures, ensuring the tool remains adaptable to varied use cases. Effectively use Forge Providers to manage authentication and integrate APIs like Google while maintaining seamless user experiences. Leverage Rovo AI to generate actionable insights that directly impact strategic decision-making for leaders and teams alike. Collaborate closely with marketing professionals to ensure the app addresses practical challenges and delivers meaningful value. These insights not only shaped Campaign Analyser but also reinforced the importance of combining simplicity, innovation, and practicality in solving complex problems. What's next for Campaign Analyser Predictive Analytics: Introducing features that forecast campaign outcomes and resource needs to help leaders plan proactively. Expanded Integrations: Adding support for more analytics platforms and tools like Hubspot or Mailchimp to sync marketing data across platforms and provide a unified perspective on every aspect of a campaign. Enhanced Reporting: Building more robust and customizable reporting capabilities tailored to executive-level needs. Campaign Analyser is just the beginning. Our vision is to revolutionize how marketing leaders set strategies, manage portfolios, and deliver maximum value — all powered by data-driven insights and the capabilities of Atlassian Rovo. <div