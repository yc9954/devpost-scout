---
slug: "medico-for-healthcare-assistance"
url: "https://devpost.com/software/medico-for-healthcare-assistance"
title: "Medico for Healthcare Assistance"
hackathon: "Kore.ai Botathon"
organization: "Kore.ai"
winner: true
words: 722
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/developer"
  - "user/patient_family"
---

# Medico for Healthcare Assistance

> Customer-centric Intelligent Virtual Assistant with greater personalization focusing on the fulfillment of customer's requirements in Healthcare

[Devpost](https://devpost.com/software/medico-for-healthcare-assistance) · hackathon [[Kore.ai Botathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[civic_government]] [[developer_tools]] [[health_clinical]]
**user** [[clinician]] [[developer]] [[patient_family]]

**stack** email, facebook-messenger, javascript, kore.ai-datatables, kore.ai-webclient, mockapi, ngrok, node.js, otp-auth, twilio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for medico for healthcare assistance

## Body

Custom Dashboard for Bot Analysis Medico Features Doctor Appointment & Order Medicines Features Risk Assessment & Our Services Tools & Technologies Used Inspiration The demand for quality healthcare is more prevalent than ever in the modern world, especially since the start of Covid. Enhance the efficiency of an organization's processes by building a bot that will speed up the process. What it does Medico can schedule Doctor Appointment , collect patient details, perform Health Risk Assessment , provide medical assistance by Order Medicines facility, schedule Appointments for Diagnosis Lab Tests , and answer FAQs about diseases Medico Assistant is available in 2 channels - Web/Mobile client, Facebook messenger How we built it Doctor Appointment, Order Medicines, and Diagnosis Lab Tests need User Authentication achieved with 2- step OTP Authentication using the Twilio Verify API service. User SignUp validation is done if there's an active account present with the same Mobile number. User Authentication with Login is needed for every new conversation session. If the user once authenticated need not be necessary to authenticate within the same user session. Doctor Appointment - Users can Book, View, Cancel or Modify Appointments Book Appointment - Existing Users - If there are any previous appointments registered they can use them, else can schedule with new data. New Users - If they are booking for themselves, then details used for registration are used here; else, they can schedule with new data. View/Cancel/Modify Appointments - A list of available appointments is displayed in a Carousel format. So, users can perform the required tasks on them. Sends an Email notification after accomplishing the above tasks. Health Risk Assessment - Assess the risk of infection by selecting the symptoms the end user is possessing currently. Order Medicines - Can order medicines using a prescription or specifies whatever the user wants or can request a callback to talk to Human-agent. Sends an Email notification for successful orders. Our Services - Users can avail of Ambulance service and schedule Lab tests like X-rays, MRI, etc... Developers can monitor bot performance using the Custom Dashboard of Bot analytics provided with custom widgets. Challenges we ran into Fetching user details from Data tables and displaying them in Carousel format, but fixed it later. Couldn't able to generate a card response format for the Telegram channel which lead to the removal of this channel capability. Facing issues while publishing the version with multi-lingual support. Faced issues with Facebook integration but was able to fix it. We are using free trial Twilio account for OTP authentication service. Since it's a trial account there's a limit on number of verify service API calls. Because of that we are manually changing verify api credentials to make it available 24/7. This can overcome by taking paid service. Accomplishments that we're proud of Multiple validations at User Authentication - Registration/Login. Interruption handling between tasks. 2-factor authentication using phone number validation and SMS OTP with Twilio Verify API. Sending Dynamic Email notifications for Doctor Appointments and Order Medicines use cases. Multiple channel integrations with Web/Mobile client and Facebook messenger. Providing variations on user experience with the Digital form approach and conversational approach. Dynamically Prefilling Data in Digital forms. What we learned Conversation building with Digital forms approach and conversational approach and designing. 2-factor authentication using phone number validation, and SMS OTP with Twilio. Creating meta tags used for designing custom dashboards to monitor statistics on bots. Interruption handling between tasks. Designing training data -Training utterances for ML Engine, Pattern, Negative Patterns ( to disqualify intent qualification ) for FM Engine Sentiment Analysis of user responses. What's next for Medico for Healthcare Assistance At present Facebook-messenger is accessible only to developers. We have to publish the page to make it available to customers. Enhance the Doctor appointment use case by adding Appointment time to user requirements for Booking Appointment. At present Order Medicines - Prescription flow is static, we want it to make dynamic with OCR extraction and display medicine details with prescription. Obtaining the schedule of doctors and displaying those who are available Bookings outside of clinic hours are not permitted. Find the Card response template for Telegram and add it as an additional channel. Enabling the Multi-Lingual feature to the bot by fixing the French language publishing issue. Adding Live Agent feature for the Callback option of Order Medicines. <div