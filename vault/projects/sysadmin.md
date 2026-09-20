---
slug: "sysadmin"
url: "https://devpost.com/software/sysadmin"
title: "SysAdmin"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 538
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/web_dom"
---

# SysAdmin

> A project made using fastapi to access your machine remotely through REST APIs and get system info and save files, run scripts and schedule them to get automated emails about your machine.

[Devpost](https://devpost.com/software/sysadmin) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[web_dom]]

**stack** bash, fastapi, linux, python, windows

## How they structured the write-up

- inspiration
- what it does
- installation instructions:
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sysadmin

## Body

Alert Box Sent to user after email has been sent. Web Tunneled URL email. Scheduled Script email. Create Task API example Run Task API example Manually running .exe file (Windows) Inspiration Developers often have a lot of files and scripts on their local machines and sometimes due to issues, they don't have access to their system or system information. SysAdmin is a RESTful tool made using fast-api. This is coupled with web tunneling so that you can access your system remotely via REST APIs. SysAdmin allows the user to control tasks and schedule them using APIs and transfer data to and from the tunneled URL using simple tasks. What it does SysAdmin is distributed as an executable which can be installed on your system. Once installed successfully, you will receive an email with your tunneled url which can be used to access your system remotely. The API endpoints available are mentioned in the API documentation with example requests and responses. It is also capable of scheduling tasks so that you receive outputs via mail to get system updates no matter where you are sitting. You can access APIs on local machine using http://localhost:8000/ . Supported Platforms: Windows Debian based Linux Distributions The only requirement to use SysAdmin remotely is that the machine to be accessed needs to be up and running so that the api can reach it. Installation Instructions: For Windows: Extract the SAC.rar file. Run the executable installer file. Enter an email when prompted. "START: The operation completed successfully." should show up on your screen. You can exit the installer now. You will receive the tunneled url at the entered email in a few minutes. In the Postman collection, replace the value of {{fast_api}} variable with this value. For Debian Based Linux Distributions Extract the SysAdmin.zip file Open the terminal where the files have been extracted. Run chmod +x install.sh to make install.sh executable. NOTE: install.sh and SysAdmin have to be in the same directory. Run ./install.sh to start the server Enter an email when prompted. Now SysAdmin has been installed as a service. "Client ready and running as a service" should show up on your screen. In the Postman collection, replace the value of {{fast_api}} variable with the tunneled url value. To uninstall the service you need to run chmod +x uninstall.sh and ./uninstall.sh How we built it The server is built using the fastapi which is a lightweight and speedy framework to build apis. We have used ngrok for web tunneling and google apis to send mails using python programmatically. Challenges we ran into Developing a cross operating system solution and mainiting uniformity amongst them. Generalising endpoints so that the user can make the maximum out of SysAdmin. Accomplishments that we're proud of Using libraries and converting them into a RESTful system so that it can be used easily by developers. Scheduling tasks and learning tunneling to access systems remotely. What we learned Fast API Advanced language syntax Web tunneling Cross system products What's next for SysAdmin Adding more features and api endpoints to make the experience more interactive and useful for the users. More security for the user. Making scheduling more efficient. An interface for showing the user a dashboard and statistics. <div