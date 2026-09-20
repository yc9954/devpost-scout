---
slug: "bb8"
url: "https://devpost.com/software/bb8"
title: "BB8"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 650
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "user/developer"
  - "user/educator_student"
  - "user/general_public"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# BB8

> Seamless 2FA and Account Watchdog via Typing Biometrics

[Devpost](https://devpost.com/software/bb8) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[developer_tools]] [[education]] [[finance_payments]]
**user** [[developer]] [[educator_student]] [[general_public]]
**substrate** [[sensor_telemetry]] [[web_dom]]

**stack** css, html, php, postman, sendgrid, typingdna

## How they structured the write-up

- the idea 🧠
- the benefits
- the apis ⚙️
- the other possible use-cases
- the hackathon demo
- the community input

## Body

BB8 Profile Pic BB8 Public Workspace BB8 Team BB8 Landing Page BB8 Login Demo BB8 Successful 2FA BB8 Failed TypingDNA Authentication BB8 Email OTP BB8 Typing Pattern Generator BB8 cover The idea 🧠 Long gone are the days when we could use JUST a password to protect our online accounts. 🔐 Today, two-factor authentication became the status-quo, and finding the perfect balance between security and user experience is what makes or breaks an authentication solution. Cue typing biometric authentication, or recognizing people by the way they type. Since we type our passwords anyway, why not use the typing pattern itself as the second factor for authentication? The Benefits 👨‍💻 User Experience . Remove authN challenges, reduce device switching. ⌨️ Accessibility . No hardware, bandwidth or computer literacy prerequisites. 💰 Cost . It is FREE to use for small-medium enterprises. (Limit of 1 authentication per second). On top of acting as a Seamless 2FA , this solution is also an Account Watchdog , alerting the user in case somebody tries to break into his/her account. The APIs ⚙️ Our intent was to build a Developer-First solution, empowering the Developer Community to easily test & integrate it into their own projects. Thus, we chose APIs from companies that share a Developer-First vision: TypingDNA and SendGrid . By putting them together, the developers benefit from the best: Technical Solutions : Best-In-Class capabilities in terms of Typing Biometrics and Emails Developer Experience : Developer-Tailored Products, Documentation and Support Pricing : Free-forever licenses The other possible use-cases For this hackathon, we chose the typing pattern verification to be done on the email & password fields. However, the technology allows us to do much more with the same APIs, especially since TypingDNA works in 2 scenarios: the verified text is the same every time OR the verified text can change during each verification. For example, you could: 🚀 Implement the typing biometrics 2FA on a randomly generated text , that changes for every user, to appear after the initial email & password validation. 🚀 Ask the users to type a standard agreement phrase, such as “I hereby acknowledge that I have read, understand and agree to the terms and conditions.”, thereby generating a written Consent/Affidavit backed by a digital signature . 🚀 Capture samples of each student’s typing behavior during an online exam . This won’t interfere with the student’s exam and focus (since he/she would anyway be typing the answers), and it could be leveraged to prevent cheating or investigate possible fraud-attempts. The Hackathon Demo Curious to see it in action? 👉 Check-out this functional demo! http://postmanhackathon.co.uk/ 🎥 No time to test? Just watch the Demo Youtube video . The Demo has 2 functionalities: 👉 Login : 2FA enabled via email & password and typing behavior . To build the unique typing profile, we require the user to enroll 3 times before the first verification. This typing profile is enriched continuously , to keep up with the user’s typing pattern evolution in time. For the verification, if the email & password are correct, but the typing pattern doesn’t match the user’s unique profile, we use the existing email address to send out a one-time code that allows the user to login, together with an alert in case this was a hacking attempt. 👉 Typing Pattern : Learn more about typing patterns and generate unlimited unique samples to be used for your own API testing in Postman. Since we believe in the power of open-source, the Demo’s sources are available on GitHub, for other developers to have a starting point in their implementation: https://github.com/aditzup/postmanhackathon For building the Demo, we used the following tech stack: TypingDNA Authentication API: /auto endpoint SendGrid API HTML/CSS PHP Backend The community input Let us know what you think about this project, using the community collaboration tools offered by the public workspace. Comments, Mentions, Pull-Requests are highly encouraged and appreciated! 🙌 <div