---
slug: "plug-n-play-send-email-multiple-attachments"
url: "https://devpost.com/software/plug-n-play-send-email-multiple-attachments"
title: "Plug N Play - Send Email Multiple Attachments"
hackathon: "Power Up Automation"
organization: "UiPath"
winner: true
words: 445
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/code_repository"
---

# Plug N Play - Send Email Multiple Attachments

> Ready-to-use Plug & Play BOT for Email Automation which can be published under the umbrella called as BOT FACTORY.

[Devpost](https://devpost.com/software/plug-n-play-send-email-multiple-attachments) · hackathon [[Power Up Automation]]

## Facets

  <sub>weak: provenance_signing</sub>
  <sub>weak: developer_tools</sub>
  <sub>weak: developer</sub>
**substrate** [[code_repository]]

**stack** reframework, roboticenterpriseframework, roboticprocessautomation, rpa, uipath

## Body

Inspiration Introducing the Plug & Play BOT, a ready-to-use UiPath workflow that can be integrated easily with any project across different customers that too without any modification. Need of reusable components across multiple projects/customers inspired me to create the Plug 'N' Play BOT to Send Email Multiple Attachment using UiPath. What it does? Send email is one of the most common functionality that we come across in almost every RPA implementation. Developers face challenges to configure the BOT to send more than one email attachment. BOT sends one or more email attachment(s) to the ‘To’ & ‘Cc’ recipients mentioned in config file. It reads the email Subject and Body from the email templates stored in Data\Template folder. How I built it? It is built on the concept of Robotic Enterprise Framework (ReFramework). It can be easily integrated with non-ReFramework projects as well. Configured the BOT to read one or more email attachment(s) as an array of string to store the attachment name with folder path. BOT attach one or attachment file(s) to the email using Invoke Method activity. Send Outlook Mail Message is used to address the Email Subject, Email Body and Recipients details. Successfully tested the execution for different customers. It works very well without any change in code. It can be run standalone or can be integrated with any project. What's Next? Publish it under the centralized umbrella called as BOT Factory or Market Place which can be easily downloaded by the RPA professionals having access to it. How to use Send Email Multiple Attachment Plug & Play workflow? Filename: Send Email.xaml (A) Pre-requisite: Download the complete project repository (B) Update Config.xlsx: To recipients email address - stores recipient email address to be marked in 'To' section of the send email activity Cc recipients email address - stores recipient email address to be marked in 'Cc' section for success/exception scenario (C) Invoke: Integration with existing project Use Invoke Workflow activity in your project sequence/workflow Click import arguments 2.1. Optional: Pass Config (Data Dictionary) variable to the input argument in_Config, if you are using ReFramework 2.2. Optional: Pass runtime message (string data type) variable to the input argument in_strMessage, value will be updated in the placeholder mentioned in email template 2.3. Pass Email Template Filename (string data type) variable to the input argument in_strEmailTemplateFilename 2.4. Pass attachment filenames (Array of String) variable to the input argument in_arrAttachments, you can pass more than one filename separated by comma as a delimeter (D) Run: Standalone execution To Run standalone: Open “Send Email.xaml” -> hit run Project repository details: /Framework/InitAllSettings.xaml Send Email.xaml Main.xaml project.json /Data/Config.xlsx /Data/Input/Input File.xlsx /Data/Logs/Audit Trail.txt /Data/Output/Result.xlsx /Data/Template/Exception Email.docx 10 . /Data/Template/Success Email.docx <div