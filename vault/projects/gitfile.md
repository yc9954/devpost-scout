---
slug: "gitfile"
url: "https://devpost.com/software/gitfile"
title: "GitFile"
hackathon: "HackUTD 2024: Ripple Effect"
organization: "hackutd"
winner: true
words: 787
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# GitFile

> Git for ANY file type - Reducing storage costs by 500x, streamlining version control, and fostering efficient collaboration

[Devpost](https://devpost.com/software/gitfile) · hackathon [[HackUTD 2024- Ripple Effect]]

## Facets

**mechanism** [[benchmark_measured]] [[cross_origin_web]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[document_pdf]] [[web_dom]]

**stack** azure, c, cloudfare, express.js, git, iframe, nextjs, node.js, pdf.js, pinata, ssh, terraform

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we are proud of us
- what we learned
- what's next for gitfile

## Body

Inspiration Git exists for programmers. We use it for coding. But what about documents with file types like PDFs, DOCX, XLSX, JPG, etc? Businesses today store backups of most their data on a repeating basis where the data doesn't change much every day, yet multiple copies are kept. As you might have guessed, every single copy only doubles the data being stored. The storage, bandwidth, and latency costs as a result of this are tremendous. What It Does Our website is a fully-functional POC demonstrating how our custom-built git wrapper can transform the realm of unstructured data file types. When a user edits a pdf document or any other flat file, our software figures out the difference between the two versions and captures this. We offer an interface to edit a file and view the storage costs of having multiple versions after running a "git push" of the file to the cloud server. We effectively demonstrate the use of a low-level C wrapper surrounding git that works on flat files that have changes between versions. How we built it We built our frontend built in NextJS and hosted it on a Virtual Machine by using Terraform on an Azure ecosystem (also surrounded by other Azure services like gateways, networks, etc). We enlisted gitfile.tech as our root domain which hosts the main root of our website (as well as subdomains at main-server, ssh, etc for the other services that make the software work via A records using cloudfare setup). We connected an ssh session to a local git session to demo the functionality of git in an environment and the resulting version history in a dashboard one-screen format. In this system, we used Pinata to store our git history (similar to how GitHub acts as a cloud storage service) and made use of both storage and retrieval APIs effectively in this process. In our ssh terminal functionality at the bottom of the dashboard, we made use of Mozilla's PDF.js library for pdf-editing functionality which can be run with the command "edit " to edit the pdf and view its effects. Challenges We Ran Into Setting up the low-level software which wrapped around common git functions like "git add" and "git push" to support our use case of flat filetypes was a bit challenging, but thanks to a bit of research we were able to get it done in time Getting the edit pdf functionality to work was a time consuming process as it required the need for multiple services to act appropriately and the documentation for this was very thorough and hard to finish understanding in a short period of hackathon time Accomplishments We Are Proud of Us An accomplishment we are extremely proud of is the successful benchmarking of real-world business use cases to showcase the effectiveness of our solution. By applying our custom build wrapper we generated over a 500 times reduction in storage costs. This was pivotal in understanding the importance of something like this and the protentional value to business that rely on document storage. We are also really proud of completing in time! This hackathon we used a variety of technologies ranging from Azure hosting to integrating custom SSH functionalities which really pushed us to our limit. Finally being able to design a seamless user experience with functionalities like real time pdf editing and visualization in the dashboard was something we were really proud of considering we are not too experienced in front-end development,=. What We Learned One major thing we learned was setting up SSH sessions restricted to specific holders and embedding it in an iframe on a static-rendered website taught us about the intricate workings of secure sessions and really opened our eyes to the importance of security in development. Using Terraform to deploy Azure services was another learning curve we had to tackle. We gained experience in infrastructure and understanding how to manage virtual machines, gateways, and networks in an Azure ecosystem. One of the most enriching aspects was writing custom commands in C that interfaced with Git's default commands. This dive into Got internals gave us all a better understanding of how version control systems work and how they can be modified for specific use cases. What's Next for GitFile The next step would be to open source the project by sharing the code with the developer community and gather valuable feedback. By open sourcing developers and business can experiment with our tool and identify potential features or optimizations. We also want to look into ways to improve the editing and versioning features. This could be a refined dashboard interface or enhanced integration between the editing commands and version history visualization, making GitFile an even more user-friendly tool. <div