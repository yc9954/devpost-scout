---
slug: "ecozen"
url: "https://devpost.com/software/ecozen"
title: "EcoZen"
hackathon: "Agentforce Virtual Hackathon"
organization: "Salesforce"
winner: true
words: 599
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/climate_energy"
  - "substrate/sensor_telemetry"
---

# EcoZen

> AI Intelligence for Carbon-Efficient Computing.

[Devpost](https://devpost.com/software/ecozen) · hackathon [[Agentforce Virtual Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[climate_energy]]
**substrate** [[sensor_telemetry]]

**stack** amazon-web-services, apex, azure, climatiq, gcp, salesforce

## How they structured the write-up

- 🔖 tagline
- 🧠 inspiration
- 🛠️ what it does
- ⚙️ how we built it
- ❓how we calculate carbon emissions
- 🧩 challenges we ran into
- ✅ accomplishments that we're proud of
- 🚀 what's next
- 💻 components

## Body

AI Agent Decision Flow Azure Trend Dashboard 🌱 EcoZen: Smarter Clouds. Smaller Footprint 🔖 Tagline Empowering organizations to monitor and reduce cloud carbon footprints with intelligent, automated insights. 🧠 Inspiration As cloud computing becomes integral to business operations, understanding and mitigating its environmental impact is crucial. EcoZen addresses this by providing real-time carbon emission tracking across major cloud providers, enabling organizations to make sustainable choices with well-grounded recommendations. 🛠️ What It Does EcoZen is a Salesforce-native application that: Aggregates virtual machine (VM) data from AWS, Azure, and GCP. Calculates carbon emissions using the Climatiq API. Visualizes emissions data within Salesforce dashboards. Automates data refreshes and emission calculations via Apex and Flow integrations. Publishes Weekly detailed trend analysis reports on Slack. Integrates and works perfectly as a Slack Agentforce agent. ⚙️ How We Built It Data Collection : Utilized Apex callouts to fetch VM details from cloud providers. Emission Calculation : Integrated Climatiq API for accurate emission metrics. Salesforce Integration : Leveraged Apex classes and Flows for seamless automation and user interaction. Named Credentials : Uses Named Credentials to store secret keys and fetches refresh tokens. User Interface : Designed intuitive dashboards for easy interpretation of emissions data. Slack : Integrated and installed the Agent in Slack for ease of use. ❓How We Calculate Carbon Emissions We use the Climatiq API , a reliable and science-backed platform, to calculate carbon emissions based on real-time cloud VM data. Once we fetch virtual machine specifications (like region, instance type, and uptime) from AWS, Azure, or GCP, we pass this data to Climatiq, which returns precise CO₂ equivalent emissions. Climatiq’s standardized emission factors ensure accuracy and consistency across all cloud providers. Notably, Salesforce has already partnered with Climatiq as part of its Net Zero Cloud initiative , which makes our solution seamlessly aligned with Salesforce’s broader sustainability goals. 🤝 How EcoZen Complements and Extends Net Zero by Salesforce While Salesforce Net Zero Cloud excels in sustainability tracking and reporting, EcoZen adds an intelligent, automation-driven layer on top: 🌐 Unified Multi-Cloud Insights: EcoZen connects directly with AWS, Azure, and GCP through custom-built connectors, pulling real-time resource metrics from all major cloud platforms. 💬 Slack-Powered Contextual Intelligence: We integrate with Slack not just for collaboration but to fetch user complaints that inform optimization strategies, and to publish weekly cloud-specific sustainability reports and recommendations. 📊 Actionable Optimization with Impact Estimates: EcoZen analyzes and compares current and suggested cloud configurations, estimating carbon reduction impact upfront — enabling informed decision-making before implementation. 🧩 Challenges We Ran Into API Limitations : Navigated rate limits and data inconsistencies across cloud provider APIs. Data Normalization : Standardized diverse data formats for uniform processing. Asynchronous Processing : Implemented @future methods to handle callouts without blocking operations. ✅ Accomplishments That We're Proud Of Cross-Cloud Compatibility : Successfully integrated data from multiple cloud platforms. Real-Time Insights : Enabled near-instantaneous emission calculations upon data retrieval. User Empowerment : Provided actionable insights to users, fostering informed decision-making. 🚀 What's Next Expanded Metrics : Incorporate additional environmental metrics like water usage. Predictive Analysis : Utilize AI to forecast emissions based on usage trends. User Alerts : Implement notifications for emission thresholds and anomalies. 💻 Components Apex Classes Custom Connectors to Fetch Data : EcoZen_AzureVMService, EcoZen_EC2Details, EcoZen_GCPVMService Climatiq Calculations: EcoZen_Climatiq_Calculator, EcoZen_CompareInstanceEmissions Slack Integrations: EcoZen_SendSlackMessages, EcoZen_SendSlackSummary, EcoZen_SlackComplaintSearch Misc: EcoZen_CreateSnapshotService, EcoZen_DataFetchDecisionMaker, EcoZen_DummyDataService, EcoZen_FlowVMInfo, EcoZen_Object_CRUD Flows Daily_Carbon_Emission_Refresh: Calculates and refresh carbon emissions. Scheduled flow to run daily. EcoZen_Carbon_Emissions_Refresh: Agent Triggered Flow to refresh carbon emissions EcoZen_Daily_Carbon_Emissions_Snapshot: Takes daily Snapshots for all types of carbon emissions Weekly_Carbon_Emission_Report_Flow: Fetches the weekly snapshot records and generates summary prompt builder. Dashboard Lightning App: EcoZen <div