---
slug: "pneumo-apis"
url: "https://devpost.com/software/pneumo-apis"
title: "Pneumo Apis"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 924
team_size: 3
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/medical_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Pneumo Apis

> Secured AI Apis with the purpose to assist radiologists with fast and accurate pneumonia detection amid this COVID-19 pandemic.

[Devpost](https://devpost.com/software/pneumo-apis) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]] [[education]] [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[medical_record]] [[structured_db]] [[video_visual]]

**stack** postman, pytorch, tensorflow

## How they structured the write-up

- background
- inspriation
- solution
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pneumo apis

## Body

Current Chest Xray Diagnosis vs Process with noval Pneumo Apis Chart of wait time reduction Team Cover Background In screening for COVID-19, patients can first be screened for flu-like symptoms using a nasal swap to confirm their status. After 14 days of quarantine for confirmed cases, the hospital draws the patient’s blood and takes the patient’s chest X-ray. Chest X-ray is a golden standard for physicians and radiologists to check for the infection caused by the virus. An X-Ray imaging will allow your doctor to see your lungs, heart, and blood vessels to help determine if you have Pneumonia. When interpreting the x-ray, the radiologist will look for white spots in the lungs (called infiltrates) that identify an infection. This exam, together with other vital signs such as temperature, or flu-like symptoms, will also help doctors determine whether a patient is infected with Pneumonia or other Pneumonia-related diseases. The standard procedure of Pneumonia diagnosis involves a radiologist reviewing chest x-ray images and send the result report to a patient’s primary care physician (PCP), who then will discuss the results with the patient. Inspriation A survey by the University of Michigan shows that patients usually expect the result came back after 2-3 days a chest X-ray test for Pneumonia. (Crist, 2017) However, the average wait time for the patients is 11 days (2 weeks). This long delay happens because radiologists usually need at least 20 minutes to review the X-ray while the number of images keeps stacking up after each operation day of the clinic. New research has found that an artificial intelligence (AI) radiology platform such as our CovidScan.ai can dramatically reduce the patient’s wait time significantly, cutting the average delay from 11 days to less than 3 days for abnormal radiographs with critical findings. (Mauro et al., 2019) With this wait-time reduction, patients I critical cases will receive their results faster and receive appropriate care sooner. Solution Using the power of pretrained machine learning models from open source, CovidScan.ai is created as a full-scaled AI tool for radiology clinics and hospitals. It can automate the process of security log-in, PPE safety check for medical staff, and assist radiologists to determine signs of COVID-19 on chest X-ray images with high accuracy indicate pneumonia. This tool of cutting edge technology can be used to reduce the workload for clinicians, and speed up patients’ wait time for pneumonia lab results in this critical time of the COVID-19 pandemic. ID Badge Scanner: For security purpose, only authorized personnel can access the web-app, which contains patients’ confidential health information (name, date of birth, chest X-ray, medical history…). Hence, the web-app will use pretrained scan the medical’s badge to grant them access to the software. PPE Safety Check: Due to hospitals/clinics’ strict guidelines in PPE usage, especially during this COVID-19 outbreak, the web-app will ask the medical staff if he/she is in direct contact with patients for chest X-ray taken. If yes, then the web-app will use AWS pretrained to check for medical staff’s PPE to see if the staff follow the safety protocols to minimize any exposures to the disease. If the medical staff passed both the secured check and safety, he/she can move on to the next step. COVID-19 Chest X-ray Testing: In the last step, the medical staff take patients’ chest X-ray images using the specialized machine and then upload the taken images to the database of the web-app for testing for a sign of COVID-19 infection or bacterial pneumonia. It is due to the fact that an AI system can review, highlight the pneumonia sign and classify each X-ray image all in less than 10 seconds (comparing the radiologist’s 20 minutes that we mentioned earlier), and it can do that same task effortlessly for 24 hours without taking a break. This time cut is especially critical in the time amid the pandemic of COVID-19. With this spreading rate, it will be overwhelming for radiologists to review a massive number of chest X-ray images of potential COVID-19 infected patients. With the assistance of CovidScan.ai, it can automatically highlight the suspected signs of pneumonia for the radiologists and speed up the process of chest X-ray review. Therefore, more COVID-19 positive-tested patients will get their results back faster and receive appropriate care sooner to prevent the spread of the virus. Challenges we ran into This hackathon project was a very different experience for us which challenged us throughout this project with the AWS sagemaker. This is the first time we all were working with AWS sagemaker and creating endpoints of the pre-trained TensorFlow model. Also, understanding curated models and determining their accuracy was a little bit challenging for us. Even after successfully deploying the model’s endpoints, calling Amazon SageMaker model endpoints using Amazon API Gateway and AWS Lambda gave us a very hard time. Accomplishments that we're proud of We manage to finish the project in such a limited time of 1 week in our free time from school and work. We still keep striving to submit on time while learning and developing at the same time. We are really satisfied and proud of our final product for the hackathon. What we learned Through this project, we learnt to contribute and collaborate effectively through the Postman shared workspace. Although we regularly use POSTMAN as our API testing tool but this experience was quite amazing. What's next for Pneumo Apis In Future, we can add multiple pathologies detection using different body scans for example brain MRI image, breast mammogram. We can make a complete radiology tool for radiologists. <div