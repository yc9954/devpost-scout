---
slug: "diagnosys"
url: "https://devpost.com/software/diagnosys"
title: "DiagnoSys"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 786
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/education"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/educator_student"
  - "user/patient_family"
  - "substrate/video_visual"
---

# DiagnoSys

> A revolutionary device to automate disease screening with Azure AI

[Devpost](https://devpost.com/software/diagnosys) · hackathon [[Azure AI Hackathon]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[education]] [[health_clinical]]
**user** [[clinician]] [[educator_student]] [[patient_family]]
**substrate** [[video_visual]]

**stack** adafruit, azure, python, raspberry-pi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for diagnosys

## Body

GIF The main DiagnoSys apparatus. Raspberry Pi body of our device. Testing our initial prototype at a pathology lab at one of the biggest hospitals in Las Vegas. Huge thank you to them! Inspiration As a premedical student, with extensive experience shadowing doctors and volunteering at hospitals, I know firsthand of the problems doctors and patients face in the healthcare space. The Azure AI hackathon gave me the opportunity to tackle a big inefficiency I've noticed in disease and cancer screening processes at hospitals. Any time you go to the doctor and get samples taken for a disease or cancer screening, your sample is sent to a special doctor called a pathologist, who takes a look at your sample with a microscope. For you technical folks at Microsoft, you can think of these guys as the backend of the healthcare system, while the doctor you interact with is the frontend. These pathologists have to manually screen thousands of microscope slides a day, so they often use machines to assist them. This is where the problem lies. These machines cost tens of thousands of dollars, are extremely large and power hungry, and to make matters worse are usually only specialized for diagnosing a single disease. This makes them terribly cost-inefficient and impractical for smaller clinics especially. To combat this problem, our team decided to create a device that can replace these machines at less than 1% of the cost, price, and size, while maintaining similar levels of accuracy by leveraging the power of AI on the cloud with Microsoft Azure. Furthermore, our device can be deployed in areas where access to healthcare professionals is lacking, and make a positive difference in our world. After weeks of soldering, 3D-printing, coding, and testing (at an actual pathology at one of the biggest hospitals in Las Vegas, NV), we completed DiagnoSys. What it does DiagnoSys is an automated disease and cancer screening assistant intended for use in hospital pathology labs (where they run tests on bodily samples) and for deployment in rural areas and developing countries where healthcare professionals are scarce. DiagnoSys is equipped with a state-of-the-art microscope, and using motors, can manipulate the microscope slide to capture an image of the entire microscope slide. Through an API call to our Azure Custom Vision models, DiagnoSys can automatically screen slides for hundreds of possible diseases (based on the model chosen) and help pathologists screen slides much quicker. Finally, the user can (optionally) securely store inferenced images on the cloud via Azure Blob Storage for future reference by doctors. How we built it The brains of our device is a Raspberry Pi 3. This is connected to an Adafruit DC motor hat over I2C, which controls 2 geared DC motors. These DC motors are connected to the gears of our custom DIPLE microscope, and allows for manipulation of the microscope slide. A connected Raspberry Pi camera takes pictures of the slide at key intervals after movement, and stores them locally. Through an API call to our Azure custom vision model, inferences are ran on these images. The inferences are visualized through OpenCV and can be uploaded to the cloud via Azure Blob Storage for future reference. Challenges we ran into This was a challenging project to build in terms of the hardware component of things. Microscopes and computer are quite expensive, and we had to really get creative with things if we wanted to reduce costs so that our device is more accessible. We were able to keep costs low by using a $30 Raspberry Pi 3 and a custom DIPLE microscope (most traditional microscopes cost thousands of dollars, while ours is less than $100). Accomplishments that we're proud of We're very proud of creating a device that we think has the potential to truly revolutionize healthcare, especially in areas where access to healthcare professionals is lacking. By running inferences on the cloud through Azure, we are able to keep hardware costs very low and keep model accuracy high. Additionally, we can keep all of our models centralized in one location securely and ensure that all of our models are up to date. What we learned We learned a ton about how to leverage Azure AI services to create problem-solving innovations. To be honest, our project was made possible because we ran inferences on the cloud. We also learned a lot about Azure storage services, and how to leverage them in our applications. What's next for DiagnoSys We believe that DiagnoSys has a lot of potential as a product. This is probably the coolest thing we've developed to date (and we've developed a LOT of things these past 6 months). We will definitely continue working on refining and improving DiagnoSys. <div