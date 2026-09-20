---
slug: "secure-share"
url: "https://devpost.com/software/secure-share"
title: "Secure Share"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 1357
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# Secure Share

> Secure Share provides a solution that’s tightly integrated with Atlassian products and allows users to send important files encrypted end-to-end directly to others, safely and securely.

[Devpost](https://devpost.com/software/secure-share) · hackathon [[Codegeist 2021]]

## Facets

**mechanism** [[privacy_tech]]
**domain** [[developer_tools]] [[finance_payments]] [[labor_employment]] [[security_privacy]]
**user** [[developer]]
**substrate** [[document_pdf]] [[financial_record]] [[sensor_telemetry]] [[web_dom]]

**stack** amazon-api-gateway, amazon-dynamodb, amazon-web-services, firefox-send, flask, python, serverless, vue, vue-atlaskit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for secure share

## Body

Outbox Send Inbox Inspiration Many important business processes require sharing data with people in the organizations. Consultants send contracts, invoices and proposals, accountants send financial data. Onboarding processes may contain login credentials and hiring processes have similar file sharing requirements. Traditional methods of file sharing exposes a fundamental problem where a lot of often highly sensitive data is stored unencrypted in multiple servers for unspecified periods of time, i.e. attachments in Jira or Confluence and emails on mail servers. Another problem is that recipients aren't native to the and don’t want to leave the applications that run critical business processes such as Jira or Confluence. We aim to solve the problems by focusing on the following key principles. Security First. Provide an excellent solution that’s tightly integrated with Atlassian products. Expand our functionality to include digital signatures and integrate with other DMS (such as Google drive and O365 products) What it does Secure Share provides a way to share documents, end-to-end encrypted, with other users within your organization. At its core, the app allows users to send and receive files. When sending a file, a user specifies its recipient, an email address of the recipient and the file itself. Optionally, the user can specify a description. When the file is sent, it will appear in the recipient's inbox and the decryption key is sent to the recipient's specified email address. The recipient can then open the file in their Secure Share inbox and, with the decryption key, decrypt and download the original file. The decryption is performed in the browser. After the file has been downloaded, it is deleted from our servers, preventing any further downloads. If the file is not downloaded within three days, it is also deleted from our servers. In the Secure Share inbox, a user can see an overview of the files they have received, including their description as well as when they were sent and received. The user is also presented with the status of each file, i.e., whether it was downloaded or not, or if it can still be downloaded. A similar overview is provided for files the user has sent in the Secure Share outbox. How we built it When a user uploads a document, an encryption key is generated client-side (by the browser) and the document is subsequently encrypted in the browser. This ensures that the document never enters ours or Atlassian's servers unencrypted. The encryption is based on the open source project Firefox Send , which utilizes HTTP Encrypted Content-Encoding scheme ( RFC8188 ) for file encryption. This protocol utilizes 128 bit AES GCM symmetric encryption, which is in accordance with NIST recommendations . The library responsible for the client-side encryption of Secure Share is made available open source , as per Firefox Send's license. After the encryption, the encrypted file is uploaded to our server. This step involves interaction with Atlassian (via Forge bridge) in order to obtain details of the recipient and sender, as well as to provide an authentication context for our servers. The encryption key, however, is sent directly to our mail server, bypassing the Atlassian ecosystem. This is done to reduce the exposure of the key as much as possible. Our two backend, the email server and the file server, are operated as two independent serverless stacks that are deployed to two operationally independent AWS accounts. As a service provider this provides an added layer of security. In order to access an unencrypted file, a malicious actor must both obtain the encrypted file as well as the file's decryption key. Therefore, a breach of only one of the backends would not provide a malicious actor to any of our customer's data. Keeping the two components operationally separate, mitigates the risk of a breach of both services simultaneously. The backends are both run on AWS. The email service uses SES, which does not log the contents of emails, such as decryption keys. The file server utilizes DynamoDB for data storage and S3 buckets for file storage. Both backends use Serverless for cloud orchestration. The user interface is built using vue.js and utilizes components from vue-atlaskit . Our website is a Jekyll page hosted on Github and is behind Cloudflare’s DNS. Challenges we ran into We started out by trying to use the native ForgeUI which was really clean and great to work with but we soon ran into challenges when our requirements required more complicated UI functionality. Atlas-kit was our second choice because we were set on keeping in line with Atlassian design guidelines but we found the kit to be a bloated and cumbersome to work with so eventually we rewrote the UI a second time using Vue.js and an excellent library created by Spartez called vue-atlaskit. Our initial idea was to build the application directly in confluence pages and our second choice was prime real estate such as generalPages. Forge applications do not have the ability to export confluence documents as pdf’s, nor does Forge provide vendors with access to general pages (yet) so we decided to pick the most generally available location in Jira which we believe are the project pages. We had to build our own request validation for outbound calls… We found it somewhat difficult to work together on the app since it’s not possible to share apps between developers, this also made the CI/CD a little tricky to deal with. Accomplishments that we're proud of Submitting an entry into this kind of a contest requires a really broad skillset. We are really proud of how performant and seamless the user experience is. The website for the vendor and finally our demo video where we have absolutely no previous experience with video editing. By the end of the project we were using our own app to exchange documents and resources related to the submission to Codegeist and in all honesty it was more responsive and easy to use than we could have hoped for, especially given the security constraints we put in place as our main design principle. What we learned Coming from the field of cybersecurity we quickly found out it’s much easier to point out what other people do wrong than build it ourselves. The broad range of skills required to submit this entry was a little daunting as well and we had to quickly adapt and learn some new things such as video editing. We found that we should have started on the submission entry much sooner but were hyperfocused on the technology. What's next for Secure Share As it is designed, Secure Share handles both the transmission and storage of encrypted files as well as the transmission of the encryption keys via email. Although these components are kept operationally isolated, a breach of both components would compromise all documents where both the encryption key and encrypted document are intercepted. To eliminate the risk of leaking customer data, the first improvement we envision for Secure Share is to allow the customer to handle the delivery of encryption keys. In this scenario, the encrypted document would still be sent to our servers, but the customer would provide a webhook for message delivery which would be invoked directly in the browser when users send documents. This design ensures that the encryption key never enters the servers of Secure Share or Atlassian, and therefore, a compromise of either Secure Share or Atlassian would not put any customer data at risk. This design also allows the customer to adapt the message delivery to their ecosystem, whether they be their in-house email server or messaging applications such as Slack or Teams. Secure Share would provide customers with template code for message delivery through various means, such as email, Slack, etc. Our second focus is to adapt Secure Share to a wider range of products within the Atlassian ecosystem. Although our initial focus was on Jira, we are confident that the functionality Secure Share provides is applicable to a wider audience. In the long term, we intend to incorporate cryptographically secure digital signatures into Secure Share. This would allow customers to not only securely share documents, but also sign them digitally. <div