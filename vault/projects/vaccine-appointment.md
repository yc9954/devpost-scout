---
slug: "vaccine-appointment"
url: "https://devpost.com/software/vaccine-appointment"
title: "Vaccino"
hackathon: "AWS Graviton Hackathon"
organization: "Amazon"
winner: true
words: 957
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/media_journalism"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Vaccino

> A Graviton2 processor powered voice application to help people in India with their vaccination needs and essential information.

[Devpost](https://devpost.com/software/vaccine-appointment) · hackathon [[AWS Graviton Hackathon]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[media_journalism]]
**substrate** [[video_visual]] [[web_dom]]

**stack** amazon-ec2, amazon-web-services, bing-search-api, pandas, python, streamlit, wit.ai

## How they structured the write-up

- inspiration
- what it does
- how to use the web application
- how we built it
- performance analysis
- how does it work
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- step by step deployment
- what's next for vaccino

## Body

Vaccino Home Page Vaccino Features SSML About Vaccino NLP Model India current Covid Stats and Voice Outputs Important tweets related to vaccines Available Vaccine Slots Send Email Formatted message with appointment sent to Email Do this if microphone is not working. You can use the web application after this change. Inspiration India is currently dealing with misinformation of vaccines, oxygen cylinders and facing a limited supply of vaccines. It is very important to ensure that you get information from verified sources and that you do not miss out on your vaccination appointment slots. Hence, Vaccino is a web application that tries to solve these problems using voice. Voice helps you search quickly with a lot of interactivity. What it does Vaccino is an easy to use voice application to help people in India with their vaccination needs. Users can quickly see relevant news and tweets related to vaccines or oxygen cylinders, give voice commands to check available appointment slots at a particular district/city, filter the results according to their needs and send an e-mail to themselves with the details of the appointments they are interested in. You can watch the Youtube video describing its functionalities here 🎥. Vaccino is technical-expertise agnostic. Any person can use it with ease by simply talking in English. How to Use the Web Application 1) Visit the URL: http://3.142.93.196:8501/ 2) Use the 'Click and Speak' button. Enable microphone access. 3) If you are still unable to use the microphone, then type the following in your address bar: chrome://flags/#unsafely-treat-insecure-origin-as-secure 4) Now, enter the URL - http://3.142.93.196:8501 in the text box under the ' Insecure origins treated as secure ' section and select ' Enabled ' option in the dropdown menu to the right. After the changes, your page should look like this: 5) Relaunch the browser. You can now use the application. How we built it Vaccino is a responsive web application built using Python and Streamlit. News articles are fetched using Bing Search API, NLP processing by Wit and Dataframe processing using pandas library. Appointments fetched using Co-Win API (Free and public). The application is deployed on AWS Graviton2 EC2 Instance - t4g.micro You can have a look at the code here 💻. You can use the deployed application using this link . Performance Analysis One of the most compute-intensive operation in this application is processing an entire data frame. Here is a comparison of time taken to do the same between Graviton based EC2 and Google Cloud Platform E2 Instance. Time Taken (in seconds) Graviton EC2 1.03 GCP E2 1.54 A noticeable 39.6887 % performance boost is gained by using Graviton EC2 Instance. How does it work Steps : 1) Click and Speak : Hit the 'Click and Speak' Button and ask your vaccine-related query. 2) NLP : Your voice query is sent to an NLP model for recognizing intents and extracting entities. This lets the application understand your needs. 3) Voice Output : Speech Synthesis Markup Language (SSML) was used to generate voice response. Parameters tweaked in such a way that the returned voice is as human-like as possible. 4) Output : After understanding the user's need, Vaccino returns the voice output along with the expected result. Appointments fetched using Co-Win API (Free and public, provided by govt. of India). 5) Final Step - Email : Appointment details that you are interested in are sent to your mail. This ensures that you do not miss your vaccination, which is very important in these times. Challenges we ran into Some libraries only support x86 architecture and hence had to ensure that all the libraries in use are ARM-compatible. Accomplishments that we're proud of Was successfully able to migrate my application to Graviton2 based AWS EC2. What we learned This was my first time using AWS. It was a great learning experience and I was able to spin up my first Instance on the cloud. Learned essential commands of Ubuntu and running sessions using tmux . Step by Step Deployment 1. Go to your AWS Management Console and select the EC2 Service. 2. Now, from your EC2 Dashboard, click the Launch Instance button. 3. Choose an Amazon Machine Image (AMI). For a Graviton2 enabled EC2 instance, select an AMI with 64-bit (Arm). I have chosen Ubuntu Server 18.04 LTS (HVM), SSD Volume Type, 64-bit Arm. 4. Choose an instance type. I have selected the t4g micro instance. 5. Click 'Next: Configure Instance Details' and all the following 'Next: ...' buttons until you reach the step called 'Configure Security Group'. Now, we have to add a Custom TCP Rule for our project. Click the 'Add Rule' button and select the options for the rule as shown in the image below. 6. Click Review and Launch . 7. Now, click the Launch button. In the pop-up window that appears, create a new key pair and download it. This is not to be shared publicly and will be used in later steps. Click Launch Instances . 8. Your Graviton2 based instance is now up and running. you can connect to this instance from your local machine using the following command: ssh -i <"key_pair_name">ubuntu@<Your Public DNS Address (IPv4)> 9. Execute the following commands: git clone <Repo_HTTPS_URL> sudo apt update sudo apt-get install python3-pip pip3 install Cython pip3 install --upgrade pip setuptools sudo apt-get install tmux cd <Cloned_Repo_Name> pip3 install -r requirements.txt tmux new -s StreamSession streamlit run <filename.py> Now, press Ctrl + B and then D to keep the website running even if you leave the terminal. 10. Our web application is now ready. You can visit the instances' IPv4 Public IP Address to access it. What's next for Vaccino Be able to recommend the ideal vaccination slots for a person automatically using Machine Learning. <div