---
slug: "veriloan"
url: "https://devpost.com/software/veriloan"
title: "VeriLoan"
hackathon: "DeveloperWeek 2025 Hackathon"
organization: "DevNetwork"
winner: true
words: 1196
team_size: 0
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/legal_professional"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# VeriLoan

> Intelligent loan fraud prevention powered by Fingerprint's device intelligence, protecting banks from sophisticated fraud while ensuring seamless customer experiences

[Devpost](https://devpost.com/software/veriloan) · hackathon [[DeveloperWeek 2025 Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]] [[transportation]]
**user** [[legal_professional]]
**substrate** [[financial_record]] [[structured_db]]

**stack** bootstrap, css3, django, fingerprintjs, git, html5, javascript, mysql

## How they structured the write-up

- inspiration
- what it does
- how we built it
- how fraud detection works
- how to trigger fraud alerts (for judges)

## Body

VeriLoan: Fraud Detection and Prevention System Inspiration VeriLoan was inspired by the growing need for sophisticated fraud prevention in banking systems. Traditional security measures often fail to detect modern fraud techniques, leading to significant financial losses. The project leverages Fingerprint's advanced device intelligence capabilities to create a robust fraud detection system. What It Does VeriLoan is an intelligent loan fraud detection and prevention system designed for banks and financial institutions. It integrates with Fingerprint's device intelligence platform to analyze loan applications in real-time, using multiple risk factors and Smart Signals to identify and prevent fraudulent activities. How We Built It The system was built using Django with a microservices architecture, incorporating: FingerprintJS for device fingerprinting and Smart Signals Custom risk scoring algorithms Real-time fraud detection Comprehensive admin dashboard Redis caching for performance optimization How Fraud Detection Works Risk Scoring: The fraud detection system utilizes a Risk Scoring Service to calculate a risk score for each loan application. The risk score is determined based on the following factors: Identity Risk : Compares personal details such as name, phone number, and email to detect inconsistencies (e.g., applications with the same personal details but different visitor IDs). Device Risk : Evaluates device and browser-related risks, such as detecting bots, VPN usage, proxies, or browser tampering. A higher risk score is given to suspicious device behaviors. IP Risk : Assesses the risk based on the applicant's IP address. Repeated applications from the same IP address or unusual IP behaviors could trigger a higher risk score. Application History Risk : Checks the history of loan applications submitted by the same visitor. If there are multiple applications from the same visitor within a short time, it increases the risk score. The individual scores for these factors are weighted and combined to compute an overall risk score ranging from 0 to 100. Fraud Detection Logic: After calculating the risk score, several fraud detection tests are performed: Test 1: Multiple Applications from the Same Device : If multiple applications are submitted from the same device (i.e., using the same visitor ID), it raises a fraud alert. Test 2: Same Personal Details with Different Devices : If personal details match across multiple devices, this may indicate that fraudulent data is being used. Test 3: Fake Data Detection : The system checks if the applicant has provided suspicious or fake data (e.g., test emails, fake phone numbers, or unusual name patterns). Test 4: Similar Applications with Slightly Varying Details : It looks for applications with minor differences in details but otherwise appear suspiciously similar. Test 5: High Risk Score : If the overall risk score exceeds a set threshold (e.g., 70), it triggers a fraud alert. Fraud Alert Creation: If any of these tests result in suspicion, a FraudAlert is created. The loan application’s status is set to PENDING for further review. The fraud alert includes the reason for the alert (e.g., multiple applications from the same device, suspicious personal data, etc.) and the risk score. Admin Notification: The system also notifies the administrators (through the admin dashboard) of high-risk applications. This enables them to take appropriate action. How to Trigger Fraud Alerts (For Judges) Judges can trigger fraud alerts during the loan application process by simulating or identifying certain behaviors that are flagged as fraudulent. Here’s how to trigger fraud alerts: Multiple Applications from the Same Device (Visitor ID) : Action: Submit multiple loan applications from the same device or visitor ID in a short period (e.g., a few days). Result: If the system detects more than one application from the same visitor ID within 7 days, it will trigger an alert. Same Personal Details Across Different Devices : Action: Submit multiple applications with the same personal details (e.g., name, phone, email) but use different devices (i.e., different visitor IDs). Result: If the system detects such behavior, it will flag the application and trigger an alert. Suspicious Fake Data : Action: Enter suspicious or obviously fake data, such as test emails, fake phone numbers, or generic names like test user. Result: The fraud detection system will identify patterns such as test data or fake names and generate an alert. Similar Applications with Minor Variations : Action: Submit multiple loan applications with the same core details but small variations (e.g., slight name changes or minor email modifications). Result: The system will detect these similar patterns and flag them as suspicious, triggering a fraud alert. High Risk Score : Action: Based on the risk scoring logic, a loan application with a high risk score (over 70) will automatically trigger a fraud alert. Result: This is determined based on a combination of identity, device, IP, and history risk factors. Challenges We Ran Into Complex Risk Scoring : Balancing multiple risk factors while maintaining system performance was challenging. We had to implement a weighted scoring system that adapts to different fraud patterns, ensuring fair assessment without generating false positives. Real-time Processing : Handling high-volume loan applications without performance degradation required managing database transactions efficiently and implementing proper caching strategies to maintain system performance during peak times. Smart Signals Integration : Processing multiple Smart Signals simultaneously presented challenges. We needed to handle signal inconsistencies and ensure the system remained reliable during high load situations. Accomplishments We're Proud Of Comprehensive Fraud Detection : We successfully implemented a multi-layered risk assessment approach, achieving high accuracy in fraud detection. Additionally, we created an efficient visitor tracking system, which is key in identifying suspicious patterns. User Experience : We seamlessly integrated FingerprintJS, providing real-time feedback on loan applications. The system also features an intuitive admin dashboard for monitoring fraud activities, ensuring an easy-to-use experience for administrators. Technical Achievements : We implemented robust error handling and retry mechanisms to enhance system reliability. Additionally, we created an efficient database schema for tracking visitor history and developed a comprehensive admin interface for managing fraud cases. What We Learned Risk Assessment : We learned the importance of balancing risk scoring weights to avoid over-relying on any single risk factor. We also recognized the value of combining multiple fraud detection signals and the need for continuous monitoring and adjustment of thresholds to stay effective. System Design : We found that caching plays a critical role in high-traffic systems, and managing database transactions properly is essential for fraud detection. Comprehensive logging became vital for monitoring and maintaining system performance. Security : We gained a deeper understanding of the importance of CSRF protection and the need for secure handling of sensitive user data. Implementing rate limiting for API endpoints was also crucial to prevent abuse and enhance system security. What's Next for VeriLoan Enhanced Features : We plan to integrate machine learning for better pattern recognition, adding additional Smart Signal implementations, and creating custom risk scoring models tailored for different loan types to improve fraud detection. Performance Optimization : We aim to implement distributed caching, add load balancing capabilities to ensure the system scales effectively, and optimize database queries to further enhance performance. User Experience : We are working on enhancing the admin dashboard with real-time analytics and improved reporting capabilities. Additionally, we plan to allow for customizable risk thresholds and alerts to give administrators more control over fraud detection. <div