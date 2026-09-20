---
slug: "flow-restore-utility"
url: "https://devpost.com/software/flow-restore-utility"
title: "Flow Restore Utility"
hackathon: "Tableau DataDev 2024-2025 Hackathon "
organization: "Tableau"
winner: true
words: 767
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/retrieval_grounding"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Flow Restore Utility

> The $10,000 recurring Tableau product gap solved.

[Devpost](https://devpost.com/software/flow-restore-utility) · hackathon [[Tableau DataDev 2024-2025 Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[retrieval_grounding]]
**domain** [[civic_government]] [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[structured_db]] [[web_dom]]

**stack** python, streamlit, tableau, tableaucloud

## How they structured the write-up

- flow restore utility

## Body

Flow Restore Utility This utility allows users to run their flows previously backed up from one server and restored to another without being required to do the following manually: Download each flow from the server the flows were restored to. Update the connection details of any input nodes pointed at published data sources because without intervention they will still be pointed to the server for which the flows were backed up. Update the Tableau server and site details specified in each output node because they will be pointed towards the server for which the flows were backed up. Republish the flow to the server for which the flows have been restored to in its original location (project). Impact It is likely no surprise to the person reading this that organizations committed to the Tableau Server product stand up two to three server instances. One each for development, user acceptance testing, and production. When those organizations clone their production instance to the other instances to ensure each is kept relatively up to date by creating a backup and restoring the contents to those instances, all is well, except when it comes to Tableau Prep flows. The Tableau Server Site value in the connections tab of each flow page maintains its original value. These connections correspond to the input and output nodes. To successfully run any flow, it is required that each input node pointed to published data sources and those output nodes writing to the Tableau Server be updated to reflect the new full server URL. This exercise is incredibly painful even with web-authoring enabled which presents security risks for those organizations with a service account set up on their server to connect to one or more databases. Because of the level of effort required, organizations heavily invested in Tableau Prep-based solutions are increasingly reluctant to use their additional instances for anything besides server upgrade testing. I can attest firsthand that my Flow Restoration Utility fills a current Tableau product gap that would otherwise cost hundreds of hours and thousands of clicks for organizations heavily invested in the Tableau Prep product. One alternative would be to engage with a consulting company to develop a solution to solve the problem for you, but depending on your scale this could cost tens of thousands of dollars every time you need to run a migration process. That adds up quickly! API Tableau Server Client was used to create this project. The python library, streamlit, was used to create the front-end. Potential Improvements I am not a software engineer or python developer by profession. As a result, the code supporting the Flow Restoration Utility can likely be significantly improved in terms of readability and the speed for which the tool runs. Additionally, for those connections maintained in the flow that do not point to the Tableau Server, the tool can be enhanced to automate the re-embedding of credentials to data sources like external databases and those supported by Tableau’s data connectors. This operation is already supported by Tableau’s REST API and Tableau Server Client and works well based on my testing. Delivering this enhancement would be quite easy if it was known in advance the possible “class” values and structure corresponding to each connector. The class value and overall structure of the connection node details for a specific database connector, say Oracle, is maintained in the flow’s metadata and can be viewed within the “flow” file. Unfortunately, the information corresponding to each connector doesn’t seem to be publicly available and the hurdle to somehow have access to an instance for every connector is beyond unrealistic. If more time were permitted, I would make the re-embedding of credentials possible for those connectors I am familiar with. Finally, I would make it possible for the user to be more selective of which flows are restored as opposed to restoring all flows on the Tableau Server / Cloud instance. This is really easy to do by specifying the project ID for which those flows live in the current code I have developed, but there is not enough time to build out the front-end to support this functionality. As far as the front-end goes, it’s simple but effective. That said, my goal was to simply not have someone look at it and immediately think of the “when the backend developer designs the front-end” meme. GitHub Code Repository https://github.com/CodingOnWindowsOS/Hackathon YouTube Video Link https://youtu.be/-vClgCHwQpE Video Chapters 00:00 Setting the scene by explaining the product gap 01:07 About the Flow Restore Utility 01:42 Running the Flow Restore Utility 02:22 Recap 02:42 Learn more about the Flow Restore Utility <div